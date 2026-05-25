# おじさん向けコンテンツ（ojisan）

45〜55歳男性向けの「見た目・清潔感・第一印象」を、**選び方記事＋アフィリエイト**で届ける WordPress サイトのソースリポジトリです。

公開先：**https://ossan-kaizen.com**（WordPress / エックスサーバー）。pakapaka.jp / saratoga.jp と同系統の運用。note は補助導線のみ。

---

## サイトコンセプト

> **おじさんはこう見られがち → 若く・頼もしく見られたい → だからこれだけやればいい**

- ターゲット：**30代後半〜50代男性**（記事ごとにペルソナは1人に絞る）
- 最初の商材カテゴリ：フェイスケア / 日焼け止め / シャンプー（Amazon・楽天・Yahoo ショッピング）
- SEO：**ずらしたキーワード**（シーン・悩み単位）。「メンズコスメ おすすめ」の正面衝突は避ける

### おじさん5大欲求（訴求の軸）

`blog/note/payment/おじさんの攻略法.txt` より。記事・成約パートで意識的に割り当てる。

| 欲求 | 記事での例 |
| --- | --- |
| 金 | 1日○○円、ドラッグストアで買える、コスパ |
| 仕事 | 営業・面接・クライアントの第一印象 |
| 名声 | 「知っている男は最低限ここだけやっている」 |
| 女 | 老け見え、近距離の清潔感（誇大表現はしない） |
| 家族 | 妻からの一言、同窓会、再デート |

---

## 他リポジトリとの関係

| リソース | パス | 役割 |
| --- | --- | --- |
| Gutenberg 書式 | `../blog/README.md` | ブロック構文・段落・見出し・Rinker ブロック |
| セールスライティング | `../blog/note/セールスライティング仕様.md` | 成約パート・構成・NG 表現 |
| おじさん心理 | `../blog/note/payment/おじさんの攻略法.txt` | 訴求軸・同世代語彙 |

### 優先順位（矛盾時）

1. 本 README の**編集方針・商品紹介ルール**
2. `blog/README.md`（書式）
3. `blog/note/セールスライティング仕様.md`（**本サイトは【誠実版】固定**）

※ saratoga.jp の「実購入・検証のみ」方針は **本サイトには適用しない**。

---

## 編集方針（本サイト固有）

### 記事の種類

**選び方・口コミ整理型**（購入レビュー型ではない）。

| 書く | 書かない |
| --- | --- |
| 悩み・シーン・選ぶ条件（抽象） | 「私が2週間使った」等の一次体験の装い |
| Amazon / 楽天の評価・件数・口コミ傾向 | レビュー未確認の「最高」「絶対」 |
| 公式スペック（SPF、容量、医薬部外品区分） | 効果の断定・薬機法に触れる表現 |
| 向く人 / 向かない人 | 若者向け煽り・強訴求（§ 強訴求版は使わない） |

### 本文は読者向けの文章だけ（公開 HTML）

`feed/` の記事本文（見出し・段落・表・FAQ）に書くのは、**読者がそのまま読んで役立つ内容だけ**にする。

| 書く（読者向け） | 書かない（執筆者・サイト運営のメタ） |
| --- | --- |
| 悩み・手順・選び方・向く人 | 「ペルソナ」「hub」「索引」「各記事への入口」 |
| 「洗顔→保湿→UVの3ステップ」 | 「表に並べただけ」「本記事では〜だけ整理」 |
| 末尾 `<small>` の免責（AF・個人差・口コミ時点） | 冒頭の「実際に購入した体験ではなく」（離脱要因） |
| 表の列名・リンク名は商品タイプ（洗顔・クリーム等） | 「記事内主役」「選び方（記事）」など編集用語 |

- **HTML 先頭のメタコメント**（`<!-- title -->` / `post_id` 等）と **README・商品マスター** では、執筆メモ・管理用の用語を使ってよい。
- レビューやチャットでの説明もメタ表現可。**公開記事にそのまま転載しない。**

### 本文と商品リンクの分離

