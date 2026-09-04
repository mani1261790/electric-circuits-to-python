# CH57–106 横断独立レビュー追補（2026-09-04）

## 結論

第57〜106章（第VIII〜XIII巻、50章）を、既存の章別レビューを参照しつつ現行worktreeで横断再確認した。本文、演習、解答、manifest、handoff、sources、runner artifact、canonical、変更課題、故障診断、未実行境界を対象にした。本文/source YAML/manifest/handoff/runner/canonical/signoffの判定変更は行っていない。

現行の局所判定は **P0=0、P1=2系統、P2=0** とする。P1は、(1) CH99のMiniPy実装範囲とmanifestの`implemented`表示のずれ、(2) CH97〜103のgeneric contract/analytic runnerをMiniPy/CPythonの実装検証と誤読し得る境界表示である。CH57〜98の既存局所finding、CH104〜106の構造・trace導線には新たなP0/P1/P2を認めなかった。

プロジェクト共有ゲートとして、対象306 source rowが全件`candidate`、全体ledgerの`semantic_review_pending=631`であること、および全718 runner結果の測定欄が`not_run`であることは残る。したがって、この追補だけで全体の`learner-ready`やsource signoffを成立させない。

## 対象と確認方法

- 対象は`manuscript/volume-08/chapter-57`〜`manuscript/volume-13/chapter-106`の50章。各章の`chapter.txt`、`exercises.txt`、`solutions.txt`、`manifest.yml`、`handoff.yml`、`figures.yml`、`sources.yml`を読み取った。
- 各manifestの実験ID 1〜8、代表入力、必要artifact、期待値、negative testsを確認し、本文の実験カード・演習E1〜E10・解答E1〜E10の入口と対応を突合した。
- 変更課題（故障診断）、条件変更/再挑戦、故障診断手順、未実行/未測定境界の入口が50章すべてに存在することを確認した。変更課題の解答も全章に存在する。
- 既存追補の修正後判定（CH57〜64、65〜72、73〜80、81〜88、89〜96、97〜106）を履歴として参照し、現行ファイルに再度同じ問題が戻っていないことを確認した。過去のhashや修正前P判定は現行値として再利用していない。

## 章群別判定

| 範囲 | 横断確認 | 現行局所判定 |
| --- | --- | --- |
| CH57–64 | MESI/atomic、OoO、cache境界、bus/DMA、電源/熱、boot image。CH59 retire順、CH64 verification例の既存修正後を再確認。 | P0=0 / P1=0 / P2=0 |
| CH65–72 | storage/HID/display/network/assembler/linker/loader。CH70 section bounds、CH72 loader入力の既存修正後を再確認。 | P0=0 / P1=0 / P2=0 |
| CH73–80 | C layout、parser/IR/codegen、debugger/bootstrap、syscall/scheduler。CH77演習導線、CH79 raw PC/return PCの既存修正後を再確認。 | P0=0 / P1=0 / P2=0 |
| CH81–88 | MMU、page fault/COW、filesystem、process、thread、lock。自己採点表とHTML hashの既存修正後を再確認。 | P0=0 / P1=0 / P2=0 |
| CH89–96 | socket/OS統合、syntax/tokenize/scope/bytecode/VM/object。CH89状態文とページ測定の既存修正後を再確認。 | P0=0 / P1=0 / P2=0 |
| CH97–106 | GC、object、function/closure/exception/generator、module/I/O、GIL、adaptive interpreter、MiniPy、RISC-V port、trace atlas、最終mapping。下記P1を維持。 | P0=0 / P1=2系統 / P2=0 |

## 構造・導線の再確認

