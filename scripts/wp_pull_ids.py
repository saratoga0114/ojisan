#!/usr/bin/env python3
"""WordPress から slug / カテゴリ ID を manifest に取り込む。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wp_common import (
    WpClient,
    WpSyncError,
    ensure_manifest_posts_from_feed,
    load_dotenv,
    load_manifest,
    save_manifest,
    sync_manifest_from_wp,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="WP → docs/posts-manifest.json")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="manifest を書き込む（省略時は dry-run）",
    )
    args = parser.parse_args()
    apply = args.apply

    try:
        env = load_dotenv()
        manifest = load_manifest()
        client = WpClient(env["WP_BASE_URL"], env["WP_USER"], env["WP_APP_PASSWORD"])

        feed_stats = ensure_manifest_posts_from_feed(manifest)
        wp_stats = sync_manifest_from_wp(manifest, client)

        print("=== wp_pull_ids ===")
        print(f"feed スキャン: 追加 {feed_stats['added']} 件 / manifest 計 {feed_stats['total']} 件")
        print(
            "WP 同期: "
            f"カテゴリ更新 {wp_stats['categories']} / "
            f"投稿マッチ {wp_stats['posts_matched']} / "
            f"wp_post_id 更新 {wp_stats['posts_updated']}"
        )

        missing = [
            slug
            for slug, entry in manifest.get("posts", {}).items()
            if not entry.get("wp_post_id")
        ]
        if missing:
            print(f"\nwp_post_id 未設定（{len(missing)} 件）:")
            for slug in missing[:20]:
                print(f"  - {slug}")
            if len(missing) > 20:
                print(f"  ... 他 {len(missing) - 20} 件")

        if apply:
            save_manifest(manifest)
            print("\nmanifest を保存しました。")
        else:
            print("\n[dry-run] 保存していません。反映する場合は --apply を付けてください。")

        return 0
    except WpSyncError as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
