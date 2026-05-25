# feed/ — 公開記事ソース

WordPress に貼り付ける **投稿記事** の HTML を、カテゴリ別サブディレクトリで管理します。

書式は `../../blog/README.md`（Gutenberg・段落・Rinker）に従います。

---

## ディレクトリと WordPress カテゴリの対応

リポジトリのフォルダ名と、WP 管理画面で作る **カテゴリ** は次のとおり揃えます。

| ディレクトリ | WP カテゴリ名 | カテゴリ slug（WP） | 内容 |
| --- | --- | --- | --- |
| `feed/skincare/` | フェイスケア | `skincare` | クリーム・オールインワン・洗顔など |
| `feed/sunscreen/` | 日焼け止め | `sunscreen` | 顔用 UV・外回り・SPF |
| `feed/hair/` | シャンプー・頭皮 | `hair` | 頭皮ケア・匂い・ベタつき |
| `feed/grooming/` | エチケット・身だしなみ | `grooming` | 鼻毛・眉・ヒゲライン等 |
| `feed/body/` | ボディケア | `body` | ボディソープ・入浴 |

### WordPress 側でやること

1. **投稿 → カテゴリー** で上記5つを作成（slug は表のとおり）
2. 親カテゴリは **なし**（最初はフラットで十分）
3. 記事公開時に該当カテゴリにチェック

※ フォルダ名は Git 用（英小文字）。表示名は WP カテゴリの日本語で問題ありません。

---

## ファイル命名

```
feed/{カテゴリ}/{slug}.html
```

例：

- `feed/skincare/mens-face-cream-50s-guide.html`
- `feed/sunscreen/sales-outdoor-uv-not-sticky.html`
- `feed/hair/mens-shampoo-oily-scalp-40s.html`
- `feed/body/mens-body-soap-separate-face-50s-guide.html`
- `feed/grooming/mens-razor-sensitive-skin-50s-guide.html`
- `feed/body/mens-deodorant-roll-on-sales-50s-guide.html`
- `feed/skincare/mens-face-wash-dry-skin-50s-guide.html`
- `feed/skincare/mens-lip-balm-unscented-50s-guide.html`
- `feed/hair/mens-shampoo-dry-scalp-40s-guide.html`

各ファイル先頭にメタコメント：

```html
<!-- title: ... -->
<!-- slug: mens-face-cream-50s-guide -->
<!-- tags: [フェイスクリーム, 50代メンズ, メンズスキンケア] -->
<!-- description: ... -->
<!-- wp_category: skincare -->
```

`wp_category` はリポジトリ管理用（WP には手動でカテゴリ付与）。

本文のトーン・NG 表現（読者向けのみ／メタ語禁止）は **`../README.md` の「本文は読者向けの文章だけ」** と **`../docs/article-template.md`** を参照。

---

## 記事一覧

| 順 | ファイル | カテゴリ | Rinker post_id | 状態 |
| --- | --- | --- | --- | --- |
| 1 | `skincare/mens-face-cream-50s-guide.html` | フェイスケア | 19 | 公開済 |
| 2 | `sunscreen/sales-outdoor-uv-not-sticky.html` | 日焼け止め | 20 | 公開済 |
| 3 | `hair/mens-shampoo-oily-scalp-40s.html` | シャンプー・頭皮 | 21 | 公開済 |
| 4 | `skincare/mens-face-wash-oily-50s-guide.html` | フェイスケア | 59 | 公開済 |
| 5 | `sunscreen/uv-reapply-stick-sales-guide.html` | 日焼け止め | 66 | 公開済 |
| 6 | `skincare/mens-all-in-one-gel-busy-morning-guide.html` | フェイスケア | 73 | 公開済 |
| 7 | `hair/mens-shampoo-dryness-conditioner-40s-guide.html` | シャンプー・頭皮 | 80 | 公開済 |
| 8 | `hair/mens-shampoo-scalp-odor-40s-guide.html` | シャンプー・頭皮 | — | **保留**（アフィリ不可） |
| 9 | `skincare/mens-minimal-morning-routine-50s-guide.html` | フェイスケア | 59 | 公開済 |
| 10 | `grooming/mens-minimal-grooming-nose-eyebrow-50s-guide.html` | エチケット・身だしなみ | 94 | 公開済 |
| 11 | `skincare/mens-minimal-night-routine-50s-guide.html` | フェイスケア | 19 | 公開済 |
| 12 | `body/mens-body-soap-separate-face-50s-guide.html` | ボディケア | 103 | 公開済 |
| 13 | `grooming/mens-razor-sensitive-skin-50s-guide.html` | エチケット・身だしなみ | 112 | 公開済 |
| 14 | `body/mens-deodorant-roll-on-sales-50s-guide.html` | ボディケア | 119 | 公開済 |
| 15 | `skincare/mens-face-wash-dry-skin-50s-guide.html` | フェイスケア | 128 | 公開済 |
| 16 | `skincare/mens-lip-balm-unscented-50s-guide.html` | フェイスケア | 137 | 公開済 |
| 17 | `hair/mens-shampoo-dry-scalp-40s-guide.html` | シャンプー・頭皮 | 138 | 公開済 |
| 18 | `grooming/mens-shaving-foam-sensitive-50s-guide.html` | エチケット・身だしなみ | 152 | 公開済 |
| 19 | `skincare/mens-face-lotion-50s-guide.html` | フェイスケア | 153 | 公開済 |
| 20 | `grooming/mens-electric-shaver-sensitive-50s-guide.html` | エチケット・身だしなみ | 167 | 公開済 |
| 21 | `grooming/mens-beard-hair-removal-50s-guide.html` | エチケット・身だしなみ | — | 公開済 |
| 22 | `hair/mens-shampoo-scalp-odor-amazon-40s-guide.html` | シャンプー・頭皮 | 183 | 公開済 |
| 23 | `hair/mens-conditioner-dry-hair-40s-guide.html` | シャンプー・頭皮 | 209 | 公開済 |
| 24 | `grooming/mens-gray-hair-dye-beard-50s-guide.html` | エチケット・身だしなみ | 219 | 公開済 |

