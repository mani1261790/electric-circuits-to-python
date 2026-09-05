# 電気回路で学ぶPython

電磁場、半導体、CMOS、CPU、OS、言語処理系を経て、一行のPythonが実行されるまでを一続きに学ぶ日本語教材です。

## 公開サイト

https://mani1261790.github.io/electric-circuits-to-python/

現在は「公開制作版」です。先行一周と第1〜106章を公開していますが、章別の必修実験・受入ゲートには未実行項目があり、学習者向け完成版とは表示していません。

現行スナップショット:

- HTML本文: 先行一周＋106章
- 固定runner: 718/718成功（測定欄は全件 `not_run`）
- canonical artifact: 739件（全件 `measured=false`）
- 独立出典sign-off: 631/631、hold 0
- MiniPy参照runtime: 20受入ケース成功
- 利用可能章host evidence: 第1〜21・24・32・92章の24/24章（物理測定ではない）
- 第1〜106章change/fault教育モデル: 106/106章で変更・故障経路を確認（`measured=false`、learner gateではない）
- 現行HTML分量: 先行一周12頁、第1〜106章3,498頁、合算3,510頁（各章24〜40頁、24頁未満0章）

第1〜106章の限定的な教育モデル実行記録は、[`site/reviews/chapter-change-fault-20260905.md`](./site/reviews/chapter-change-fault-20260905.md) と [`site/artifacts/learning-contract/chapter-change-fault-20260905.json`](./site/artifacts/learning-contract/chapter-change-fault-20260905.json) にあります。これは学習者の合格、外部tool、物理測定、独立レビュー、106章全体の完了を示しません。

FPGAを試す読者向けの任意追加経路は、[`site/machine-spec/fpga-optional-path.md`](./site/machine-spec/fpga-optional-path.md) に候補条件・必要artifact・合格境界をまとめています。現状は `candidate` / `not_built` で、PC-only必修経路の代替ではありません。

このリポジトリは公開サイト用に抽出した静的ファイルだけを保持します。制作原本、取得した第三者PDF、一時ファイル、ローカル実行環境は含みません。`site/PUBLICATION-MANIFEST.json` に公開ファイルのhashを記録しています。

## ライセンス

- 特記のない独自の本文・図版: [CC BY 4.0](./LICENSE-CONTENT.md)
- コード例と検査用コード: [MIT License](./LICENSE-CODE)
- 引用・参照した第三者資料: 各権利者および各出典の条件

誤りや改善案はGitHub Issuesで知らせてください。生成HTMLへの直接変更ではなく、該当章と内容が分かる報告を歓迎します。