- **本文**：「フェイスクリーム」「日焼け止め」「シャンプー」など **カテゴリ・条件** で記述
- **Rinker（成約）**：調査済みの **具体商品1本（主役）＋比較0〜2本**

### 商品選定（購入なし）

1. 記事のペルソナ・シーンを決める
2. Amazon / 楽天でカテゴリ検索
3. 評価・レビュー件数で候補を絞る（目安は `docs/product-master.md`）
4. レビュー50件以上を読み、良い点・悪い点の **パターン** をメモ
5. Rinker に登録 → `post_id` を商品マスターに記録
6. 執筆時に評価・価格は **必ず各モールで再確認**（時点を本文に書く）

### 数値・ファクト

- 星評価・レビュー件数・価格は **執筆時点のモール表示** を根拠にする（記憶・古い記事の転載禁止）
- 確認できない数字は書かない
- 医薬部外品でも「治る」「必ず改善」は書かない

### 免責（各記事末尾）

- 本記事はアフィリエイトプログラムを利用していること
- 効果・感じ方には個人差があること
- 口コミ要約は執筆時点の情報であること

---

## 技術・収益

| 項目 | 方針 |
| --- | --- |
| CMS | WordPress（Gutenberg） |
| アフィリリンク | **Rinker** プラグイン（`[itemlink post_id="..."]`）— **WP 公式検索不可。BOOTH から ZIP アップロード**（`docs/xserver-setup.md` 参照） |
| ASP | Amazon / 楽天 / Yahoo ショッピング（アカウント保有済み） |
| AdSense | 申請済・審査中（2026-05） |
| note | 主戦場にしない。特おすすめ記事への **誘導用** のみ |

---

## ディレクトリ構成（予定）

```
ojisan/
├── README.md                 ← 本ファイル（ルール・ドメイン）
├── docs/
│   ├── product-master.md     ← 商品マスター・初期3商品
│   ├── article-template.md   ← 記事構成テンプレ・メタ例
│   └── xserver-setup.md      ← サーバー・WP セットアップ
├── image/                    ← サイト共通画像（Nano Banana 生成・WP も配置）
│   ├── ossan-kaizen-eyecatch.png  ← デフォルトアイキャッチ（1200×630 想定）
│   └── ossan-kaizen-icon.png      ← サイトアイコン（512×512 想定）
├── static/                   ← 固定ページソース（WP 貼り付け用 .html）
│   ├── owner.html            ← 運営者情報
│   └── privacy.html          ← プライバシーポリシー
└── feed/                     ← 投稿記事ソース（カテゴリ別 .html）
    ├── README.md             ← カテゴリと WP の対応表
    ├── skincare/             ← フェイスケア（WP: skincare）
    ├── sunscreen/            ← 日焼け止め（WP: sunscreen）
    ├── hair/                 ← シャンプー・頭皮（WP: hair）
    ├── grooming/             ← エチケット・身だしなみ（WP: grooming）
    └── body/                 ← ボディケア（WP: body）
```

記事 HTML の書式は `../blog/README.md` に従う。競馬サイト用の吹き出し等は使わず、段落・見出し・Rinker・表のみで足りる。

---

## 記事作成フロー

1. `docs/article-template.md` でペルソナ・KW・欲求軸を宣言
2. 選び方条件 → 候補比較 → 口コミ要約 → 主役1本
3. `docs/product-master.md` に商品・Rinker `post_id` を追記
4. `feed/{カテゴリ}/` に HTML を保存（メタコメント付き）
5. WordPress へ反映 — [`docs/wp-sync.md`](docs/wp-sync.md) の REST 同期（**新規記事は `wp_push --apply`**）。既存20本は手動公開済み・manifest 同期済み

カテゴリ設計・WP との対応は [feed/README.md](feed/README.md)。

### 固定ページ（`static/`）

| ファイル | 用途 | WP 公開 |
| --- | --- | --- |
| `static/about.html` | **ASP申請用**サイト紹介文（審査フォームへコピー） | しない |
| `static/owner.html` | 運営者情報 | `owner` |
| `static/privacy.html` | プライバシーポリシー | `privacy` |

`owner.html` / `privacy.html` はソース更新後、WP 側の該当固定ページにも再貼り付けする。