---

## 記事ロードマップ（8〜21）

| 順 | テーマ | 配置 | 状態 |
| --- | --- | --- | --- |
| 8 | **A.** 頭皮匂い・デオドラント | `feed/hair/` | **保留**（楽天公式限定・アフィリ不可） |
| 9 | **B.** 朝の最低限ルーティン（hub） | `feed/skincare/` | 公開済 |
| 10 | **C.** エチケット・身だしなみ（鼻眉ライン） | `feed/grooming/` | 公開済 |
| 11 | **D.** 夜の最低限ルーティン（hub） | `feed/skincare/` | 公開済 |
| 12 | **E.** ボディソープ（顔と体を分ける） | `feed/body/` | 公開済 |
| 13 | **F.** ヒゲ剃り（敏感肌・T字） | `feed/grooming/` | 公開済 |
| 14 | **G.** 制汗デオドラント（脇・外回り） | `feed/body/` | 公開済 |
| 15 | **H.** 乾燥肌向け洗顔（つっぱり・カサつき） | `feed/skincare/` | 公開済 |
| 16 | **I.** メンズリップ（無香料・外回り） | `feed/skincare/` | 公開済 |
| 17 | **J.** 乾燥頭皮シャンプー（つっぱり・かゆみ） | `feed/hair/` | 公開済 |
| 18 | **K.** シェービングフォーム（敏感肌・T字の続き） | `feed/grooming/` | 公開済 |
| 19 | **L.** メンズ化粧水（洗顔→ローション→クリーム） | `feed/skincare/` | 公開済 |
| 20 | **M.** 電気シェーバー（敏感肌・朝の時短） | `feed/grooming/` | 公開済 |
| 21 | **N.** ヒゲ脱毛（医療・サロン・剃り続け） | `feed/grooming/` | 公開済 |

---

## 記事ロードマップ（22〜30）

詳細は **[../docs/article-roadmap.md](../docs/article-roadmap.md)** を参照。

| 順 | テーマ | 配置 | 状態 |
| --- | --- | --- | --- |
| 22 | **O.** 頭皮匂い・消臭（Amazon可・第8代替） | `feed/hair/` | 公開済 |
| 23 | **P.** コンディショナー（きしみ） | `feed/hair/` | 公開済 |
| 24 | **Q.** 白髪・白ヒゲ染め | `feed/grooming/` | 公開済 |
| 25 | **R.** 目元クリーム | `feed/skincare/` | 未着手 |
| 26 | **S.** 身だしなみ hub | `feed/grooming/` | 未着手 |
| 27 | **T.** 日焼け止め hub | `feed/sunscreen/` | 未着手 |
| 28 | **U.** ハンドクリーム | `feed/body/` | 未着手 |
| 29 | **V.** 第21更新（クリニックAF） | — | Phase2 |
| 30 | **W.** ボディトリマー | `feed/grooming/` | 未着手 |

---

## 将来の拡張（記事が増えてから）

| 追加 | 用途 |
| --- | --- |
| `hubs/` | カテゴリ索引ページ（saratoga の `hubs/` と同様） |
| `template/` | 同型記事の量産テンプレ |
| `feed/{新カテゴリ}/` | 例：制汗・デオドラント等（第8保留テーマの代替） |
| `docs/article-roadmap.md` | 第22以降のテーマ・優先順・slug案 |

**5大欲求（金・仕事・名声・女・家族）** でフォルダを切らない。欲求は記事内の訴求軸であり、商品カテゴリと一致しないためです。

---

## 固定ページとの役割分担

| パス | 用途 |
| --- | --- |
| `static/` | 運営者情報・プライバシーポリシー等 **固定ページ** |
| `feed/` | **投稿記事** のみ |
