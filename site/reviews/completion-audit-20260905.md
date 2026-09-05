# 完成監査追補（2026-09-05）

この追補は、既存の独立レビュー後に生成器・台帳・第1〜106章のchange/fault教育モデルを更新した現行状態を、完了条件ごとに再確認した記録である。本文やsourceの意味判定を、実験・学習者受入の合格へ昇格させるものではない。

## 現行で確認できたこと

| 条件 | 現行証拠 | 判定 |
| --- | --- | --- |
| 全106章の構造 | `./tools/validate_book` が `validated global manifest and 106 written chapter(s)` | pass |
| 章別change/fault教育モデル | `artifacts/learning-contract/chapter-change-fault-20260905.json` の第1〜106章106件 | 106/106基準・変更・故障 pass |
| 実験台帳HTML | `build/html/runner.html` の `id="run-..."` が718件 | pass |
| 第97〜106章の実験導線 | manifestの実験コマンドもHTMLへ含まれる | pass |
| 出典semantic gate | `source-semantic-signoff-verification-20260904.json` の631/631行、`verified=423`、`accepted_boundary=208`、`hold=0`、`gate_complete=true` | pass（出典範囲） |
| Prelude＋106章＋13巻の統合 | 別sessionの現行統合レビューが構造・意味境界・導線・lineage範囲を確認 | pass（範囲限定） |
| 実装受入との境界 | `runner.html` が `command_status=implemented` は入口・契約であり実装本体受入ではないと明記 | pass |
| 範囲限定のhost tool証跡 | `external-acceptance-evidence-20260905.json` がmacOS host run 30件を検査し、第9〜12章4章をhash・版・終了コード・狭い不変条件つきで確認 | pass（範囲限定、measured=false） |
| MiniPy対象外の境界 | 第99章E5/E7が `contract_model_only`、`execution_scope=contract_model_only_not_minipy` | pass |
| HTMLリンク・公開Bundle | `check_public_site.py` と `check_site.py` が失敗0、Pages実URL HTTP 200 | pass |

## 完了扱いにできないこと

- 固定runner 718件は成功しているが、718件すべて `measurement_status=not_run` である。
- canonical artifact 739件は全件 `measured=false` である。
- 章受入台帳は106章・699行のうち、構造確認294行、未実行405行、学習者実行0行である。構造確認は本文・manifest・artifactの形を検査したもので、実験や理解の合格ではない。
- FPGA、SPICE波形、RTL/QEMU、実CPU性能、USB/TTY、block device、NIC、実回路・物理測定は、対応する境界を越えて実行していない。
- 独立レビューのP1/P2判定は、この追補だけでは完了扱いにしない。出典semantic gateと範囲限定のwhole sign-offは完了しているが、外部domain測定、章固有の変更・故障診断、学習者受入は別ゲートである。
- host toolの範囲限定証跡は第9〜12章の狭いprobeに限られる。第13章以降の全domain acceptance、変更・故障診断、FPGA、物理測定へは昇格しない。

## 結論

公開制作版としての構造・HTML・Pages・出典gate・範囲限定の統合確認・教育モデルの現行確認は完了した。一方、学習者向け完成版を宣言するには、未実行の受入・測定・章固有の変更／故障診断が残る。`learner-ready=false`、`measured=false`を維持するのが正しい。
