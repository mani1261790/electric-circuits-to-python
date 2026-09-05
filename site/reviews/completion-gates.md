# 完成ゲート台帳

この台帳は、HTML正本を学習開始可能と呼べるかを、解析runnerの合格と混同しないための記録である。

## 現在合格しているもの

- 先行一周と第1〜106章、各章7成果物、演習・解答、handoffが存在する。
- 固定Linux `linux/amd64` image、runner、adapter、Dockerfile、canonical indexのhashが `environment/lock.yml` と一致する。
- `book run` は718実験を終了コード0で実行し、`analytic_verified` 127件、入力由来の `contract_model_verified` 553件、`domain_verified` 26件、`educational_model_verified` 12件（MiniPy・minios・rv32edu）を保存する。
- Docker VM復旧後、`tools/run_all_experiments.py`で718/718件を固定runnerから再実行し、終了コード0を `artifacts/runner/full-run-20260902.json` に保存した。adapter 0.5では時刻・host固有値をartifactから除き、同じpayloadの再実行で同じSHA-256になる `execution.reproducible=true` を固定した。さらに代表入力の構造・不変条件を検査する `projects/domain_models.py` を契約モデルとして統合した。各artifactの `measurement.measured=false` / `measurement.status=not_run` とcanonical lineage hashを再検査し、canonical indexのhashをlockへ反映した。
- 718件すべてで `measurement.status=not_run`、`measurement.measured=false`、`analytic_prediction.measured=false` を維持する。
- canonical artifact indexは720件で、実ファイル、runner lineage、SHA-256、未実測境界を記録する。
- `tools/validate_book`（uvでPyYAML 6.0.3を取得）、`./tools/build_html`、Python構文検査、shell構文検査が通る。固定runnerの入口も`tools/book`へ統一した。
- `tools/test_domain_models.py` は625件の代表入力を走査し、536件の入力由来契約モデルを誤判定0件で検査した。モデルは構造・不変条件だけを扱い、外部tool・実測値へ昇格させない。
- `case_ref`を持たない古いmanifestでも、実験直下の`inputs`を代表入力としてpayloadへ保存するフォールバックを追加した。これにより第20〜24章などのinline入力も、期待値だけでなく入力hash・契約モデルの系譜を追跡できる。
- HTMLは本文107、演習・解答212の321文書で、見出しID、内部リンク、用語リンク、キーボード操作、数式span、runner718件を検査済み。
- 第3章AMAT、第7章連続の式、trace-AのAST/AddおよびCPU→UART因果経路は、独立レビュー指摘後に修正して再実行した。
- 第33〜40章の別session独立追補では、第39章counterの期待値不整合（CH39-P1-01）を修正後に再照合し、同範囲のP0/P1/P2を0/0/0と確認した。全体の実ドメイン実験・一次資料照合・章/巻/全体統合確認は別ゲートとして残る。
- 第45章・第50章では、RV32Iのレジスタ/命令/抽象メモリ演習とboot ROM・UART・JAL停止条件を、チェックイン済みのrv32edu教育モデルで実行した。
- 第104章5では、`projects/minipy`、`projects/minios`、`projects/rv32edu`の実行可能教育モデルを同じtrace-A入力で動かし、MiniPy stdout、minios syscall、RV32I ADD、UART出力とイベントIDの因果鎖を検査した。
- 第104章8では、同じ三実装の未対応構文・未知syscall・未割当store・STATUS/ROM書込みをfail closedで診断した。
- trace registryは実装で使う `trace-{entry_letter}-{slug}` 形式と単体APIの既定値を明記し、symbol registryはchapter-localの重複glyphをID・文脈で区別する規則と全グループを明記した。lockのsymbol registry hashも更新済みである。

## まだ合格と呼べないもの

- 現在のrunnerの大半はmanifestの解析式・期待値の再生である。`educational_model_verified` はチェックイン済みのMiniPy・minios・rv32edu教育モデル、`domain_verified` は章固有の決定的モデルであり、いずれも外部実験とは別である。第24・32・92章の代表ケースはホスト外部実行を追補し、公式xv6-riscvのkernel→init→shell起動もmacOSホストQEMUで確認したが、全章のdomain実験、固定runner内の完全OS経路、FPGA基準board、実回路は未実行である。
- 外部ツールの導入後、CPython 3.14.7、ngspice-47、Verilator 5.050、Icarus 13.0、Yosys 0.68+postで、第24・32・92章の代表ケースをホスト実行した。さらにQEMU 11.1.1 / `riscv64-elf-gcc` 16.2.0で公式xv6をビルド・起動した。コマンド・版・ログ・出力は `reviews/external-domain-host-runs.md`、`reviews/external-xv6-host-run.md`、`artifacts/external/host-20260902/index.json`、`artifacts/external/xv6-host-20260902/index.json` に隔離している。ただしこれは固定Linux runnerの718件の測定昇格ではなく、FPGA基準board・実回路・シリコン測定、全章対応付け、独立確認が残るため、P1-01は未解除である。
- いったんDocker daemon不応答（VMログの `no space left on device`）で停止したが、Docker Desktopを再起動して復旧した。lockのimage digest（`sha256:daccf702...`）一致、代表実験、第1〜106章の718件全件再実行を確認した。初期障害の診断は `reviews/docker-environment-diagnostic-20260902.md` に履歴として残し、現行の固定runner再現ゲートは解除済みとする。
- 基準組版量はケースブック追補後に測定済み・達成である。固定Headless ChromeのLetter条件で、先行一周を含む本文107件は3,522頁、本文106章は合計3,511頁、平均33.12頁、最小24、最大40、24頁未満0章となった。演習・解答は補助教材として987頁を別掲し、本文総量の3,150〜4,150頁へ二重計上しない。詳細は `reviews/page-volume-report.md` に記録した。
- `accessed_for_this_draft:false` の一次資料・版固定は、出典候補の台帳であり、全章の一次資料照合完了を意味しない。
- 公式資料の部分照合（Python 3.14 AST/dis/tokenize、ngspice、Verilator、Yosys）を `reviews/primary-source-fetch-log.md` に記録し、該当entryだけ `accessed_for_this_draft:true` とした。全章・全sourceの照合ではないため、一次資料ゲートは未完了のままである。
- 2026-09-02に候補URLを整理し、現行63種類を自動取得したところ51種類の2xx/3xx本文を得た（source行では166行中145行）。最終URL・タイトル・本文SHA-256・関連語ヒットを `reviews/source-content-evidence-20260903.{json,md}` へ保存し、旧URL、404、redirect-only、出版社ページの内容不一致も記録した。これはlocatorと取得本文の固定を強める追補であり、主張・版・節の意味照合や `accessed_for_this_draft:true` への昇格ではない。
- 全source URL 66種類の読み取り専用到達性を調べ、51件の2xx/3xx、15件の404/拒否を `reviews/source-url-probe.md` に記録した。到達性は内容・版・節の照合ではないため、未確認sourceを学習根拠へ昇格させない。
- 別sessionの独立全体レビューは保存済みだが、章ごとの確認、巻統合確認、全体統合確認をすべて完了した状態ではない。
- 別sessionによるページ測定追補は、ケースブック追補後の集計と「固定条件で測定済み・達成」という状態更新を確認した（`reports/independent-full-book-review-page-followup.md`）。
- 最新の別session追補監査は、ページ測定、uv入口、外部ホストhash、lock整合を再確認した（`reviews/independent-current-followup.md`）。同監査のP1（全章domain/環境再現/一次資料・独立確認）は残存するが、ページ測定JSONのprelude row/hash、依存のsingle source、履歴ラベル、外部追補のoutput hash schemaは更新済みである。
- 最新追補の再確認ではP2なし、現行HTML 107 rowのhash不一致0件である。P1は全章domain・一次資料・章/巻/全体の独立確認の2件に限定され、`learner-ready`判定は未解除である。
- 同じ別sessionのP2追補は、trace ID形式の統一、duplicate glyph 18組とchapter-local scopeの完全一致、重複3組のcanonical ID統合、lock hash一致を確認し、final-7のP2を解消と判定した。
- manifest、図、source、symbol registryの台帳境界は正規化済みだが、一次資料を実際に照合したことを示す `accessed_for_this_draft:true` にはまだしていない。
- 出典台帳627行について、ローカルlocator、URL本文取得、`cited_in` の機械的突合を `reviews/source-ledger-verification-20260903.{json,md}` へ保存した。現行証跡ではURL行166件のうち145件を取得本文へ対応し、具体的なローカルlocator 196件のうち152件は実体へ対応した（残りは計画上の説明文）。全行の `semantic_review` は `pending` のままで、主張・版・節の独立照合へは昇格させていない。

したがって、現在は「非公開の解析検証済みドラフト」であり、`CONTEXT.md` の **学習開始可能** ではない。残る外部ドメイン実験、一次資料の実照合、章・巻・全体の独立確認を完了し、独立レビューの未解決指摘が0件になった時点で、学習開始可能へ状態を更新する。

## 2026-09-04 現行スナップショット（ローカルプレビュー継続中）

出典台帳を再生成し、現行 `reviews/source-ledger-verification-20260903.json` は 631 行、claim-bearing locator `171/171`、`cited_in` 解決 `533/533`、生成 `2026-09-04T02:14:48Z`、SHA-256 `470163ac42954cb9ad459e1b252a528cfd1c783581ad7e5ca079e35a7d4ffd2e` となった。執筆セッションとは別の独立確認セッションが ordinal 21、32、および 64–139 の現行版・直接locator・本文対応を再読し、sign-off checker の現行分類は `verified=339 / accepted_boundary=187 / hold=105`、被覆631/631、形式エラー0である。`gate_complete=false` と `semantic_review=pending` 631行は維持している。

HTML正本は `build/html/` に再生成済みで、Prelude＋106章＋演習・解答の321文書、内部リンク44,136件、欠落0、bad fragment 0を確認した。固定条件のページ測定はPrelude 11頁、本文3,514頁、合算3,525頁、各章24–40頁、107/107 HTML hash一致である。固定runnerは718/718成功、canonicalは739件、全件`measured=false`、runner測定`not_run`である。

独立全体統合レビューは構造106/106、schema errors 0、registry参照全解決、runner/canonical/lock整合、HTML導線を再確認した。P0=0。P1はsource semantic hold105行とPrelude＋106章・13巻・全体の意味sign-off未完、P2はCH4 S3のbase URL取得境界と、未選択FPGA・trace D/E/F下位層の未実行境界であり、`learner-ready` は保留のままとする。

ローカル確認用サーバーは `127.0.0.1:8765` で稼働中で、入口は <http://127.0.0.1:8765/>。これはlocalhost限定で、外部公開・デプロイはしていない。

## 12. 量子井戸数値の再計算後スナップショット

確認日: 2026-09-03（Asia/Tokyo）。第13〜15章で共通参照していた1 nm無限量子井戸の準位を、本文に明記した `ℏ=1.054571817×10^-34 J s`、`m_e=9.1093837×10^-31 kg`、`L=1.0×10^-9 m` から再計算した。現行値は `E_1=6.0247×10^-20 J≈0.3760 eV`、`E_2≈1.504 eV`、`E_3≈3.384 eV` である。第13〜15章の本文、演習、解答、manifest、handoff、図台帳をこの値へ統一した。

修正後に全718実験を再実行し、718/718成功・失敗0を確認した。canonical artifact index（720件）を再マテリアライズし、`environment/lock.yml` のcanonical index hashを `f7b141eee94f1801b0748bdfebe662f2afe8b0f314fbeab3af3c17917a1913a5` へ更新した。HTMLも再生成・再測定し、本文3,511頁、先行一周11頁、合算3,522頁、各章24〜40頁、hash不一致0件を確認した。

この修正は数値の内部整合性を直すもので、718件の `measurement.status=not_run`、全627 source rowの `semantic_review=pending`、別sessionによる全106章・13巻・全体統合未完というP1境界は変更しない。したがって、P0=0、残存P1=2領域、P2=0、`learner-ready`不可である。

## 13. 第9・11章修正と外部SPICE追補後スナップショット

確認日: 2026-09-03（Asia/Tokyo）。第9章では、現行の式レジストリに登録済みの
`lossless_wave_equation`、`lossless_line_wave`、`characteristic_impedance`を本文とhandoffで
明示し、固定runnerの実装・実行済み状態（ただし測定ではない）へ説明を更新した。第11章では
`artifacts/chapter-11/netlists/rc-transient.cir` と `rlc-transient.cir` を実体化し、ngspice-47で
両方を終了コード0で実行した。RC 5,091行、RLC 5,098行のCSVと、コマンド・ツールログを
`artifacts/external/host-20260902/`へ隔離して、入力hash・出力hash・ログhashを記録した。
この外部追補は`source_kind=external_tool_run`、`measurement.status=external_tool_output`、
`physical_measurement=false`であり、固定runnerのcanonical artifactや実回路測定値へ昇格させない。

修正後に固定runner 718/718件（失敗0）を再実行し、canonical index 720件を再マテリアライズした。
HTMLは107 main + 212 companionを再生成し、Chrome headless/Letter計測は先行一周11頁、本文
3,511頁（106章）、合算3,522頁、各章24〜40頁、24頁未満0章となった。空PDFを再試行する計測
保護も追加した。現行識別hashは次の通りである。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `8ab240fa0add4d6809f1c3944969a603f41cf1fe34d0ddb3843abe6e31b07de2` |
| `artifacts/canonical/index.json` | `6db424a40e2d618a94bdea1442ca51ad94f75b10de982d45d8e758f05c38cf23` |
| `environment/lock.yml` | `4bc22265795f1b56a4601b73faf41824dead2cc82e84009feafa9d6a10d148e6` |
| `tmp/page-counts.json` | `64822a1b1c638e2c1de9aeec1b32aafd66ce83eb9a5a487e4b77187bbd5c4494` |
| `artifacts/external/host-20260902/index.json` | `110588f8cbd526e9f66da5836a7932c7a5e0ce20816c2b74b656aec163b7172f` |

独立reviewの残りは、出典627行の意味照合、全章の外部domain/実測、章・巻・全体統合確認である。
第9章のP2指摘は解消し、第11章のnetlist不足も解消したが、これらの共有P1ゲートは継続する。

## 14. canonical directory materialization追補

第11章のnetlistディレクトリに実体ファイルが存在することをcanonical indexでも明示するため、
materializerが`.artifact-metadata.json`以外の具体ファイルを含むディレクトリを
`materialized:true`として扱い、相対pathと内容からディレクトリhashを計算するよう更新した。
第4章の既存ディレクトリartifactも同じ規則で再計算した。現在の第11章netlist recordは
`materialized:true`、RC/RLC入力のhashは外部ngspice indexの各recordと一致し、測定値への昇格はない。

再マテリアライズ後のSHA-256はcanonical indexが
`24dab904ae0df761f0f44b819c6f38aef3835b3677325a2d25ffe5d481d7c616`、
`environment/lock.yml`が`1ebfdd24a8b6a69872238c55c19f88130769531c73427eaffbabb699e9ae30f0`である。
固定runnerの718/718成功、HTMLの3,522頁、source ledger 627行のsemantic review pending、
全章domain/一次資料/章・巻・全体統合の未完境界は変更しない。

## 15. 最終manifest反映後スナップショット

確認日: 2026-09-03。第11章のcanonical artifact種別を`calculation_output`、`simulation_input`、
`visualization_output`へ整理した最終manifestを固定runnerへ反映し、718/718成功で再生成した。
canonical indexとlockを更新し、HTMLを再生成・全107行再測定した。現行HTMLとのhash不一致は0件である。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `5bfa83c5279bdd0eb4f5c5e5952359384de56031e868aabebb92a59bf7250ae3` |
| `artifacts/canonical/index.json` | `5deb1271d4dd224cbbd119c467b55f59cce1a3cfb54d94ede33a152891643afe` |
| `environment/lock.yml` | `70e7ed6ceaa8da4875d2ebbf47e6cd6c5eb88e693a14c9c8c236a31adb45e49c` |
| `tmp/page-counts.json` | `eb56a589260165d76a7c9b3e660d4bfcefb6e1d4b922dc40b9a8a94a22357370` |
| `artifacts/external/host-20260902/index.json` | `110588f8cbd526e9f66da5836a7932c7a5e0ce20816c2b74b656aec163b7172f` |

ページ計測値は先行一周11頁、本文106章3,511頁、合算3,522頁、各章24〜40頁、24頁未満0章。
`test_domain_models.py`（625代表入力、536 modeled、failures 0）と`validate_book`も通過した。
独立reviewは、第9章registry/runner、第11章netlist・ngspice・canonical/HTML整合をP2/P1解消と確認し、
残存P1を全章外部domain・一次資料意味照合・全106章/13巻/全体統合の2領域としている。

## 16. HTML導線の現行機械監査

旧レビューに残っていた「後半章のexperiment-panel不足」「runner台帳が一部のみ」という指摘を、
現行生成物で再検査した。全manifest実験718件について、各章HTMLに対応する`book run <chapter> <id>`
があること、`runner.html`の`run-<chapter>-<id>`が718件と1対1で一致することを確認した。
用語リンクのhref内への入れ子`<a>`も全HTMLで0件だった。現行値はmanifest experiments 718、
runner rows 718、missing 0、extra 0、chapter command issues 0、nested href anchor 0である。
この監査はHTML導線のP2を解消するが、外部domain実験・一次資料意味照合・章/巻/全体統合のP1は解除しない。

## 17. 第1〜8章独立レビュー後の修正スナップショット

確認日: 2026-09-03。別sessionの第1〜8章レビューで挙がった局所指摘に対して、第1章のtrace-A、本文表記、固定runner artifactの内容を修正した。

- 第1章のCPU列を `addi x8,x7,48` とし、`ADD`の結果 `x7=3` からASCII `0x33`を作るデータ依存へ変更した。`tools/cross_layer_trace.py` と `projects/rv32edu/core.py` はレジスタ読み出しと推移的な `data_dependency_event_ids` を記録し、traceの `uart_data_depends_on_add`、実行可能stackの同名検査を追加した。現行traceの全checkはtrueである。
- 第1章のAST表記を `Call(func=Name("print"), args=[...])` へ統一した。第5章では導体の静電誘導（electrostatic induction）と誘電体の分極（polarization）を別概念として定義した。
- 第1〜8章のrunner記述とmanifest受入条件を、固定runnerの解析・契約再生済み、domain未実行、外部測定未実施という現行状態へ同期した。生成済み解析artifactの `availability` と `planned` も更新した。
- `tools/materialize_canonical.py` は、各canonical artifactへrunnerの入力hash、計算結果、検証状態、測定境界を格納するよう更新した。ディレクトリartifactには `runner-results.json` を追加し、実測・外部tool結果とは明確に分離した。第1〜8章の旧「メタデータだけ」のP1は、この内容追補で局所解消した。ただし外部domain／実測ゲート全体は未解除である。
- 修正後に固定runner 718/718件を再実行し、失敗0。`validate_book` と `test_domain_models`（625代表入力、536 modeled、失敗0）、HTML再生成・Chrome測定（本文3,511頁、先行一周11頁、各章24〜40頁、24頁未満0）を完了した。

現行識別hashは次の通りである。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `1a5c75c5fd6956456cbb28296b6cfc5c0109ab1cf3342a76ada0c1e959c5d3dc` |
| `artifacts/canonical/index.json` | `91c33b76a22331c47b58a55f5efe25fd4aa9f0468c89183baa05d6f51636d712` |
| `environment/lock.yml` | `0b6b2f016812672ed7d4486b869c6898982fdd04cd5f0e5da17775c4147dbfbf` |
| `tmp/page-counts.json` | `e2bfe44828d46b275705518c73831604468ad34d8c87ec282f36b39915a5f07f` |
| `artifacts/trace-A-print-1-plus-2.json` | `d6de0438680f9c4929e53cf83271bda926805391701e6e10798f7f1e0e384a68` |

局所修正後も、全106章の外部domain実験・変更課題・故障診断、一次資料627行の意味/版/節照合、全106章・13巻・全体の別session統合確認は残存P1である。`learner-ready`はまだ不可とする。

## 18. 第1〜8章ホストCPython probe追補

2026-09-03、ホストCPython 3.14.7で第1〜8章の基礎計算probeを実行した。AST/bytecode、整数境界、次元契約、Euler更新、電場、平行板、連続の式、導電率を各1件ずつ検査し、外部host indexは18 runs・全コマンド成功となった。入力スクリプト、コマンドログ、JSON出力、hashは `reviews/external-domain-host-runs.md` と `artifacts/external/host-20260902/index.json` に記録した。

これはCPythonの外部tool出力を追加したもので、章全体のdomain実験、SPICE/RTL/QEMU、FPGA、実回路・シリコン測定を完了したことを意味しない。固定runner 718件の `measurement.not_run` と、全章外部domainゲートの未完了境界は維持する。host index SHA-256は `ff58d84f3058a971a15b3d677a07da443d1885643b7c2b00ab27a0eb55361412` である。

## 19. canonical Python artifactの構文修正

第1〜8章の独立追補確認後、canonical materializerが生成する`.py`成果物の説明文字列を三重引用符へ修正した。これにより、`executable_source_excerpt` と宣言された全artifact Pythonファイルを `python3 -m py_compile` で検査できる状態にした（`artifact-python-syntax-ok`）。計算結果、入力hash、検証状態、`measured:false` の境界は維持している。

修正後のSHA-256は `tools/materialize_canonical.py` が `e9ef4f66c362787c2de32e01dde9925439c9851663af456f4428218a81b55e2d`、canonical indexが `3b7a7a3629011c48c74bd72476f91397597bbc9a39af6f95196f3832c591466c`、lockが `16b4df707ffcfc9dd78133686e9c865ee29324b3cdcb7d2d5df184bbcf8690c5` である。`validate_book` は106章で成功した。

これは成果物の構文・内容品質を直す局所修正であり、全章外部domain実験、一次資料の意味照合、全106章/13巻/全体の別session統合という共有P1は残る。

## 20. 生成Python構文の独立追補確認

