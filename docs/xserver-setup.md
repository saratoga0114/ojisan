# Xserver セットアップ（ossan-kaizen.com）

エックスサーバーで WordPress を公開する手順メモ。パネル表記は取得時期で変わる場合があります。

---

## 前提

| 項目 | 値 |
| --- | --- |
| ドメイン | `ossan-kaizen.com` |
| サイト名 | おじさん改善ラボ（確定） |
| キャッチフレーズ | 45歳からの身だしなみと清潔感 |
| サーバー | エックスサーバー（レンタルサーバー） |

---

## 1. ドメインを Xserver に向ける

ドメインを **Xserver 以外**（お名前.com 等）で取得した場合：

1. エックスサーバー → **ドメイン** → **ドメイン設定追加**
2. `ossan-kaizen.com` を追加
3. 取得レジストラ側でネームサーバを Xserver 指定に変更  
   （サーバーパネル「ネームサーバー設定」に表示される 2〜4 台）
4. 反映まで数時間〜最大 72 時間程度

Xserver と同時取得した場合は、多くの場合この作業は不要です。

---

## 2. SSL（HTTPS）

1. サーバーパネル → **SSL設定**
2. `ossan-kaizen.com` を選択 → **独自SSL 設定**（Let's Encrypt）
3. 反映後、`https://ossan-kaizen.com` で開けることを確認
4. WordPress 設置後、**http → https リダイレクト** を有効にする（WordPress 側 or .htaccess）

---

## 3. WordPress 簡単インストール

1. サーバーパネル → **WordPress 簡単インストール**
2. ドメイン：`ossan-kaizen.com`（サブドメインではなくルート推奨）
3. ディレクトリ：**空欄**（`/` に設置）
4. サイト名：**おじさん改善ラボ**
5. 管理者ユーザー・パスワードは **他サイトと使い回さない**
6. インストール完了後、`https://ossan-kaizen.com/wp-admin/` にログイン

### インストール直後（WordPress 管理画面）

| 設定 | 推奨値 |
| --- | --- |
| 設定 → 一般 → サイトのタイトル | おじさん改善ラボ |
| 設定 → 一般 → キャッチフレーズ | 45歳からの身だしなみと清潔感 |
| 設定 → 一般 → WordPress アドレス / サイトアドレス | ともに `https://ossan-kaizen.com` |
| 設定 → パーマリンク | **投稿名**（`/%postname%/`） |
| 設定 → 表示設定 | ホームページは後で固定ページを指定（記事が増えてからでも可） |

---

## 4. テーマ

- **JIN:R** ＋ **jinr-child**（子テーマを有効化）— 確定
- pakapaka.jp / saratoga.jp と同系統。デザイン詳細（カラー・ロゴ・ウィジェット）は後回し可
- 記事ソースの書式：`../blog/README.md`

---

## 5. 必須プラグイン

**Rinker は WordPress 公式プラグイン検索に出ません。** BOOTH から ZIP をダウンロードし、**プラグインのアップロード** でインストールします。

1. [Rinker 公式（おやこそだて）](https://oyakosodate.com/rinker/) または [BOOTH：Rinkerベーシック](https://booth.pm/ja/items/891465) を開く
2. **無料ダウンロード** → `yyi-rinker-*.zip` を取得（**解凍しない**）
3. WP 管理画面 → **プラグイン → 新規追加 → プラグインのアップロード**
4. ZIP を選択 → **今すぐインストール** → **有効化**
5. 左メニューに **商品リンク**・**Rinker設定** が増えれば OK

インストール手順の図解：[Rinkerインストール方法](https://oyakosodate.com/rinker/manual/rinkerinstall/)

pakapaka / saratoga で既に使っている場合、手元の `yyi-rinker-*.zip` でも同じ手順で入れられます。

| プラグイン | 用途 |
| --- | --- |
| **Rinker** | Amazon / 楽天 / Yahoo アフィリリンク |
| （任意）Site Kit by Google | Search Console / Analytics 連携 |

インストール後 **Rinker 設定**：

1. Amazon アソシエイト ID
2. 楽天アフィリエイト ID
3. Yahoo バリューコマース（**設定済**・2026-05）
4. 商品を3本登録 → `post_id` を `docs/product-master.md` に記録

---

## 6. 公開前の固定ページ

| ページ | 内容 | 状態 |
| --- | --- | --- |
| プライバシーポリシー | Cookie・アフィリエイト・Analytics 等 | `static/privacy.html` |
| 運営者情報 | サイト運営者・アフィリエイト免責等 | `static/owner.html` |
| 編集方針（任意） | 口コミ整理型・効果の非保証 | `owner.html` に追記可 |

フッターまたはメニューからリンク。

---

## 7. Search Console

1. [Google Search Console](https://search.google.com/search-console)
2. プロパティ：`https://ossan-kaizen.com`
3. 所有権確認（HTML タグ or Site Kit）
4. **サイトマップ** 送信：`https://ossan-kaizen.com/wp-sitemap.xml`
5. **国** を日本向けに（設定可能な場合）

---

## 8. セキュリティ（推奨）

- 管理画面 URL はデフォルトのままでも、**強力なパスワード**＋**二要素認証**（プラグイン可）
- `wp-config.php` の編集権限は最小限
- 不要プラグインは入れない

---

## 9. セットアップ完了チェックリスト

- [x] WordPress インストール・サイト名設定
- [x] JIN:R ＋ jinr-child 有効化
- [x] 独自 SSL（HTTPS）・WP URL を https に統一
- [ ] パーマリンク「投稿名」
- [x] Rinker 設置・ASP ID 設定
- [x] 初期3商品を Rinker 登録（post_id: 19 / 20 / 21）
- [x] プライバシーポリシー・運営者情報（固定ページ）
- [ ] フッター／メニューから固定ページへリンク
- [ ] 運営方針（編集方針）— 任意
- [ ] Search Console 登録・サイトマップ送信
- [ ] 第1記事公開
- [ ] JIN:R デザイン詳細（任意・後回し可）

---

## 10. AdSense

- 2026-05に申請済。**審査結果待ち**
- 審査中は AF 記事の量産を続けて問題なし

---

## 11. REST API 同期（任意）

手動貼り付けの代わりに `feed/*.html` → WordPress を自動化できます。

- 手順: [docs/wp-sync.md](wp-sync.md)
- 認証: **アプリケーションパスワード**（ユーザー → プロフィール）
- 台帳: `docs/posts-manifest.json`（slug ↔ WP 投稿 ID）

---

*Xserver 公式マニュアル：[WordPress 簡単インストール](https://www.xserver.ne.jp/manual/man_wordpress_install.php)*
