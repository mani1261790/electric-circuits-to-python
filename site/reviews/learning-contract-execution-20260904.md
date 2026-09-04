# PC-only変更・故障診断 実行確認（2026-09-04）

## 結論

基準PC-only経路の最小縦断例について、入力を一つだけ変える変更課題と、各層の失敗を閉じ込める故障診断を実行した。固定runnerの解析・契約再生とは別に、チェックイン済みのMiniPy、minios、rv32eduを通る教育用実行モデルと、章のPC側Python artifact 26本を実行し、すべて終了コード0となった。

結果の正本は [`artifacts/learning-contract/pc-only-change-fault-20260904.json`](../artifacts/learning-contract/pc-only-change-fault-20260904.json) である。`measured:false` を維持しており、SPICE、RTL、FPGA、実機・物理測定の結果ではない。

## 実行した変更課題

| 層 | 変更 | 合格条件 | 結果 |
| --- | --- | --- | --- |
| MiniPy | `print(1 + 2)` → `print(1 + 3)` | 出力が `3` → `4` へ追従する | PASS |
| minios | UART payload `3\n` → `4\n` | UART bytesとsyscall長が入力変更を反映する | PASS |
| rv32edu | `ADD` → `SUB` | `x7=3` → `0xffffffff`、traceの演算種別も変わる | PASS |

いずれも変更前後の入力と出力を同じJSONへ保存し、上位の表示だけを固定して下位の変更を隠す経路にはしていない。

## 実行した故障診断

| 層 | 故障 | 期待した診断 | 結果 |
| --- | --- | --- | --- |
| MiniPy | 非対応の `**` 構文 | `MiniPyError`（feature boundary） | PASS |
| minios | 未知のsyscall番号99 | `-38` / `ENOSYS` | PASS |
| rv32edu | 未割当MMIOへの `SW` | `unmapped SW address` で拒否 | PASS |
| MiniPy verifier | 不正opcode `UNKNOWN` | 実行前にbytecode検証で拒否 | PASS |

加えて、既存の縦断trace-A正常系と負の境界テストを再実行し、正常系の全チェックと負のチェックがともに合格した。

## PC側artifactの再実行

`artifacts/chapter-*/**/*.py` のチェックイン済みPython artifact 26本を、現在のPythonで個別に起動した。26/26 が終了コード0である。これは章の計算用コードと教育用モデルの再実行証跡であり、718件すべての外部domain実験を代替しない。

## 完成ゲート上の位置づけ

今回閉じたのは、PC-only経路で実際に変更し、壊し、診断するための共通縦断アンカーと既存artifactの再実行である。各章のdomain固有変更課題、SPICE/RTL/QEMUの全実験、FPGA任意経路、実機測定は別ゲートとして残る。従って、この確認だけでは `learner-ready` を宣言しない。

106章のmanifestに宣言された必修ゲートとの対応は、別の [章別学習ゲートinventory](./chapter-learning-gate-inventory-20260904.md) に固定した。そこではacceptance_tests 699件、negative_tests 459件、章別変更・故障診断artifact 0章を個別に数え、今回の3変更・4故障アンカーを全章の合格へ拡張していない。acceptanceは結果行699件を生成したが実行済み0件、negativeは結果行459件のうち教育モデル実行済み12件（measured=false）である。

追加で、manifestのnegative IDのうち、実装モデルへ一意に対応づけられる12件（CH35/45/48/91/94/95のMiniPy／rv32edu opcode・syntax・stack・jump・unmapped address）を実行した。12/12が`educational_model_verified`となったが、`measured=false`であり、残る447件のnegativeや699件のacceptanceを実行済みとは扱わない。
## acceptance構造検査の追補

acceptance 699件に対しては、実験や学習者操作ではなく、manifest・本文・演習・解答・artifactの構造契約をtest ID単位で検査した。構造契約検査は239件がverified、failed 0件、domain／learner adapter未実装が460件で、全件`measured=false`である。構造契約のverifiedは、必修実験・外部実装受入・変更課題・故障診断の実行済みを意味しない。結果の正本は [`chapter-acceptance-results-20260904.json`](../artifacts/learning-contract/chapter-acceptance-results-20260904.json)、章別の対応行は [`chapter-learning-gate-inventory-20260904.json`](../artifacts/learning-contract/chapter-learning-gate-inventory-20260904.json) に保存した。

## acceptance構造検査の再同期（2026-09-05）

checkerの構造アダプタを追加し、演習・解答の複数形、固定runnerの解析再生と外部測定の分離、解析・数値・runner・測定の出所欄、artifact・figure・source registryのリンク、四層（自然法則・モデル・契約・実装）の本文語を検査した。結果は699件中261件verified、failed 0件、438件not_run、`measured=true` 0件。ここでのverifiedは形状・出所の契約であり、実験・測定・学習者操作の合格ではない。

## CH99 cleanup-only MiniPy runtime（2026-09-05）

参照runtimeにcleanup専用`try/finally`を実装し、正常終了と例外伝播後のcleanupを含む20ケースを全件passさせた。`except ... finally`、finally内return、generatorは対象外である。CH99実験5/7の`book run`は一般契約模型（`contract_model_only`、`measured=false`）のままで、runtime実装テストと外部domain測定を混同しない。

全718件runnerは再実行後も718/718成功、全件`measurement_status=not_run`。acceptance構造検査は261/699、未実行438、実行済み0、negativeは教育モデル12/459・未実行447で、learner-readyは保留する。