2026-09-03、執筆セッションとは別の確認セッションが、materializer修正後の生成Pythonを再確認した。`artifacts/**/*.py` 35ファイルの `python3 -m py_compile` は失敗0件、canonical indexは720件、うち `runner_results` 付き705件、`measured: true` 0件であった。materializer・canonical index・environment lockのhashも一致した。

この確認で第1〜8章の局所P0/P1/P2はすべて0と判定したが、全章の外部domain実験・変更課題・故障診断、一次資料627行の意味・版・節照合、全106章・13巻・全体統合確認は未完了である。したがって `learner-ready` は解除しない。

現行識別hashは次の通りである。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `1a5c75c5fd6956456cbb28296b6cfc5c0109ab1cf3342a76ada0c1e959c5d3dc` |
| `artifacts/canonical/index.json` | `3b7a7a3629011c48c74bd72476f91397597bbc9a39af6f95196f3832c591466c` |
| `environment/lock.yml` | `16b4df707ffcfc9dd78133686e9c865ee29324b3cdcb7d2d5df184bbcf8690c5` |
| `tools/materialize_canonical.py` | `e9ef4f66c362787c2de32e01dde9925439c9851663af456f4428218a81b55e2d` |

同日の出典URL再収集では、unique URL 63件中51件を取得し、source row換算145件となった。出典台帳の `locator_ok` は297件だが、意味・版・節の独立確認は627行すべて `semantic_review: pending` のままである。この更新は到達性の証跡だけを新しくしたもので、一次資料ゲートの合格を意味しない。

再収集後の識別hashは、`reviews/source-content-evidence-20260903.json` が `d7f2625bd79d181a5235266768f836cf32c2403cc0e8dad5938c619ea558afb62`、`reviews/source-ledger-verification-20260903.json` が `058100b84921d290f8c8c32d5992b2e6642f117b2baa192018afe7bce3117cf0` である。

## 21. 第5・6章のCODATA 2022値統一

独立確認で指摘された真空の誘電率の不一致を修正した。本文・演習・解答、解析adapter、ホストCPython基礎probeを `ε0=8.8541878188×10^-12 F/m`（CODATA 2022）へ統一し、固定runner 718件を再実行、失敗0件を確認した。canonical artifact、HTML、ページ測定も再生成した。第1〜8章の局所P1は解消したが、locator記法と`cited_in`追跡不足のP2、および全体共有P1（全627行の意味照合、全章domain、全106章・13巻・全体統合）は残る。

修正後の主要hashは次の通りである。

| 対象 | SHA-256 |
|---|---|
| `tools/experiment_driver.py` | `d7963fad09d46afc8f8989dc3f275e8eeb6b1d1eea5591a8bc795bfd647343fe` |
| `artifacts/runner/full-run-20260902.json` | `954c1faa0d98a88c74973f0a81f327b487a80e3b576b1f2aff0154df637a0841` |
| `artifacts/canonical/index.json` | `c87d99e14f275af2e3357460e21ff02dffa6b4e73c2f17417c06193ed38c2aa9` |
| `environment/lock.yml` | `8723d5c776cd7d96aa7ca48ecd8454471ab59feb9838edd99c89eab1e7e7fdc7` |
| `tmp/page-counts.json` | `88037cce5b80bc0d27262ecc1a841f1b2050f130cbd060679285b3cdbe158261` |
| `artifacts/external/host-20260902/index.json` | `52df623fd2feb2b1babc197223118d0717acef3fdf01679308b395486f83e9e4` |

## 22. 第20・21章のε0波及修正後再生成

第5・6章で採用したCODATA 2022の真空の誘電率を、第20・21章の半導体デバイス例にも
反映した。本文、演習、解答、manifestの入力・期待値を更新し、固定runnerを再実行した。
全718件が終了コード0で、canonical artifactとHTMLを同じ入力から再生成した。HTMLのページ数は
先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0章である。

| 対象 | SHA-256 |
|---|---|
| `tools/experiment_driver.py` | `d7963fad09d46afc8f8989dc3f275e8eeb6b1d1eea5591a8bc795bfd647343fe` |
| `tools/external_host_runs.py` | `d87048a1f7120c06c74d7dd609350a53de5501366cd768be9df89b570f501a20` |
| `artifacts/runner/full-run-20260902.json` | `3996201a86606b83da443eaaa29267e6b52fa85996a6bd94ed27edb62d9b35d0` |
| `artifacts/canonical/index.json` | `a47fcae1a62e1ea2f2bf7771b518debe328baad130cf0c85522ac17979280fec` |
| `environment/lock.yml` | `b396ced5169095e1d152c204d12118e5e855ba28bb8c32b00b3f4eb67677bd73` |
| `tmp/page-counts.json` | `f4e55ed86a0b9323419c244628cad86575d83cd1e90d726b268626388e681b5d` |
| `artifacts/external/host-20260902/index.json` | `48d8f9cc5af9e6842774810688c983e4580b65d0db39ea3d952643d0405ce39d` |

旧ε0の文字列は現行の本文・manifest・実行adapterから除去され、今回の第20・21章を含む
固定runner成果物も更新済みである。これは数値・成果物系譜の局所修正を完了した記録であり、
全718件の測定not_run、全627 source rowの意味・版・節照合、全106章・13巻・全体の
別session統合確認、FPGA・実回路・シリコン境界という共有P1を解除しない。

## 24. 出典台帳の明示locator範囲検査（2026-09-04）

`tools/verify_source_ledgers.py` に、主ロケータとは別に、各source rowの明示 `locator` に書かれたローカルファイルと行範囲を検査するチェックを追加した。ファイル列を省略した `machine-spec/a.md・b.md` のような表記も扱う。現行台帳では明示locator 265件中有効265件、範囲外0件を確認した。

この機械検査はファイル・行範囲の存在を保証するだけで、一次資料の主張との意味対応、採用版、節単位の独立確認を済みとはしない。`semantic_review=pending` は維持する。

## 25. 外部host代表実行の再確認（2026-09-04）

`python3 tools/external_host_runs.py` を再実行し、CPython 3.14.7、ngspice-47、Icarus Verilog 13.0、Verilator 5.050、Yosys 0.68+postを使う代表30 runsがすべて終了コード0となることを確認した。記録は `artifacts/external/host-20260902/index.json` にある。これらは固定runnerの718件を置き換えず、実測、FPGA、実回路、シリコン測定、全章のdomainゲートへは昇格しない。

## 23. 出典locator正規化後の最終再測定

第1章S4の `cited_in` にあった配列添字付き表記を、監査器が解決できる
`manifest.yml:experiments` へ正規化した。出典台帳を再生成し、`cited_in_ok` は545行へ
増加した。意味・版・節の独立確認は自動昇格せず、627行すべて `semantic_review: pending`
を維持する。出典表示を含むHTMLを再構築・再測定し、ページ数と全107行のHTML hashを再確認した。

| 対象 | SHA-256 |
|---|---|
| `reviews/source-ledger-verification-20260903.json` | `27eea61dcd872aef264b3a479361850d023bbbede1832b9baf52e00c42ca6e83` |
| `tmp/page-counts.json` | `c6c15b22a2c67369b39ce94ceed296fac148bf9665d8257205c170035dcff227` |
| `artifacts/runner/full-run-20260902.json` | `3996201a86606b83da443eaaa29267e6b52fa85996a6bd94ed27edb62d9b35d0` |
| `artifacts/canonical/index.json` | `a47fcae1a62e1ea2f2bf7771b518debe328baad130cf0c85522ac17979280fec` |
| `environment/lock.yml` | `b396ced5169095e1d152c204d12118e5e855ba28bb8c32b00b3f4eb67677bd73` |

現行測定値は先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0章、
HTML hash不一致0件である。局所P2（locator記法）は解消したが、`cited_in` の空欄を含む
意味・版・節の全件照合、全718件の測定not_run、全106章・13巻・全体の別session統合確認、
FPGA・実回路・シリコン測定は未完であり、`learner-ready`は解除しない。

## 24. 第9〜16章ホスト解析probe追補

第9〜16章（第11章はngspice追補済み）の代表解析probeをCPython 3.14.7で実行し、
外部host indexへ追加した。現行host indexは25 runs・全コマンド成功、SHA-256は
`81f39211523562c87ffcde08b33a079d68b688c9aa01b3bbf812ef82f263bf80` である。
第9章の線路モデル、第10章のMNA残差、第12章のDFT・雑音・反射、第13〜16章の
有限差分・固有値・Fermi分布・tight-bindingをJSON出力として保存した。これは代表解析の
再現性を増す追補だが、全章のdomain実験、固定runnerの測定not_run、FPGA・実回路・
シリコン測定、一次資料・独立統合ゲートは解除しない。

## 25. 第17〜21章半導体probe追補

第17〜21章の中心式をホストCPython 3.14.7で再計算し、host indexへ追加した。真性
キャリア、ドーピング電荷中性、drift-diffusion、p-n接合、MOS容量の5 probeはいずれも
終了コード0である。現行host indexは30 runs・全コマンド成功、SHA-256は
`6740d1e9d6b8e030f91fb98ba53cb419a66cd84295bfe4558852ab1a4b6d1066`。
解析probeは固定runnerの測定値や半導体試料・FPGA・実回路・シリコン測定を代替しない。

## 27. 第21〜23章のCODATA連鎖値修正後の再実行

第21章で採用した酸化膜容量の更新値を起点に、第22章の線形・飽和MOS電流、相互コンダクタンス、
第23章のチャネル長変調・速度飽和上限までを再計算した。`C_ox=0.0034531332493319996 F/m^2`、
`I_D,sat=0.00032315269763958363 A`、`I_D(lambda)=0.00034900491345075035 A`を本文・演習・解答・
manifestへ伝播し、仕事関数差は`phi_F`→`phi_s`→`phi_ms`の順に再現できる説明を追加した。

修正後、固定runner 718件を再実行して718/718成功・失敗0を確認した。manifestとrunnerの実験ID差分、
runner成果物hash不一致、canonical lineage不一致、`runner.html`の実験anchor差分はいずれも0である。
canonical index 720件を再生成し、lockのcanonical hashを更新した。`./tools/validate_book`（106章）、
`tools/test_domain_models.py`（representative_cases=625、modeled=536、failures=0）、compileall、artifact
内Pythonのpy_compileも成功した。HTMLは再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、
各章24〜40頁、24頁未満0章である。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `c84369168a561387ee089ffe84a3ec40a0aebef5f19edae205756d45b244e34a` |
| `artifacts/canonical/index.json` | `8ed481246d9287ac4518da4e14a5e18a07523ecdc7954c012b15ffb112ab0027` |
| `environment/lock.yml` | `eadbc19eb71d1eac871a2a847b4d6206fc9e225b6bd8ec79a8ba8ad50a2921b6` |
| `tmp/page-counts.json` | `cb8149c5b76fd5c7b1e2e9e44ba57d3fa23e297f51228e3f7ca56bb80b21ce79` |

この追補で第17〜24章独立レビューの局所数値P1とrunner状態表示P2は修正対象になったが、固定runnerの
全718件`measurement.status=not_run`、全627 source rowの意味レビュー、全106章・13巻・全体統合、
FPGA・実回路・シリコンの物理測定は未完了である。従って`learner-ready`は解除しない。

## 26. 第15章E4修正と最終HTML再測定

第15章E4の解答に残っていた「runnerがまだ実行されたことを意味しない」という陳腐化した
表現を、入力由来の契約モデルは実行済みだが実在試料の測定ではない、という現行状態へ修正した。
対応HTMLを再生成し、別sessionの独立再確認で第10・13・15章の旧runner表記を全件解消、
局所P0/P1/P2を0と判定した（`reviews/chapters-09-16-independent-review-20260903.md`）。

修正後の最終HTML測定は、先行一周11頁、本文106章3,511頁、合算3,522頁、各章24〜40頁、
24頁未満0、107行である。`tmp/page-counts.json`に記録された全107件のHTML SHA-256を
現行ファイルへ再計算し、不一致0件を確認した。`./tools/validate_book`は106章で成功し、
`tools/test_domain_models.py`は`failures=0`（representative_cases=625、modeled=536）、
`projects`と`tools`のcompileall、および`artifacts`内Python 47ファイルのpy_compileも成功した。
manifest実験718件と固定runner結果718件のID差分は0、runner成果物hash不一致0、canonical
file成果物hash不一致0、runner.htmlの実験anchorは718件で差分0である。固定runnerは718/718成功、
失敗0、全718件`measurement_status=not_run`を維持する。

### 最終識別hash

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `3996201a86606b83da443eaaa29267e6b52fa85996a6bd94ed27edb62d9b35d0` |
| `artifacts/canonical/index.json` | `a47fcae1a62e1ea2f2bf7771b518debe328baad130cf0c85522ac17979280fec` |
| `environment/lock.yml` | `b396ced5169095e1d152c204d12118e5e855ba28bb8c32b00b3f4eb67677bd73` |
| `tmp/page-counts.json` | `4471214e1aebe1ff39458f09b12b120dc6f1e3551c6943aa65d7bf41ff4bf7b9` |
| `reviews/source-ledger-verification-20260903.json` | `27eea61dcd872aef264b3a479361850d023bbbede1832b9baf52e00c42ca6e83` |
| `artifacts/external/host-20260902/index.json` | `6740d1e9d6b8e030f91fb98ba53cb419a66cd84295bfe4558852ab1a4b6d1066` |

局所修正は完了したが、共有P1として、全106章の外部domain実験・変更課題・故障診断、
全627 source rowの主張・版・節の意味照合、全106章・13巻・全体の別session統合review、
FPGA・実回路・シリコンの物理測定が残る。したがって、固定runnerの成功やhost probeを
測定へ昇格させず、`learner-ready`は解除しない。

## 28. 出典本文の再取得後スナップショット

2026-09-03の出典本文取得を再実行し、現行JSONと機械監査を同期した。unique URLは63、取得成功は51、source row換算は166である。台帳の行換算ではURL行166件中143件が取得証跡へ対応し、ローカルlocatorは196件、`locator_ok`は295件、`cited_in_ok`は545件である。取得成功は到達性・本文hashの証跡にとどまり、主張・版・節の意味確認を完了したことを意味しない。

現行ファイルのSHA-256は次の通りである。

| 対象 | SHA-256 |
|---|---|
| `reviews/source-content-evidence-20260903.json` | `a09c84510c23de6667014c6e94dca816789999059bb6e69b4020a02fe30bfa8f` |
| `reviews/source-ledger-verification-20260903.json` | `5bb9369620267b57bc0fab806ef05ab8c765bbf07c88eac75a55ba5062a09bbc` |

この再取得で、取得件数に関するP2は解消した。P1として、全627行のsemantic review、全718件の測定 `not_run`、外部domain実験・変更課題・故障診断、全106章・13巻・全体の別session統合、FPGA基準board・実回路測定は残っている。

## 29. 本文局所修正後のHTML再測定

固定runnerの契約再生済み状態と矛盾する「runnerは予定入口／未実行」という演習・本文の表現を、第1・2・9・10・47・48章で、共通runnerの契約artifactと外部domain・実測の未実行境界を区別する記述へ修正した。本文と演習を再HTML化し、Chrome headless + Letter + `pdfinfo` の固定手順で先行一周と106章を再測定した。

- 先行一周: 11頁
- 本文106章: 3,511頁
- 先行一周込み: 3,522頁
- 章ごとの範囲: 24〜40頁
- 24頁未満: 0章
- HTML文書: 本文107、演習・解答212
- `validate_book`: 106章で成功
- `test_domain_models`: failures=0、representative_cases=625、modeled=536

現行ページ測定JSONのSHA-256は `5fcef82ae028bf67f76a1a34876496e7198462634623a63c96c2805d4a149674` である。ページ数と成果物hashの再測定は構造・表示の確認であり、source semantic review、外部domain、FPGA・実回路、独立統合のP1を解除しない。

## 32. 第25〜32章の独立指摘修正後スナップショット（2026-09-03）

別sessionの第25〜32章レビューで見つかった状態表記の残差（第25〜27章）を、固定runnerの解析・契約再生済み／SPICE・実測未実行という現行境界へ修正した。第32章の `sv_decoder` 代表sourceは、本文の明示的4本の `assign` と同じ内容へ統一し、代表モデルへ完全代入・可変添字禁止の検査を追加した。