---

## 公開情報（確定）

| 項目 | 値 |
| --- | --- |
| ドメイン | **ossan-kaizen.com** |
| サイト名 | **おじさん改善ラボ**（確定） |
| 運営者名 | **改善係**（JIN:R プロフィール・運営者情報に使用） |
| キャッチフレーズ | **45歳からの身だしなみと清潔感** |
| ASP申請用サイト紹介文 | `static/about.html`（短文版・確定） |
| URL | https://ossan-kaizen.com |
| サーバー | エックスサーバー（レンタルサーバー） |
| CMS | WordPress（Gutenberg） |
| テーマ | **JIN:R** ＋ **jinr-child**（子テーマ有効） |

ブランド表記：`おじさん改善ラボ`（日本語）／ `Ossan Kaizen Lab`（フッター・英字表記用・任意）。

記事 HTML の Gutenberg 書式は **`../blog/README.md`** に従う（`jinr-heading`・段落・Rinker ブロック等。pakapaka.jp / saratoga.jp と同系統）。

### 画像アセット（`image/`）

| ファイル | 用途 | WP 設定 |
| --- | --- | --- |
| `ossan-kaizen-icon.png` | サイトアイコン（favicon） | 外観 → カスタマイズ → サイトアイコン |
| `ossan-kaizen-eyecatch.png` | デフォルトアイキャッチ / OG フォールバック | JIN:R のデフォルト設定 |

**記事ごとのアイキャッチ**は JIN:R の自動生成（タイトル文字入り）に任せる。`image/` はサイト共通の2点のみ Git 管理。

`.com` 運用時は Search Console で日本向け設定し、固定ページに運営方針を載せる（信頼・審査用）。

### セットアップ手順

詳細は [docs/xserver-setup.md](docs/xserver-setup.md)。

### 公開前チェックリスト

- [x] ドメイン取得（`ossan-kaizen.com`）
- [x] WordPress インストール・初期設定
- [x] 独自 SSL（HTTPS）・WP の URL を `https://ossan-kaizen.com` に統一
- [x] テーマ：JIN:R ＋ jinr-child 有効化
- [x] サイトアイコン・デフォルトアイキャッチ（`image/` → WP 設置済み）
- [ ] JIN:R デザイン詳細（カラー・ロゴ等）— アイキャッチ自動生成の微調整は任意
- [x] Rinker 設定（Amazon / 楽天 / Yahoo ID）
- [x] 初期3商品を Rinker 登録（post_id: 19 / 20 / 21 → `docs/product-master.md`）
- [x] 固定ページ：プライバシーポリシー（`static/privacy.html`）
- [x] 固定ページ：運営者情報（`static/owner.html`）
- [x] 固定ページ：編集方針の追記（`static/owner.html` → 口コミ整理型）
- [x] フッター／メニューから上記固定ページへリンク
- [x] Google Search Console 登録・サイトマップ送信
- [x] 初期3記事公開（`mens-face-cream-50s-guide` / `sales-outdoor-uv-not-sticky` / `mens-shampoo-oily-scalp-40s`）
- [x] 第4記事公開（`mens-face-wash-oily-50s-guide`・Rinker 59）
- [x] 第5記事公開（`uv-reapply-stick-sales-guide`・Rinker 66）／第2記事に内部リンク反映
- [x] 第6記事公開（`mens-all-in-one-gel-busy-morning-guide`・Rinker 73）／第1記事に内部リンク反映
- [x] 第7記事公開（`mens-shampoo-dryness-conditioner-40s-guide`・Rinker 80）／第3記事に内部リンク反映
- [x] 第9記事公開（`mens-minimal-morning-routine-50s-guide`・Rinker 59）／第10記事へ内部リンク反映
- [x] 第10記事公開（`mens-minimal-grooming-nose-eyebrow-50s-guide`・Rinker 94）／カテゴリ「エチケット・身だしなみ」新設
- [x] 第11記事公開（`mens-minimal-night-routine-50s-guide`・Rinker 19）／第9記事に内部リンク反映
- [x] 第12記事公開（`mens-body-soap-separate-face-50s-guide`・Rinker 103）／カテゴリ「ボディケア」新設
- [x] 第13記事公開（`mens-razor-sensitive-skin-50s-guide`・Rinker 112）／第10記事に内部リンク反映
- [x] 第14記事公開（`mens-deodorant-roll-on-sales-50s-guide`・Rinker 119）／第12記事に内部リンク反映
- [x] 第15記事公開（`mens-face-wash-dry-skin-50s-guide`・Rinker 128）／第4・第9・第11記事に内部リンク反映
- [x] 第16記事公開（`mens-lip-balm-unscented-50s-guide`・Rinker 137）／第9・第15記事に内部リンク反映
- [x] 第17記事公開（`mens-shampoo-dry-scalp-40s-guide`・Rinker 138）／第3・第7記事に内部リンク反映
- [x] 第18記事公開（`mens-shaving-foam-sensitive-50s-guide`・Rinker 152）／第13記事に内部リンク反映
- [x] 第19記事公開（`mens-face-lotion-50s-guide`・Rinker 153）／第1・第11・第15記事に内部リンク反映
- [x] 第20記事公開（`mens-electric-shaver-sensitive-50s-guide`・Rinker 167）／第13記事に内部リンク反映
- [x] 第21記事公開（`mens-beard-hair-removal-50s-guide`・Rinkerなし）／第20記事に内部リンク反映
- [x] 第22記事公開（`mens-shampoo-scalp-odor-amazon-40s-guide`・Rinker 183）／第3・第12・第14に内部リンク反映
- [x] 第23記事公開（`mens-conditioner-dry-hair-40s-guide`・Rinker 209）／第3・第7・第17に内部リンク反映
- [x] AdSense 申請（2026-05・**審査中**）
- [x] バリューコマース：Rinker Yahoo ID 設定済（2026-05）
- [ ] クリニックAF：A8.net 等に**未登録** → 登録・審査通過後、第21に紹介リンク追記