- 50/50章で必須7ファイルが存在し、YAML parse errorは0件だった。
- manifestは50/50章が実験8件、代表入力8件、required outputs 7件、review gates 4件を持つ。`acceptance_tests`は全章にあり、`negative_tests`も全章にある。
- `exercises.txt`と`solutions.txt`は50/50章でE1〜E10を持ち、10個のE見出しは章内で一致する。各E節の本文は空ではなく、変更課題の解答も存在する。
- figuresは50/50章で6件。全300件が`planned=true`かつ`measured=false`である。これは図の欠落ではなく、図を実測結果と呼ばない現行境界である。
- handoffは50/50章で、CH57の前章56からCH106の前章105まで、前後のchapter/idが連続している。`handoff_status`は50件すべて`planned_pending_runner_and_independent_review`である。runner成功後も独立reviewゲートを完了扱いにしていないプロセス状態であり、runner失敗とは分類しない。

## runner・artifact・未実行境界

### 現行証跡

| 対象 | 現行値 |
| --- | --- |
| `artifacts/runner/full-run-20260904.json` | SHA-256 `16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10` |
| `artifacts/runner/execution-snapshot-20260904.json` | SHA-256 `e1420aed3fafb90804b997b78411917a2ad120e8780551e3707d1edc60333ae0` |
| `artifacts/canonical/index.json` | SHA-256 `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f` |
| `environment/lock.yml` | SHA-256 `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c` |
| `reviews/source-ledger-verification-20260903.json` | SHA-256 `117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741` |
| `tmp/page-counts.json` | SHA-256 `fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb` |

`full-run-20260904.json`は全718件が終了コード0（718/718、失敗0）。対象CH57〜106は400件で、`contract_model_verified=322`、`analytic_verified=56`、`domain_verified=15`、`educational_model_verified=7`、終了コード0が400/400、`measurement_status=not_run`が400/400だった。全体のverification内訳はcontract 548、analytic 127、domain 26、educational 17である。

canonical indexは739 artifact entriesで、739/739が`materialized=true`、`measured=false`、`status=executed_analytic`。対象範囲は395 entriesだが、そこから参照されるrunner artifactは400実験分すべて揃っており、参照された実ファイルのSHA不一致は0件だった。`execution-snapshot`は現行runner SHA、718件、718成功、0失敗、固定Docker image `electron-to-python-runner:bookworm`（amd64）を指す。

ページ測定JSONは106章、本文3,514頁、先行一周11頁、合算3,525頁、各章24〜40頁、24頁未満0。対象CH57〜106は50章・1,718頁・33〜36頁である。これはページ数とHTML hashの機械的証跡であって、内容のsource semantic passや外部実測の証明ではない。

### trace B〜Fの現在判定

既存レビューに残っていた「trace B〜Fが未実装/未検証」という表現は、現行状態にはそのまま適用しない。`tools/trace_atlas.py`にB〜Fの実行関数があり、保存済みartifactは次のとおり全チェック通過している。

| artifact | checks | event数 | 現行の観測範囲 |
| --- | ---: | ---: | --- |
| `artifacts/trace-B-list-construction.json` | 10/10 | 13 | MiniPy list/object教育模型。cache/VM/DRAM等は未実行・適用外。 |
| `artifacts/trace-C-range-loop.json` | 10/10 | 1,010 | `sum(range(1000))`と1000反復の入力由来loop模型。pipeline/cache/timeは未実行。 |
| `artifacts/trace-D-file-input.json` | 13/13 | 8 | 一時regular fileのhost read。block device/physical storageは未実行。 |
| `artifacts/trace-E-device-input.json` | 13/13 | 8 | 供給stdinのhost operation。TTY/keyboard/USB deviceは未実行。 |
| `artifacts/trace-F-network-output.json` | 13/13 | 8 | host loopback TCP send/receive。packet capture/NIC/physical linkは未実行。 |

各artifactの`measured=false`、eventの`measured=false`、parent chain、source referenceは整合している。したがってB〜Fのartifact欠落は現行P1ではない。一方、これらをCPython完全互換、実CPU/cache/DRAM、実OS device、実NIC、物理測定へ昇格する根拠はなく、下位層の未実行境界は共有P1として残す。

## 未解消finding

### P1-CH99-MINIPY-SCOPE

