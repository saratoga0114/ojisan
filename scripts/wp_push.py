#!/usr/bin/env python3
"""feed/*.html → WordPress REST API（新規 / 更新）。"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wp_common import (
    ROOT,
    WpClient,
    WpSyncError,
    ensure_manifest_posts_from_feed,
    load_dotenv,
    load_manifest,
    parse_article_html,
    rel_path,
    save_manifest,
)


def git_changed_feed_files() -> list[Path]:
    files: list[Path] = []

    def collect(args: list[str]) -> None:
        try:
            out = subprocess.check_output(
                args,
                cwd=ROOT,
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            return
        for line in out.splitlines():
            line = line.strip()
            if line.endswith(".html"):
                p = ROOT / line
                if p.exists() and p not in files:
                    files.append(p)

    collect(["git", "diff", "--name-only", "HEAD", "--", "feed/"])
    collect(["git", "diff", "--name-only", "--", "feed/"])
    return sorted(files)


def slug_from_path(path: Path) -> str | None:
    try:
        return parse_article_html(path).slug
    except WpSyncError:
        return None


def resolve_targets(
    *,
    slug: str | None,
    changed_only: bool,
    all_posts: bool,
    manifest: dict,
) -> list[str]:
    if slug:
        return [slug]
    if changed_only:
        slugs: list[str] = []
        for path in git_changed_feed_files():
            s = slug_from_path(path)
            if s:
                slugs.append(s)
        return slugs
    if all_posts:
        slugs = []
        for slug, entry in manifest.get("posts", {}).items():
            if entry.get("wp_post_id") is None:
                continue
            if entry.get("status") == "hold":
                continue
            slugs.append(slug)
        return slugs
    raise WpSyncError("--slug / --changed-only / --all のいずれかを指定してください。")


def push_one(
    client: WpClient,
    manifest: dict,
    slug: str,
    *,
    apply: bool,
    status: str,
    create_tags: bool,
) -> dict:
    posts = manifest.setdefault("posts", {})
    entry = posts.get(slug)
    if not entry:
        raise WpSyncError(f"manifest に slug がありません: {slug}")

    file_rel = entry.get("file")
    if not file_rel:
        raise WpSyncError(f"manifest[{slug}].file がありません")

    path = ROOT / file_rel
    if not path.exists():
        raise WpSyncError(f"HTML が見つかりません: {path}")

    article = parse_article_html(path)
    if article.slug != slug:
        raise WpSyncError(
            f"slug 不一致: manifest={slug} / html={article.slug} ({rel_path(path)})"
        )

    payload = client.build_post_payload(
        article,
        manifest,
        status=status,
        create_tags=create_tags,
    )

    wp_post_id = entry.get("wp_post_id")
    action = "update" if wp_post_id else "create"
    result = {
        "slug": slug,
        "action": action,
        "wp_post_id": wp_post_id,
        "title": article.title,
        "content_bytes": len(article.content.encode("utf-8")),
    }

    if not apply:
        result["mode"] = "dry-run"
        return result

    if wp_post_id:
        response = client.post(f"posts/{int(wp_post_id)}", payload)
    else:
        response = client.post("posts", payload)

    new_id = int(response["id"])
    entry["wp_post_id"] = new_id
    entry["file"] = rel_path(path)
    entry["status"] = response.get("status", status)
    if article.rinker_post_id is not None:
        entry["rinker_post_id"] = article.rinker_post_id

    result["wp_post_id"] = new_id
    result["link"] = response.get("link")
    result["mode"] = "applied"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="feed → WordPress REST API")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="WP に送信する（省略時は dry-run）",
    )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--slug", help="1記事の slug")
    target.add_argument("--changed-only", action="store_true", help="git diff で変更された feed のみ")
    target.add_argument("--all", action="store_true", help="manifest 内の全記事")

    parser.add_argument(
        "--status",
        choices=("publish", "draft", "pending", "private"),
        default="publish",
        help="新規作成時のステータス（既定: publish）",
    )
    parser.add_argument(
        "--create-tags",
        action="store_true",
        help="存在しないタグを WP に作成してから付与",
    )
    args = parser.parse_args()
    apply = args.apply

    try:
        env = load_dotenv()
        manifest = load_manifest()
        ensure_manifest_posts_from_feed(manifest)
        client = WpClient(env["WP_BASE_URL"], env["WP_USER"], env["WP_APP_PASSWORD"])

        slugs = resolve_targets(
            slug=args.slug,
            changed_only=args.changed_only,
            all_posts=args.all,
            manifest=manifest,
        )

        if not slugs:
            print("対象記事がありません。")
            return 0

        print(f"=== wp_push ({'apply' if apply else 'dry-run'}) ===")
        print(f"対象: {len(slugs)} 件\n")

        for slug in slugs:
            try:
                r = push_one(
                    client,
                    manifest,
                    slug,
                    apply=apply,
                    status=args.status,
                    create_tags=args.create_tags,
                )
                print(
                    f"[{r['action']}] {slug} "
                    f"(wp_post_id={r.get('wp_post_id')}, "
                    f"content={r['content_bytes']} bytes)"
                )
                if r.get("link"):
                    print(f"  → {r['link']}")
            except WpSyncError as e:
                print(f"[ERROR] {slug}: {e}", file=sys.stderr)
                return 1

        if apply:
            save_manifest(manifest)
            print("\nmanifest を保存しました。")
        else:
            print("\n[dry-run] WP には送信していません。反映する場合は --apply を付けてください。")

        return 0
    except WpSyncError as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