---

## 公開記事（41本）

| 順 | slug | カテゴリ | Rinker | 状態 |
| --- | --- | --- | --- | --- |
| 1 | `mens-face-cream-50s-guide` | フェイスケア | 19 | 公開済 |
| 2 | `sales-outdoor-uv-not-sticky` | 日焼け止め | 20 | 公開済 |
| 3 | `mens-shampoo-oily-scalp-40s` | シャンプー・頭皮 | 21 | 公開済 |
| 4 | `mens-face-wash-oily-50s-guide` | フェイスケア | 59 | 公開済 |
| 5 | `uv-reapply-stick-sales-guide` | 日焼け止め | 66 | 公開済 |
| 6 | `mens-all-in-one-gel-busy-morning-guide` | フェイスケア | 73 | 公開済 |
| 7 | `mens-shampoo-dryness-conditioner-40s-guide` | シャンプー・頭皮 | 80 | 公開済 |
| 8 | `mens-shampoo-scalp-odor-40s-guide` | シャンプー・頭皮 | — | **保留**（アフィリ不可） |
| 9 | `mens-minimal-morning-routine-50s-guide` | フェイスケア | 59 | 公開済 |
| 10 | `mens-minimal-grooming-nose-eyebrow-50s-guide` | エチケット・身だしなみ | 94 | 公開済 |
| 11 | `mens-minimal-night-routine-50s-guide` | フェイスケア | 19 | 公開済 |
| 12 | `mens-body-soap-separate-face-50s-guide` | ボディケア | 103 | 公開済 |
| 13 | `mens-razor-sensitive-skin-50s-guide` | エチケット・身だしなみ | 112 | 公開済 |
| 14 | `mens-deodorant-roll-on-sales-50s-guide` | ボディケア | 119 | 公開済 |
| 15 | `mens-face-wash-dry-skin-50s-guide` | フェイスケア | 128 | 公開済 |
| 16 | `mens-lip-balm-unscented-50s-guide` | フェイスケア | 137 | 公開済 |
| 17 | `mens-shampoo-dry-scalp-40s-guide` | シャンプー・頭皮 | 138 | 公開済 |
| 18 | `mens-shaving-foam-sensitive-50s-guide` | エチケット・身だしなみ | 152 | 公開済 |
| 19 | `mens-face-lotion-50s-guide` | フェイスケア | 153 | 公開済 |
| 20 | `mens-electric-shaver-sensitive-50s-guide` | エチケット・身だしなみ | 167 | 公開済 |
| 21 | `mens-beard-hair-removal-50s-guide` | エチケット・身だしなみ | — | 公開済 |
| 22 | `mens-shampoo-scalp-odor-amazon-40s-guide` | シャンプー・頭皮 | 183 | 公開済 |
| 23 | `mens-conditioner-dry-hair-40s-guide` | シャンプー・頭皮 | 209 | 公開済 |
| 24 | `mens-gray-hair-dye-beard-50s-guide` | エチケット・身だしなみ | 219 | 公開済 |
| 25 | `mens-eye-cream-50s-guide` | フェイスケア | 223 | 公開済 |
| 26 | `mens-minimal-grooming-hub-50s-guide` | エチケット・身だしなみ | 94 | 公開済 |
| 27 | `mens-outdoor-uv-hub-sales-guide` | 日焼け止め | 20 | 公開済 |
| 28 | `mens-hand-cream-sales-50s-guide` | ボディケア | 252 | 公開済 |
| 29 | `mens-beard-hair-removal-50s-guide` | エチケット・身だしなみ | — | 公開済（Phase2） |
| 30 | `mens-body-trimmer-50s-guide` | エチケット・身だしなみ | 262 | 公開済 |
| 31 | `mens-shampoo-scalp-hub-40s-guide` | シャンプー・頭皮 | 21 | 公開済 |
| 32 | `mens-foot-deodorant-sales-50s-guide` | ボディケア | 278 | 公開済 |
| 33 | `mens-minimal-skincare-hub-50s-guide` | フェイスケア | 59 | 公開済 |
| 34 | `mens-meeting-grooming-hub-50s-guide` | エチケット・身だしなみ | 252 | 公開済 |
| 35 | `mens-body-mist-unscented-50s-guide` | ボディケア | 301 | 公開済 |
| 36 | `mens-body-care-hub-50s-guide` | ボディケア | 103 | 公開済 |
| 37 | `mens-thinning-hair-shampoo-50s-guide` | シャンプー・頭皮 | 324 | 公開済 |
| 38 | `mens-suit-wrinkle-steamer-50s-guide` | エチケット・身だしなみ | 334 | 公開済 |
| 39 | `mens-leather-shoe-polish-50s-guide` | エチケット・身だしなみ | 342 | 公開済 |
| 40 | `mens-leather-shoe-waterproof-spray-50s-guide` | エチケット・身だしなみ | 349 | 公開済 |
| 41 | `mens-suit-lint-roller-50s-guide` | エチケット・身だしなみ | 361 | 公開済 |
| 42 | `mens-mouthwash-unscented-sales-50s-guide` | ボディケア | 369 | 公開済 |
| 43 | `mens-leather-briefcase-care-50s-guide` | エチケット・身だしなみ | 377 | 公開済 |
| 44 | `mens-shirt-collar-stain-50s-guide` | エチケット・身だしなみ | 386 | 公開済 |
| 45 | `mens-suit-clothes-brush-50s-guide` | エチケット・身だしなみ | 393 | 公開済 |
| 46 | `mens-suit-fabric-refresher-spray-50s-guide` | エチケット・身だしなみ | 407 | 公開済 |
| 47 | `mens-shirt-collar-prewash-50s-guide` | エチケット・身だしなみ | 443 | 公開済 |