修正後に固定runnerを再実行し、718/718成功・失敗0、`measurement_status=not_run` 718件を確認した。第32章decoderは `contract_model_verified`、source契約 `explicit_assign_all_outputs`、checks 10/10となった。canonical index 720件を再生成し、lockのcanonical index hashと代表契約モデルhashを同期した。HTMLは再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0である。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260902.json` | `7a025557047b72e7b5dc7f6ff556394a1cb7f5c4282ed1db36c1c2f4f28720ef` |
| `artifacts/canonical/index.json` | `23494773c8668f1238f4047856b3ffb344d8ae36a7d7827c4d6b3588168e8882` |
| `environment/lock.yml` | `fba71a65fe3eeaaaa4703094c68a1eb20c9319390aada7fc340528e8095f19c4` |
| `projects/domain_models.py` | `391f965f963448d58e3b3bac5e2f2950dd143e3d131feced61f4ac1b543561d7` |
| `tmp/page-counts.json` | `2d82c7c6d8e7c770721fb2cdfaa312729b5e2649eef7e298a432ed23816d26f8` |

局所P1/P2は修正後の再実行で解消したが、全718件の外部domain・物理測定、全627 source rowの意味・版・節照合、全106章・13巻・全体の別session統合確認は未完である。したがって `learner-ready` は引き続き不可とする。

## 33. RISC-V公式locatorの版固定後スナップショット（2026-09-03）

Prelude、第1章、第2章のRISC-V候補URLを、リダイレクト先ではなく公式 `v20260120` のunprivileged／privilegedページへ固定した。取得証跡を再生成し、RV32I本文、x0、ADD/ADDI/LUI、load/store、SW、および特権仕様prefaceの本文を取得できる状態を確認した。source台帳の機械集計は rows 627、URL rows 166、fetched 143、`locator_ok=295`、`semantic_review_pending=627`で変わらない。意味・版・節の独立照合は引き続き未完である。

現行出典証跡のSHA-256は `source-content-evidence-20260903.json`=`44887f12686bc85acc1017bf5c18f493d155bb2689349395150ed212305af559`、`source-ledger-verification-20260903.json`=`8ac8949d015f7fe0d28a4a25f9457c2e8c578e22506c55e5cd3081e877d52afe` である。RISC-V公式ページは仕様版のlocatorを改善したが、全627行のsemantic gateを解除するものではない。

## 34. RISC-V locator反映後のHTML再測定（2026-09-03）

RISC-Vの版付きlocatorを本文の出典表示へ反映するためHTMLを再生成した。先行一周11頁、本文106章3,511頁、合算3,522頁、章ごと24〜40頁、24頁未満0で、HTML文書は本文107＋演習・解答212、内部リンク欠落0・不正anchor 0だった。現行 `tmp/page-counts.json` のSHA-256は `05caa742f80d99ac0605db94d636c2690321681b934dbbf558c0258137284e21` である。ページ再測定は出典意味照合や外部domain・FPGA・実回路の完成を意味しない。

## 35. 外部host代表実行の現行再実行（2026-09-03）

`tools/external_host_runs.py` を同じ固定コマンドで再実行し、CPython 3.14.7、ngspice-47、Icarus 13.0、Verilator 5.050、Yosys 0.68+postの代表30 runsがすべて終了コード0であることを確認した。現行 `artifacts/external/host-20260902/index.json` のSHA-256は `23d1484220797d2447bddda93d8e83b4adc2a06899184b07f2c9b2faedd5bf43`。外部host出力は固定runnerのcanonical artifactや測定statusへ混ぜず、FPGA・実回路・シリコン測定および全章domainゲートを解除しない。

## 36. 第44章状態表示修正と現行再測定（2026-09-03）

第41〜48章の独立レビューで見つかった第44章の「runnerはまだ実行していない」という古い状態表示を、固定runnerの契約再生済み・formal／実CPU／実測未実行へ修正した。HTMLを再生成し、全107文書を同じHeadless Chrome/Letter条件で再測定した結果、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0である。現行 `tmp/page-counts.json` のSHA-256は `b84fa8a20cfc4b6076b72af2ad2d85930de62f9fb134f77de7e81565f7e27699`、測定スクリプトSHA-256は `17a72bd4f349eeeb4ce1e2ca4937904824997abc1a16996425c0c3bd4742bc44`、第44章HTMLのSHA-256は `18810f759221fd500de853a681309a4f19a45adcad3930127f1a98f72db8c5d3` である。

同時点の出典機械監査は rows 627、URL rows 173、取得149、`locator_ok=301`、`cited_in_ok=545`、`semantic_review_pending=627`。外部host代表実行は30/30成功で、index SHA-256は `23d1484220797d2447bddda93d8e83b4adc2a06899184b07f2c9b2faedd5bf43`。第41〜48章の局所P2は0へ更新したが、全718件の外部domain・測定、全source意味照合、全章・13巻・全体の独立統合、FPGA・実回路・シリコン測定の共有P1は残り、`learner-ready`は不可である。
現行runner full-run SHA-256は `7a025557047b72e7b5dc7f6ff556394a1cb7f5c4282ed1db36c1c2f4f28720ef`、canonical indexは `23494773c8668f1238f4047856b3ffb344d8ae36a7d7827c4d6b3588168e8882`、`environment/lock.yml` は `fba71a65fe3eeaaaa4703094c68a1eb20c9319390aada7fc340528e8095f19c4` で、canonical hashのlock照合は一致している。
現行出典証跡のSHA-256は `source-content-evidence-20260903.json`=`f5d932ba5e992e9843023a4b80b02473211db9c45249d833e9f92c8a86000ff2`、`source-ledger-verification-20260903.json`=`d32357652227410a92f37a46c33d1fc1f7cee25db983c79395aa368a46968e8c` である。

## 37. 第49〜56章独立指摘の修正後スナップショット（2026-09-03）

別sessionの第49〜56章レビューで見つかった第50章UART `wstrb` の本文／解答不一致と、第56章TLB keyのVPN[0]／full VPN混同を修正した。第50章はword幅storeの`wstrb=0b1111`・下位byte送信へ、第56章はfull VPN `0x401`／`0x402`へ統一した。修正後に対象runnerを再実行し、exit 0、測定`not_run`、artifact hashのfull-run一致を確認した。

対象範囲の局所P1/P2は0へ更新した。全718件の外部domain・測定、全627 source rowの意味照合、全106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定の共有P1は残るため、`learner-ready`は不可である。現行HTML・ページ値は§36の `tmp/page-counts.json` SHA-256 `b84fa8a20cfc4b6076b72af2ad2d85930de62f9fb134f77de7e81565f7e27699` を維持する。

## 38. 第57〜64章独立指摘の修正後スナップショット（2026-09-03）

第59章はI1の4 cycle memory waitを本文・manifest・解答へ追加し、I2→I1→I3のexecute完了とI1→I2→I3のin-order retireを同じ代表入力から追えるようにした。第64章は正常なhash一致入力なのに不正imageを期待していた箇所を、`valid_image_allows_copy_and_jump`へ本文・manifest・解答の期待値として統一した。対象実験を再実行し、全718件を再実行した結果は718/718成功・失敗0、全件`measurement_status=not_run`である。現行runner SHA-256は`3d1cab91777d9595792f5dfca1c3cf2aa15435d057da8ad2a629e591f2474917`、canonical indexは`e1f7f0a72829b30f6ab4eb66a5d2b761123473472941814e54574fbb43d82620`、lockのcanonical参照は一致する。

HTMLを再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0、内部リンク欠落0を確認した。現行`tmp/page-counts.json` SHA-256は`04a509d87c996bf4f3bb9e376b5237e782a10e8f5efa2260b50f6189385f6d90`。第57〜64章の局所P0/P1/P2は0へ更新したが、全source意味照合、全章外部domain・物理測定、106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定は共有P1として残り、`learner-ready`は不可である。

## 39. 第65〜72章独立指摘の修正後スナップショット（2026-09-03）

第70章の`.text`範囲矛盾を、4 byte命令3個の12 byteへ拡張し、`loop` offset=8をsection内へ収める形で本文・manifest・ケース台帳を同期した。第72章E3は`vaddr=0x200`の補足後に本文・manifest・解答と一致している。第70章対象実験を再実行し、全718件を再実行した結果は718/718成功・失敗0、全件`measurement_status=not_run`である。現行runner SHA-256は`65553686d71956bd35e2845f17782ff6098ea73877ae10a582b7b14495817175`、canonical indexは`996803515d1cbfdbc13be649c1b72fbb88d12655a640c438cf6e389bc6dd34b7`、lockのcanonical参照は一致する。

HTMLを再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0、内部リンク欠落0を確認した。現行`tmp/page-counts.json` SHA-256は`b8a7f148ae917082092346687e9e73dad23e6c19976c2f7873437ca7cacca834`。第65〜72章の局所P0/P1/P2は0へ更新したが、全source意味照合、全章外部domain・物理測定、106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定は共有P1として残り、`learner-ready`は不可である。

## 40. 第73〜80章独立指摘の修正後スナップショット（2026-09-03）

第77章の演習解答E4〜E9を設問順へ修正し、対象8章すべてに代表case・入力・期待値を対応づける自己採点表と解答キーを追加した。第79章は同期ecallのraw fault PC=`0x100`とtoy policyのreturn PC/mepc=`0x104`を別fieldとして本文・manifestへ統一した。別sessionの再監査で対象局所P0/P1/P2はすべて0となった。

固定runnerを再実行し718/718成功・失敗0、全件measurement `not_run`を確認した。現行runner SHA-256は`1c17115f1bc46abccbf15e8cf491dbe5935e1dda79221b5a2a5015435b00421a`、canonical indexは`9d1be641a16690ff45d8d70291e4f7b93586b813d9afd39b38f060232c33e024`、environment/lock.ymlは`bbeafd4cbae986552dbcd616a3b4b05b6af230e0f4cf0a7b60a8c7d161f99eae`で、canonical参照は一致する。

HTMLを再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0、内部リンク欠落0を確認した。現行`tmp/page-counts.json` SHA-256は`c5fcf0e01362787e49fcd86bc11afa024c272483e663eb4089fd34032e3bf5e2`。共有P1（全718件の外部domain・実測、全627 source rowの意味・版・節照合、全106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定）は残るため、`learner-ready`は不可である。

## 41. 第81〜88章独立指摘の修正後スナップショット（2026-09-03）

第81章はSv39のS-mode/U-page条件をSUM=1相当のtoy前提として本文・manifest・演習へ明記し、実Sv39全条件との混同を防いだ。第82章はimmutable read-onlyとCOW marker付きread-onlyを本文・manifest・E3解答で分岐した。第81〜88章の演習・解答へ代表case、具体的入力、期待値の自己採点表を追加し、HTML正本へ反映した。別sessionの再監査で対象局所P0/P1/P2はすべて0となった。

固定runnerを再実行し718/718成功・失敗0、全件measurement `not_run`を確認した。現行runner SHA-256は`f67028f3e9bf47705dcf20c0234d0ccdd65409b3f3b4c5e9359dd07edda6065c`、canonical indexは`92ce9b2ee70c4073b8e073ab16f90bdf3e26363685ba138d6ef68a0fdabd9ed1`、environment/lock.ymlは`2f0e2729a9771fe010fa60fbe2a768ebedb3affbdf5e75512d630a427fd08a77`で、canonical参照は一致する。

HTMLを再生成・再測定し、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0、内部リンク欠落0を確認した。現行`tmp/page-counts.json` SHA-256は`bf2652e5f64d19d4f5f8e12628f76bf4dc7c4e39d2cfcb503aa1fabf89661c72`。共有P1（全718件の外部domain・実測、全627 source rowの意味・版・節照合、全106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定）は残るため、`learner-ready`は不可である。

## 42. 最終修正後の完成ゲート現行スナップショット（2026-09-03）

第89章のrunner境界表現、第97〜106章の実験カード・観測表・図のcase列（第103章fig5を含む）、第1〜2章および第4〜8章の出典追跡を修正し、HTMLと機械台帳を再生成した。別セッションの独立レビュー側でも、現行worktreeを再読して4つのレビュー報告へ最終追補を追加した。旧節のfinding・hashは履歴として保持し、以下を現行値とする。

- 局所的な独立監査判定は、**P0=0 / P1=0 / P2=0**。これは章・図・状態表示・追跡記録の現行不整合が残っていないという範囲の判定であり、本文全体の意味正確性を保証するものではない。
- 固定runnerは `718/718` 成功、失敗0。内訳は `contract_model_verified=553`、`analytic_verified=127`、`domain_verified=26`、`educational_model_verified=12`。全718件の `measurement_status` は `not_run` であり、外部domain、CPython実測、QEMU完全OS経路、ngspice、RTL/FPGA、実回路、実network、実機性能の測定済みを意味しない。
- canonical indexは730件がmaterialized、`measured=0`。`environment/lock.yml` のcanonical index SHAは現行indexと一致する。`./tools/validate_book` は `validated global manifest and 106 written chapter(s)` を返した。
- HTML測定は `generated_at=2026-09-03T02:46:57+00:00`、先行一周11頁、本文3,511頁、合算3,522頁、各章24〜40頁、24頁未満0。全107行の記録hashと実HTMLの不一致は0件で、`tmp/page-counts.json` SHA-256は `9792fde16b31a1b3ba13d81b0e594dd1683815823465a92c7bed87a619b6b5e0`、測定script SHA-256は `17a72bd4f349eeeb4ce1e2ca4937904824997abc1a16996425c0c3bd4742bc44` である。
- 出典台帳は627行、`metadata_ok=129`、`locator_ok=301`、`locator_descriptive=265`、`cited_in_ok=551`、URL行173（取得149）、local189。`semantic_review_pending=627` のため、取得本文・hash・機械locatorは意味・採用版・節の独立合格を表さない。
- 現行識別値は、runner=`8aa3715723523bbb0b3d64f70d6186e1bd7c5533c7fcbc13f0b1152f90db028c`、canonical=`97c5e79fcecf9fd6846d1c9b6a56b600aebd64e2b04c3aa1418d01e7b421193f`、lock=`8a42a4b849a06a4bcdd1ef85881305db6324c4c25f7055ffc7dad36c27362fa1`、source-content=`f5d932ba5e992e9843023a4b80b02473211db9c45249d833e9f92c8a86000ff2`、source-ledger=`96f67725cd884c29f9ecb3afef165940916e2d17dac895fbcb17db950cac028e` である。外部host indexは30/30コマンド成功だが、これは全章測定の代替ではない。

### 未解除の共有P1

1. 全718件について、固定runnerの契約再生とは別に、必要な外部domain・変更課題・故障診断・物理測定を実行し、結果をartifactへ固定すること。FPGA、RTL、SPICE、実回路、シリコン、実network、実機性能の未実行境界を残したまま完了扱いにしない。
2. 全627 source rowについて、本文の主張、採用版、正確な節/ページ、`cited_in`、取得本文を独立に意味照合すること。現在は全行がsemantic review pendingである。
3. 全106章・13巻・全体を、式・前提・単位・出典・trace・handoff・学習順まで横断して別セッションで統合し、合格sign-offを出すこと。今回の独立報告は現行構造と局所findingを確認した記録であり、この意味統合sign-offそのものではない。

従って、現行成果物は **全106章のHTML草稿と再現可能な機械検証・独立監査の記録** であり、完成教材としての **`learner-ready` は不可** である。HTMLを学習開始可能版として案内するのは、上記3共有P1を解除してからとする。

## 43. 外部host代表実行のログ更新後スナップショット（2026-09-03）

`tools/external_host_runs.py` を再実行し、CPython 3.14.7、ngspice-47、Icarus 13.0、Verilator 5.050、Yosys 0.68+postを含む30 runsが全て終了コード0であることを確認した。実行時刻・経過時間を含むログ更新後の現行index SHA-256は `acb3257ba5edcd5dad244a5bf6335a6f4d692874061ea4178cbc8b94e77705be` である。この外部host証跡は固定runnerの718件の測定、全章domainゲート、FPGA・実回路・シリコン測定を解除しない。`learner-ready`の共有P1判定は変更しない。

## 44. 出典意味レビュー・バッチ1の独立確認（2026-09-03）

執筆セッションとは独立した確認セッションが、source ledger配列の先頭100行を、本文・演習・解答・manifest/handoff・取得証跡へ突合した。保守的な判定は `pass=6`、`needs_fix=48`、`hold=46`。この結果は [出典意味レビュー・バッチ1](./source-semantic-review-batch-20260903.md) に、batch ordinal、本文位置、取得本文のhash、版・locator不足、取得不能URLを含めて保存している。台帳JSONの `semantic_review` は627行すべて `pending` のままである。

このバッチで、直ちに危険な操作を誘発するP0は確認しなかった。一方、全source rowの主張・版・節の意味照合は未完で、未監査527行、取得不能・旧URL、CH4の `supports`/`relevance` 不統一が残る。したがって一次資料ゲートと `learner-ready` 判定は解除しない。

## 45. 第4章出典スキーマ正規化後の現行値（2026-09-03）

独立レビューのP2指摘に基づき、第4章 `sources.yml` の7行で `relevance` を標準の `supports` 配列へ統一した。出典本文取得と機械台帳を再生成し、現行集計は rows=627、`metadata_ok=136`、`locator_ok=304`、`cited_in_ok=551`、URL rows=173（取得152）、local=189、`semantic_review_pending=627` となった。`semantic_review` は自動昇格していない。先頭100行の独立意味レビューは正規化前スナップショットであり、更新後も `pass=6 / needs_fix=48 / hold=46` の結論を意味合格へ拡張しない。一次資料ゲートと `learner-ready` は未解除である。

## 46. 出典意味レビュー・バッチ2の独立確認（2026-09-03）

執筆セッションとは独立した確認セッションが、source ledgerの101–200行を本文・演習・解答・manifest/handoff・取得証跡へ突合した。保守的な判定は `pass=4`、`needs_fix=41`、`hold=55`。報告は [出典意味レビュー・バッチ2](./source-semantic-review-batch-20260903-101-200.md) に保存している。取得不能・HTTP 202・`cited_in` の節表記、候補URLの版・節・`supports`不足が残り、未監査は427行である。台帳JSONの `semantic_review` は627行すべて `pending` のままで、一次資料ゲートと `learner-ready` は解除しない。

## 47. 第6章出典スキーマ正規化後の現行値（2026-09-03）

第4章に続き、第6章 `sources.yml` の6行で `relevance` を標準の `supports` 配列へ統一した。機械台帳の現行集計は rows=627、`metadata_ok=142`、`locator_ok=304`、`cited_in_ok=551`、URL rows=173（取得152）、local=189、`semantic_review_pending=627`。HTML hashは変わらず、意味・版・節の独立レビューを自動昇格していない。一次資料ゲートと `learner-ready` は未解除である。

## 48. ページ測定器修正後の境界（2026-09-03）

Chrome既定プロファイル競合を避けるため `tools/measure_html_pages.py` を修正した（現行SHA-256 `ccc740de2bfd5c88b5a452926e499bd5cf389dcad1411c3347d94989a6faac38`）。修正後の全107文書測定はホスト一時領域不足で第22章にて中断し、`tmp/page-counts.json` は直前の成功測定（生成時刻 `2026-09-03T02:46:57+00:00`、旧測定器SHA-256 `17a72bd4f349eeeb4ce1e2ca4937904824997abc1a16996425c0c3bd4742bc44`）を保持している。HTML hashとページ値は変更されていないが、修正後測定器による全件render gateは未完として扱う。`learner-ready`判定は変更しない。

## 49. 出典意味レビュー・バッチ3の独立確認（2026-09-03）

執筆セッションとは独立した確認セッションが、source ledgerの201–300行を本文・manifest・handoff・演習・解答・図・取得証跡へ突合した。`pass=0`、`needs_fix=48`、`hold=52`、P0なし。対象100行は全て `supports_count=0`、`cited_in`空欄で、計画locator・候補版・未作成artifactの確認根拠不足が残る。報告は [出典意味レビュー・バッチ3](./source-semantic-review-batch-20260903-201-300.md) に保存した。未監査は327行で、台帳JSONの `semantic_review` は627行すべて `pending` のまま、一次資料ゲートと `learner-ready` は解除しない。
## 50. 第33・35・36・40章の状態表記修正後スナップショット（2026-09-03）

別セッションの第201〜300行レビューで指摘された、固定runnerの解析・契約再生済みと外部HDL/SPICE・実測未実行の境界が曖昧な記述を、第33・35・36・40章で修正した。HTMLを再生成し、対象章の個別ページを再測定した結果は36/36/33/34頁で、現行 `tmp/page-counts.json` は本文3,512頁、先行一周込み3,523頁、各章24〜40頁、24頁未満0章、保存HTML hash不一致0件となった。

現行page-counts SHA-256は `280e8c96751da29c08ea2a3d53a64999412bfbcf33f267bcd7ab7ae59727e87e`、測定器SHA-256は `ccc740de2bfd5c88b5a452926e499bd5cf389dcad1411c3347d94989a6faac38`。`validate_book`、domain model検査（failures=0、modeled=536）、`compileall` は通過した。

修正は本文表現だけで、runner manifest・canonical artifactは変更していないため、既存の718/718成功記録を継続利用する。ただし、修正版測定器による全107文書一括renderは一時領域不足で中断しており、全718件の外部domain・実測、全627 source rowの意味・版・節照合、全106章・13巻・全体の独立統合sign-offは未完である。従って共有P1と `learner-ready` 不可の判定を維持する。
## 51. source semantic review batch 4 反映（2026-09-03）

別セッションの独立確認で、source ledger ordinal 301–400（第53〜68章）を突合し、`pass=0`、`needs_fix=31`、`hold=69`、P0なしに分類した。128件の固定runnerはexit code 0だが、測定は全件 `not_run`。報告は `reviews/source-semantic-review-batch-20260903-301-400.md` に保存した。

対象100行は主張単位の `supports`、固定版、具体的な節/行locator、本文 `cited_in` が未確定で、台帳の `semantic_review` は全627行 `pending` のままである。CH53〜68の本文・数式・演習に今回新たなP0/P1級の明白な矛盾は確認されなかったが、出典の意味・版・節照合と外部RTL/SPICE/FPGA/実測のゲートは解除しない。

## 52. 第54・56〜60・64章の状態境界修正後スナップショット（2026-09-03）

第53〜68章の独立レビューで見つかった「全成果物planned」と読める表記を、固定runnerの解析・契約再生済み、外部RTL/SPICE/QEMU/FPGA/実測はplannedという境界へ修正した。HTMLを再生成し、対象章の個別ページは35/36/34/34/33/33/34頁となった。`validate_book`、domain model検査、`compileall` は通過し、runner manifest・canonical artifactは変更していない。

現行 `tmp/page-counts.json` は本文3,513頁、先行一周込み3,524頁、各章24〜40頁、24頁未満0章、HTML hash不一致0件、JSON SHA-256 `f860fce022d706cd326d736c22989d104c2c6229c2a4460ffed9fd886dbc65a5` である。修正版測定器による全107文書一括renderは一時領域不足で中断しているため、これは全件render合格の代替ではない。全718件の外部domain・実測、全627 source rowの意味・版・節照合、全106章・13巻・全体の独立統合sign-off、FPGA・実回路・シリコン測定は未完であり、`learner-ready` 不可を維持する。
## 53. source semantic review batch 5 反映（2026-09-03）

別セッションの独立確認で、source ledger ordinal 401–500を全件突合した。実際の章範囲は第69〜84章（401–488が第69〜82章、489–500が第83〜84章）で、`pass=0`、`needs_fix=22`、`hold=78`、P0なしだった。報告は `reviews/source-semantic-review-batch-20260903-401-500.md` に保存した。

対象100行は `supports_count=0`、`metadata_ok=false`、`cited_in=[]`、`semantic_review=pending` で、標準・実装候補の版・節・本文主張対応が未完である。CH69〜84の固定runner 128件はexit code 0、canonical 118件はSHA一致、測定は全件 `not_run`。全627行の意味照合と外部domain/物理測定の共有P1は維持する。

## 54. 第73〜80章manifestのcanonical status同期（2026-09-03）

第401〜500行レビューで見つかった第73〜80章のmanifest `canonical_artifacts.status: planned` と、実際のcanonical index `executed_analytic` の差を修正した。固定runner再実行はDocker起動待ちで中断したが、既存の718/718 artifactは保持され、`materialize_canonical.py --force` 後も730件・canonical index SHA-256 `97c5e79fcecf9fd6846d1c9b6a56b600aebd64e2b04c3aa1418d01e7b421193f`である。

これは解析・契約再生済みの表示同期であり、外部RTL/QEMU/FPGA/実CPU/物理測定済みを意味しない。manifestの実験statusは既存の`executed_analytic`境界を保ち、measurementは`not_run`のままにしている。

## 55. 出典意味レビュー・バッチ6と第85〜88章成果物境界の修正（2026-09-03）

別セッションの独立確認で、source ledger ordinal 501–627（第85〜106章）を突合した。保守的な内訳は `pass=0`、`needs_fix=42`、`hold=85`、P0なしで、報告は [出典意味レビュー・バッチ6](./source-semantic-review-batch-20260903-501-627.md) に保存した。対象127行は主張単位の `supports`、採用版、節/行locator、本文 `cited_in` が未確定であり、台帳の `semantic_review=pending` は維持する。

同レビューのP2指摘を受け、第85〜88章のE8実験にE1と同じconfig成果物を再利用させず、`chapter-85-priority-inversion`、`chapter-86-partial-completion`、`chapter-87-journal`、`chapter-88-shell` を固有のcanonical artifactとして追加した。manifestだけでなく、本文のE8実験カードも同じIDへ同期した。canonical indexは734件、SHA-256は `075e14e391e6994230a57c7894ec7289c3a9d4e2a5f8786249804f07d7502e80`、`environment/lock.yml` の参照も同期済みである。併せてhandoffのrequired_inputsを、lock資源・DMA完了・journal recovery・FD/TTY起動traceなど章固有の境界へ具体化した。

新しい4成果物は既存の固定runner `experiment-08` の解析・契約再生出力からmaterializeしたもので、測定値ではない。manifest変更に伴う第85〜88章32 artifactのfingerprintは、実験payload・prediction・measurementを変えずに現行manifestへ同期し、[lineage refresh明細](../artifacts/runner/lineage-refresh-20260903.json)（SHA-256 `1e871300a2e3fe31421a348a5e17512648e38b5d33d2cf5ca246854508fb1672`）と[全件投影](../artifacts/runner/full-run-lineage-refresh-20260903.json)（SHA-256 `11d313482f6bc665ca593103bbd4d66d2f68000b98d5d94873409beeccb76aac`）へ記録した。元の実行時全件記録は[execution snapshot](../artifacts/runner/execution-snapshot-20260902.json)（SHA-256 `8aa3715723523bbb0b3d64f70d6186e1bd7c5533c7fcbc13f0b1152f90db028c`）、現行artifact hash投影は[full-run-20260902](../artifacts/runner/full-run-20260902.json)（SHA-256 `87cfd7cee25ba83735178b80fb21cf1371ce1ac5342a1c732d0d0024ffd9ecff`）である。これはDocker実験を再実行した記録ではなく、外部OS/device/filesystem/terminal、FPGA、実機測定を解除しない。第85〜88章のrunner成果物は各8件の既存成功記録を保ち、`measurement=not_run`である。したがって、全627 source rowの意味照合、全106章・13巻・全体の意味統合sign-off、外部domain/物理測定の共有P1と `learner-ready` 不可の判定は維持する。

## 56. lineage-refresh後のcanonical hash現行値（2026-09-03）

第85〜88章32件のrunner artifact fingerprintを同期した後、canonical indexを再materializeし、現行SHA-256 `72680a8a9cd8891f647f012118838a49972ae76dc6ee2c58acd7f996beb2a485` を `environment/lock.yml` へ反映した。canonicalは734件、全件 `status=executed_analytic`・`measured=false`、runner lineage不一致0件である。現行 `full-run-20260902.json` は718件すべてのartifact hashが実体と一致し、実行時原本は `execution-snapshot-20260902.json` として別保存している。独立再確認の判定はP0=0 / P1=0 / P2=1（`from_previous.required`の入力粒度）である。

## 57. 第85〜88章引き継ぎ条件の章固有化後スナップショット（2026-09-03）

第85〜88章のhandoff `from_previous.required` を、各章の直前章から受け取るべき資源境界・完了状態・診断情報を含む章固有の集合へ更新した。本文、演習・解答E10、manifest bridge、HTML表示、runner、canonicalを別セッションで再突合し、章固有requiredと前後章の契約が一致することを確認した。

- `./tools/validate_book` は終了コード0（106章）。
- 固定runnerは718/718成功、artifact hash不一致0件。CH85〜88のmanifest provenance、payload、deterministic input、canonical hashは各32/32一致する。
- canonical indexは734件、全件 `status=executed_analytic`・`measured=false`。`environment/lock.yml` の参照SHAは現行canonicalと一致する。
- HTMLは321文書、正規化ローカルリンク43,800件、欠落0、bad fragment 0。先行一周11頁、本文3,513頁、合算3,524頁、24頁未満0章。

この修正により、直前の **P2-85-88-GENERIC-FROM-PREVIOUS** は解消し、対象範囲の局所判定は **P0=0 / P1=0 / P2=0** となった。なお、全627 source rowの意味照合、全106章・13巻・全体の意味統合sign-off、全718件の外部domain・物理測定（FPGA、実回路、シリコン、実network、実機性能を含む）は共有P1として残る。source semantic batch6の分類は `pass=0 / needs_fix=42 / hold=85`、全627行の`semantic_review=pending`を維持するため、`learner-ready`は不可である。

## 58. 出典台帳の引用位置解決と先頭行の主張補完（2026-09-03）

出典の機械検査器を拡張し、`chapter.txt#2.2-3.4`、`exercises.txt:E1-E4`、複数参照、bare exercise IDを、章・演習ファイルの実在見出しへ解決できるようにした。別セッションの独立確認で、取得済み一次資料または実在local資料の根拠を主張単位で安全に補える6行（prelude 1〜3、CH1 S1/S2、CH2 S2）へ、固定版・節locator・本文引用位置を追加した。

