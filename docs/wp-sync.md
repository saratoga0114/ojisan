# WordPress REST API 同期（feed → WP）

`feed/*.html` を正として、WordPress へ **新規公開・本文更新** するスクリプトです。  
手動のコードエディタ貼り付けの代わりに、内部リンク修正などを一括反映できます。

---

## 前提

| 項目 | 内容 |
| --- | --- |
| API | `https://ossan-kaizen.com/wp-json/wp/v2/` |
| 認証 | **アプリケーションパスワード**（Basic 認証） |
| 台帳 | `docs/posts-manifest.json`（slug ↔ WP 投稿 ID） |
| 依存 | Python 3.9+（標準ライブラリのみ） |

**Rinker の `post_id`**（19, 167 等）は本文 HTML に含まれます。  
**WordPress 投稿 ID**（`wp_post_id`）は manifest で別管理します。

---

## 初回セットアップ

### 1. アプリケーションパスワード

1. WP 管理画面 → **ユーザー → プロフィール**
2. **アプリケーションパスワード** → 名前 `ojisan-sync` 等 → **新しいアプリケーションパスワードを追加**
3. 表示されたパスワードをコピー（スペース含むままで OK）

### 2. `.env`

```powershell
cd c:\work\workspace\ojisan
copy .env.example .env
# .env を編集
```

```env
WP_BASE_URL=https://ossan-kaizen.com
WP_USER=管理者ユーザー名
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
```

### 3. manifest に WP ID を取り込む

```powershell
python scripts/wp_pull_ids.py
python scripts/wp_pull_ids.py --apply
```

- 公開済み投稿を slug でマッチし、`wp_post_id` を manifest に書き込みます
- カテゴリ term ID も同期します
- `feed/` 内の HTML から **未登録 slug** を manifest に追加します（`wp_post_id: null`）

---

## 日常の使い方

### 新規記事の公開（第22以降の標準フロー）

1. `feed/{カテゴリ}/` に HTML を執筆・保存（メタコメント付き）
2. dry-run で確認:

```powershell
python scripts/wp_push.py --slug 新しいslug
```

3. WP に公開:

```powershell
python scripts/wp_push.py --slug 新しいslug --apply
```

4. 既存記事に内部リンクを追加したら、変更分だけ push:

```powershell
python scripts/wp_push.py --changed-only --apply
```

`wp_pull_ids.py` は **初回セットアップ済み** なら、新規記事ごとに実行不要です（`wp_push --apply` が manifest に `wp_post_id` を自動保存します）。

---

### 1記事だけ更新（内部リンク反映など）

```powershell
python scripts/wp_push.py --slug mens-razor-sensitive-skin-50s-guide
python scripts/wp_push.py --slug mens-razor-sensitive-skin-50s-guide --apply
```

### Git で変更した feed のみ一括更新

```powershell
python scripts/wp_push.py --changed-only
python scripts/wp_push.py --changed-only --apply
```

### 新規記事を公開

manifest に `wp_post_id: null` の行がある状態で:

```powershell
python scripts/wp_push.py --slug mens-beard-hair-removal-50s-guide --apply
```

成功すると manifest に `wp_post_id` が自動保存されます。

---

## コマンド一覧

| スクリプト | 用途 |
| --- | --- |
| `wp_pull_ids.py` | WP → manifest（ID 同期・feed スキャン） |
| `wp_push.py` | manifest + feed → WP（新規 / 更新） |

### wp_pull_ids.py

| オプション | 説明 |
| --- | --- |
| `--apply` | manifest を書き込む（**省略時は dry-run**） |

### wp_push.py

| オプション | 説明 |
| --- | --- |
| `--apply` | WP に POST（**省略時は dry-run**） |
| `--slug SLUG` | 1記事指定 |
| `--changed-only` | `git diff` で変更された feed のみ |
| `--all` | manifest 内の全記事（`wp_post_id: null` と `status: hold` は除外） |
| `--status publish\|draft` | 新規作成時のステータス（既定: publish） |
| `--create-tags` | 存在しないタグを WP に作成してから付与 |

---

## 送信される内容

HTML 先頭メタから自動設定:

| メタ | REST フィールド |
| --- | --- |
| `<!-- title: ... -->` | `title` |
| `<!-- slug: ... -->` | `slug` |
| `<!-- description: ... -->` | `excerpt` ＋ JIN:R メタ `_jinr_description_display` |
| `<!-- tags: [a, b] -->` | `tags`（term ID に解決。`[]` 内はカンマ区切り・引用符不要） |
| `<!-- wp_category: skincare -->` | `categories`（manifest の term ID） |
| `<!-- rinker post_id: ... -->` | manifest 記録のみ（本文に含まれる） |
| 8行目以降の Gutenberg HTML | `content` |

メタ行（1〜6行目付近）は **WP 本文に送りません**。

---

## トラブルシュート

| 症状 | 対処 |
| --- | --- |
| 401 Unauthorized | `.env` のユーザー名・アプリパスワードを確認 |
| 404 on REST | パーマリンク設定を「投稿名」に保存し直す |
| カテゴリ未設定 | `wp_pull_ids.py --apply` で categories を同期 |
| `wp_post_id` が null | 先に WP で公開済みか確認 → pull。未公開なら push で新規作成 |
| エディタでデザインが崩れる | `content` は 8行目以降のみ送っているか確認 |

---

## 安全運用

- **常に dry-run（`--apply` なし）で確認してから `--apply`**
- 初回は `--status draft` で下書き作成 → プレビュー確認 → publish も可
- `.env` は Git にコミットしない（`.gitignore` 済み）