### 記事ロードマップ（8〜21）

| 順 | テーマ | 状態 |
| --- | --- | --- |
| 8 | **A.** 頭皮匂い・デオドラント | **保留**（アフィリ不可） |
| 9 | **B.** 朝ルーティン hub | 公開済 |
| 10 | **C.** エチケット・身だしなみ（鼻眉ライン） | 公開済 |
| 11 | **D.** 夜ルーティン hub | 公開済 |
| 12 | **E.** ボディソープ（顔と体を分ける） | 公開済 |
| 13 | **F.** ヒゲ剃り（敏感肌・T字） | 公開済 |
| 14 | **G.** 制汗デオドラント（脇・外回り） | 公開済 |
| 15 | **H.** 乾燥肌向け洗顔（つっぱり・カサつき） | 公開済 |
| 16 | **I.** メンズリップ（無香料・外回り） | 公開済 |
| 17 | **J.** 乾燥頭皮シャンプー（つっぱり・かゆみ） | 公開済 |
| 18 | **K.** シェービングフォーム（敏感肌・T字の続き） | 公開済 |
| 19 | **L.** メンズ化粧水（洗顔→ローション→クリーム） | 公開済 |
| 20 | **M.** 電気シェーバー（敏感肌・朝の時短） | 公開済 |
| 21 | **N.** ヒゲ脱毛（医療・サロン・剃り続け） | 公開済 |