現行の機械集計は source rows=627、`metadata_ok=142`、`locator_ok=305`、`cited_in_ok=627`、URL rows=173（取得153）、local rows=189、`semantic_review_pending=627` である。これは引用先の存在確認を改善したもので、主張の意味・採用版・節の独立合格を自動昇格させていない。先頭100行の独立判定は `pass=6 / needs_fix=48 / hold=46` のままである。

出典台帳現行JSONのSHA-256は `b81aed29cf51db7e610a8763991bb6b3f524a6a825d09ad0e3870a5006755b6a`、本文HTMLを含む全107文書の再生成・hash整合、`./tools/validate_book`（106章）、domain model検査（failures=0）を再確認した。外部domain・物理測定、全627行の意味照合、全106章・13巻・全体の意味統合sign-offは引き続き共有P1であり、`learner-ready`は不可である。

## 59. 章33〜35出典欄の主張単位補完後スナップショット（2026-09-03）

第33〜35章の出典欄を再読し、実在する計画・前章local manuscript・RISC-V公式仕様・runner artifactについて、主張単位の `supports` と本文・演習・解答の `cited_in` を補完した。RISC-VのlocatorはRV32I 2.1（ISA release `v20260120`）の公式ページへ統一し、runner行は各章の実在artifactへ固定した。前章のchapter本文とhandoffは曖昧な文字列をやめ、`paths`で前章ディレクトリの実体を明示した。未取得資料、採用版が未確定な候補、外部HDL/SPICE/FPGA/実測の未実行境界は変更していない。

- `./tools/validate_book` は `validated global manifest and 106 written chapter(s)`、domain model検査は `failures=0`（modeled=536、representative_cases=625）、`python3 -m compileall -q tools projects` は成功した。
- HTMLは107 main/212 companion（計321文書）を再生成し、ローカルリンク43,800件の欠落0、bad fragment 0を確認した。保存済みページ測定はprelude 11頁、本文3,513頁、合算3,524頁、24頁未満0である。修正版測定器による全107文書一括renderは従前どおり未完であり、保存JSONの自己整合を全件render合格とは扱わない。
- source ledgerは627行、`metadata_ok=168`、`locator_ok=309`、`locator_descriptive=260`、`cited_in_ok=627`、URL行174（取得151）、local193、`semantic_review_pending=627`。機械検査は存在・到達性・引用位置を確認するだけで、意味・版・節の独立合格を自動昇格しない。
- source-content evidence SHA-256は `dc62c7568b479f2610eabfb5d5955ca550688f869094ebc153e504e05453d3dd`、source-ledger verification SHA-256は `ef548f127e918cec4e0bbeecdba55cf2eb866378cee619e3f1ae95791358624`。canonical indexは734件・SHA-256 `72680a8a9cd8891f647f012118838a49972ae76dc6ee2c58acd7f996beb2a485` でlockと一致し、固定runnerは718/718成功・全件 `measurement=not_run` の既存記録を維持する。

独立レビューのbatch 2再確認は `pass=15 / needs_fix=30 / hold=55` とし、新規P0/P1/P2は確認していない。batch 1は `pass=6 / needs_fix=48 / hold=46`、batch 3以降も未完である。したがって全627 source rowの意味・版・節照合、全106章・13巻・全体の意味統合sign-off、外部domain・物理測定（FPGA、実回路、シリコンを含む）は共有P1として残り、`learner-ready` は不可である。

## 60. 章33〜35の前章パス明示後の独立再確認（2026-09-03）

独立確認セッションが、CH33〜35のsource YAMLで前章 `chapter.txt` と `handoff.yml` を `paths` の明示配列へ変更した状態を再読した。project locatorは実在するglobal manifest本体へ統一され、RISC-Vは公式RV32Iページ、runnerは章固有artifactを指す。`verify_source_ledgers.py` は現行627行を `metadata_ok=168`、`locator_ok=309`、`locator_descriptive=260`、`cited_in_ok=627`、URL行174（取得151）、local193として再計算した。

独立判定はbatch 3全体で `pass=3 / needs_fix=52 / hold=45`。pass候補はCH33/34/35のrunner artifact 3行で、manifest provenance・payload/input hash・終了コード0・`measurement=not_run`が整合する。needs_fix/holdは、RISC-V/IEEE 754の主張単位の規範節不足、未確定版や取得不能資料、残りCH36〜52のsupports/cited_in未補完であり、推測では昇格していない。新規P0はなく、全627行のsemantic review、全章・巻・全体の意味統合、外部domain・FPGA・実回路・物理測定の共有P1は継続する。

## 61. 全出典台帳・HTML・実行系の最終同期（2026-09-03）

CH36〜52、CH53〜68（台帳301〜400）、CH69〜106（台帳401〜627）の主張単位local/manifest依存補完と独立確認が完了した状態で、親セッションが最終同期を行った。未固定の標準・tool・SPICE・RTL・FPGA・物理測定候補は、版・節・実行証跡を推測せず候補/holdのまま残している。

- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/verify_source_ledgers.py` は rows=627、`metadata_ok=381`、`locator_ok=390`、`locator_descriptive=181`、`cited_in_ok=627`、URL rows=174（行換算の取得150）、local rows=272、`missing_locator=0`、`semantic_review_pending=627` を返した。生成JSON SHA-256は `5412463fda9f8ce7d123a69cfcb402dd37df7b825c21dfb39d674679d9da523b`。本文取得証跡は unique URL 64、取得51、source row 174で、JSON SHA-256は `6b27c0da8b080db1b350372a5ac3dcc149ce8228cd05647334c88294036370fc` である。
- `./tools/build_html` は107 main＋212 companion（計321 HTML）を生成し、`./tools/validate_book` は `validated global manifest and 106 written chapter(s)` で終了した。正規化ローカルリンク43,800件の欠落0、bad fragment 0。修正版測定器で全107文書を再測定し、prelude 11頁、本文3,513頁、合算3,524頁、各章24〜40頁、24頁未満0を確認した。`tmp/page-counts.json` SHA-256は `97f84355987c5dc0a24ed6ce64587cf688760410c57fbbcd25bfa52ae6736719`、測定器SHA-256は `ccc740de2bfd5c88b5a452926e499bd5cf389dcad1411c3347d94989a6faac38`。保存JSONに対する実HTML SHA不一致も0件である。
- domain model検査は `failures=0`、`modeled=536`、`representative_cases=625`、`python3 -m compileall -q tools projects` は成功した。canonical indexは734件すべて `executed_analytic`、`measured=false`、materialized不一致/欠落0件で、SHA-256 `72680a8a9cd8891f647f012118838a49972ae76dc6ee2c58acd7f996beb2a485` が `environment/lock.yml` と一致する。固定runnerの既存記録は718/718成功（失敗0）で、現行artifact hash投影SHA-256 `87cfd7cee25ba83735178b80fb21cf1371ce1ac5342a1c732d0d0024ffd9ecff`、実行時原本SHA-256 `8aa3715723523bbb0b3d64f70d6186e1bd7c5533c7fcbc13f0b1152f90db028c`、全件の `measurement_status=not_run` を維持する。CH85〜88のlineage refreshは再実験ではなく、SHA-256 `11d313482f6bc665ca593103bbd4d66d2f68000b98d5d94873409beeccb76aac` の投影である。
- 外部host代表実行は30/30成功、index SHA-256 `acb3257ba5edcd5dad244a5bf6335a6f4d692874061ea4178cbc8b94e77705be`。これは固定runner全件の外部domain・CPython実測・QEMU完全経路・ngspice・RTL/FPGA・実回路・実機性能を解除する証跡ではない。
- 別sessionの独立出典レビューは、batch 1=`pass 6 / needs_fix 48 / hold 46`、batch 2=`pass 15 / needs_fix 30 / hold 55`、batch 3（CH33〜35補完後）=`pass候補 11 / needs_fix 44 / hold 45`、batch 4（CH53〜68補完後）=`pass候補 47 / needs_fix 0 / hold 53`、batch 5/6（CH69〜106補完後）=`pass候補 109`。これは局所的な実在local/manifest対応の確認であり、台帳の全627行の `semantic_review` は推測で昇格させず pending を維持する。別sessionの全106章・13巻・全体の意味統合sign-offは未完である。

したがって、構造・HTML・機械的引用位置・解析runner系譜は現行値へ同期済みだが、共有P1（全627 source rowの主張・版・節の意味照合、全718件で必要な外部domain/変更課題/故障診断/物理測定、全106章・13巻・全体の独立統合、FPGA・実回路・シリコン測定）は残る。`learner-ready` は解除せず、HTMLは非公開ドラフトとして扱う。

## 62. 出典補完後の最終HTML・台帳再同期（2026-09-03）

別sessionの独立確認により、CH20〜24の20 source row、CH36〜68の4 source rowを追加補完した。POSIX/ngspice/Rabaey、RISC-V psABI/Supervisor ISA、Verilator/Yosys公式docsを固定できる範囲だけを反映し、未実行SPICE・RTL・FPGA・測定候補はhold、全627行の`semantic_review=pending`は維持した。

- source ledgerは627行、`metadata_ok=405`、`locator_ok=397`、`locator_descriptive=178`、`cited_in_ok=627`、URL行178（行換算の取得157）、local271、`missing_locator=0`、`semantic_review_pending=627`。JSON SHA-256は `464d4151d37fece86adcae6f0b4e97cdbbfd3ef6a1a5ecf1355e69a91e4b5b05`。本文取得証跡はunique URL 68、取得57、source row 178、JSON SHA-256は `052ba7204d0daa81c354278ee426901f3f3c577854a5437690e09e8b3d968e4e`。
- `./tools/build_html` は107 main＋212 companion（321 HTML）を生成し、`./tools/validate_book` は106章検証に成功。正規化ローカルリンク43,800件の欠落0、bad fragment 0。Chrome headless new＋Letter＋pdfinfo（2 isolated profiles）で2026-09-03T08:43:40Zに全107 mainを再測定し、prelude11頁、本文3,513頁、合算3,524頁、各章24〜40頁、24頁未満0、実HTML SHA不一致0。`tmp/page-counts.json` SHA-256は `611bbbfb4217352dc546278ee426901f3f3c577854a5437690e09e8b3d968e4e`、測定器SHA-256は `ccc740de2bfd5c88b5a452926e499bd5cf389dcad1411c3347d94989a6faac38`。
- domain model検査は`failures=0`、`modeled=536`、`representative_cases=625`、`python3 -m compileall -q tools projects`は成功。canonical indexは734件すべて`executed_analytic`・`measured=false`でlock SHAと一致、固定runner既存記録は718/718成功・全件`measurement_status=not_run`、外部host代表は30/30成功を維持する。

この追補で構造・HTML・機械locator・引用位置の値を現行sourceへ同期したが、全627 source rowの意味・版・節の独立semantic sign-off、全718件に必要な外部domain/変更課題/故障診断/物理測定、全106章・13巻・全体の独立意味統合、FPGA・実回路・シリコン測定は未完である。従って共有P1と`learner-ready`不可を維持する。

## 63. 最終検証実行後の現行ハッシュ（2026-09-03）

出典台帳を最終再計算した結果、`metadata_ok=405`、`locator_ok=398`、`locator_descriptive=178`、`cited_in_ok=627`、URL178（行換算取得158）、local271、`missing_locator=0`、`semantic_review_pending=627`となった。現行JSONのSHA-256は `5da3bf856adf5492caf39a1f1fa4445106d64adf8a59d7eed873938a8cf07d74`、本文取得証跡はunique URL68・取得57・source row178、SHA-256 `052ba7204d0daa81c354278ee426901f3f3c577854a5437690e09e8b3d968e4e`である。

最終検証では`validate_book`成功、domain model `failures=0`（modeled=536、representative_cases=625）、`compileall`成功、HTML321文書のローカルリンク43,800件で欠落0/bad fragment 0、全107 mainのpage hash mismatch 0を再確認した。ページJSONはprelude11頁・本文3,513頁・合算3,524頁・24〜40頁・under24=0、SHA-256 `611bbbfb4217352dc5467dd9751dde1e176a7e67f72056db591b872c486bbddf`である。

この最終検証は機械的・構造的な同期を確認するもので、全627 source rowの意味semantic sign-off、全718件の外部domain/物理測定、全106章・13巻・全体の独立意味統合を完了扱いにはしない。共有P1と`learner-ready`不可を維持する。

## 64. Docker Desktop復旧後の718件実行（2026-09-03）

Docker Desktopを起動し、`environment/lock.yml` のrunner image `electron-to-python-runner:bookworm` と `sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e` の一致を確認した。そのうえで `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/run_all_experiments.py` を実行し、718/718成功、失敗0を得た。実行時の全結果は `artifacts/runner/full-run-20260903.json`（同一内容を旧 `full-run-20260902.json` にも保持、SHA-256 `5c75d2de8e3ad2e6605d8ec6cdbaabfe15faf85f9877371453cb6d7ee93a7eae`）へ保存し、Docker context、image ID、全結果を `artifacts/runner/execution-snapshot-20260903.json`（SHA-256 `79d692ad4d2eb0f31f430fac35512a53188f6f0adf2463e76098d0d9560dd81d`）へ記録した。

再実行結果は従来の分類（analytic_verified=127、contract_model_verified=553、domain_verified=26、educational_model_verified=12）を維持し、全718件の`measurement_status=not_run`、`measurement.measured=false`も維持した。canonical indexを再マテリアライズし、734件・全件`executed_analytic`・`measured=false`、SHA-256 `29f933bc84bddf29cebf202620e096d39cb7b4ba14a96406f20a5651c5066202`をlockへ反映した。

これは固定Linuxの再現可能な解析・契約実行ゲートを強化するものだが、SPICE/RTL/QEMU/CPythonの外部domain結果、FPGA・実回路・シリコン測定、全source semantic、章・巻・全体の独立意味統合を自動的に完了扱いにはしない。共有P1はそのまま維持する。

## 65. 外部hostツール代表実行の再取得（2026-09-03）

Docker再実行後に `python3 tools/external_host_runs.py` を再実行し、CPython 3.14.7、ngspice-47、Verilator 5.050、Icarus 13.0、Yosys 0.68+post、QEMU 11.1.1、riscv64-elf-gcc 16.2.0の利用可能性を確認した。30件すべて終了コード0、index SHA-256は `5fcd5ebab5798ec13595a0577dd4b52e294f262c8d0f6b883a5a03c4025416c8`、生成時刻は2026-09-03T09:39:56Zである。

これは第1〜21・24・32・92章などの代表的なhost計算、SPICE、HDL、合成、CPython probeを、固定runner・canonical artifactと別系統の`external_tool_run`として記録したものだ。全718件の外部domain対応、FPGA基準board、実回路・シリコン測定、全source semantic、全章・巻・全体の独立意味統合を代替しないため、共有P1と`learner-ready`不可を維持する。

## 66. CH1〜19独立出典確認後の最終再同期（2026-09-03）

執筆セッションとは別の確認セッションがPrelude＋CH1〜19（source ledger ordinal 1〜138）を再読し、公式資料の版・主張単位locator 79件と、本文・演習・解答の`cited_in` 9行を補完した。候補資料を推測で昇格せず、`semantic_review`は全627行で`pending`を維持した。対象範囲の独立判定は pass候補42、needs_fix84、hold12、P0=0である。

- source ledgerは627行、`metadata_ok=420`、`locator_ok=407`、`locator_descriptive=170`、`cited_in_ok=627`、URL178（行換算取得159）、local279、`missing_locator=0`、`semantic_review_pending=627`。現行JSON SHA-256は `b0750d71a6c32b9816411799548c2cbde7f234e47b71b715296c877f3c294e13`。
- source-content evidenceはunique URL68、source row178、取得58件。現行JSON SHA-256は `723a8069f06639b562064f86685edad1cee9c5909a16e4beb5e0d91ce15b1d88`。
- HTMLは107 main＋212 companion（321文書）で、`./tools/build_html`、`./tools/validate_book`（106章）、domain model（failures=0、modeled=536）、`compileall`を再実行した。内部リンクは42,363件で欠落0・bad fragment 0。保存済みページ測定との107件のHTML hash mismatchも0件（prelude11頁、本文3,513頁、合算3,524頁、24〜40頁、under24=0、JSON SHA-256 `611bbbfb4217352dc5467dd9751dde1e176a7e67f72056db591b872c486bbddf`）。

対象範囲の補完は出典の実在性・引用位置を改善するものだが、主張の意味・採用版・節の全件semantic sign-off、全718件の外部domain/FPGA/実機測定、全章・巻・全体の独立統合を完了扱いにはしない。従って共有P1と`learner-ready`不可を維持する。

## 67. 独立出典再確認後の全体最終同期（2026-09-03）

CH53〜68では公式資料4行（RISC-V A extension、QEMU、USB HID、RFC）を、CH69〜106ではPython `tokenize`公式資料1行を独立確認して補完した。対象範囲で本文・handoff・演習・解答間の明白な新規矛盾は確認されず、全627行の`semantic_review`は`pending`を維持している。

- source ledger: 627 rows、`metadata_ok=436`、`locator_ok=421`、`locator_descriptive=161`、`cited_in_ok=627`、URL182（行換算取得163）、local284、`missing_locator=0`、`semantic_review_pending=627`。JSON SHA-256 `c43b14d23f4ad3e18a7c648f5d89eb98f6b1d422bd7a4b86b0565180d7310179`。
- source-content evidence: unique URL72、source row182、取得62件。JSON SHA-256 `326902c3b38ef5a43758cd0f2d0ea243214b26c015d6468dcf4a010058903b82`。
- `build_html`（107 main＋212 companion）、`validate_book`（106章）、domain model（failures=0、modeled=536）、`compileall`を再実行。HTML321文書の内部リンク42,363件は欠落0・bad fragment 0、107 mainの保存hash mismatch 0。ページはprelude11頁、本文3,513頁、合算3,524頁、各章24〜40頁、under24=0、`tmp/page-counts.json` SHA-256 `611bbbfb4217352dc5467dd9751dde1e176a7e67f72056db591b872c486bbddf`。
- 固定runnerはDocker lock digest一致で718/718成功、canonical734件はlock SHA一致、外部host代表30/30成功を維持する。全718件のmeasurementは`not_run`である。

この同期は機械的な出典・HTML・実験系譜を更新したもので、全source rowの意味・版・節の独立sign-off、外部domain/FPGA/実機測定、全106章・13巻・全体の独立統合を完了扱いにはしない。P0=0、共有P1継続、`learner-ready`不可である。

## 68. 2026-09-04 現行プレビュー同期

取得不能だった出典候補を公式ページへ置き換え、本文取得証跡・台帳・HTMLを再生成した。現行の機械集計は source rows=627、URL rows=182、URL本文取得=182/182、`metadata_ok=436`、`locator_ok=440`、`locator_descriptive=161`、`cited_in_ok=627`、local rows=284、`missing_locator=0`、`semantic_review_pending=627` である。取得成功とlocator一致は、主張・版・節の意味照合済みを意味しない。

`./tools/build_html` は107 main＋212 companion（321 HTML）を再生成し、`./tools/validate_book` は106章検証に成功した。正規化ローカルリンクは43,800件で欠落0、bad fragment 0。domain modelは failures=0（modeled=536、representative_cases=625）、`compileall`も成功した。固定runner既存記録は718/718成功、canonicalは734件、全件`executed_analytic`・`measured=false`、全718件の測定statusは`not_run`である。

全107文書のページ測定は再実行中であり、完了後に`tmp/page-counts.json`と本記録を同期する。独立出典レビューCH36〜52は pass候補64 / needs_fix 7 / hold 11（P0=0）だが、全627行のsemantic sign-off、全106章・13巻・全体の独立統合sign-off、SPICE/RTL/FPGA/実回路/実機を含む外部domain・物理測定は未完である。したがって現行判定は P0=0、共有P1継続、`learner-ready`不可である。

## 70. MiniPy bytecode/VM出典の具体化（2026-09-04）

独立トリアージで本文必修依存と判定された第94章 `src-94-bytecode-candidate` と第95章 `src-95-minipy-vm-candidate` に、既存の `machine-spec/minipy-bytecode.md`、`projects/minipy/runtime.py`、仕様版、主張単位の`supports`、本文・演習の`cited_in`を追加した。これはMiniPy教育実装の出所を具体化する補完であり、CPython互換、外部tool、実機測定を意味しない。

再検証値は source rows=627、`metadata_ok=438`、`locator_ok=442`、`locator_descriptive=159`、`cited_in_ok=627`、local rows=286、URL rows/fetched=182/182、`semantic_review_pending=627`。本文・出典YAMLの変更後にHTMLを再生成し、`validate_book`は106章で成功した。ページ測定はこの版で再実行する。

未補完191行の独立トリアージは、A（必修依存で補完必須）32行、B（候補明示でよい）73行、C（実体不足でhold）86行と分類した（[トリアージ報告](source-semantic-gap-triage-20260904.md)）。A/Cの補完と全627行の意味sign-off、外部domain/実測、全体sign-offはP1として継続する。

## 69. 2026-09-04 独立全体統合確認

別sessionがglobal/local manifest、全handoff、spine章のbridge、trace A〜F、HTML目次・runner、canonical/lock系譜を実ファイルで再突合した（[独立全体統合確認](independent-volume-whole-integration-20260904.md)）。P0=0、P2=0で、巻内・巻間・全体導線の明白な破綻は見つからなかった。一方、全source semantic、外部domain/実測、全体sign-offの3領域はP1として継続し、統合sign-offと`learner-ready`は不可である。

## 71. 2026-09-04 追加出典補完後の同期

第25〜26章の教科書、第53〜56・61・64章のrv32edu契約、第91〜93・96〜106章のPython/MiniPy契約について、現存する仕様・実装・公式資料を版、path、主張単位locator、`cited_in`つきで補完した。候補を外部実行済み・完全互換・測定済みへ昇格させる変更は行っていない。

- source ledger: 627 rows、`metadata_ok=473`、`locator_ok=472`、`locator_descriptive=131`、`cited_in_ok=627`、URL rows=185（行換算取得184）、local rows=311、`missing_locator=0`、`semantic_review_pending=627`。
- `fetch_source_evidence.py`: unique URL 72、source row 182、fetched 72。URL行の184/185は同一URLの重複行による差で、未取得のunique URLはない。
- この補完後にHTMLを再生成・検証し、ページ測定は最新版に対して継続中。固定runner 718/718成功、canonical 734件、全件`measured=false`、外部domain/物理測定未完の境界は維持する。

P0=0。全source rowの意味・版・節の独立照合、外部domain/FPGA/実機・物理測定、全106章・13巻・全体の独立sign-offは未完で、`learner-ready`不可を維持する。

## 72. 2026-09-04 locator・MMIO修正後の機械値

独立確認で指摘された14件のlocator上限を実在行へ合わせ、第61章では抽象紙面例とcanonical rv32edu memory mapを本文・解答に明記して分離した。出典本文取得と台帳検証を再実行し、`rows=628`、`metadata_ok=474`、`locator_ok=474`、`locator_descriptive=131`、`cited_in_ok=628`、`url_rows=185`、`url_fetched=185`、`local_rows=312`、`missing_locator=0`、`semantic_review_pending=628`を確認した。取得証跡はunique URL 73、source row 185、fetched 73である。

この値は機械的な実在・到達性・引用位置の確認であり、全628 source rowの意味・版・節の独立照合を完了した値ではない。外部domain/FPGA/実回路/物理測定、MiniPy実装範囲外のruntime/artifact、13巻・全体の独立sign-offはP1として残る。ページ測定はこのHTML版で完走し、先行一周11頁、本文3,513頁、合算3,524頁、24頁未満0章、hash不一致0件を確認済みである。

source YAML内の行範囲を実ファイルへ解決する追加機械チェックも行い、875範囲を検査して範囲外0件だった。

## 2026-09-04 第61章抽象MMIO出典の標準欄補完

第61章の `src-61-abstract-mmio-map` に、他のsource rowと同じ `accessed_for_this_draft: false`、`measured: false`、`status: candidate` を追加した。これは紙上の抽象mapをcanonical rv32edu mapへ昇格させる変更ではなく、既存の未測定・候補境界を標準欄へ揃えた記録である。`verify_source_ledgers.py`、`build_html`、`validate_book` を再実行し、rows=628、metadata_ok=474、locator_ok=474、cited_in_ok=628、URL rows/fetched=185/185、local_rows=312、missing_locator=0、semantic_review_pending=628、ページhash不一致0を確認した。全source semantic、外部domain/実測、巻・全体sign-offはP1継続であり、`learner-ready`は不可である。

## 2026-09-04 CH104 trace-A成果物を出典台帳へ接続

第104章の既存 `artifacts/trace-A-print-1-plus-2-executable-stack.json`（schema 1、1,111行）を、`src-104-trace-a-artifact` として `sources.yml` およびmanifestのsource一覧へ追加した。MiniPy compiler/VM・minios UART syscall・rv32edu subsetを共通trace_idで接続するローカル教育モデルであり、CPython、FPGA、実回路・実測結果へは昇格させていない。本文のtrace-A記述、manifest artifact、演習E5/E5解答へ `cited_in` を付け、`verify_source_ledgers.py`、`build_html`、`validate_book` を再実行した。現行値は rows=629、metadata_ok=475、locator_ok=475、cited_in_ok=629、URL rows/fetched=185/185、local_rows=313、missing_locator=0、semantic_review_pending=629、ページhash不一致0である。全source semantic、外部domain/実測、巻・全体sign-offはP1継続であり、`learner-ready`は不可である。

同じ監査で、空の候補・計画行を機械的な引用解決済みと誤読しないため、`cited_in_resolved=475`、`cited_in_present=475`、`cited_in_empty=154` を追加出力した。従来の `cited_in_ok=629` は空欄を許す互換集計として残し、非空引用475行はすべて実在ファイルへ解決している。これは意味・版・節の独立確認を完了扱いにする変更ではなく、semantic_review=629 pendingとP1境界を維持する監査表示の改善である。

## 73. 2026-09-04 出典semantic独立確認 ordinal 101–200

別セッションが現行台帳のordinal 101–200（100行）を、`sources.yml`、本文・演習・解答、manifest/handoff、取得証跡、runner/canonical境界へ突合した（[独立レビュー](independent-source-semantic-review-101-200-20260904.md)）。限定付きの `pass` 候補37行、`needs_fix` 45行、`hold` 18行で、P0=0、共有P1継続、記録修正P2=45行となった。公式資料の到達性や `cited_in` 実在性だけでは意味・版・節の合格とせず、台帳全体の `semantic_review_pending=628` は維持している。本文・sources.yml・台帳JSONの変更はない。

## 74. 2026-09-04 出典semantic独立確認 ordinal 1–100

別セッションが現行台帳のordinal 1–100（Prelude、第1〜14章）を再確認した（[独立レビュー追補](independent-source-and-integration-review-20260903.md)）。P0=0、共有P1はclaim-level semantic sign-offと外部domain/実測の2領域を継続、P2はPrelude外部6行の直接`cited_in`不足、および版未固定67行・claim locator不足68行である。対象100行は機械的には`metadata`・`locator`・`cited_in`全件OKだが、`semantic_review`は100/100 pendingのままにした。対象17実験も全件exit 0ながら`measurement=not_run`・`measured=false`であり、外部実測の代替とはしていない。

この確認を受け、Prelude外部6行（Python language/AST/dis、POSIX、RISC-V、Verilator）へ本文の対応行を`cited_in`として追加した。HTMLを再生成し、`validate_book`と台帳検証を再実行したが、107 mainの保存HTML hash不一致は0件で、ページ測定（11頁＋本文3,513頁）は維持される。これは直接追跡の補完であり、版・節の意味semantic sign-offや外部実測の完了ではない。

## 75. 2026-09-04 取得器の公式SciPy mirror fallback

SciPy公式docsホストの一時的な接続失敗に備え、`tools/fetch_source_evidence.py` に3 URL限定の公式SciPy GitHub Pages mirror fallbackを追加した。元URLをsource rowから置換せず、fallback利用時は `retrieved_via_fallback`、最終URL、本文hashを取得証跡へ保存する。再収集値はunique URL=73、source row=185、取得73/73で、台帳はrows=629、`locator_ok=475`へ同期した。これは本文到達性を補助する監査機能であり、版・節の意味照合やsemantic_reviewの昇格ではない。全source semantic、外部domain/実測、章・巻・全体sign-offはP1継続、`learner-ready`不可である。

## 2026-09-04 RISC-V / SystemVerilog出典追補

第32章の `src-32-systemverilog` に IEEE 1800-2023 公式標準ページを登録し、第45〜48章のRISC-V仕様rowに、programmers' model、base formats/immediate、load/store、branch、JAL/JALR、alignment/reserved境界の節アンカーを追加した。登録直後の値は source rows=629、`metadata_ok=476`、`locator_ok=476`、非空かつ解決済み `cited_in=476`、空の候補・計画行153、URL rows/fetched=186/186（74ユニークURL）、local rows=312、`semantic_review_pending=629` である。これは引用先の具体化と公式入口の登録であり、主張単位の独立semantic sign-off、外部RTL/SPICE/FPGA/物理測定、全体sign-offの完了ではない。

## 2026-09-04 RISC-V Privileged出典追補

第49章の `src-49-riscv-candidate` に、RISC-V Privileged Architecture の machine-level 公式ページ（ISA release v20260120）と、mstatus、mtvec、mepc、mcause、mtval、mretに対応する節アンカーを追加した。現行値は source rows=629、`metadata_ok=477`、`locator_ok=477`、非空かつ解決済み `cited_in=477`、空の候補・計画行152、URL rows/fetched=187/187（75ユニークURL）、local rows=312、`semantic_review_pending=629` である。公式入口・locatorの補完であり、rv32eduのmachine-mode模型がRISC-V全体や実行済みRTL/実機を意味するわけではない。全体semantic sign-off、外部RTL/SPICE/FPGA/物理測定、全体sign-offはP1継続である。

## 2026-09-04 RISC-V引用locator追補

第45〜48章のRISC-V仕様rowに、公式RV32I 2.1ページのprogrammers' model、base formats/immediate、load/store、branch、JAL/JALR、alignment/reserved境界の節アンカーを追加した。これは引用先の具体化であり、主張単位の独立semantic sign-off、外部RTL/SPICE/FPGA/物理測定、全体sign-offの完了ではない。

## 2026-09-04 YAML重複キー検査

`tools/validate_book.py` がYAMLの重複mapping keyを黙って上書きしない `UniqueKeyLoader` を使うようにし、出典台帳の重複フィールドを整理した。全YAMLを検査して重複キー0件、`validate_book` exit 0を確認した。これは台帳構造の品質を固定する修正であり、一次資料semantic、外部domain/実測、独立全体sign-offの未完了境界は維持する。

`validate_book` には生の `\\[...\\]` 数式区切りを検出するHTMLチェックも追加した。現行321 HTMLで重複ID 0ページ、生の表示用数式 0ページ、semantic math span 8個を再確認した。

## 2026-09-04 出典semantic独立確認 ordinal 1–100（現行台帳）

別セッションが現行 `source-ledger-verification-20260903.json` の ordinal 1–100（Prelude、第1〜14章）を、`sources.yml`、本文・演習・解答、manifest/handoff、取得証跡へ再突合した（[独立レビュー](independent-source-semantic-review-001-100-20260904.md)）。限定付きの `pass` 候補29行、`needs_fix` 71行、`hold` 0行、P0=0である。対象100行の `cited_in` は100/100解決済みで、`measured=false` も確認したが、これは主張単位の意味・採用版・節の独立合格や全体sign-offを意味しない。

現行台帳は `rows=630`、`metadata_ok=478`、`locator_ok=478`、`declared_locator_rows=266`（有効266、範囲外0）、`cited_in_present=478`、`cited_in_resolved=478`、`cited_in_empty=152`、URL 187/187取得、`semantic_review_pending=630` である。主な残件は教科書・標準資料の版/節固定、物性・定数の条件固定、SciPy採用版と取得版の整合で、共有P1と `learner-ready` 不可は維持する。

## 2026-09-04 第1章出典追跡補強後の同期

第1章のCPython source tree、strace manual、RV32I標準の `cited_in` とclaim locatorを本文の主張位置へ戻し、rv32eduのUART MMIO契約を `machine-spec/rv32edu-memory-map.yml:15-29` の独立source rowとして追加した。`build_html`、`validate_book`、source ledger検証を再実行し、HTMLは107 main＋212 companion（321文書）、source rows=630、metadata/locator=478/478、明示locator=266/266（範囲外0）、非空引用478/478解決、URL 187/187取得、semantic pending=630となった。これは追跡性の機械的補強であり、一次資料の意味・版・節の全件semantic sign-off、外部domain/FPGA/実機測定、章・巻・全体sign-offは未完のままP1を維持する。

## 2026-09-04 MiniPy参照実装 `minipy-reference-0.2`

`projects/minipy/runtime.py` を、`machine-spec/minipy-language.md` と `machine-spec/minipy-bytecode.md` の必須範囲へ拡張した。host標準`ast`を入口に、決定的なtoken/AST JSON、code object（constants・names・locals・free・line/exception table）、`LOAD_*`、算術・比較、分岐・loop、list/dict、function/closure、`return`、`raise/try/except`、`print`・`len`・`range`、実行前verifierとsource span付きVM traceを実装している。Python全体やCPython内部の互換性を主張せず、ASCII runtime stringと対象外構文をfail closedにした。

`python3 tools/test_minipy_runtime.py` は正常11ケース（算術、値、組込み、while/for、function、読み取り専用closure、mutable closure、nested closure、list/dict、例外）と負の検査6ケース（非ASCII、return外、未知opcode、無効jump、constant/name table範囲）を通過した（合計17ケース）。`python3 tools/stack_integration_trace.py --output artifacts/trace-A-print-1-plus-2-executable-stack.json` も全check成功し、MiniPy→minios→rv32eduの共通traceを再生成した。`materialize_canonical.py`、lock hash、`build_html`、`validate_book`、source ledger、domain modelを再同期済みである。

この実装・traceはhost上の教育用モデルであり、CPython完全互換、QEMU/RTL/FPGA、外部domain、実回路・物理測定の結果ではない。source rows=630、metadata/locator=478/478、明示locator=266/266（範囲外0）、非空引用478/478解決、URL 187/187取得、semantic pending=630を維持し、独立semantic・外部実測・巻/全体sign-offと`learner-ready`不可は継続する。

## 2026-09-04 MiniPy 0.2 可変クロージャ・現行hash追補

`nonlocal` を含む共有セル（mutable closure）と2段階のnested closureを実装し、`tools/test_minipy_runtime.py` の正常11＋負6＝17ケースを再実行した。`projects/minipy/runtime.py` SHAは `6a383025c0944654ee9864fc16ee86bab48eef5d94dc03a2cc29b74ef8fb9d40`、`artifacts/canonical/index.json` SHAは `0e65d38b711f98e84d24f6be5f173377d2782e6c2119c24ade0e76c0b2eade4a` で、`environment/lock.yml` と一致する。通常trace 13 checks、negative trace 5 checks、`validate_book`、source ledger、domain modelも再実行済みである。CH104 runner lineage、全source semantic、trace B–F、外部/FPGA、全体sign-offはなおP1であり、`learner-ready`は不可のままとする。

## 2026-09-04 独立全体統合確認（現行同期版）

別sessionがlock/runtime/canonicalの現行hashを再確認し、`validate_book` exit 0、`minipy_runtime_sha256=598d64dd...`、canonical index SHA `285180d2...` の一致を確認した（[現行報告](independent-volume-whole-integration-20260904-current.md)）。P1-LOCKは解消済みと判定された。一方、CH104 runner lineage、source semantic pending、trace B–F、外部/FPGA gate、全体sign-offの5領域はP1継続で、`learner-ready`不可である。

上記の独立報告は実装前のhashを記録した履歴である。実装後の現行値は直前の追補（runtime `6a383025...`、canonical `0e65d38b...`）を正本とし、lock同期を再確認した。

最終HTMLも再生成し、`tmp/page-counts.json`（SHA `5e2eeb6d336175f02393d750740657171943a886b079d75027aa45596578f82b`）を全107文書へ再測定した。Prelude 11頁、本文3,513頁、合算3,524頁、各章24〜40頁、24頁未満0、保存hash不一致0件、内部リンク欠落0件である。

## 2026-09-04 固定runner全718件の再スイープ

Docker Desktopを起動してlockのimage digest一致を確認し、全718実験を固定runnerで再実行した。`artifacts/runner/full-run-20260904.json` は718/718成功・失敗0（SHA `377bbe4eae21a88ec6e39f3c79fff4fd33acea2d57ba22a8bdd8559ed9071512`）、検証内訳はcontract 553、analytic 127、domain 26、educational model 12、測定statusは718件すべて`not_run`である。CH104の8 runner artifactは現行manifest SHAおよびpayload/input hashと8/8一致し、CH104 runner lineage P1を解消した。残る共有P1はsource semantic、trace B–F、外部/FPGA、全体sign-offの4領域であり、固定runner再実行を物理測定済みへ昇格させない。

再スイープ後に734件のcanonical artifactを再materializeし、canonical index SHA `444716a2d564a12c7ad80639a64dbea0a7302d71757c76021aa2d3630adce970`、runtime SHA `6a383025c0944654ee9864fc16ee86bab48eef5d94dc03a2cc29b74ef8fb9d40` がlockと一致することを確認した。`validate_book`、source ledger、domain model、MiniPy 17ケースも再通過した。

併せて、欠落していた第20〜24章の`handoff_status`を補い、5ファイルすべてを`draft_pending_runner_and_independent_review`へ統一した。`validate_book`は再び106章でexit 0となり、P2-HANDOFF-STATUSは解消した。残るP2はreview_gates等の旧新schema混在1領域である。

## 2026-09-04 HTML目次へ現行スナップショットを表示

ローカルプレビューで現状を確認しやすくするため、`tools/build_html.py` のHTML目次へ、現行のrunner・canonical・source ledger・ページ測定JSONから生成する「現行スナップショット」欄を追加した。目次から完成ゲート台帳、現行全体統合確認、出典台帳の機械監査へ直接移動できる。`./tools/build_html` と `./tools/validate_book` は成功し、321 HTML文書のローカルリンク43,803件は欠落0だった。これは表示導線の改善であり、source semantic、外部/FPGA/実測、章・巻・全体の独立sign-off、`learner-ready`判定は変更しない。

## 76. 2026-09-04 第105章 trace-B/C atlasをcanonicalへ接続

`tools/trace_atlas.py` を追加し、`x = [1, 2, 3]`（trace-B）と `print(sum(range(1000)))`（trace-C）をMiniPyの実行可能教育モデル、host CPythonのAST/bytecode要約、明示的なobject/loop modelへ接続した。Bは4 node・3 edge、Cはstdout `499500`・1000反復を検査し、各artifactのschema/trace ID/親鎖/重複ID/`measured=false`を10/10 checksで確認した。二回の再生成で意味内容のSHAが安定し、runtimeの組込み`sum`表示からCPythonのアドレス依存表現も除去した。

新しい成果物は `artifacts/trace-B-list-construction.json`（SHA `5c26e2b4ca95b97784670e8d2448fd72147b2f935e2accabf81da43426c380c2`）と `artifacts/trace-C-range-loop.json`（SHA `f4ec6ffb1db36a0e6716d8c8952d87c332e826d6978e806fdd0c97feab15627d`）で、第105章manifestのcanonical artifactおよびsource rowへ接続した。Cの1000反復は入力由来の教育用loop modelであり、CPU cycle、branch prediction、cache、DRAM、FPGA、実測ではない。canonical indexは736件、SHA `f87f954bbab3bb43f55d6ece15c9d07ab0deb532345a864e85561e546e5e0a88`となった。

MiniPyの`sum`追加後、`python3 tools/test_minipy_runtime.py` は正常12＋負6＝18ケースを通過した。`validate_book`、source ledger検証（rows=631、metadata/locator=479/479、declared locator=267/267、cited_in=631/631、semantic pending=631）も通過した。全718件の固定runnerを再スイープし、`artifacts/runner/full-run-20260904.json` は718/718成功・失敗0（SHA `ccc37495e707c34cee09dbc8a5e287cd2358ed7b4ebba6ffb62f05a69769ea79`）、測定欄718件すべて`not_run`である。

この追補でtrace B/Cのhost上教育モデル部分は前進したが、trace D–FおよびB/Cのvirtual memory・cache・DRAM・RTL/FPGA・実機層、全source semantic、全106章・13巻・全体の独立意味sign-offは未完である。したがって4共有P1（source semantic、trace atlasの未実行層、external/FPGA、全体sign-off）と`learner-ready`不可は維持する。

## 77. 2026-09-04 HTML目次からtrace-B/Cへ直接リンク

HTML目次の現行スナップショットへtrace-B/CのJSONリンクを追加し、`./tools/build_html` と `./tools/validate_book` を再実行した。321 HTML文書の内部リンク44,126件を解析し、欠落0、bad fragment 0を確認した。目次に表示するページ数3,524頁は、本文追補前の直近完走測定として明示し、未完走の再測定値を作成していない。表示導線の改善は、source semantic・external/FPGA・実測・独立sign-offのP1判定を変更しない。

## 78. 2026-09-04 第105章runnerをatlas実行へ同期

`tools/experiment_driver.py` の第105章`list_trace`/`sum_trace` adapterを、`trace_atlas.py`の実行可能教育モデルへ接続した。`./tools/book run 105 2` と `105 3` はDockerのlock一致image内でそれぞれ `educational_model_verified`、各10/10 checksとなり、Bのevent 13件・object 4 node/3 edge、Cのevent 1,010件・1000反復・最終accumulator 499500をcompact runner projectionへ保存した。完全なevent列はcanonicalのtrace-B/C JSONに保持し、runner measurementは`not_run`のままとした。

この変更後の固定全件再スイープは718/718成功・失敗0、verification内訳 `analytic_verified=127`、`contract_model_verified=551`、`domain_verified=26`、`educational_model_verified=14`、measurement `not_run=718`。full-run SHAは `5aeb92d15e343304a27891e3bbf0c41dc70c98882128643d7b2ba6c4e5509576`、canonical index 736件のSHAは `83101abce7f292ac551a1d035db8771451335013904906e5d1c70b5c10424034`。lockのadapter/runtime/trace atlas/canonical hashを同期し、`validate_book`、MiniPy 18ケース、trace atlas regression、source ledger（rows=631、semantic pending=631）を再通過した。

教育モデルの実行可能範囲はB/Cのsource〜VMとモデル化したobject/loopまでであり、B/Cのvirtual memory・cache・DRAM・RTL/FPGA・実機層、trace D–F、全source semantic、全106章・13巻・全体意味sign-offは未完である。P1の4領域と`learner-ready`不可は維持する。

## 79. 2026-09-04 trace-D/E/F追加後の現行値

第105章のtrace-D〜Fを `tools/trace_atlas.py` へ追加し、host CPythonのfile read、供給stdinによる`input()`、loopback TCPのsend/receiveを実行した。Dはfilesystemまで、Eはpipe-like stdinのsyscall境界まで、Fはloopback socketまでをevent親鎖へ保存している。block device、physical storage、TTY（Eではnot_applicable）、keyboard、packet、network deviceは`not_run`または`not_applicable`として明示し、物理測定へ昇格させていない。D/E/Fは各13/13 checks、全event `measured=false`、二回の再生成で意味SHAが一致した。

- trace-D: `artifacts/trace-D-file-input.json`, SHA `9384c5be574c9a610703e75cc46cf089933b2e10b1b7b6e596b2bb09705292f9`
- trace-E: `artifacts/trace-E-device-input.json`, SHA `e2fc28ad1793c15b1a2930d2bff0587d4157fff99faed496a70c46b8d218c385`
- trace-F: `artifacts/trace-F-network-output.json`, SHA `93fc6dc2357e89254daa53edde9216594a11b193cceca5b1e550bc122d1a0013`

第105章manifestの実験4〜6へ三つのartifactを接続し、`book run 105 4..6` は固定Linux runner内で `educational_model_verified`（各13 checks）となった。全718件の再スイープは成功718、失敗0、verification内訳 `analytic_verified=127`、`contract_model_verified=548`、`domain_verified=26`、`educational_model_verified=17`、measurement `not_run=718`。full-run SHAは `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`、canonical indexは739件・SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`。lockへadapter、materializer、trace atlas、canonical、D/E/F artifactのhashを同期し、`validate_book`、MiniPy 18ケース、trace atlas回帰、source ledger（631行、semantic pending 631）、HTML 321文書・43,810内部リンク・欠落0・bad fragment 0を再通過した。