`manuscript/volume-13/chapter-99/manifest.yml:219-260`は、E5 `finally cleanup`とE7 `generator suspension`を`command_status: implemented`、`status: executed_analytic`として記録する。しかし現行MiniPy compilerは`projects/minipy/runtime.py:424-426`で`try/finally`を拒否し、`machine-spec/minipy-language.md:36-38`でもgeneratorを必須範囲外としている。E5/E7のrunner artifactが`contract_model_verified`でも、それはmanifestから作った一般契約モデルの通過であり、MiniPy runtimeがfinally/generatorを実行できることの証明ではない。

これは本文の概念説明が直ちに誤りというfindingではない。本文自身がMiniPy subsetとCPython/発展機能を分けているため、manifestの`implemented`を「実装・受入済み」と読む学習者への境界表示P1である。解消には、実装するか、E5/E7を明示的なanalytic/out-of-scope契約へ分類し、期待値・runner status・演習の実行範囲を同じ語彙へそろえる必要がある。

### P1-ANALYTIC-RUNNER-BOUNDARY

`tools/experiment_driver.py:381-464`は、章固有実装がない場合に`projects/domain_models.py`の入力由来契約モデル、またはmanifest analytic fixtureを用いる。`tools/experiment_driver.py:225-317`でMiniPy/host operationへ入る専用縦断はCH104およびCH105の一部に限られる。従ってCH97〜103の`contract_model_verified`/`domain_verified`/`analytic_verified`は、GC・GIL・JIT・module/I/O・CPython比較を実行したという意味ではない。

本文とartifactには未実行・非測定境界が多数明記されており、runner自体の失敗ではない。ただしmanifestの全実験が`command_status: implemented`で、実行モード名も学習者がdomain実装済みと読み得るため、CH97〜103の「入力由来モデルの検証」と「MiniPy/CPythonの実装受入」を分離した表示が必要である。

### 共有P1-SOURCE-SEMANTIC

CH57〜106のsource rowは306件で、306/306が`status: candidate`、305/306が`accessed_for_this_draft: false`（trueはCH92 tokenize行の1件のみ）、claim locatorを持つ行は11件に留まる。CH97〜106の62件は全件candidate・未アクセスで、claim locatorは3件だけである。CH100〜104のlanguage/CPython候補には、例えば「language subset and version to be fixed at source gate」「source tag/build option to be fixed at source gate」という記述的locatorが残っている（各sources.ymlのcandidate行）。CH93の`src-93-symbol-table-candidate`も`MiniPy-0.1 / minipy-reference-0.2`という混在版表記を保持している。

current ledgerは機械的locator/cited_in検査として`rows=631`、`locator_ok=533`、`cited_in_ok=631`、`semantic_review_pending=631`を記録する。これらの数値は到達性を示すが、本文claim・採用版・公式節の意味対応を完了した証跡ではない。source YAML本体はこの追補で変更していない。

### 共有P1-EXTERNAL-MEASUREMENT

固定Linux Docker runnerは再現可能な契約・解析・教育模型を718/718実行したが、全718件が`measurement_status=not_run`である。対象CH57〜106の400件も同じで、SPICE波形、RTL/形式検証、QEMU/xv6実行、実CPU性能、FPGA、実回路、keyboard/USB、block device、NIC/packet、物理測定の完了を意味しない。trace D/E/Fのhost filesystem/stdin/loopback operationはそれぞれ境界内のhost operationであり、下位device・physical layerの観測ではない。

## 判定と次ゲート

- 本追補の対象範囲に新たなP0はない。
- 既存の章別局所findingは修正後に再発しておらず、CH57〜98およびCH104〜106の局所P0/P1/P2は0とした。
- CH99の実装範囲表示とCH97〜103のgeneric runner境界を、対象範囲のP1 2系統として維持する。
- source semantic、外部domain/物理測定、全106章・13巻・全体の統合signoffは共有P1として維持する。
- signoff YAMLの自動昇格・decision変更は行っていない。次の判定には、MiniPy scope/statusの明示、公式sourceの版・claim locator意味照合、外部domain測定の別証跡、全体統合reviewが必要である。

