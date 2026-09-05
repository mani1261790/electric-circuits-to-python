# 章別学習ゲート inventory（2026-09-04）

これは合格宣言ではなく、106章のmanifestに書かれた学習者向けゲートと、現時点で実行証跡がある範囲を分離する監査です。

- 宣言: 106章 / 実験718件 / acceptance_tests 699件 / negative_tests 459件
- 固定runner: 718/718成功、測定欄not_run 718件
- acceptance_tests結果行: 699件（構造契約検査済み 294件、構造契約failed 0件、domain/learner実行済み 0件、not_run 405件）
- negative_tests結果行: 459件（教育モデル実行済み 12件、not_run 447件）、measured=true 0件
- manifest negativeの教育モデル検証: 12/12件（measured=false）
- 章別変更・故障診断実行artifact: 0章
- 変更課題の記述を検出: 97/106章
- 故障診断の記述を検出: 106/106章

## 判定

`learner-ready` は保留です。共通runnerの成功は、各章のacceptance／negative、変更課題、故障診断を実行済みとは扱いません。

### 残る理由

- manifest acceptance_tests have 294 structural-contract rows verified; 0 structural rows failed and 405 domain/learner rows remain not_run
- manifest negative_tests have 12 educational-model result rows; the remaining 447 are not_run and measured=true is still zero
- no chapter-keyed change/fault execution artifact exists; the PC-only anchor is a separate three-change/four-fault check
- the explicit model mapping is still only an educational contract check; it does not close external-tool, FPGA, physical, or learner interaction gates

詳細な章別行は同じディレクトリのJSONを参照してください。PC-only縦断アンカーの3変更・4故障とは別の台帳です。