この実装でD/E/Fのhost操作と未実行境界は再現可能になったが、B/Cのvirtual memory・cache・DRAM・RTL/FPGA・実機層、D/E/Fのkernel/TTY/packet/device内部、全source semantic確認、全106章・13巻・全体の独立意味sign-offは未完である。従ってP1（source semantic、trace未実行層、external/FPGA、全体sign-off）と`learner-ready`不可を維持する。

## 80. 2026-09-04 現行runner lineage snapshot

全718件スイープの詳細artifactに加え、`artifacts/runner/execution-snapshot-20260904.json` を作成した。snapshotは `full-run-20260904.json` のSHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`、lock image digest `sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e`、718/718成功を記録し、第105・106章の16 runner artifact hashを現行ファイルと突合できる。第105/106章 `sources.yml` のlocal-contract rowは旧snapshotからこの現行snapshotへ更新した。

これにより旧snapshotを参照するP1-lineageは解消したが、snapshot自体は固定runnerの解析・契約・教育モデル実行を記録するもので、外部domain、FPGA、実回路、物理測定、source semanticの意味sign-offを代替しない。P1（全source semantic、trace未実行下位層、external/FPGA、全体sign-off）と`learner-ready`不可は維持する。

## 81. 2026-09-04 trace atlasの説明範囲同期

`tools/trace_atlas.py` のdocstringを現行のB〜F生成範囲へ合わせ、B/Cだけを対象とする古い説明を除去した。現行SHAは `b16c8419ad6ceb95a46ab4453583a9a8cc59034e7ca4327fdac3e697606e3e3d` で、`environment/lock.yml` と一致し、`./tools/validate_book` は106章で成功した。D/E/Fのartifact内容・hashやrunner/canonical値は変えていない。

この修正で説明上のP2（docstring対象範囲）は解消したが、source rowのclaim locatorはなお実装ファイル全体を指すため、field単位の監査可能性はP2として残す。全source semantic、外部/FPGA/物理測定、全体独立sign-off、`learner-ready`不可の判定は変更しない。

## 82. 2026-09-04 教育用境界仕様と第73〜80章の出典台帳補完

学習者が「どこまでがこの教材の模型で、どこからが未実行の外部・実機領域か」を本文から追えるよう、`machine-spec/educational-boundaries.md`（`EDU-BOUNDARY-2026-09-04`）を追加した。rv32edu/C subset、MiniOS/xv6、MiniPy/CPython、host tool version、FPGAを任意経路として整理し、教育用実装・外部host実行・未実行境界・実測を混同しない契約を明記している。

この仕様を参照する第73〜80章の32 candidate source rowへ、`paths`、版（`version`）、主張対応（`supports`）、本文位置（`cited_in`）、宣言locatorを補完した。現行機械監査は source rows=631、`metadata_ok=511`、`locator_ok=511`、非空かつ解決済み `cited_in=511`、`cited_in_empty=120`、明示locator=299/299（範囲外0）、URL=187/187取得、`semantic_review_pending=631` である。

これは境界と追跡性を構造化した補強であり、主張単位の意味・版・節の独立合格や、対象rv32eduのRTL/Verilator差分・FPGA bitstream・board UART・物理測定を実施したことを意味しない。独立全体確認の最新判定は P0=0、P1継続（全source semantic、FPGA任意経路の実証、全106章・13巻・全体sign-off）、P2継続（claim locator粒度、schema drift、page metadata再測定）で、`learner-ready`は保留のままとする。

## 83. 2026-09-04 現行台帳に対する独立再確認

別sessionの独立エージェントが、現行worktreeの出典 ordinal 201〜300 と 401〜500、および全体統合・外部/FPGA境界を再確認した。対象 batch 201〜300 は最新の独立レビューに、401〜500 は [独立レビュー](independent-source-semantic-review-401-500-20260904.md) に記録し、いずれも現行631行・`semantic_review=pending`、CH73〜80の追加32行、trace locator、runner 718/718、canonical 739、全件 `measured=false` を再突合した。

独立全体統合の最新判定は P0=0、P1=3領域（全source semantic/CPython版境界、FPGA任意経路の実証、全106章・13巻・全体sign-off）、P2=3領域（claim locator粒度、manifest/handoff schema drift、現行HTMLに対するpage metadata再同期）である。外部/FPGA再確認でも、対象rv32eduのRTL差分・FPGA bitstream・board UART・物理測定は未実行で、host Verilator/Yosys/Icarusとxv6/QEMU smokeを対象CPUの実機証拠へ昇格させない境界が確認された。これらの独立確認によりP0は増えていないが、全source semanticの合格や`learner-ready`への昇格は行っていない。

## 84. 2026-09-04 第69〜72章toolchain境界と第81〜84章候補の追跡補完

第69〜72章の assembler、object、static linker、loader を対象に、`machine-spec/rv32edu-toolchain.md`（`RV32EDU-TOOLCHAIN-BOUNDARY-2026-09-04`）を追加した。pass 1/2、section/symbol/relocation、memory regionへの配置、`.bss` zero-fill、entry/初期stackを教育用候補契約として定め、標準ELF全体、完全なRISC-V psABI、dynamic linking、host OS実行を代替しない境界を明記した。

この仕様と既存の`educational-boundaries.md`、`rv32edu.md`、`minios-abi.md`を、第69〜72章の10 candidate source row（うち9行はtoolchain仕様を直接参照）と、第81〜84章の12 candidate source rowへ接続した。現行機械監査は source rows=631、`metadata_ok=533`、`locator_ok=533`、非空かつ解決済み `cited_in=533`、空の候補・計画行98、明示locator=321/321（範囲外0）、local rows=365、URL=187/187取得、`semantic_review_pending=631` である。YAML構造と`validate_book`は通過し、全補完行は`status=candidate`、`accessed_for_this_draft=false`、`measured=false`を維持する。

独立全体確認では、今回のCH69〜72/81〜84補完に直接的な主張過剰は見つからなかったが、公式ELF/RISC-V privileged仕様の意味査読、実toolによるassembler/linker/loader、対象rv32eduのRTL差分、FPGA/実機測定は未完である。機械的なlocator補完はP1（全source semantic）の範囲を狭める進捗ではあるが、P1の解除や`learner-ready`昇格には用いない。

## 85. 2026-09-04 現行HTMLの全件ページ測定とmetadata同期

Chrome headless new／Letter／隔離一時profile／pdfinfoの固定条件でPrelude＋第1〜106章の107文書を再測定した。Prelude 11頁、本文3,514頁、合算3,525頁、章ごと24〜40頁、24頁未満0で、`tmp/page-counts.json` 107行の保存HTML SHA-256と現行HTMLの不一致は0件だった。測定JSONはSHA `2022ec348f91382b2eefa225bb76627db5bccd669e3704d2ddb28e83f028fda9`、測定器はSHA `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`、Chrome `152.0.7977.76`、pdfinfo `26.07.0`である。

現行HTMLの内部リンクは321文書・43,812件を解析し、local target欠落0、bad fragment 0を確認した。これによりP2として残っていた「現行HTMLに対するpage metadata 107 hash不一致」は解消した。ページ整合はsource semantic、外部domain/FPGA/実機、全体独立sign-offを代替しないため、最新の共有判定は P0=0、P1=3領域、P2=2領域（claim locator粒度、manifest/handoff schema drift）、`learner-ready`保留である。

## 86. 2026-09-04 章メタデータ互換schema監査

`book-spec/chapter-metadata-schema.md`（`CHAPTER-METADATA-NORMALIZED-1`）と読み取り専用の `tools/check_chapter_schemas.py` を追加した。現行106章について、`review_gates` の旧配列19件・mapping87件、およびhandoffの旧形式14件・新形式91件・終端1件を、本文・runner payloadを書き換えずに共通投影へ正規化できることを確認した。途中章のnext chapter ID/titleはglobal manifestと一致し、第20〜24章を含む全handoffで`handoff_status`の欠落はなく、エラー0件である。

`tools/validate_book`へも、review gateの型、legacy id/titleの片側欠落・新旧混在、handoff status、第106章の番号なし終端を検査するチェックを追加し、`validated global manifest and 106 written chapter(s)`を再確認した。HTMLを再生成し、321文書・43,813 local target、欠落0・bad fragment 0を確認した。

この対応でschemaの読み取り互換性と検出可能性は固定したが、既存ファイルの形そのものを一括移行したわけではない。したがって独立全体統合のP2判定は、独立再確認が済むまで「互換契約で緩和、残件」として扱う。source semantic、外部domain/FPGA/物理測定、章・巻・全体の意味sign-off、`learner-ready`判定は変更しない。

## 87. 2026-09-04 台帳501〜631の独立再確認と3件の補正

執筆側と別セッションの独立確認が、現行台帳 ordinal 501〜631（131行）を本文・演習・解答・manifest・handoff・artifactへ再突合した。修正前は `pass候補90 / needs_fix 3 / hold 38` だったが、指摘された3件を実ファイルへ合わせて補正した。

- ordinal 558（第94章 bytecode）は、仕様 `machine-spec/minipy-bytecode.md:1-61` と `projects/minipy/runtime.py:572-624` をlocatorへ含め、解答E1〜E10の`cited_in`を追加した。
- ordinal 574（第97章 MiniPy候補）は、allocator/GCの実装を過大に支えないようsupportsを境界記述へ狭め、実在するcompiler/VM範囲 `runtime.py:297-309,894-917` へ合わせた。
- ordinal 612（第104章 trace-A）は、UART event、checks、未実行境界を含むartifact全1542行へlocatorを拡張した。

修正後の独立再確認は `pass候補93 / needs_fix 0 / hold 38`、P0=0、対象範囲のrow-level P1=0となった。source verifierは `metadata/locator/cited_in=533/533/533`、明示locator321/321、範囲外0を返している。ただし全631行の`semantic_review`はpendingであり、hold 38行の候補固定、主張単位の意味・版・節確認、外部domain/FPGA/物理測定、章・巻・全体sign-offは未完のまま共有P1として残る。runner 718/718、canonical739、全件`measured=false`にも変更はない。

独立全体統合の最新判定は、schema互換監査後の **P0=0 / P1=3領域 / P2=1領域（claim-bearing locator粒度）**、`learner-ready`保留である。

## 88. 2026-09-04 schema checkerのstatus型検査追補

`tools/check_chapter_schemas.py` と `tools/validate_book.py` の `handoff_status` 検査を、存在確認から「非空文字列」確認へ強化した。再実行は `chapters=106 / normalized=106 / errors=0`、`validate_book` は106章通過で、review gate/handoffの分類とrunner・canonical・sourceの値に変更はない。現行SHAはchecker `5b391cf3eb9b4c130780a75b94b360df8471bd71f1ad69850d800a008567ac13`、validator `8d9e3f748dd447061b1fa45a2f8b6be2f9f7b31e09e8e838e299b85de6cbe07c` である。

## 89. 2026-09-04 claim-bearing locator検査の追加

出典台帳に任意の `claim_locators` を追加し、supportsに対応する具体的な仕様・artifact範囲を機械検査できるようにした。第92章tokenize、第105章trace contract/trace atlas、第106章統合contractへ、registry・trace JSON・runner snapshot・実装の行範囲を登録した。`verify_source_ledgers.py` は `claim_locator_rows=83`、`claim_locator_ok=83`、`claim_locator_invalid=0` を返し、全631行の既存集計（metadata/locator/cited_in=533/533/533、明示locator321/321、semantic pending631）とrunner/canonicalの状態は維持した。

目次にも「主張単位locator: 83/83（範囲検査）」を表示し、HTMLは321文書・43,813 local target、欠落0・bad fragment 0。行範囲の実在性は改善したが、hold 38行の候補固定と全sourceの意味・版・節の独立sign-offを代替しない。現行全体判定はP0=0、P1=3領域（全source semantic、FPGA任意経路、章・巻・全体sign-off）、P2=1領域（残るclaim locator粒度）で、`learner-ready`は保留である。

## 90. 2026-09-04 全source row独立sign-offの被覆完了

独立した確認セッションによる出典sign-offを ordinal 1–200、201–400、401–631 の3ファイルへ分割して保存した。`uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json` は `source_rows=631`、`signoff_entries=631`、`coverage_complete=true`、重複0、欠落0、形式エラー0を返した。`tools/verify_source_ledgers.py`（SHA-256 `5b896ea8f4a2be796f5d25b564ff49ba1e169c86215a0d681343ab0416d40030`）は同一入力の再監査で生成時刻を保持し、台帳SHAを不用意に変えない。`tools/check_source_signoff.py` の現行SHAは `e50d55fdee833e75a4cb5237d522cf23968c6a3bb514d563b28491ec05f7f8cb`、監査JSON SHAは `54e9dcba31630e3f37a6275a48f6e487f6e680758fb9ce60056ff976b0455530` である。

- verified: 325
- accepted_boundary: 187
- hold: 119
- `semantic_review=pending`: 631（Sv32のclaim locatorを1行修正したが、意味レビュー状態はpendingのまま）

監査出力は [`reviews/source-semantic-signoff-verification-20260904.json`](source-semantic-signoff-verification-20260904.json) / [`reviews/source-semantic-signoff-verification-20260904.md`](source-semantic-signoff-verification-20260904.md) にあり、`gate_complete=false` は保留119行を理由にした正しい未完了表示である。各sign-offは現行 `reviews/source-ledger-verification-20260903.json`（SHA-256 `deb86fb260d73ca99fa10e49510e39a881813bb5c9ebbea3be1aa0b477405be0`）を参照し、holdを自動的にverifiedへ昇格させていない。

同時点で `./tools/build_html` を再実行し、現行HTMLは321文書・43,815 local target、欠落0・bad fragment 0。目次へsign-off件数・監査・契約の導線を追加した。runner 718/718、canonical 739、全件`measured=false`、測定`not_run`は維持する。

FPGAは ADR 0008（[`docs/adr/0008-fpga-optional-add-on-path.md`](../docs/adr/0008-fpga-optional-add-on-path.md)）により、本リリースの選択経路をPC-onlyとする。FPGA任意追加経路のboard/tool/bitstream/timing/board UART証跡は未作成で `candidate` / `not_built` と表示し、PC-onlyの学習開始条件とは分離した。

現行判定は **P0=0、P1=2領域、P2=0領域、`learner-ready`保留**。P1は、hold 119行を含む全sourceの公式資料・採用版・節・本文claimの意味確認、およびPrelude＋106章・13巻・全体の独立意味sign-offである。出典行の被覆、構造・リンク監査、PC-only runner成功は、意味確認を代替しない。

## 91. 2026-09-04 第5〜8章出典locator補正後の現行値

第5〜8章の本文claim位置に合わせ、NIST/BIPM/OpenStax/MIT/Ioffe出典へ直接節または版locatorを追加し、CH5 S3/S6/S8とCH6 S2/S5の`cited_in`を本文の使用位置へ補正した。`verify_source_ledgers.py` の現行値は source rows=631、metadata_ok=533、locator_ok=532、claim locator rows/ok=113/113、cited_in present/resolved=533/533、semantic_review_pending=631。独立sign-offは `verified=325 / accepted_boundary=187 / hold=119`、coverage complete、gate complete=falseを維持する。

基準台帳は `reviews/source-ledger-verification-20260903.json`（生成 `2026-09-04T01:40:37Z`、SHA-256 `deb86fb260d73ca99fa10e49510e39a881813bb5c9ebbea3be1aa0b477405be0`）。HTMLは321文書、43,815件の内部リンクで欠落0・bad fragment 0、ローカルプレビューは `http://127.0.0.1:8765/`。locator補正とHTML整合は、出典の意味・版の独立確認や未実行domain/FPGA/実機ゲートを完了扱いにしない。

## 92. 2026-09-04 独立出典再判定後の現行同期

執筆セッションとは別の独立確認セッションが、第5〜8章の残存10行（ordinal 42, 48, 52, 55, 57, 58, 60, 61, 62, 63）を、現行sources.yml・本文・公式資料へ戻って再読した。直接節・版・本文claimが対応する ordinal 42、48、52、61、63 の5行を `verified` へ更新し、NIST統計資料とlocal artifact schemaの不一致（55）、BIPM/NISTの直接claim locator不足（57, 58）、物質代表値を支えない講義一覧（60）、古典散乱式を直接支えない半導体節（62）は `hold` を維持した。その後、同じ独立セッションがordinal 66、79も再読し、直接対応を確認して `verified` へ更新した。

現行 `tools/check_source_signoff.py --json` は `source_rows/signoff_entries=631/631`、`verified=346 / accepted_boundary=187 / hold=98`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false` を返す。台帳は `reviews/source-ledger-verification-20260903.json`、生成 `2026-09-04T02:51:52Z`、SHA-256 `885368a50c92ea21218dd1a983633afb7b00250c78e97ec43839d8448b02c3e0`。`semantic_review=pending` 631行と `measured=false` は維持する。

構造・runner/canonical・リンク・ページの既存値は、Prelude 11頁、本文3,514頁、合算3,525頁、107/107 HTML hash一致、321文書、内部リンク欠落0・bad fragment 0を維持する。P0=0、P1（source semantic hold 98行、全体意味sign-off）、P2（CH4 S3取得境界、未選択FPGA・trace D/E/F下位層）は継続し、`learner-ready`は保留である。ローカルプレビューは <http://127.0.0.1:8765/> で稼働中である。

ページ測定の現行ファイルは `tmp/page-counts.json`（生成 `2026-09-04T03:13:08+00:00`、SHA-256 `f6b8c9402a6ac6be87a735dabee62b656f19184f82b313dd28fc25bee10438a4`）であり、上記107/107 hash一致と同じ測定結果を指す。

## 93. 2026-09-04 BIPM・直接locator補正後の現行同期

第5〜19章のBIPM S1へ公式の組立単位・電気単位節を追加し、第8・9・10・12〜16・19章のOpenStax/MIT資料へ本文に対応する公式節別locatorを追加した。第11章SciPy S6には1.18.0版と`solve_ivp` locatorを追加し、第17〜19章MIT 6.012資料へ半導体・MOSの講義resource locatorを追加した。独立確認セッションが変更範囲を再読し、BIPM S1の対応行をverifiedへ更新した。現行sign-off checkerは631/631被覆、`verified=358 / accepted_boundary=187 / hold=86`、重複0、欠落0、形式エラー0、`gate_complete=false`である。台帳は生成 `2026-09-04T03:35:39Z`、SHA-256 `49a56cca47685055d019e14fae73974d90b6653019ed71d480d1a0e1efc5af2e`。

HTMLを再生成し、内部リンクは321文書・43,815件で欠落0・bad fragment 0。固定Chrome測定はPrelude 11頁、第1〜106章3,514頁、合算3,525頁、各章24〜40頁、24頁未満0章で完了した。`tmp/page-counts.json` は生成 `2026-09-04T04:02:59+00:00`、SHA-256 `4719f892fdd1aa17126a0319475411cfd24bc5eb4b2fb18ec406c04ea88d5990`、107行のHTML hash不一致0件である。source semantic hold、全体独立sign-off、未実行の外部domain/FPGA/実機経路は継続し、`learner-ready`は保留する。

## 94. 2026-09-04 現行sign-off・全体統合の最終同期

独立出典確認セッションの最終反映後、現行 `tools/check_source_signoff.py --json` は source rows/sign-off entries `631/631`、`verified=369 / accepted_boundary=187 / hold=75`、`coverage_complete=true`、missing/duplicate/errors `0/0/0`、`gate_complete=false` を返した。基準台帳は生成 `2026-09-04T03:35:39Z`、SHA-256 `49a56cca47685055d019e14fae73974d90b6653019ed71d480d1a0e1efc5af2e`、claim-bearing locatorは `172/172`、`semantic_review=pending` は631行である。

執筆セッションとは別の全体統合確認セッションが、Prelude＋106章・13巻、章間handoff、trace A–F、runner/canonical/lock、HTML導線を現行worktreeへ再突合した。構造は106/106章、必須ファイル各106/106、schema errors 0、runner 718/718成功、canonical 739件（`measured=true=0`）、HTML 321文書・内部リンク44,136件（欠落0・bad fragment 0）、ページはPrelude 11頁・本文3,514頁・合算3,525頁・107/107 hash一致である。独立全体レビューはsource decisionを変更せず、CH32 ordinal 202、CH33 ordinal 208を含む残存holdを維持した。

判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1はhold 75行を含むsource意味sign-offとPrelude＋106章＋13巻＋全体の独立意味sign-off、P2はCH4 S3のbase URL取得境界と、PC-only基準外のFPGA・trace D/E/F下位層未実行境界である。HTML正本のローカルプレビューは `http://127.0.0.1:8765/` で継続利用できる。構造・hash・runner/canonicalの機械passは、未完の意味確認・実測・FPGA任意経路を完了扱いにしない。