### 記事ロードマップ（22〜30）

第22以降の詳細（テーマ・slug案・優先順・執筆メモ）は **[docs/article-roadmap.md](docs/article-roadmap.md)** を参照。

| 順 | テーマ | 状態 |
| --- | --- | --- |
| 22 | **O.** 頭皮匂い・消臭シャンプー（Amazon可・第8代替） | 公開済 |
| 23 | **P.** コンディショナー（きしみ・パサつき） | 公開済 |
| 24 | **Q.** 白髪・白ヒゲ染め（近距離） | 公開済 |
| 25 | **R.** 目元クリーム（クマ・たるみ） | 公開済 |
| 26 | **S.** 身だしなみ hub | 公開済 |
| 27 | **T.** 日焼け止め hub | 公開済 |
| 28 | **U.** ハンドクリーム（握手・乾燥） | 公開済 |
| 29 | **V.** 第21 Phase2更新 | Phase2更新済 |
| 30 | **W.** ボディトリマー（胸毛・襟足） | 公開済 |

---

## 記事ロードマップ（31以降・フェーズ4）

詳細は [docs/article-roadmap.md](docs/article-roadmap.md) のフェーズ4を参照。

| 順 | テーマ | 状態 |
| --- | --- | --- |
| 31 | **X.** シャンプー・頭皮 hub | 公開済 |
| 32 | **Y.** フットケア（靴・匂い） | 公開済 |
| 33 | **Z.** フェイスケア hub | 公開済 |
| 34 | **AA.** 面接・会議 hub | 公開済 |
| 35 | **AB.** 無香料ボディミスト | 公開済 |
| 36 | **AC.** ボディケア hub | 公開済 |
| 37 | **AD.** 薄毛・ボリュームシャンプー | 公開済 |
| 38 | **AE.** スーツ・シワ・衣類スチーマー | 公開済 |
| 39 | **AF.** 革靴・靴磨き | 公開済 |
| 40 | **AG.** 革靴・防水スプレー | 公開済 |

**推奨次**: 第39テーマ検討

**審査・収益化**: バリューコマース**完了**（商品AF・Rinker設定済）／AdSense**審査中**／クリニックAF→**A8等・未登録**（第21リンク追記は登録後）

---

## 公開 URL（想定）

