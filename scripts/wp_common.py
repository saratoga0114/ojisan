#!/usr/bin/env python3
"""WordPress REST API 共通処理（認証・HTML パース・manifest）。"""

from __future__ import annotations

import ast
import base64
import json
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "docs" / "posts-manifest.json"
FEED_DIR = ROOT / "feed"
ENV_PATH = ROOT / ".env"

META_RE = re.compile(r"^<!--\s*(\w[\w\s]*?):\s*(.*?)\s*-->\s*$")
RINKER_RE = re.compile(r"^<!--\s*rinker post_id:\s*(.+?)\s*-->\s*$", re.IGNORECASE)


@dataclass
class ArticleMeta:
    file: Path
    title: str
    slug: str
    description: str
    wp_category: str
    tags: list[str]
    rinker_post_id: str | None
    content: str


class WpSyncError(Exception):
    pass


def load_dotenv(path: Path = ENV_PATH) -> dict[str, str]:
    if not path.exists():
        raise WpSyncError(
            f".env が見つかりません: {path}\n"
            f"  copy .env.example .env して WP_USER / WP_APP_PASSWORD を設定してください。"
        )
    env: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    for key in ("WP_BASE_URL", "WP_USER", "WP_APP_PASSWORD"):
        if not env.get(key):
            raise WpSyncError(f".env に {key} が設定されていません。")
    return env


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, Any]:
    if not path.exists():
        raise WpSyncError(f"manifest が見つかりません: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(data: dict[str, Any], path: Path = MANIFEST_PATH) -> None:
    data["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_tags(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        try:
            value = ast.literal_eval(raw)
            if isinstance(value, list):
                return [str(v).strip() for v in value if str(v).strip()]
        except (SyntaxError, ValueError):
            pass
        inner = raw[1:-1].strip()
        if inner:
            return [t.strip() for t in inner.split(",") if t.strip()]
    return [t.strip() for t in raw.split(",") if t.strip()]


def parse_rinker_post_id(raw: str) -> str | None:
    raw = raw.strip()
    if not raw or raw.startswith("なし"):
        return None
    m = re.match(r"^(\d+)", raw)
    return m.group(1) if m else raw


def parse_article_html(path: Path) -> ArticleMeta:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    meta: dict[str, str] = {}
    rinker_post_id: str | None = None
    content_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("<!-- wp:"):
            content_start = i
            break
        m = RINKER_RE.match(line)
        if m:
            rinker_post_id = parse_rinker_post_id(m.group(1))
            continue
        m = META_RE.match(line)
        if m:
            key = m.group(1).strip().lower().replace(" ", "_")
            meta[key] = m.group(2).strip()
            continue

    if content_start == 0:
        raise WpSyncError(f"Gutenberg 本文の開始が見つかりません: {path}")

    slug = meta.get("slug")
    title = meta.get("title")
    if not slug or not title:
        raise WpSyncError(f"title / slug メタが不足しています: {path}")

    content = "\n".join(lines[content_start:]).strip() + "\n"
    rel = path.relative_to(ROOT).as_posix()

    return ArticleMeta(
        file=path,
        title=title,
        slug=slug,
        description=meta.get("description", ""),
        wp_category=meta.get("wp_category", ""),
        tags=parse_tags(meta.get("tags", "[]")),
        rinker_post_id=rinker_post_id,
        content=content,
    )


def discover_feed_html() -> list[Path]:
    return sorted(FEED_DIR.rglob("*.html"))


def rel_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


class WpClient:
    def __init__(self, base_url: str, user: str, app_password: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_base = f"{self.base_url}/wp-json/wp/v2"
        token = base64.b64encode(f"{user}:{app_password}".encode()).decode("ascii")
        self.headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
            "User-Agent": "ojisan-wp-sync/1.0",
        }
        self._ssl = ssl.create_default_context()

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        url = f"{self.api_base}/{endpoint.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(params, doseq=True)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
        try:
            with urllib.request.urlopen(req, context=self._ssl, timeout=60) as resp:
                raw = resp.read().decode("utf-8")
                if not raw:
                    return None
                return json.loads(raw)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            raise WpSyncError(f"HTTP {e.code} {method} {url}\n{detail}") from e

    def get(self, endpoint: str, **params: Any) -> Any:
        return self.request("GET", endpoint, params=params or None)

    def post(self, endpoint: str, body: dict[str, Any]) -> Any:
        return self.request("POST", endpoint, body=body)

    def paginate(self, endpoint: str, **params: Any) -> list[dict[str, Any]]:
        page = 1
        items: list[dict[str, Any]] = []
        while True:
            batch = self.get(endpoint, per_page=100, page=page, **params)
            if not batch:
                break
            if not isinstance(batch, list):
                raise WpSyncError(f"予期しないレスポンス: {endpoint}")
            items.extend(batch)
            if len(batch) < 100:
                break
            page += 1
        return items

    def fetch_categories_by_slug(self) -> dict[str, dict[str, Any]]:
        rows = self.paginate("categories", context="edit")
        return {row["slug"]: row for row in rows}

    def fetch_tags_by_name(self) -> dict[str, dict[str, Any]]:
        rows = self.paginate("tags", context="edit")
        return {row["name"]: row for row in rows}

    def resolve_tag_ids(
        self, names: list[str], *, create_missing: bool = False
    ) -> list[int]:
        cache = self.fetch_tags_by_name()
        ids: list[int] = []
        for name in names:
            if name in cache:
                ids.append(int(cache[name]["id"]))
                continue
            if create_missing:
                created = self.post("tags", {"name": name})
                ids.append(int(created["id"]))
                cache[name] = created
                continue
            raise WpSyncError(
                f"タグ '{name}' が WP にありません。"
                " --create-tags を付けるか、管理画面で作成してください。"
            )
        return ids

    def build_post_payload(
        self,
        article: ArticleMeta,
        manifest: dict[str, Any],
        *,
        status: str = "publish",
        create_tags: bool = False,
    ) -> dict[str, Any]:
        cat_slug = article.wp_category
        cat_entry = manifest.get("categories", {}).get(cat_slug, {})
        cat_id = cat_entry.get("wp_term_id")
        if not cat_id:
            raise WpSyncError(
                f"カテゴリ '{cat_slug}' の wp_term_id がありません。"
                " 先に wp_pull_ids.py --apply を実行してください。"
            )

        payload: dict[str, Any] = {
            "title": article.title,
            "slug": article.slug,
            "content": article.content,
            "excerpt": article.description,
            "status": status,
            "categories": [int(cat_id)],
        }
        if article.description:
            payload["meta"] = {
                "_jinr_description_display": article.description,
            }
        if article.tags:
            payload["tags"] = self.resolve_tag_ids(
                article.tags, create_missing=create_tags
            )
        return payload


def ensure_manifest_posts_from_feed(manifest: dict[str, Any]) -> dict[str, int]:
    """feed/*.html をスキャンし、manifest.posts に不足分を追加。追加件数を返す。"""
    posts = manifest.setdefault("posts", {})
    added = 0
    for path in discover_feed_html():
        article = parse_article_html(path)
        rel = rel_path(path)
        entry = posts.get(article.slug)
        if entry is None:
            posts[article.slug] = {
                "file": rel,
                "wp_post_id": None,
                "rinker_post_id": article.rinker_post_id,
                "status": "publish",
            }
            added += 1
        else:
            entry["file"] = rel
            if article.rinker_post_id is not None:
                entry["rinker_post_id"] = article.rinker_post_id
    return {"added": added, "total": len(posts)}


def sync_manifest_from_wp(manifest: dict[str, Any], client: WpClient) -> dict[str, int]:
    """WP 上の投稿・カテゴリ ID を manifest に反映。"""
    stats = {"categories": 0, "posts_matched": 0, "posts_updated": 0}

    wp_categories = client.fetch_categories_by_slug()
    for slug, entry in manifest.get("categories", {}).items():
        wp_cat = wp_categories.get(slug)
        if wp_cat:
            new_id = int(wp_cat["id"])
            if entry.get("wp_term_id") != new_id:
                entry["wp_term_id"] = new_id
                stats["categories"] += 1

    wp_posts = client.paginate("posts", status="any", context="edit", orderby="id")
    by_slug = {p["slug"]: p for p in wp_posts}

    for slug, entry in manifest.get("posts", {}).items():
        wp_post = by_slug.get(slug)
        if not wp_post:
            continue
        stats["posts_matched"] += 1
        new_id = int(wp_post["id"])
        if entry.get("wp_post_id") != new_id:
            entry["wp_post_id"] = new_id
            stats["posts_updated"] += 1
        entry["status"] = wp_post.get("status", entry.get("status", "publish"))

    return stats