## 95. 2026-09-04 CH20–26 POSIX locator再監査反映

独立source reviewerが、CH20–26のPOSIX runner row（ordinal 143, 147, 151, 155, 159, 165, 171）について、The Open Group Issue 7, 2018 editionのutility contentsおよびexit/shell exit-status節と本文の`book run`・成功/失敗境界が対応することを再確認し、7行を`verified`へ更新した。物理モデル、SPICE実行結果、実測値への帰属は行わず、`measured=false`・`semantic_review=pending`を維持している。

更新後のcheckerは source rows/sign-off entries `631/631`、`verified=376 / accepted_boundary=187 / hold=68`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳生成 `2026-09-04T03:35:39Z`、SHA-256 `49a56cca47685055d019e14fae73974d90b6653019ed71d480d1a0e1efc5af2e`、claim-bearing locator `172/172`である。独立全体統合側の追加decision変更はなく、P0=0、P1=2領域、P2=2領域、`learner-ready`保留を維持する。HTMLは321文書・内部リンク44,136件、ページはPrelude 11頁・本文3,514頁・合算3,525頁・107/107 hash一致、ローカルプレビューは `http://127.0.0.1:8765/` である。

## 96. 2026-09-04 現行sign-off・候補境界反映後

独立出典確認セッションがCH18 S4のMIT 6.012直接PDF対応を再監査し、ordinal 129を`verified`へ昇格した。別の独立確認セッションはCH85–90・CH97–106の21候補行を、本文のtoy/MiniPy限定、planned/not_run、PC-only境界に照合し、外部仕様・実装・実機のverifiedへは昇格させず`accepted_boundary`として受理した。現行checkerは source rows/sign-off entries `631/631`、`verified=377 / accepted_boundary=208 / hold=46`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T04:30:31Z`、SHA-256 `da9fda19fe1b06d8c6810dc0fa5f515071054444930556d04873c58ec5d15ce7`、claim-bearing locator `172/172`である。

独立全体統合確認はglobal/local manifestの106章・13巻、Prelude先行一周、handoff、trace A–F、runner/canonical/lock、FPGA任意経路境界を再突合し、構造エラー0、runner 718/718（全件`not_run`）、canonical 739、HTML 321文書・内部リンク44,136件（欠落0・bad fragment 0）を確認した。ページ測定はPrelude 11頁、本文3,514頁、合算3,525頁、各章24–40頁、24頁未満0、保存HTML hash 107/107一致である。ローカルプレビューは `http://127.0.0.1:8765/` である。

判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1は残るsource semantic hold 46行と、Prelude＋106章・13巻・全体の独立意味sign-off未完。P2はCH4 S3 base URLの取得境界、およびPC-only基準外のFPGA・trace D/E/F下位層・外部domain/実機未実行境界である。今回の21行は必修外境界としてのみ受理し、学習者向け完成ゲートを解除するものではない。
## 97. 2026-09-04 前半保留の独立再監査反映

執筆セッションとは別の独立確認セッションが、ordinal 1–120の残存holdを現行sources.yml・本文・演習・解答・公式資料へ戻って再読した。ordinal **55（CH7 S6）、58（CH8 S2）、107（CH15 S3）**は、直接locator・版・本文claimの対応が揃うため `verified` へ更新した。accepted_boundaryの追加はなく、AMAT期待値、物質比較・緩和時間、伝送線路、RLC/反射、放射、量子井戸、Bloch/tight-binding/DOSなど直接claim locatorが不足する17行はholdを維持した。

現行checkerは source rows/sign-off entries `631/631`、`verified=380 / accepted_boundary=208 / hold=43`、missing/duplicate/errors `0/0/0`、`coverage_complete=true`、`gate_complete=false`。台帳は生成 `2026-09-04T04:30:31Z`、SHA-256 `da9fda19fe1b06d8c6810dc0fa5f515071054444930556d04873c58ec5d15ce7`。全631行の `semantic_review=pending` と各行の `measured=false` は維持する。

独立全体確認ではPrelude＋106章・13巻、handoff、trace A–F、runner/canonical/lock、FPGAのPC-only任意経路境界に構造上の追加問題はなく、runner 718/718（全件 `measurement=not_run`）、canonical 739（全件 `measured=false`）、HTML 321文書・内部リンク44,136件（欠落0・bad fragment 0）、ページPrelude 11・本文3,514・合算3,525、107/107 hash一致を維持する。判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1は残存source semantic hold 43行と、全体意味sign-off未完であり、PC-onlyを越えるFPGA・外部domain・実機測定は未実行のままである。
## 98. 2026-09-04 cited_in範囲の限定後

本文が実際に使う範囲へ合わせ、CH8 S4の引用位置を `chapter.txt:206-214`、CH8 S6を `chapter.txt:103-113`、CH9 S4を `chapter.txt:6.2-6.3` へ限定した。これは主張の帰属を広げないための執筆側補正であり、独立semantic sign-offのdecisionは再確認まで変更していない。台帳を再生成し、生成 `2026-09-04T05:34:59Z`、SHA-256 `f4f96ddc1f5ec8437c3a203546b6ada68452edbaee667c129efe1b0f76480f8e`、metadata 533/631、locator 532/631、claim locator 172/172、cited_in 533/631、形式エラー0を確認した。

現行出典sign-offは `verified=380 / accepted_boundary=208 / hold=43`、631/631被覆、`gate_complete=false`。独立確認がこの3行を再読するまで、CH8 S4/S6・CH9 S4のholdは保持する。HTML、runner、canonical、ページ測定、FPGA境界は前節の現行値（HTML 321文書・44,136内部リンク、Prelude 11頁・本文3,514頁・合算3,525頁、107/107 hash一致、runner 718/718・全件not_run）を維持する。
## 99. 2026-09-04 CH8/CH9 cited_in再監査後

独立確認セッションが、執筆側の引用範囲限定（CH8 S4/S6、CH9 S4）後の3行を再読した。CH8 S6（ordinal 62）はOpenStax 9.4–9.6と本文103–113の「緩和時間模型の限界・後段への引渡し」が対応するため `verified` を維持した。CH8 S4（ordinal 60）は物質比較の五条件を直接定義する節・版が不足し、CH9 S4（ordinal 67）は指定OpenStax 16.2 locatorが404で伝送線路固有節でもないため、いずれも `hold` を維持した。

現行checkerは `verified=381 / accepted_boundary=208 / hold=42`、source rows/sign-off entries `631/631`、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T05:34:59Z`、SHA-256 `f4f96ddc1f5ec8437c3a203546b6ada68452edbaee667c129efe1b0f76480f8e`。HTML目次は同じsign-off表示へ再生成済みで、HTML 321文書・内部リンク44,136件、ページPrelude 11・本文3,514・合算3,525、107/107 hash一致を確認した。

全体判定は **P0=0、P1=2領域、P2=3領域、`learner-ready`保留**。P1は残存source semantic hold 42行と全体意味sign-off未完、P2はCH4 S3 URL境界、FPGA/trace D–F下位層未実行、今回のCH8/CH9直接locator不足である。本文・manifest・runner・canonical・lockは変更していない。

## 100. 2026-09-04 cited_in修正後の全107文書再測定

CH8 S4/S6、CH9 S4の `cited_in` 範囲修正と独立再監査後のHTMLを、`tools/measure_html_pages.py`（SHA-256 `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`）でChrome `152.0.7977.76`・Letter・隔離一時profile・pdfinfo `26.07.0`の固定条件により全107文書再測定した。Prelude 11頁、第1〜106章本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、保存した107行のHTML SHA-256との不一致0件である。`tmp/page-counts.json` は生成 `2026-09-04T06:04:51+00:00`、SHA-256 `8717ffa4f634a3346566cbcab8ba7e35828a733e26ade0f32d114a837e3b69e9`。

現行HTMLは321文書、正規化local target 44,136件、欠落0・bad fragment 0。現行出典sign-offは `verified=381 / accepted_boundary=208 / hold=42`、631/631被覆、形式エラー0、`gate_complete=false`。ページ・リンクの整合は、残るsource semantic hold、全体意味sign-off、外部domain/FPGA/実回路/実機測定を完了扱いにしない。HTML正本のローカルプレビューは `http://127.0.0.1:8765/` で継続利用できる。

## 101. 2026-09-04 独立出典再監査・ngspice/量子資料補正後の同期

独立確認セッションが、直接PDF locatorを追加した9行（CH8 S4、CH9 S4、CH11 S4、CH12 S5、CH15 S7、CH16 S4、CH22 S3、CH25 S5、CH26 S5）を再読した。CH8 S4、CH9 S4、CH11 S4、CH15 S7、CH16 S4の5行は本文claimと公式資料の対応が揃うため `verified` へ更新し、ngspice v42.2のtarget runtime未実行またはAC分析locator不足に依存するCH12 S5、CH22 S3、CH25 S5、CH26 S5の4行は `hold` を維持した。v47 manualおよびhost実行をtarget v42.2や実測へ昇格させず、`measured=false`・`semantic_review=pending`を維持する。

現行checkerは source rows/sign-off entries `631/631`、`verified=387 / accepted_boundary=208 / hold=36`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T06:31:26Z`、SHA-256 `ed09d9c66a3a4945ebe8d1dad2fd8b2ebcdabeeff23b6eaa96fbcc66e960a842`、claim-bearing locator `172/172`である。

出典補正後にHTMLを再生成し、`tools/measure_html_pages.py`で全107文書を再測定した。Prelude 11頁、第1〜106章本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、保存HTML hash 107/107一致。`tmp/page-counts.json`は生成 `2026-09-04T06:47:54+00:00`、SHA-256 `04dbca8964757f7647189621049b55f78189033da3e91633c8f1762df438f8c1`である。HTMLは321文書・正規化local target 44,136件、欠落0・bad fragment 0で、ローカルプレビューは `http://127.0.0.1:8765/`。

構造・runner・canonical・trace・FPGA境界の判定は維持する。`./tools/validate_book`、MiniPy 18件、trace B/C/D/E/Fの受入確認は成功した。P0=0、P1=2領域（残存source semantic holdとPrelude＋106章・13巻・全体の独立意味sign-off）、P2=2領域（CH4 S3取得境界、PC-only基準外のFPGA/trace D–F下位層未実行）であり、`learner-ready`は保留する。

## 102. 2026-09-04 最終ローカルプレビュー・全体統合同期

独立出典確認セッションによるCH14 S4・CH16 S5の再監査後、目次を再生成し、最終HTMLを固定Chrome条件で再測定した。現行 `tools/check_source_signoff.py --json` は source rows/sign-off entries `631/631`、`verified=390 / accepted_boundary=208 / hold=33`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。基準台帳は `reviews/source-ledger-verification-20260903.json`、生成 `2026-09-04T07:16:26Z`、SHA-256 `7802765eb0bbdb682d62fe0b0b5b535780e9bca9c49673f385174af0ed2cd9cd`、claim-bearing locator `172/172`である。

HTMLは `./tools/build_html` で107 main＋212 companion（321文書）を生成し、目次の出典表示は `390/208/33` でcheckerと一致する。相対href 44,136件、local target欠落0、bad fragment 0を確認した。`tmp/page-counts.json` は生成 `2026-09-04T07:53:10+00:00`、SHA-256 `2e01f35048a63f4857f7d41290490bca2969264a53e33187a77d05ffb78284ae`、Prelude 11頁、本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、107/107 HTML hash一致である。`./tools/validate_book`、MiniPy 18ケース、trace B/C/D/E/F回帰、domain model（failures=0、modeled=536、representative_cases=625）、`compileall`も通過した。

執筆セッションとは別の[独立全体統合確認](./independent-volume-whole-integration-20260904-current.md)が、Prelude＋106章・13巻、既存の章順序・巻境界・handoff、trace A–F、runner/canonical/lock、HTML導線、PC-only/FPGA境界を再突合し、schema 106/106、handoff legacy/modern/terminal=14/91/1、runner 718/718 success（全件`measurement_status=not_run`）、canonical 739（`measured=true=0`）を確認した。ローカルプレビューの主要エンドポイント（root、Prelude、第1・14・106章、runner）はHTTP 200で応答している。

今回の判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1は残存source semantic hold 33行とPrelude＋106章・13巻・全体の独立意味sign-off、P2はCH4 S3 base URLの取得境界およびPC-only基準外のFPGA・trace D/E/F下位層未実行である。構造・ページ・リンク・固定runnerのpassを、外部domain、FPGA、実回路、シリコンの実測完了へ読み替えない。HTMLを正本、PDFを配布しない方針と、`http://127.0.0.1:8765/` のローカルプレビューを維持する。

## 103. 2026-09-04 現行source再監査・最終ページ測定

CH20〜26の独立source reviewerが変更行を再読し、ordinal 141、144–146、148–149、152–153、156–157、162–163、169を `verified` へ更新した。接合容量・金属接触、ngspice target runtime 42.2、資料版不一致など直接対応の不足する行はholdを維持した。現行 `tools/check_source_signoff.py --json` は source rows/sign-off entries `631/631`、`verified=403 / accepted_boundary=208 / hold=20`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T08:11:43Z`、SHA-256=`fd9d8e4f15fc5c32bebe3e51a8fb52f38146e97bc9fc842595191ddd97b17c28`、claim-bearing locator `187/187`である。

目次を再生成し、`./tools/validate_book`（exit 0）を通過させた。HTMLは321文書、相対href 44,136件、local target欠落0、bad fragment 0。固定Chrome測定はPrelude 11頁、第1〜106章本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、107/107 HTML hash一致。`tmp/page-counts.json` は生成 `2026-09-04T08:42:02+00:00`、SHA-256=`457383a1c42835bf5645481be3640665852a868dc966667c727ae3a97c5093cf`である。

runnerは718/718成功だが全件 `measurement_status=not_run`、canonicalは739件で `measured=true=0`。P0=0、P1=2領域（残存source semantic holdとPrelude＋106章・13巻・全体の独立意味sign-off）、P2=2領域（CH4 S3 URL取得境界、PC-only基準外のFPGA/trace D–F下位層未実行）を維持し、`learner-ready`宣言は行わない。HTMLを正本、PDFを配布しない方針とローカルプレビュー `http://127.0.0.1:8765/` を維持する。

## 104. 2026-09-04 現行source sign-off・ページ再測定

CH12 S6（IEEE 1057）とCH20 S3（MIT 6.720J Lecture 19）の独立再監査を反映し、`tools/check_source_signoff.py --json` は source rows/sign-off entries `631/631`、`verified=405 / accepted_boundary=208 / hold=18`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T09:02:21Z`、SHA-256=`23e9509eeeaffb587a387519122a29131b67ea203389e1b9ee276d93e557e714`、claim locator `188/188` です。

`./tools/build_html`、`./tools/validate_book`（exit 0）後のHTMLは321文書、相対href（fragment含む）44,136件、local target欠落0、bad fragment 0。固定Chrome `152.0.7977.76`＋Letter＋隔離一時profile＋pdfinfo `26.07.0`で全107文書を再測定し、Prelude 11頁、第1〜106章本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、107/107 hash一致。`tmp/page-counts.json` は生成 `2026-09-04T09:24:50+00:00`、SHA-256=`f8f341f065ad64863066a2bf0e317213e64be276f516f93254620e75376aea5e` です。

runner 718/718は全件 `measurement_status=not_run`、canonical 739件は `measured=true=0`。MiniPy/trace/domain/compileallの合格は解析・契約・教育モデルの証跡であり、外部domain、FPGA、実回路、実機、性能測定の完了ではありません。P0=0、P1=2領域（残存source semantic hold、全体独立意味sign-off）、P2=2領域（CH4 S3 URL取得境界、PC-only基準外のFPGA/trace D–F下位層未実行）、`learner-ready`保留を維持します。HTML正本、PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/` です。

## 105. 2026-09-04 ngspice Version 42反映後の現行確認

第12章S5のngspice Version 42マニュアル（p.94/PULSE、p.121/伝送線路、p.309/.AC、p.317/.TRAN・tmax、p.335/.PLOT・.FOUR）を独立再監査し、`hold`から`verified`へ更新した。現行checkerは source rows/sign-off entries `631/631`、`verified=406 / accepted_boundary=208 / hold=17`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T09:30:14Z`、SHA-256=`c2c686d5dcedd864b646197792f6e95efa1005f2d8f516efe4c0dc0a032fa594`、claim locator `188/188`です。target runtime ngspice-42.2との境界を明記し、host ngspice-47実行や測定値へ昇格させていません。

`./tools/build_html`、`./tools/validate_book`（exit 0）後のHTMLは321文書、相対href（fragment含む）44,136件、local target欠落0、bad fragment 0。固定Chrome `152.0.7977.76`＋Letter＋隔離一時profile＋pdfinfo `26.07.0`で全107文書を再測定し、Prelude 11頁、本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、107/107 hash一致。`tmp/page-counts.json` は生成 `2026-09-04T09:48:50+00:00`、SHA-256=`d5935594030f130c287be3aa63cd899651be23335955a85507b33a1fd854c8bb`です。

runner 718/718は全件 `measurement_status=not_run`、canonical 739件は `measured=true=0`。P0=0、P1=2領域（残存source semantic hold 17行、Prelude＋106章＋13巻＋全体の独立意味sign-off）、P2=2領域（CH4 S3 URL取得境界、PC-only基準外のFPGA/trace D–F下位層未実行）、`learner-ready`保留を維持する。HTML正本、PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/`です。

## 106. 2026-09-04 第17〜20章出典反映後の現行統合確認

第17〜19章S5をMIT 6.720J Lectures 2–4・7・9へ差し替え、CH20 S1をMIT 6.012 Spring 2009 Recitation 6のp1–3・p5–7へ拡張したうえで、2つの独立確認セッションが本文claimとの対応を再監査した。CH17 S5、CH18 S5、CH19 S5は `hold→verified`、CH20 S1は `verified`へ更新し、質量作用則の完全導出・数値solver・runner/SPICE・測定値は外部資料へ帰属させず、`measured=false` と `semantic_review=pending`を維持した。

現行 `tools/check_source_signoff.py --json` は source rows/sign-off entries `631/631`、`verified=410 / accepted_boundary=208 / hold=13`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T10:10:45Z`、SHA-256=`baf0667c3be9910198a82c3a4aa1e23226e37a6333b1af86a6eb173e4b7e3d8a`、claim locator `188/188`である。

`./tools/build_html` は107 main＋212 companion（321文書）を生成し、`./tools/validate_book`はexit 0。HTMLの相対href（fragment含む）は44,136件、local target欠落0、bad fragment 0、目次表示は410/208/13とcheckerへ一致する。固定Chrome `152.0.7977.76`＋Letter＋隔離一時profile＋pdfinfo `26.07.0`で全107文書を再測定し、Prelude 11頁、本文3,514頁、合算3,525頁、各章24〜40頁、24頁未満0章、107/107 HTML hash一致。`tmp/page-counts.json`は生成 `2026-09-04T10:28:19+00:00`、SHA-256=`fe43aa82f2724910becdcbbb623eb4d266634ac2c94e9303446f747e45ea065a`である。

独立全体統合確認も、Prelude＋106章・13巻境界、schema/handoff、trace A–F、runner 718/718成功（全件`measurement_status=not_run`）、canonical 739（`measured=true=0`）、PC-only基準とADR 0008のFPGA任意追加経路を再確認した。P0=0、P1=2領域（残存source semantic hold 13行、Prelude＋106章＋13巻＋全体の独立意味sign-off）、P2=2領域（CH4 S3 base URL取得境界、PC-only基準外のFPGA/trace D–F下位層未実行）、`learner-ready`保留である。HTML正本、PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/` を維持する。

## 2026-09-04 11:12Z 現行source再監査・HTML再測定後

独立再監査で8行を `hold→verified` とし、現行source checkerは `631/631`、`verified=418 / accepted_boundary=208 / hold=5`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=false`。台帳は生成 `2026-09-04T10:51:40Z`、SHA-256=`398155589bcaae1a9347695d8c5d1e6af83ad20852d67cb139fdc639831be477`。残存holdはCH22 S3、CH25 S5、CH26 S5、CH32 S3、CH33 S4で、target runtime版またはIEEE節locator不足を理由に維持する。

`./tools/build_html`／`./tools/validate_book`（exit 0）後のHTMLは321文書、相対href 44,136件、欠落0、bad fragment 0。固定Chrome条件の全107文書測定はPrelude 11頁、本文3,514頁、合算3,525頁、min/max 24/40、under24=0、107/107 HTML hash一致。`tmp/page-counts.json` は生成 `2026-09-04T11:11:53+00:00`、SHA-256=`fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb`。

runner 718/718は成功だが全件`not_run`、canonical 739件は`measured=true=0`。MiniPy、trace B〜F、domain model、compileallも通過。P0=0、P1=2領域（残存source holdとPrelude＋106章＋13巻＋全体の独立意味sign-off）、P2=2領域（CH4 S3 URL境界、PC-only基準外のFPGA/trace D〜F下位層未実行）。`gate_complete=false` のためlearner-readyは保留し、ローカルプレビュー `http://127.0.0.1:8765/`、HTML正本、PDF非配布を維持する。