- https://ossan-kaizen.com/mens-face-cream-50s-guide/
- https://ossan-kaizen.com/sales-outdoor-uv-not-sticky/
- https://ossan-kaizen.com/mens-shampoo-oily-scalp-40s/
- https://ossan-kaizen.com/mens-face-wash-oily-50s-guide/
- https://ossan-kaizen.com/uv-reapply-stick-sales-guide/
- https://ossan-kaizen.com/mens-all-in-one-gel-busy-morning-guide/
- https://ossan-kaizen.com/mens-shampoo-dryness-conditioner-40s-guide/
- https://ossan-kaizen.com/mens-minimal-morning-routine-50s-guide/
- https://ossan-kaizen.com/mens-minimal-grooming-nose-eyebrow-50s-guide/
- https://ossan-kaizen.com/mens-minimal-night-routine-50s-guide/
- https://ossan-kaizen.com/mens-body-soap-separate-face-50s-guide/
- https://ossan-kaizen.com/mens-razor-sensitive-skin-50s-guide/
- https://ossan-kaizen.com/mens-deodorant-roll-on-sales-50s-guide/
- https://ossan-kaizen.com/mens-face-wash-dry-skin-50s-guide/
- https://ossan-kaizen.com/mens-lip-balm-unscented-50s-guide/
- https://ossan-kaizen.com/mens-shampoo-dry-scalp-40s-guide/
- https://ossan-kaizen.com/mens-shaving-foam-sensitive-50s-guide/
- https://ossan-kaizen.com/mens-face-lotion-50s-guide/
- https://ossan-kaizen.com/mens-electric-shaver-sensitive-50s-guide/
- https://ossan-kaizen.com/mens-beard-hair-removal-50s-guide/
- https://ossan-kaizen.com/mens-shampoo-scalp-odor-amazon-40s-guide/
- https://ossan-kaizen.com/mens-conditioner-dry-hair-40s-guide/
- https://ossan-kaizen.com/mens-gray-hair-dye-beard-50s-guide/
- https://ossan-kaizen.com/mens-eye-cream-50s-guide/
- https://ossan-kaizen.com/mens-minimal-grooming-hub-50s-guide/
- https://ossan-kaizen.com/mens-outdoor-uv-hub-sales-guide/
- https://ossan-kaizen.com/mens-hand-cream-sales-50s-guide/
- https://ossan-kaizen.com/mens-body-trimmer-50s-guide/
- https://ossan-kaizen.com/mens-shampoo-scalp-hub-40s-guide/
- https://ossan-kaizen.com/mens-foot-deodorant-sales-50s-guide/
- https://ossan-kaizen.com/mens-minimal-skincare-hub-50s-guide/
- https://ossan-kaizen.com/mens-meeting-grooming-hub-50s-guide/
- https://ossan-kaizen.com/mens-body-mist-unscented-50s-guide/
- https://ossan-kaizen.com/mens-body-care-hub-50s-guide/
- https://ossan-kaizen.com/mens-thinning-hair-shampoo-50s-guide/
- https://ossan-kaizen.com/mens-suit-wrinkle-steamer-50s-guide/
- https://ossan-kaizen.com/mens-leather-shoe-polish-50s-guide/
- https://ossan-kaizen.com/mens-leather-shoe-waterproof-spray-50s-guide/
- https://ossan-kaizen.com/mens-suit-lint-roller-50s-guide/
- https://ossan-kaizen.com/mens-mouthwash-unscented-sales-50s-guide/
- https://ossan-kaizen.com/mens-leather-briefcase-care-50s-guide/
- https://ossan-kaizen.com/mens-shirt-collar-stain-50s-guide/
- https://ossan-kaizen.com/mens-suit-clothes-brush-50s-guide/
- https://ossan-kaizen.com/mens-suit-fabric-refresher-spray-50s-guide/
- https://ossan-kaizen.com/mens-shirt-collar-prewash-50s-guide/

※ 第8（頭皮匂い・デオドラント）は楽天アンファー公式限定のため Rinker／アフィリ不可 → **公開保留**。**第22がAmazon可の実用版**。ソースは `feed/hair/mens-shampoo-scalp-odor-40s-guide.html`（第8）と `feed/hair/mens-shampoo-scalp-odor-amazon-40s-guide.html`（第22）に残置。

ソースは `feed/{カテゴリ}/` に HTML 管理。リライト時は執筆時点の価格・評価を各モールで再確認。

---

## 参照ドキュメント

- [Xserver セットアップ](docs/xserver-setup.md)
- [feed/ カテゴリ設計](feed/README.md)
- [商品マスター](docs/product-master.md)
- [記事テンプレート](docs/article-template.md)
- [WordPress REST 同期](docs/wp-sync.md)
- [記事ロードマップ（第22以降）](docs/article-roadmap.md)
- [blog 書式仕様](../blog/README.md)
- [セールスライティング仕様](../blog/note/セールスライティング仕様.md)

---

*ルールは運用しながら更新する。*