## 2026-09-04 11:21Z 現行ゲート同期

最新台帳（生成 `2026-09-04T11:20:33Z`、SHA-256=`742baaa651eafcca831298a8af474aeea35a434abd7dae73fdf07a45906a6d68`）と3分割sign-offを同期した。`tools/check_source_signoff.py --json` は source rows/sign-off `631/631`、`verified=418 / accepted_boundary=208 / hold=5`、`coverage_complete=true`、missing/duplicate/errors `0/0/0`、`gate_complete=false` を返す。残存holdはCH22/25/26のngspice Version 42.2 target runtime・URL到達性境界3行と、CH32/33のIEEE 1800/754公式clause locator不足2行である。CH4 NI-SCOPE aliasing URLのHTTP 200確認により、CH4 URL P2は閉じた。

独立全体統合確認は、HTML 321文書・44,136 href（欠落0・bad fragment 0）、Prelude 11頁・本文3,514頁・合算3,525頁・24〜40頁・107/107 hash一致、runner 718/718成功（全件`not_run`）、canonical 739件（`measured=true=0`）を再確認した。判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P2はCH12 ngspice-42 URL取得境界とPC-only基準外のFPGA/trace D〜F下位層未実行境界であり、URL取得・機械検証だけでtarget実行や実測を完了扱いにしない。HTML正本・PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/` を維持する。

## 2026-09-04 12:03Z 現行ゲート（source semantic完了後）

独立専門家役がCH32 `src-32-systemverilog` とCH33 `src-33-ieee754`を節単位で再読し、残存hold 2行を `verified`へ更新した。現行 `tools/check_source_signoff.py --json` は source rows/sign-off `631/631`、`verified=423 / accepted_boundary=208 / hold=0`、coverage complete、missing/duplicate/errors `0/0/0`、`gate_complete=true`。ledgerは生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`、claim locator `190/190`である。

独立whole統合確認は、Prelude先行一周＋106章＋13巻、schema/handoff、HTML 321文書・44,136 href（欠落0・bad fragment 0）、ページ Prelude 11頁・本文3,514頁・合算3,525頁・24〜40頁・107/107 hash一致、runner 718/718成功（全件`not_run`）、canonical 739件（`measured=true=0`）、trace A〜F checksを再確認した。P0=0。P1は章・巻・全体の独立統合確認と必修実験の再現、P2はPC-only基準外の任意FPGAおよびtrace D〜F下位層を含む実機・物理測定の未実行境界で、`learner-ready`は保留する。ローカルプレビュー `http://127.0.0.1:8765/`、HTML正本、PDF非配布を維持する。

## 2026-09-04 12:14Z 固定Linux runner全718件再現

Docker Desktop `desktop-linux`のlock固定image `electron-to-python-runner:bookworm`（amd64、image ID `sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e`）から`tools/run_all_experiments.py`を実行し、全718件を再現した。`experiment_count=718`、`successful=718`、`failed=0`、検証内訳はcontract 548、analytic 127、domain 26、educational 17、全件`measurement_status=not_run`。出力は[`full-run-20260904.json`](../artifacts/runner/full-run-20260904.json)、SHA-256=`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`である。これは固定環境の解析・契約・教育モデル再現であり、外部domain、FPGA、実回路、実機測定の証跡ではない。

この実行によりrunner再現ゲートの証拠は更新されたが、P1として全106章の章合格（変更課題・故障診断を含む）、13巻・全体の独立意味統合、P2として任意FPGA・trace D〜F下位層・物理測定が残る。source semantic gateは`423/208/0`で完了済み、`learner-ready`は引き続き保留する。

## 107. 2026-09-04 現行最終スナップショット（境界修正・HTML再測定後）

本文・共通runnerの境界表現を修正し、現行の完成ゲートを再確認した。CH12/14/15/16では固定runnerの解析・契約モデル実行済みと外部domain・実測の`measurement.status=not_run`を分離した。CH99ではfinally/generatorを契約模型として扱い、現行MiniPy runtimeの実装受入とは区別した。CH97〜103と共通runnerにも、`command_status=implemented`（入口と契約の用意）と`educational_model_verified`（専用教育実装の実行）の違いを明記した。

- source sign-off: `631/631`、verified `423`、accepted_boundary `208`、hold `0`、`gate_complete=true`
- schema/handoff: 106/106、errors=0、handoff `legacy/modern/terminal=14/91/1`
- fixed runner: 718/718 success、failed=0、全件`measurement_status=not_run`
- canonical: 739件、全件materialized、`measured=true=0`
- HTML: 321文書、href 44,140、missing=0、bad fragment=0
- page measurement: Prelude 11頁、本文3,515頁、合算3,526頁、24〜40頁、under24=0、107/107 HTML hash一致
- page ledger: `tmp/page-counts.json` SHA-256 `b307a9e549caef13d06b293242c5756b31fccb5087843a0ad9fe34fab8b4b4fd`

独立章レビューの現行判定はPrelude＋CH1〜56、CH9〜32、CH57〜106の各範囲でP0=0。現行全体判定は **P0=0 / P1=2領域 / P2=2領域 / `learner-ready`保留** である。P1は13巻・全体の独立統合確認と、必修実験・変更課題・故障診断・外部実装の未実行。P2はPC-only基準外の任意FPGA経路と、trace D/E/Fの下位層・実機／物理測定の未実行である。source gate、HTML整合、固定runner成功を、学習開始可能または実測完了へ読み替えない。

## 108. 2026-09-04 PC-only変更・故障診断アンカー実行後

`tools/check_learning_contract.py`を追加し、基準PC-only経路の最小縦断例を実行した。MiniPyの式変更、miniosのUART payload変更、rv32eduの`ADD`→`SUB`変更は3/3、非対応構文・未知syscall・未割当MMIO・不正bytecodeの故障診断は4/4、チェックイン済みPC側Python artifactは26/26成功した。結果は[`learning-contract-execution-20260904.md`](./learning-contract-execution-20260904.md)と[`pc-only-change-fault-20260904.json`](../artifacts/learning-contract/pc-only-change-fault-20260904.json)に保存し、`measured=false`を維持する。

この確認で共通縦断アンカーの「小さな変更→動作差→故障の切り分け」経路は閉じたが、全106章の章固有変更課題・故障診断、外部domain実験、任意FPGA、実機・物理測定を代替しない。従って現行判定はP0=0、`learner-ready`保留を維持する。

## 109. 2026-09-04 現行ローカルプレビュー最終同期

13巻の独立意味統合レビュー（[`volumes-01-13-integration-review-20260904-current.md`](./volumes-01-13-integration-review-20260904-current.md)）を追加し、各巻の局所判定をP0=0 / P1=0 / P2=0として記録した。これは巻の役割・接続・境界・導線に限定した判定であり、全体whole sign-offや全章の必修実験完了へは昇格させない。PC-only変更・故障診断アンカーは変更3/3、故障4/4、章PC側artifact 26/26がpassしている。

導線追加後に`./tools/build_html`、`./tools/validate_book`（exit 0）、`tools/measure_html_pages.py`を再実行した。現行HTMLは321文書、href 44,145件、local target欠落0、bad fragment 0。ページはPrelude 11頁、第1〜106章本文3,515頁、合算3,526頁、最小24頁・最大40頁・24頁未満0章、保存HTML hash 107/107一致で、`tmp/page-counts.json`は生成 `2026-09-04T14:27:34+00:00`、SHA-256=`2839b1c1559cb5a6fdb3b461725ddb599a59e72cf4afe3a6d7c41ad3e7bf19ff`である。

現行source semantic gateは`631/631`、verified 423 / accepted_boundary 208 / hold 0、coverage complete、errors 0、`gate_complete=true`。固定runnerは718/718 successだが全件`measurement_status=not_run`、canonicalは739件すべて`measured=false`である。現行全体判定は **P0=0 / P1=2領域 / P2=2領域 / `learner-ready`保留**。P1はPrelude＋106章＋13巻のwhole sign-offと、必修実験・章固有の変更／故障診断・外部実装の未実行。P2はPC-only基準外のFPGA任意経路とtrace D/E/F下位層を含む実機・物理測定である。ローカルプレビューは `http://127.0.0.1:8765/`、HTMLを正本、PDF非配布の方針を維持する。

## 110. 2026-09-04 章別学習ゲートinventory・whole sign-off範囲限定完了

別sessionの独立全体統合確認が、Prelude＋106章＋13巻、manifest/schema/handoff、HTML、source gate、runner lineage、canonical、trace A–Fについて、**whole integration sign-off: pass（範囲限定）**を追補した。これは構造・意味統合の確認を閉じるものであり、外部domain実験、実装受入、測定、章固有の変更／故障診断を合格扱いにしない。

現行の章別学習ゲートinventory（[`chapter-learning-gate-inventory-20260904.md`](./chapter-learning-gate-inventory-20260904.md)、[`JSON`](../artifacts/learning-contract/chapter-learning-gate-inventory-20260904.json)）を生成した。106章のmanifest宣言は、実験718件、acceptance_tests 699件、negative_tests 459件。固定runnerは718/718成功で測定欄718件すべて`not_run`である。acceptanceは結果行699件を生成済みだが実行済み0件、negativeは結果行459件のうち12件だけが教育モデルで実行済み（`measured=false`）、章別変更・故障診断execution artifactは0章である。negativeの12件（CH35/45/48/91/94/95のMiniPy／rv32edu）は`educational_model_verified`として12/12を確認したが、残る447件のnegativeや699件のacceptanceを完了扱いにはしない。PC-only縦断アンカーの3変更・4故障・PC側artifact 26/26 passは、これら全章ゲートとは別台帳である。

これによりP1を重複なく次の1領域へ縮約する。

1. **必修実験・章固有の変更／故障診断・外部実装受入** — 共通runnerの契約・解析・教育モデル再生は完了しているが、699 acceptance、459 negative、106章の変更／故障診断を実行済みとはいえない。SPICE、RTL、QEMU/xv6、CPython対象観測、実CPU、実機測定も同様に未完である。

別sessionのwhole integration sign-offは範囲限定で閉じたため、P1から「Prelude＋106章＋13巻のwhole sign-off」を除外した。導線追加後の現行HTMLは321文書・href 44,145、欠落0・bad fragment 0で、ページ値はPrelude 11・本文3,515・合算3,526、107/107 hash一致を維持する。現行ページ測定JSONは生成 `2026-09-04T14:27:34+00:00`、SHA-256=`2839b1c1559cb5a6fdb3b461725ddb599a59e72cf4afe3a6d7c41ad3e7bf19ff`。現行判定は **P0=0 / P1=1領域 / P2=2領域 / `learner-ready`保留**。P2はPC-only基準外のFPGA任意経路とtrace D/E/Fの物理下位層未実行であり、基準学習経路のP1と混同しない。HTML正本、PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/` を維持する。
## 111. 2026-09-04 acceptance構造検査の現行同期

acceptance 699件について、実験・測定・学習者操作を実行したとは扱わず、manifest・本文・演習・解答・artifactの構造契約だけを章／test ID単位で検査した。結果JSON（[`chapter-acceptance-results-20260904.json`](../artifacts/learning-contract/chapter-acceptance-results-20260904.json)）は、構造契約検査済み239件、構造契約failed 0件、domain／learner adapter未実装460件、`measured=true` 0件である。構造契約検査済みは、演習IDと解答ID、出典・artifact状態、handoff、本文量などのファイル形状の整合を意味し、必修実験の再現や変更課題の合格には昇格しない。

章別inventory（[`chapter-learning-gate-inventory-20260904.md`](./chapter-learning-gate-inventory-20260904.md)）にもこの結果を取り込み、acceptance結果行699件のうち構造契約239件、未実行460件、実行済み0件を明示した。negativeは結果行459件のうち教育モデル12件が検証済み、447件が未実行、`measured=true` 0件である。章別change／fault execution artifactは0章のままで、共通PC-onlyアンカー3変更・4故障・artifact26本のpassとは別台帳である。

## 112. 2026-09-05 acceptance構造検査の再同期

acceptance checkerの安全な構造アダプタを拡張し、演習・解答の複数形、runner解析再生と外部測定の分離、解析・数値・runner・測定の出所分離、artifact・figure・source registryのリンク、自然法則・モデル・契約・実装の見出し語を追加検査した。現行結果は699件中261件が`structural_contract_verified`、failed 0件、438件がdomain／learner未実行、`measured=true` 0件である。

これは本文・manifestの形状と出所欄、固定runnerの測定境界を検査したものであり、SPICE／RTL／QEMU／CPython／FPGA、物理測定、学習者の変更課題・故障診断を実行済みへ昇格させない。章別inventoryの`acceptance_executed_rows`は0件、negativeの教育モデルは12/459件、learner-readyは引き続き保留である。

この追加検査後も、現行の全体判定は **P0=0 / P1=1領域 / P2=2領域 / `learner-ready`保留**。P1は必修実験・外部実装受入・章固有change／faultの実行、P2はPC-only基準外のFPGA任意経路とtrace D/E/F物理下位層である。HTML正本、PDF非配布、ローカルプレビュー `http://127.0.0.1:8765/` を維持する。

## 113. 2026-09-05 CH99 cleanup-only MiniPy実装後

CH99の参照MiniPy runtimeへcleanup専用`try/finally`を追加し、正常経路・例外伝播経路（外側handlerで捕捉）の両方を`tools/test_minipy_runtime.py`で確認した。MiniPy受入は20ケース全件pass。`except ... finally`、finally内`return`、generatorは対象外のまま、仕様・bytecode説明・本文の範囲を一致させた。CH99のbook runner実験5/7は、実装本体の受入ではなく契約模型として`contract_model_only`、`measured=false`を維持する。

現行成果物を再同期した。固定runner全718件は718/718成功・失敗0、全件`measurement_status=not_run`（full-run SHA-256=`52374aac59aa2330e10232dd96deb71ea146a2de87531df0828a46af510dc4ef`）。短い実行snapshot（SHA-256=`bf865f88d8f2b95756f072b138d15de759d79670aee50a6a56d539406f976e47`）もこのfull-run hashへ更新した。canonicalは739件・全件`measured=false`（index SHA-256=`781da074e530761d4c9fb8373835ed950c3485618b1aac736bf7a6a248d6614e`）、lockのruntime（`02db5ee8fd5838665448e6fc5f9c9e5738cb3ae334709df9759e9c57fb9a5109`）／canonical参照も現行hashへ更新し、`validate_book`はexit 0である。full-run記録と実artifactのSHA、およびcanonical runner lineageの不一致は0件。acceptanceは699件中構造契約検査261、failed 0、未実行438、実行済み0、negativeは教育モデル12・未実行447、`measured=true` 0である。

HTMLは107 main＋212 companionの321文書、href 44,147、missing 0、bad fragment 0。固定Chrome測定はPrelude 11頁、本文3,516頁、合算3,527頁、min/max 24/40、under24=0、107/107 hash一致。`tmp/page-counts.json`は生成`2026-09-04T15:49:26+00:00`、SHA-256=`d1d20c3ac0c4fdc5510bbd30c2c60ab7c04dee2e890784e36f70c8fd0b6b319b`である。

独立whole統合の現行追補もCH99変更を再確認し、新たなP0/P1/P2を追加していない。判定は **whole integration sign-off: pass（範囲限定） / P0=0 / P1=1（acceptance・negative、章固有change/fault、必修外部実験・実装受入） / P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。ローカルプレビュー`http://127.0.0.1:8765/`、HTML正本、PDF非配布を維持する。

## 114. 2026-09-05 GitHub Pages公開制作版の分離

HTML正本を公開制作版として表示し、全321文書へ未完了ゲートの警告とライセンス導線を追加した。本文・独自図版はCC BY 4.0、コード例はMIT Licenseとし、第三者資料は原権利条件のまま分離する。`tools/build_public_site.py`は生成HTMLから到達可能なファイルだけを抽出し、`tmp/`、第三者PDF、manuscript原本、projects実装を公開対象に含めない。`tools/check_public_site.py`は公開禁止path、リンク、fragment、root逸脱を検査する。

固定Chrome再測定はPrelude 11頁、本文3,527頁、合算3,538頁、min/max 24/40、under24=0、107/107 HTML hash一致。`tmp/page-counts.json`は生成`2026-09-04T16:32:02+00:00`、SHA-256=`3cfb4867504c1979f050c01c4d4ac28789e2354165d831c6d14e945cbe725839`である。公開bundle初回検査は1,071ファイル、約21.2MB、HTML 323文書（root/404を含む）、local link 44,791件、failures 0である。

公開は可視性と配布経路を追加するが、学習ゲートの判定を変更しない。引き続き **P0=0 / P1=1 / P2=2 / `learner-ready`保留**であり、公開ページでは「公開制作版」と表示する。

## 115. 2026-09-05 GitHub Pages初回公開確認

公開専用リポジトリ `https://github.com/mani1261790/electric-circuits-to-python` をpublicとして作成し、制作原本とは別のGit履歴へ公開bundleだけを保存した。Pagesはcustom GitHub Actions workflowで構成し、現行commit `f070018dea30c5aa67d4877afb56c387c100d6b3`、Actions run `33896118145` はpublication検査、artifact upload、deployをすべてpassした。公開URLは `https://mani1261790.github.io/electric-circuits-to-python/`、HTTPS enforced=trueである。

公開後にroot、HTML目次、第1章、runner artifact、CC BYライセンスの各URLを外部取得し、すべてHTTP 200を確認した。公開リポジトリのmainはorigin/mainと同期し、Pages workflowはNode 24対応のcheckout v7、configure-pages v6、upload-pages-artifact v5、deploy-pages v5へ更新済みである。

この確認は公開配信ゲートのpassであり、教材内容の未実行acceptance、negative、章固有change/fault、外部domain・物理測定を閉じない。判定は **P0=0 / P1=1 / P2=2 / `learner-ready`保留**を維持する。

## 116. 2026-09-05 第1巻acceptance証拠の再確認

執筆へ戻る最初の区切りとして、第1章の`trace_a_constant_folding_pair_present`と、第1〜7章の`independent_review_pending`を再確認した。前者はmanifestの入力対`print(1 + 2)`／`a = 1; b = 2; print(a + b)`、AST・bytecodeのrequired artifact、固定runnerのexit 0・`measurement.status=not_run`、Trace Aの全check true・`measured=false`を照合した。後者は執筆セッションとは別の独立確認artifactがCH1〜8をP0=0 / P1=0 / P2=0と判定し、最終的に対象範囲Prelude＋CH1〜56を同判定としていることを照合した。

これによりacceptance 699件中`structural_contract_verified`は269件、failed 0件、domain／learner未実行は430件となった。章別inventoryの`acceptance_executed_rows`は0件、negative教育モデルは12/459件、章固有change／fault execution artifactは0章、`measured=true`は0件のままである。独立レビューの完了と解析artifactの存在を、CPython・SPICE・RTL・QEMU・FPGA・実機測定や学習者操作の合格へ読み替えていない。

現行判定は **P0=0 / P1=1（必修実験・章固有change/fault・外部実装受入） / P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**を維持する。

## 118. 2026-09-05 第9〜12章host実行エビデンスの独立台帳化

既存のmacOS host実行を、固定Linux runnerの解析・契約モデルや物理測定へ昇格させず、別台帳 [`external-acceptance-evidence-20260905.json`](../artifacts/learning-contract/external-acceptance-evidence-20260905.json) として検査した。入力・出力・ログのSHA-256、終了コード、ツール名・版、`physical_measurement=false`を確認し、狭い出力不変条件を照合した。

- 第9章 CPython: `τ=5 ns`、`v_p=2e8 m/s`、`t_prop=5 ns`、50Ω整合・open反射、4 ns/5 nsの分布ステップ境界を確認
- 第10章 CPython: manifest入力の抵抗網で `V1=2.75 V`、`V2=2.50 V`、最大KCL残差 `8.7e-19 A`を確認
- 第11章 ngspice-47: RC/RLC netlistの終了コード、行数、列数、過渡波形の範囲、ログを確認
- 第12章 CPython: `f_c`、RC利得、熱雑音RMS、有限終端反射係数、DFT bin構造を確認

結果は4/4章 `host_evidence_verified`、`measured=true=0`、`physical_measurement=false`、`learner_ready=false`。このverifiedは外部tool実行と記録の整合だけを意味し、章末演習の理解、全acceptance、変更・故障診断、固定Linux target版、独立専門家確認、FPGA、実回路・実機測定を閉じない。現行判定は **P0=0 / P1=1 / P2=2 / `learner-ready`保留**を維持する。

## 117. 2026-09-05 第1巻本文内容契約の追加確認

第1巻の本文を学習者向けの読み順で再確認し、未確認だった25件を、実験測定へ昇格させない構造・内容契約としてcheckerへ追加した。第2章は四つの抽象化台帳行、抵抗モデルの適用範囲、NANDの真理値表と波形の分離、RV32Iの有限幅を照合した。第3章は次元解析から形式文法までの数学mapと変更・故障診断欄、第4章はfigure/source registryとRC四経路・測定負荷・収束／不確かさの分離を照合した。第5〜8章は電場・電束・電位エネルギー・連続の式・電流の向き・発熱の式と境界を、本文および既存artifactへ照合した。

結果JSON（[`chapter-acceptance-results-20260904.json`](../artifacts/learning-contract/chapter-acceptance-results-20260904.json)）はacceptance 699件中`structural_contract_verified` 294件、structural failed 0件、domain／learner未実行405件、`measured=true` 0件である。章別inventory（[`chapter-learning-gate-inventory-20260904.json`](../artifacts/learning-contract/chapter-learning-gate-inventory-20260904.json)）も同じ内訳へ更新した。構造確認は本文・manifest・演習・解答・artifactの整合を示すだけであり、全章必修実験、章固有change／fault、外部実装受入、FPGA、実回路・実機測定の完了へは昇格させない。

現行判定は **P0=0 / P1=1（必修実験・章固有change/fault・外部実装受入） / P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**を維持する。
