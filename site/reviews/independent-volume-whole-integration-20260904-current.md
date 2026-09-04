# 独立全体統合確認（現行 2026-09-04）

## 判定

現行ファイルを直接突合した最新判定は **P0=0、P1=4領域、P2=2領域**。構造上の学習経路は保たれているが、`learner-ready` および全体統合 sign-off は **不可（保留）** とする。本文中の以前のP1/P2値は、その時点の worktree を残す履歴であり、末尾の「現行追補」を最終判定とする。

P0=0 は、106章・13巻の番号欠落、必須ファイル欠落、handoff の飛び先不一致、HTML の壊れた内部リンク、`measured=true` の偽表示を確認しなかったことを示す。未実行の意味・外部ゲートは P1 として扱った。

## 確認範囲と方法

本文・global/local manifest・handoff・trace registry・concept/symbol/equation registry・HTML・runner/canonical/lock を現行 worktree から読み取った。既存の章別・巻別レビューは照合対象の所在確認にのみ使い、既存判定の結合はしていない。本文の意味、出典の採用版・節・claim locator、外部実験の実測については、機械的な到達性や exit 0 を合格へ昇格させていない。

- global manifest は 13巻・106章、学習順は「先行一周の後、章ID 1から106まで昇順」、canonical reading は HTML、hardware は必須でなく FPGA は任意経路と定義している（[global manifest](../electron_to_python_chapter_manifest.yaml:4)、[learning contract](../electron_to_python_chapter_manifest.yaml:32)、[delivery contract](../electron_to_python_chapter_manifest.yaml:45)、[dependency policy](../electron_to_python_chapter_manifest.yaml:72)）。
- 巻範囲は I:1–8、II:9–16、III:17–24、IV:25–32、V:33–40、VI:41–48、VII:49–56、VIII:57–64、IX:65–72、X:73–80、XI:81–90、XII:91–98、XIII:99–106。local manifest 106件の identity（章番号、題名、巻、巻内番号）は全件 global と一致し、全章に7必須ファイルがある。
- Prelude の manifest と本文は第1章の前、操作・環境構築・演習・暗記を要求しない契約で一致する（[Prelude manifest](../manuscript/prelude/manifest.yml:1)、[Prelude本文](../manuscript/prelude/prelude.txt:1)）。
- 全105本の CH1→CH2 … CH105→CH106 は次章 ID と題名が一致する。CH106 は「付録と継続学習」へ終端する仕様で、数値の次章 ID は要求されない。
- 106章の実験は718件、canonical artifact は734件、演習は1,121件。全演習 ID が `exercises.txt` と `solutions.txt` の見出しへ一致し、実験の required artifact と canonical index の欠落は0件。runner 入口も期待718件に対して欠落・余分とも0件。

## registry と trace の突合

- concept registry は756件（ID重複0）。全章・Prelude の introduced concept 1,406参照は registry へ解決し、`first_introduced` 不一致0件。
- symbol registry は474件（shared 434、chapter-local 40、ID重複0）。重複 glyph 18組はすべて chapter-local で、共有記号の衝突は確認しなかった。
- equation registry は280件。manifest の1,311参照に未知 ID は0件。未参照の registry entry は `diode_equation` と `dram_retention_time` の2件で、学習経路を壊す参照欠落とは扱わず、棚卸し対象として残す。
- [trace registry](../book-spec/trace-registry.yml:1) の A〜F（print arithmetic、list construction、range loop、file input、device input、network output）は CH105 の代表入力へ対応している。ただし CH105 の A〜F は全て `status: planned`、`measured: false`。現物の cross-layer event artifact は A（MiniPy→minios→rv32edu の教育用 executable stack と境界例）のみで、B〜F の `artifacts/trace-*` は存在しない（[CH105 representative inputs](../manuscript/volume-13/chapter-105/manifest.yml:280)）。除外理由（MiniPy/minios の必須範囲外）は記録されており、未実装を実測済みとは表示していない。

## runner / canonical / HTML

- `artifacts/runner/full-run-20260903.json` は718/718 exit 0、失敗0。ただし全718件の各 artifact は `measurement.status=not_run`、`measured=false` で、検証内訳は contract 553、analytic 127、domain 26、educational model 12。これは固定入力の契約・解析再生であり、外部 tool・実機測定ではない。
- canonical index は734/734 materialized、artifact ID重複0、materialized path 欠落0、全734件 `status=executed_analytic` かつ `measured=false`。lock の canonical index SHA（`285180d2080dd0405a28a3484f6d4e810745a34255afa33d8450b327771038dd`）は現行 index と一致する。
- lock 同期後の `./tools/validate_book` は exit 0（`validated global manifest and 106 written chapter(s)`）。`environment/lock.yml:39-40` の `minipy_runtime_sha256` は現行 `projects/minipy/runtime.py` の SHA `598d64dd7ac68a73a29ddc3bf2384ef19b20e8327e56254eb58bddab523ab2fd` と一致し、再確認範囲の他の列挙済み実体 hash も一致した。P1-LOCK は解消済みと判定する。
- 同期後の識別 SHA は `environment/lock.yml`=`6d5a50719e61eba7cfe2e56862564747de344bf4ef89742ba7e58737f4a50b33`、`artifacts/canonical/index.json`=`285180d2080dd0405a28a3484f6d4e810745a34255afa33d8450b327771038dd`。この lock/canonical の現行値を基準に、以降の lineage 判定を行った。
- さらに現行 [CH104 manifest](../manuscript/volume-13/chapter-104/manifest.yml:1) は SHA `f012e53475db00d30627dfde72e1424c224d249b453a8d142566b48346884cad` だが、`artifacts/runner/chapter-104/experiment-01.json`〜`08.json` は旧 manifest SHA `ccdc75f9...c48f0879` と旧 payload/input hash を保持する。現行 manifest から `book_runner.payload_for` を再計算すると8件すべて不一致である。canonical index が現行 runner file を指すことは、この source-to-runner lineage の stale を解消しない。
- HTML は321文書（main 106、演習106、解答106、Prelude/index/runner）。44,121 href を実解析し、local target 欠落0、bad fragment 0。`tmp/page-counts.json` は Prelude 11頁、本文3,513頁、合算3,524頁、章ごと24–40頁、24頁未満0、保存 HTML hash 不一致0を記録する。

## P1（未解決）

1. **P1-CH104-LINEAGE:** CH104 の8 runner artifact が現行 manifest と結び付かない。現行 manifest で8実験を再実行し、結果を採用する場合だけ canonical index と lock を再確認する。
2. **P1-SOURCE-SEMANTIC:** 現行 `reviews/source-ledger-verification-20260903.json` の実行時点は630 rows（親から想定された628ではない）。`metadata_ok=478`、`locator_ok=478`、非空 `cited_in` 478件は到達するが、空の候補・計画行152件を含め全630件が `semantic_review=pending`。版・節・主張の意味・本文使用箇所の独立 sign-off は未完であり、既存の部分 batch を全体 pass と合算しない。
3. **P1-TRACE-ATLAS:** registry はA〜Fを定義するが、実 artifact として検証可能なのは A の教育用 stack に限られ、B〜F は CH105 の計画入力だけ。list/object graph、loop/branch、file、device、socket の各境界を別々の対象外理由と未実行境界を保ったまま materialize し、独立検証する必要がある。
4. **P1-DOMAIN-FPGA:** 718件の固定 runner は全件 `not_run`。host external index の30件成功は host-only 外部 tool 実行であり、locked runner、全章 domain、実回路・実端末・物理測定を閉じない。FPGA も [rv32edu specification](../machine-spec/rv32edu.md:9) どおり learner の必須経路ではないが、global completion contract の「一つの reference board で文書化・テスト」を満たす bitstream/timing artifact はなく、任意経路の completion gate は未解決である。
5. **P1-INDEPENDENT-SIGNOFF:** `CONTEXT.md` が要求する章確認・巻統合確認・全体統合確認の意味 sign-off は、全106章・13巻について完了していない。本報告は構造・導線・境界の独立監査であり、全式・全claim・全handoff意味の合格記録ではない。

## P2（低優先だが未正規化）

1. **P2-HANDOFF-STATUS:** `manuscript/volume-03/chapter-20`〜`chapter-24` の handoff は `from_previous`、`core_contract`、`next_chapter`、`review_checks` を持つが `handoff_status` がない。他の handoff と異なるため自動集計の状態が欠ける。次章 ID・題名自体は正常で、学習経路の破壊ではない。
2. **P2-SCHEMA-DRIFT:** local manifest の `review_gates` は CH1–19 が list、CH20–106 が dict。handoff も CH1–19 の `next_chapter_id/title` 形式と CH25以降の `next_chapter: {id,title}` 形式が混在する。validator の許容範囲内であるが、後続の集計・handoff renderer が一つの schema を前提にすると取りこぼし得るため、版付き schema または正規化を残件とする。

## 変更境界と次の判断

この確認で当セッションが編集したのは本ファイルだけである。本文、global/local manifest、sources、handoff、runner、canonical、HTML、lock は編集していない。次に解除すべき順序は、(1) CH104 lineage の正本決定、(2) source semantic と A–F trace の独立判定、(3) external/FPGA 境界を含む章・巻・全体 sign-off である。現状ではPC-onlyの学習経路の設計意図は確認できるが、プロジェクト完成または学習開始可能とは判定しない。

## 2026-09-04 現行追補（trace-B/C 接続・runner 再スイープ後）

上記の値は履歴を含むため、以下をこの時点の判定基準とする。CH105 の trace-B/C を実体化して canonical/runner/HTML/lock を読み直し、全 runner artifact の現行 manifest lineage も再計算した。

- global/local manifest は引き続き13巻・106章、718実験、736 canonical artifact、1,121演習。local identity、7必須ファイル、全105 handoff edge の次章 ID/題名は不一致0。CH20–24 の `handoff_status` も現行では補完済みである。
- `artifacts/trace-B-list-construction.json` は SHA `5c26e2b4ca95b97784670e8d2448fd72147b2f935e2accabf81da43426c380c2`、13 events、4 object nodes/3 edges、10 checks 全通過。`artifacts/trace-C-range-loop.json` は SHA `f4ec6ffb1db36a0e6716d8c8952d87c332e826d6978e806fdd0c97feab15627d`、1,010 events、1,000 iterations、MiniPy stdout `499500`、10 checks 全通過。両方とも `measured=false` で、heap・cache・pipeline・virtual memory・DRAM を実測したものではない。
- CH105 manifest の required artifact は trace-B/C JSON へ接続し、canonical index の `chapter-105-executable-list-trace`/`chapter-105-executable-loop-trace` はそれぞれ `artifacts/runner/chapter-105/experiment-02.json`/`03.json` を辿る。materialized hash 不一致0、両 artifact の runner status は `educational_model_verified`、measurement は `not_run`。trace-D/E/F は依然として計画入力と契約モデルのみで、`artifacts/trace-D*`〜`trace-F*` は存在しない。
- 現行 `artifacts/runner/full-run-20260904.json` は SHA `5aeb92d15e343304a27891e3bbf0c41dc70c98882128643d7b2ba6c4e5509576`、718/718 exit 0、失敗0、verification は `contract_model_verified=551`、`analytic_verified=127`、`domain_verified=26`、`educational_model_verified=14`、全718件 `measurement_status=not_run`。現行 manifest からの lineage 再計算は718件中 mismatch 0（旧CH104 8件も解消）である。
- canonical index は736/736 materialized、全736件 `measured=false`、SHA `83101abce7f292ac551a1d035db8771451335013904906e5d1c70b5c10424034`。lock は SHA `f129fbb04e5d1516188e99d9899bbff009b9bfbc11205069cd10ea1da4f31ae0`、runtime SHA `72702da4dcfa006286d929cc58ec110264046a73fbfb0e166f2d2a92b62d6325`、canonical/trace-atlas/trace-B/trace-C の列挙 hash は現行実体と全て一致した。`./tools/validate_book` は exit 0 で106章を検証した。
- HTML は321文書、44,126 href。現行 build/html の local target 欠落0、bad fragment 0で、CH105本文・runner目次からtrace-B/C JSONと `book run 105 2/3` を辿れる。`tmp/page-counts.json` は11頁/本文3,513頁/合算3,524頁、各章24–40頁を記録するが、現行HTML再生成後に保存された107行の HTML SHA は **107件すべて不一致**。したがってこの頁数は履歴値であり、現行HTMLのページ測定値とは扱わない。
- source ledger は現行 SHA `687bc91181fed27555ab293ddea039ede0f6f5b61f90e1bdcd13d4da0a0a1392`、631 rows。`metadata_ok/locator_ok=479/479`、`cited_in_resolved=479`、空候補・計画行152、`semantic_review_pending=631`。B/C接続による新規 source row の機械解決は確認できるが、全件の版・節・claim意味 sign-off には昇格させない。

### 現行追補のP判定

**P0=0、P1=4領域、P2=2領域。`learner-ready` は不可（保留）。**

P1 は (1) 全631 source row の意味・版・節・本文 claim 照合、(2) trace-D/E/F の実体化と、B/Cでも未実行の下位層（cache/pipeline/virtual memory/DRAM/RTL/FPGA等）を含む trace atlas、(3) 固定 runner の全718件が `not_run` のまま残る外部 domain・FPGA・実回路・実機 gate、(4) 全106章・13巻・全体の独立意味 sign-off である。B/Cの10/10 checks、MiniPy 18ケース、host外部tool成功はこの4領域を閉じない。

P2 は (1) `review_gates` の list（CH1–19）/dict（CH20–106）および handoff の旧新形式混在、(2) 現行HTMLに対して `tmp/page-counts.json` の107保存 hash が古いページ測定 metadata のままであること。前者は handoff edge を壊さず、後者はリンク導線を壊さないため、いずれもP0にはしない。

trace-B/C接続、runner再スイープ、canonical materialization、lock同期は現行成果物として整合している。以後はD–F/未実行下位層、source semantic、外部/FPGA、whole sign-offを解消するまで完成判定を上げない。今回も当セッションの編集対象はこのレビュー記録だけである。

## 2026-09-04 現行実装後の再照合

この報告の上段は実装前の識別値を含む履歴である。後続の現行worktreeでは、MiniPy runtimeに共有セル（`nonlocal` mutable closure）と2段階nested closureを追加し、`runtime.py` SHA=`6a383025c0944654ee9864fc16ee86bab48eef5d94dc03a2cc29b74ef8fb9d40`、canonical index SHA=`0e65d38b711f98e84d24f6be5f173377d2782e6c2119c24ade0e76c0b2eade4a`、lock記載値との一致を再確認した。受入テストは17ケース、通常stack traceは13 checks、negative traceは5 checks、`validate_book`は106章でexit 0である。

この更新により、旧本文にあったnegative artifact stale、verifier table-range未検証、MiniPy mutable closure未実装の指摘は現行状態では解消済みである。一方、CH104 runner provenance、全source rowのsemantic pending、trace B–F、外部/FPGA gate、全106章・13巻・全体の意味sign-offは未解消P1であり、P0=0でも `learner-ready`不可という判定は維持する。現行HTMLは再生成後の全107文書でページhash不一致0件（Prelude 11頁、本文3,513頁、合算3,524頁）を再確認した。`tmp/page-counts.json` SHA=`5e2eeb6d336175f02393d750740657171943a886b079d75027aa45596578f82b`、lock SHA=`0dbe3b105df5a84896241dc2db081e55919efb06bc13809909d9e164ab2a6422` である。

## 2026-09-04 固定runner再スイープ後のP1更新

Docker Desktopを起動し、lock記載のrunner image digest一致を確認したうえで `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/run_all_experiments.py --output artifacts/runner/full-run-20260904.json` を完走させた。全718/718件がexit 0、検証内訳は contract 553、analytic 127、domain 26、educational model 12、測定statusは718件すべて `not_run` である。CH104の8件も現行manifest SHA `f012e534...` とpayload/input hashへ一致し、旧runner provenanceのP1は解消済みと判定する。現行全体の未解消P1は、source semantic、trace B–F、外部/FPGA gate、全体sign-offの4領域である。再スイープは固定入力の解析・契約・教育モデル実行であり、外部domain、FPGA、実機・物理測定へは昇格させない。

再スイープで更新された全734 canonical artifactを再materializeし、canonical index SHA=`444716a2d564a12c7ad80639a64dbea0a7302d71757c76021aa2d3630adce970`、lock SHA=`cde526cbf5513ff080f85cf2d8326819a971dda84fbb65434f11ff781ed4cee2`、runtime SHA=`6a383025c0944654ee9864fc16ee86bab48eef5d94dc03a2cc29b74ef8fb9d40` の一致を確認した。`validate_book`、source ledger、domain model、MiniPy 17ケースも再通過し、P1-LOCKは発生していない。

第20〜24章のhandoffへ不足していた`handoff_status`を追加し、5件を`draft_pending_runner_and_independent_review`へ統一した。構造P2-HANDOFF-STATUSは解消済みで、schema混在（review_gates等）のP2のみ継続する。

## 2026-09-04 ローカルHTMLプレビューの現行表示

`tools/build_html.py` を更新し、HTML目次に最新JSONから算出した現行スナップショット（runner 718/718、canonical 734件、source ledgerのsemantic pending、ページ数）と関連レビューへの導線を表示するようにした。`./tools/build_html`、`./tools/validate_book`、321 HTML文書のリンク監査（43,803件、欠落0）を実行済みである。表示は非公開ドラフトの確認性を高めるものだが、4つの共有P1（source semantic、trace B–F、external/FPGA、全体sign-off）を解除しない。
`tools/trace_atlas.py` の追加後、現行スナップショットは下記の通り更新されている。

## 2026-09-04 現行追補：trace-B/Cを実行可能atlasとして接続

trace-B (`x = [1, 2, 3]`) と trace-C (`print(sum(range(1000)))`) を再生成した。両artifactは各10/10 checks（event schema、trace ID、親鎖、重複ID、`measured=false`を含む）に通過し、二回の再生成で同一SHAを得た。BはMiniPy compiler/VMとhost CPython AST/bytecode要約に加えて、4 node・3 edgeの教育用object graphを持つ。CはMiniPy stdout `499500`、AST/bytecode要約、1000回の入力由来loop modelを持つ。loop modelはCPU cycleやbranch predictorの計測ではない。

- trace-B: `artifacts/trace-B-list-construction.json`, SHA `5c26e2b4ca95b97784670e8d2448fd72147b2f935e2accabf81da43426c380c2`
- trace-C: `artifacts/trace-C-range-loop.json`, SHA `f4ec6ffb1db36a0e6716d8c8952d87c332e826d6978e806fdd0c97feab15627d`
- canonical index: 736 records, SHA `f87f954bbab3bb43f55d6ece15c9d07ab0deb532345a864e85561e546e5e0a88`
- source ledger: 631 rows、`metadata_ok/locator_ok=479/479`、`declared_locator_ok=267/267`、`cited_in_resolved=479`、`semantic_review_pending=631`
- fixed runner: 718/718 success、failure 0、measurement `not_run` 718（SHA `ccc37495e707c34cee09dbc8a5e287cd2358ed7b4ebba6ffb62f05a69769ea79`）
- MiniPy acceptance: normal 12 + negative 6 = 18 cases

この追補によって、B/Cのsource〜VMと教育用object/loopモデルの範囲は検証可能になった。ただし、B/Cのvirtual memory・cache・DRAM・RTL/FPGA・実機層、trace D–F、一次資料の全件semantic確認、全106章・13巻・全体の独立意味sign-offは未完である。P1は「source semantic」「trace atlas未実行層」「external/FPGA」「全体sign-off」の4領域を継続し、P2はreview_gates等の旧新schema混在1領域のみとする。`learner-ready`不可の判定は変更しない。

## 2026-09-04 HTML導線の現行再確認

HTML目次へtrace-B/CのJSONリンクと、ページ数が「追補前の直近完走測定」であることを表示した。`./tools/build_html` と `./tools/validate_book` は成功し、321文書・44,126内部リンク・欠落0・bad fragment 0である。Chromeによる全107文書の再測定は完走させていないため、3,524頁は履歴測定としてのみ参照する。ローカルプレビューは `http://127.0.0.1:8765/` で確認できる。

## 2026-09-04 runner同期後の最新値

第105章`list_trace`/`sum_trace`を`trace_atlas.py`へ接続した後、固定全件再スイープを再実行した。718/718件がexit 0で、verification内訳は `analytic_verified=127`、`contract_model_verified=551`、`domain_verified=26`、`educational_model_verified=14`、measurementは718件すべて`not_run`。full-run SHAは `5aeb92d15e343304a27891e3bbf0c41dc70c98882128643d7b2ba6c4e5509576`、canonical indexは736件・SHA `83101abce7f292ac551a1d035db8771451335013904906e5d1c70b5c10424034`である。MiniPy受入18ケース、atlas回帰テスト、`validate_book`、source ledger（631行、semantic pending 631）も通過した。

この値を本報告の現行基準とする。P1はsource semantic、trace B/Cの下位未実行層とtrace D–F、external/FPGA、全体sign-offの4領域を継続する。`learner-ready`への昇格は行わない。

## 2026-09-04 現行追補（trace-D/E/F実装・canonical 739・lock同期後）

前節までの識別値は履歴を含むため、ここを現行の最終追補とする。D/E/Fのartifact、CH105 manifest、runner、canonical index、lock、HTML導線を実ファイルへ再突合した。本文・manifest・source・runner・canonical・HTMLは編集していない。

- global/local manifest は13巻・106章で、巻境界は I:1–8、II:9–16、III:17–24、IV:25–32、V:33–40、VI:41–48、VII:49–56、VIII:57–64、IX:65–72、X:73–80、XI:81–90、XII:91–98、XIII:99–106。local identity 106/106、必須7成果物の欠落0、全105 handoff edgeの次章ID・題名不一致0、`handoff_status` 欠落0を確認した。実験は718件、演習は1,121件である。
- `artifacts/runner/full-run-20260904.json` は SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`、718/718 `exit_code=0`、失敗0。verification は `contract_model_verified=548`、`analytic_verified=127`、`domain_verified=26`、`educational_model_verified=17`、全718件の measurement は `not_run`。現行manifest SHAとのrunner lineageは718/718一致で、CH104を含む旧staleは再確認できない。
- `artifacts/canonical/index.json` は739/739 records、全739 `materialized=true`、全739 `measured=false`、全件 `status=executed_analytic`。canonical SHA は `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`。CH105のD/E/F entryは、それぞれ `artifacts/trace-D-file-input.json` / `artifacts/trace-E-device-input.json` / `artifacts/trace-F-network-output.json` と runner experiment 04/05/06へ接続している。

### trace-D/E/Fの実行範囲と下位 `not_run` 境界

- D (`trace-D-file-input`、SHA `9384c5be574c9a610703e75cc46cf089933b2e10b1b7b6e596b2bb09705292f`) は8 event、13/13 checks。host CPythonが一時regular fileをopen/readした filesystem 層までを `observed_host_operation` として記録し、block device と physical storage は `not_run`。これはstorage controller、block trace、物理媒体の測定ではない。
- E (`trace-E-device-input`、SHA `e2fc28ad1793c15b1a2930d2bff0587d4157fff99faed496a70c46b8d218c385`) は8 event、13/13 checks。供給したstdinをCPythonが消費した syscall 層を `observed_host_operation` とし、TTYは `not_applicable`、keyboard と device は `not_run`。これはキーボードイベント、USB、物理入力の観測ではない。
- F (`trace-F-network-output`、SHA `93fc6dc2357e89254daa53edde9216594a11b193cceca5b1e550bc122d1a0013`) は8 event、13/13 checks。loopback TCPのsocket層までを `observed_host_operation` とし、packet と network device は `not_run`。これはpacket capture、NIC、物理linkの測定ではない。
- 三つともtraceのchecks、親鎖、source reference、境界eventは検証済みだが、全eventおよびrunner/canonicalの `measured=false` / `measurement=not_run` を維持する。B/Cも教育用object/loop modelとしてchecksを通過した範囲に限られ、cache、pipeline、virtual memory、DRAM、RTL、FPGA等の下位層は未実行境界である。したがってD/E/Fの実装は「host-boundary modelの接続」を閉じるが、全層の外部実測を閉じない。

### lock・HTML・sourceの現行値

- `environment/lock.yml` SHA は `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`。canonical index、trace B–F、MiniPy runtime、runner adapter等、lockから解決できる列挙実体のhashは全件一致した。canonical SHAは上記 `61bfae...`、MiniPy runtime SHAは `72702da4dcfa006286d929cc58ec110264046a73fbfb0e166f2d2a92b62d6325`。`./tools/validate_book` は exit 0（`validated global manifest and 106 written chapter(s)`）。P1-LOCKは解消済みとする。
- HTMLは321文書、44,131内部hrefで、local target欠落0、bad fragment 0。CH105本文・manifest・runner目次からD/E/F JSONおよび `book run 105 4/5/6` を辿れる。`tmp/page-counts.json` は SHA `5e2eeb6d336175f02393d750740657171943a886b079d75027aa45596578f82b`、保存された107行のHTML hashは現行HTMLと107件すべて不一致であり、記載のPrelude 11頁・本文3,513頁・合算3,524頁は履歴値としてのみ扱う。
- `reviews/source-ledger-verification-20260903.json` は SHA `280cb384061b17e7174ef72220f74809f28183b94a3f4c260eff7e065441f2f2`、631 rows、`metadata_ok/locator_ok=479/479`、`declared_locator_ok=267/267`、`cited_in_resolved=479`、空候補152、`semantic_review_pending=631`。機械的なlocator/cited_in解決は全件semantic sign-offへ昇格させない。

### 現行P判定と learner-ready

**P0=0、P1=4領域、P2=2領域。`learner-ready` は不可（保留）。**

P1は次の4領域である。(1) 631 source row全件の版・節・本文claim意味照合、(2) D/E/Fで明示された下位 `not_run` 境界およびB/Cを含むtrace atlasの外部層（cache、pipeline、virtual memory、DRAM、RTL、FPGA等）、(3) 固定runner全718件が `not_run` の外部domain・FPGA・実回路・実機・物理測定ゲート、(4) 全106章・13巻・全体の独立意味sign-off。D/E/Fの13/13 checks、runnerのexit 0、canonical materialization、HTML導線の合格はこれらを解除しない。global delivery contractはFPGAを必須学習経路にしていないが、任意経路の「一つのreference boardで文書化・テスト」成果物はまだなく、完了宣言もしない。

P2は (1) local manifestの`review_gates`がCH1–19はlist、CH20–106はdictで、handoffも旧形式と`next_chapter: {id,title}`形式が混在するschema drift、(2) 現行HTMLに対し`tmp/page-counts.json`の107保存hashが古いpage metadataであること。handoffのID・題名および`handoff_status`自体は不一致・欠落0なので、旧P2-HANDOFF-STATUSは解消済みとする。

今回のD/E/F実装・canonical 739化・lock同期は、host-boundaryの出所と未実行境界を追跡可能にした現行成果である。下位 `not_run`、source semantic、external/FPGA、whole sign-offが残るため、完成・学習開始可能への判定は上げない。今回も当セッションの編集対象はこのレビュー記録だけである。

## 2026-09-04 現行追補（execution snapshot・source locator・HTML snapshot導線後）

前節までの数値は履歴を含むため、ここを現行の統合再確認として扱う。`artifacts/runner/execution-snapshot-20260904.json`、CH105/106のsource locator補正、HTML目次のsnapshot/full-run導線追加後に、Prelude・全106章・13巻、本文/演習/解答、manifest/handoff、registry、source/trace、runner/canonical/lock、HTMLを再読した。本文・manifest・source・runner・canonical・HTMLは編集していない。

### 現物突合の結果

- global contractはPrelude（第1章より前、操作・演習不要）→第1章から第106章の昇順、HTMLをcanonical reading、未解決findingはcompletionを止める契約で一致する。106章は13巻（巻境界 I:1–8、II:9–16、III:17–24、IV:25–32、V:33–40、VI:41–48、VII:49–56、VIII:57–64、IX:65–72、X:73–80、XI:81–90、XII:91–98、XIII:99–106）。local manifest 106/106、各7必須成果物の欠落0、identity mismatch 0、全105 handoffの次章ID/題名 mismatch 0、`handoff_status`欠落0である。
- 本文・演習・解答の空ファイル0。manifest実験718件・演習1,121件で、全manifest演習IDは対応する`exercises.txt`と`solutions.txt`のE見出しへ解決した（見出し不一致0）。concept registry 756（ID重複0）、symbol registry 474（shared 434/chapter-local 40、ID重複0）、equation registry 280（manifest参照の未知ID0）も再確認した。
- `artifacts/runner/execution-snapshot-20260904.json` は SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`、`generated_at_utc=2026-09-04T12:00:00Z`、`full-run-20260904.json` SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`、718/718成功・失敗0、Docker image digest `sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e`を固定する。selected CH105/106の16件はsnapshot、full-run、実体artifactのhash/statusが全件一致した。
- 現行full-runはverification `contract_model_verified=548`、`analytic_verified=127`、`domain_verified=26`、`educational_model_verified=17`、全718件 `measurement_status=not_run`。全718 artifactの存在・記載hash一致は0件不一致、現行manifest SHA lineageも718/718一致である。これは固定入力の解析・契約・教育モデル実行であり、CPython/RTL/SPICE/QEMU/FPGA/実機測定ではない。
- canonical indexは739/739、全件`materialized=true`・`status=executed_analytic`・`measured=false`、materialized file hash不一致0。canonical SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`。trace registry A〜FのB/C/D/E/F checksは `test_trace_atlas.py` で二回生成して通過し、MiniPyは18ケース通過した。

### source / trace の更新後境界

- 出典台帳は SHA `2f0c443cb0aba484f11ed028cc0352315fe9b688c3e1dcc9382f53d29c346cc5`、631 rows、`metadata_ok/locator_ok=479/479`、`declared_locator_ok=267/267`、`cited_in_present/resolved=479/479`、`cited_in_empty=152`、`missing_locator=0`、`semantic_review_pending=631`。`accessed_for_this_draft`は全件semantic合格を意味せず、機械的なlocator・cited_in解決を意味査読へ昇格させない。
- `src-105-trace-atlas-executable` は `tools/trace_atlas.py:1-501` とB〜F各JSONの先頭行を指すよう補正され、`declared_locator_ok=267/267`、invalid 0を維持した。だが`src-105-local-contract`のcanonical/snapshot locatorは各`:1-20`のままで、canonicalのclaim-bearing entry（CH105は約59129行以降）・snapshot selected result（16–31行）を直接指さない。B〜F各JSONの先頭行もfield単位のchecks、`layer_status`、hashの意味対応までは保証しない。
- Dはhost regular-file readのfilesystemまで、block device/physical storageは`not_run`。Eは供給stdinを読むsyscallまで、TTYは`not_applicable`、keyboard/deviceは`not_run`。Fはloopback TCPのsocketまで、packet/network deviceは`not_run`。B/CもMiniPy VMと教育用object/loop modelまでで、cache、pipeline、virtual memory、DRAM、RTL、FPGA、物理層を実行済みとはしない。全D/E/F artifactは各13/13 checks、`measured=false`であり、host操作成功を実機・物理測定へ昇格させない。

### lock / HTML / FPGA

- `environment/lock.yml` SHA `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`。canonical、adapter、materializer、trace atlas、D/E/F、MiniPy runtime等、lockから解決できる23実体のhashは全件一致。`./tools/validate_book`はexit 0（106章）である。
- HTMLは321文書、44,133 href、local target欠落0、bad fragment 0。HTML目次`index.html:41`からexecution snapshot、full-run、source-ledger review、現行whole review、trace D/E/Fのリンクを各1件確認した。`tmp/page-counts.json` SHA `5e2eeb6d336175f02393d750740657171943a886b079d75027aa45596578f82b`の107行hashは現行HTMLと107件すべて不一致で、ページ数3,524（Prelude 11、本文3,513）は履歴値として扱う。`completion-gates.md`の旧数値を含む上段は追補型履歴であり、同ファイルの最新snapshot節と本節の現行値を優先する。
- FPGAはglobal delivery contract上は必須学習経路ではないが、`machine-spec/rv32edu.md`および`book-spec`の任意経路契約（基準board/tool固定、合成、配置配線、timing、bitstream、board UART確認）は未完。現物は`chapter-50-fpga-contract`等の`measured=false`/`bitstream_not_built`契約で、実bitstream、timing report、board UART artifactはない。

### 現行のP判定と learner-ready

**P0=0、P1=3領域、P2=3領域。`learner-ready`は不可（保留）。**

P1は (1) 全631 source rowの意味・採用版・節・本文claim、およびhost CPython 3.14.7要約とlock runner Python 3.11.2の再現系譜の独立semantic sign-off、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-offである。D/E/Fのhost-boundary model、B/Cの教育モデル、snapshot lineage、runner/canonical/HTMLの機械整合はこれらを解除しない。下位`not_run`は各traceで明示された契約境界であり、誤表示のP0とは分類しないが、外部/物理実験の未完了を覆すものでもない。

P2は (1) `src-105-local-contract`とartifactのclaim-bearing field locatorが広く、今回補正した`src-105-trace-atlas-executable`もJSON先頭行止まりであること、(2) local manifestの`review_gates`がCH1–19はlist・CH20–106はdict、handoffの旧形式と`next_chapter: {id,title}`形式が混在するschema drift、(3)現行HTMLに対するpage metadata 107 hash不一致である。handoffのID・題名・status、required artifact、内部リンクは欠落・不一致0なのでP0にはしない。

次の一手は、まず現行snapshot/canonicalの実際のentry・result・hashを各source supportsへ直接割り当ててP2 locatorを閉じること、続いてCPython 3.14.7の実行環境・コマンド・hashを固定するか要約の主張範囲を狭めること。その後にsource全件の意味査読、FPGAを実行する場合の一枚のreference board証跡、章→巻→全体の独立sign-offを別記録で完了する。現状を完成宣言・学習開始可能へ変更しない。

## 2026-09-04 現行追補（CH73–80の教育境界・source locator補完後）

本体側で`machine-spec/educational-boundaries.md`（SHA `1e043b0fefe14761bf7ded7e3581401a95edf243d43e96fbbd349982d3df5805`）を追加し、CH73–80のcandidate row 32件へ版・paths・supports・cited_in・locatorを補完した後の状態を再確認した。ここでも本文・manifest・source・runner・canonical・HTMLは編集していない。

- source ledgerは SHA `ffebc6a4156be8ef9639f35b006300b4aeac8e66e36309db3e67de089abec914`、631 rows。機械値は `metadata_ok=511`、`locator_ok=511`、`locator_descriptive=98`、`declared_locator_rows/ok/invalid=299/299/0`、`cited_in_present/resolved=511/511`、`cited_in_empty=120`、`url_rows/fetched=187/187`、`local_rows=346`、`missing_locator=0`、`semantic_review_pending=631`。補完されたCH73–80の48 rowsはmetadata/locator/cited_inが全件解決したが、全631件の`semantic_review=pending`は維持され、版・節・claim意味の独立passへは昇格させない。
- `machine-spec/educational-boundaries.md`はC/ABI、rv32edu、OS/target、MiniPy/CPython、host tool、FPGA任意経路、引用使い分けを分離するlocal boundaryである。固定runner Python 3.11.2、host CPython 3.14.7、ngspice/Verilator/Yosys/QEMU候補、FPGA `candidate/not_built`を同じ実測値として扱わない契約と整合する。ただし新文書の存在は一次資料の意味査読や外部実験を完了させない。
- execution snapshotは現行full-run SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`を固定し、canonical 739、runner 718/718、D/E/F各13/13 checks、全measurement `not_run`という前節値から変化なし。lock SHA `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`、canonical SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`、`validate_book` exit 0も再確認した。
- HTMLは現行321文書・44,133 href、欠落0・bad fragment 0で、snapshot/full-run/source review/whole review/trace D/E/Fの導線を維持する。`tmp/page-counts.json`の107保存hashは現行HTMLに対して107件不一致のため、3,524頁は履歴値のままとする。

### 更新後のP判定

**P0=0、P1=3領域、P2=3領域。`learner-ready`は不可（保留）。**

P1は (1) 631 rowsの意味・採用版・節・本文claimの独立semantic sign-off（CPython 3.14.7 host要約とlock runner 3.11.2の再現境界を含む）、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-off。CH73–80の機械locator補完、education boundary追加、snapshot lineage、runner/canonical整合はこの3領域を解除しない。

P2は (1) CH105/106 local-contractおよびartifact locatorがclaim-bearing JSON fieldまで狭まっていないこと（CH105 executable rowの`trace_atlas.py:1-501`・各JSON先頭行補正は機械範囲を閉じたが意味粒度は未完）、(2) `review_gates` list/dictとhandoff旧新形式のschema drift、(3) 現行HTMLに対するpage metadataの107 hash不一致。handoff ID/title/status、必須成果物、HTML内部リンクは欠落・不一致0でP0にはしない。

今回の教育境界補完はCH73–80の参照可能性を上げたが、`semantic_review=pending`の631 rows、外部/FPGA、whole sign-offを残す。次の実務は、現行canonical/snapshotのentry・result・hashをsource supportsへ直接割り当て、全source semanticを独立確認し、FPGAを採用するなら一枚のreference boardで証跡を固定すること。現状を完成・学習開始可能へ変更しない。

## 2026-09-04 現行追補（source ledger再生成値の反映）

CH73–80の32 candidate row補完後にsource ledgerを再生成し、`machine-spec/educational-boundaries.md`との対応を含めて最終確認した。source ledgerは SHA `037a1fe7f425f913819bf0a72c3351015671612ba3d771f7f61cfa9e38a60346`、`generated_at_utc=2026-09-03T22:10:17Z`、631 rows。`metadata_ok/locator_ok=511/511`、`cited_in_present/resolved=511/511`、`declared_locator_rows/ok/invalid=299/299/0`、`url_rows/fetched=187/187`、`local_rows=346`、`missing_locator=0`、`semantic_review_pending=631`である。再生成時刻によるSHA変化は、本文・manifest・runner・canonicalを意味査読済みへ昇格させない。

現行のrunner 718/718、execution snapshot SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`、canonical 739（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）、D/E/F各13/13 checks、lock SHA `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`、HTML 321文書・44,133 href・欠落0/bad fragment 0に変化はない。`validate_book`とMiniPy/trace atlas受入テストも再通過している。

本補完後も判定は **P0=0、P1=3領域、P2=3領域、`learner-ready`不可（保留）**。P1は全source semantic（CPython版境界を含む）、FPGA任意経路の実証、全106章・13巻・全体sign-off。P2はclaim-bearing locator粒度、manifest/handoff schema drift、現行HTMLに対するpage metadata 107 hash不一致である。CH73–80の機械locator補完は第一のP1を縮小する進捗だが、631件の意味査読pending、外部実験・FPGA、全体sign-offを解除しない。次の一手は、補完済みrowを含む全sourceを独立に意味確認し、artifact locatorを実際のJSON fieldへ狭め、最後に章→巻→全体の別記録sign-offを行うこととする。

## 2026-09-04 現行追補（CH81–84 candidate source 補完後）

CH81–84の`sources.yml` 24行（各章6行）を、`machine-spec/educational-boundaries.md`、xv6 host-run記録、`machine-spec/minios-abi.md`等のpaths・version・locator・supports・cited_inと突合した。本文・manifest・sources・runner・canonical・HTMLは編集していない。ページ測定は別ゲートのため、ここでは判定対象外とした。

- source ledgerは現行SHA `5ac84961cc7f1d026513896f072b58c1d51a9c51bc707302b8665540532692e9`、`generated_at_utc=2026-09-03T22:15:27Z`、631 rows。全体の機械値は`metadata_ok/locator_ok=523/523`、`declared_locator_rows/ok/invalid=311/311/0`、`cited_in_present/resolved=523/523`、`cited_in_empty=108`、`url_rows/fetched=187/187`、`local_rows=355`、`missing_locator=0`、`semantic_review_pending=631`である。
- CH81–84の24行は、ledger上のmetadata、locator、declared locator、cited_inの各チェックが24/24で解決している。source本体でも全24行が`status: candidate`、`measured: false`、draft access falseである。したがって機械面は**pass候補24、needs_fix 0、semantic hold 24**と分類し、候補補完を意味査読済み・実行済みへ昇格させない。
- `educational-boundaries.md`（SHA `1e043b0fefe14761bf7ded7e3581401a95edf243d43e96fbbd349982d3df5805`）は`EDU-BOUNDARY-2026-09-04`のローカル教育境界であり、RISC-V Privileged仕様、xv6実装、POSIX/OS規格そのものではない。CH81のSv39/page-table、CH82のfault/COW/mmap、CH83のallocator/protection、CH84のatomic/CAS/orderingについて、補完rowが支えるのは「rv32eduのMMUなし境界」「RV64/xv6を別経路に隔離する方針」「toy/miniosの非提供範囲」であって、規格上の詳細や実装正しさではない。
- xv6候補の版・locator（commit `35b088427ef37611c38afdeed5a52a278cae38f9`、QEMU `11.1.1`、`reviews/external-xv6-host-run.md:1-33`）は、有界なhost QEMU smokeの出所を辿れるが、CH81–84のpage isolation、fault/COW、allocator、atomicity、複数core保証、実機/FPGA測定の証拠ではない。minios候補もsingle address space・identity mapping・MMUなしの境界に限られ、protected process address space、汎用filesystem/POSIX mmap/swap、multi-core lock-freeを支えない。この範囲は本文の「toy」「予定値」「実xv6・実device・実terminalではない」という明示と整合し、今回の補完だけから直接の主張過剰は検出しなかった。
- ただしCH81–84の標準候補はローカル境界文書をlocatorにしており、公式RISC-V/C/OS/言語仕様の版・節を意味査読したものではない。本文の数値・状態遷移・CAS/ordering等を規格上の事実として採用する前に、公式資料または実装ソースをclaim単位で割り当てる必要がある。全631行がsemantic pendingのため、ここは**P1**とする。新rowのcited_inは主に本文3–35行・manifest/handoffで解決しているが、補助演習・解答・個々のJSON fieldまで対応づける粒度ではなく、claim-bearing locator不足は**P2**継続である。
- 実行境界も変わらない。runnerは718/718 exit 0でも全件`measurement_status=not_run`、canonicalは739件がmaterializedでも全件`measured=false`。CH81–84の期待値、xv6 host smoke、minios境界を実CPU/MMU/OS/物理装置/FPGA測定へ読み替えない。`./tools/validate_book`はexit 0（106章）だった。

### 更新後のP判定と learner-ready

**P0=0、P1=3領域、P2=3領域。`learner-ready`は不可（保留）。**

P1は (1) 全631 source row（今回のCH81–84を含む）の公式資料・採用版・節・本文claimの独立semantic sign-off、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-off。CH81–84のcandidate補完は機械的な参照可能性を改善したが、この3領域を解除しない。

P2は (1) candidate rowおよびCH105/106 artifact locatorのclaim-bearing field粒度不足、(2)`review_gates` list/dictとhandoff旧新形式のschema drift、(3)現行HTMLに対して保存済みpage metadata 107 hashが不一致であること（ページ測定別ゲート）。必要なら本文の境界記述を直す段階ではなく、先に公式資料のclaim-level locatorとsemantic判定を付ける段階である。現時点でCH81–84本文に明白な過大主張修正は見つからないが、上記semantic gate完了までは完成・学習開始可能へ上げない。

次の一手は、CH81–84の候補を公式RISC-V Privileged仕様、xv6 commit/source、必要なC/OS/compiler仕様へ一つずつ割り当て、本文・演習・解答のclaimと実行artifact fieldを直接照合すること。その後、残る全source semantic、FPGA任意経路、ページ測定、章→巻→全体sign-offを別ゲートで閉じる。

## 2026-09-04 現行追補（CH69–72のrv32edu-toolchain補完後）

`machine-spec/rv32edu-toolchain.md`（SHA `606e9f01bddc84d33a95335fd2a5788f7f7f9550e0af178909cffab20d0d3648`、仕様版 `RV32EDU-TOOLCHAIN-BOUNDARY-2026-09-04`）の追加後、CH69–72の本文、manifest、handoff、source rowsを再照合した。本文・manifest・sources・runner・canonical・HTMLは編集していない。ページ測定は別ゲートとして扱った。

- source ledgerの現行SHAは `ed6acda3656f8d89e72799f53f6d17966473a774c449202757392a7430d76cae`、`generated_at_utc=2026-09-03T22:29:02Z`、631 rows。機械値は `metadata_ok/locator_ok=533/533`、`declared_locator_rows/ok/invalid=321/321/0`、`cited_in_present/resolved=533/533`、`cited_in_empty=98`、`url_rows/fetched=187/187`、`local_rows=365`、`missing_locator=0`、`semantic_review_pending=631`である。
- 新仕様のpath/locatorを直接持つcandidate rowは、current YAMLでCH69=2（assembler/tool）、CH70=3（ELF/object/tool）、CH71=2（ELF/linker）、CH72=2（ELF/loader）の計9行を確認した。親報告の「10 candidate rows」はこの9行に隣接するRV32I candidate等の更新を含む差分として扱う。少なくとも新仕様を直接指す9行はmetadata・locator・declared locator・cited_inが全て解決し、10行目を新仕様の直接接続と表示する場合だけは、source rowの対応を追加確認する必要がある（P2の記録粒度、P1には昇格しない）。
- CH69–72のsource rowsは各章7行、全28行が`status: candidate`、`measured: false`、`accessed_for_this_draft: false`である。今回の補完対象は機械面ではpass候補（新仕様の直接9行は9/9）、semantic面ではhold（CH69–72全28行がpending）と分類する。`rv32edu-toolchain.md`は標準ELF、完全なRISC-V psABI、dynamic linker、host OSの実行結果を代替しないと明記しているため、これらを規格・実装・boot成功の根拠へ広げない。
- 本文の範囲も過大ではない。CH69はRV32I教育subset・4-byte命令・pseudo展開を限定し、binary diff/bootを未確認とする。CH70はtoy objectとcandidate ELF parserを区別し、objectをexecutableとしない。CH71はstatic link・candidate ELF/flat imageに限定し、CPU実行を主張しない。CH72はELF32/RV32のtoy loaderと一つのlibrary/GOT相当へ限定し、host process isolation・完全なdynamic linker・実CPU起動を否定している。これらと新仕様の`may_not_claim`は整合し、今回の補完による直接の主張過剰は検出しなかった。
- 一方、`src-69-rv32i-candidate`等の標準候補はローカル教育境界をlocatorにしており、公式RISC-V ISA/ELF/psABIの版・節を意味査読した証跡ではない。assembly encoding、ELF header/relocation、GOT/PLT、stack初期化の規格上の主張を確定するには、公式資料または実装ソースをclaim単位で追加割当する必要がある。hostのVerilator/Yosys・parser候補の記録も、固定runnerの解析実行や実CPU/FPGA bootへ昇格させない。

### 更新後のP判定と learner-ready

**P0=0、P1=3領域、P2=3領域。`learner-ready`は不可（保留）。**

P1は (1) 全631 source row（CH69–72の補完行を含む）の公式資料・採用版・節・本文claimの独立semantic sign-off、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-offである。CH69–72の教育用toolchain境界追加は機械的な参照可能性を上げたが、いずれも解除しない。runner 718/718 exit 0・canonical 739 materializedでも、全measurement `not_run`の境界は維持する。

P2は (1) 新仕様を含むcandidate/artifact locatorのclaim-bearing field粒度不足と、報告された10行対current YAML直接9行の対応整理、(2) `review_gates` list/dictおよびhandoff旧新形式のschema drift、(3) 現行HTMLに対して保存済みpage metadata 107 hashが不一致であること（ページ測定別ゲート）。現時点でCH69–72本文に明白な過大主張修正はないが、公式仕様のclaim-level locatorとsemantic判定を完了するまでは完成・学習開始可能へ上げない。

次の一手は、10行差分の対応をsource historyまたはrow単位で確定し、CH69–72のassembler/object/linker/loader claimsを公式RISC-V/ELF/psABI資料および候補実装の版・節へ直接割り当てること。その後、全source semantic、FPGA任意経路、ページ測定、章→巻→全体sign-offを別ゲートで閉じる。

## 2026-09-04 現行追補（Chrome固定条件による全107文書ページ再測定後）

Chrome固定条件の全107 HTML文書（Prelude + 全106章）を再測定し、`tmp/page-counts.json`と各HTMLのhashを突合した。本文・manifest・sources・runner・canonical・HTMLは編集していない。

- 測定方法は`Chrome headless new Letter PDF + pdfinfo`、Chrome `152.0.7977.76`、pdfinfo `26.07.0`。`tools/measure_html_pages.py` SHAは `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`、`tmp/page-counts.json` SHAは `2022ec348f91382b2eefa225bb76627db5bccd669e3704d2ddb28e83f028fda9`、生成時刻は `2026-09-03T22:37:14+00:00` である。
- 107行（Prelude 1 + chapter 106）の保存`html_sha256`は現行HTMLと107/107一致し、欠落0、hash mismatch 0。Preludeは11頁、本文106章は合計3,514頁、合算3,525頁。本文のmin/maxは24/40頁、under24=0、over40=0で、章ごとの24–40頁条件を満たす。
- `build/html`は321文書・44,133内部href、local target欠落0、bad fragment 0の前節値から変化なし。ページ数とHTML hashが現行実体へ一致したため、これまでの「保存page metadata 107件不一致」は履歴上のP2として解消済みとする。

### 更新後のP判定と learner-ready

**P0=0、P1=3領域、P2=2領域。`learner-ready`は不可（保留）。**

P1は (1) 全631 source rowの公式資料・採用版・節・本文claimの独立semantic sign-off、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-offである。固定runner 718/718、canonical 739、D/E/F各13/13 checks、HTMLページ再測定の合格はこの3領域を解除しない。runner/canonicalは引き続き実行・測定境界を分離し、全measurement `not_run`を維持する。

P2は (1) candidate/sourceおよびartifactのclaim-bearing locator粒度不足（CH69–72のtoolchain補完もsemantic sign-offではない）、(2) `review_gates` list/dictとhandoff旧新形式のschema driftである。ページmetadata P2は解消済みであり、現行HTMLの導線・ページhash・24–40頁条件に残件はない。

ページ測定ゲートは完了したが、完了宣言は更新しない。次の一手はsource全件のclaim-level semantic査読、公式仕様・実装版の固定、FPGA任意経路を採用する場合のreference board証跡、章→巻→全体sign-offである。

## 2026-09-04 現行追補（章メタデータ正規化契約・schema checker追加後）

`book-spec/chapter-metadata-schema.md`（SHA `636be224080003fa20cd0bffb6fa63c9d0583ccb31653ca60a8e9884b7c61477`）と、読み取り専用の`tools/check_chapter_schemas.py`（SHA `7deda3787e40999fa0602d3d1d31923ed27b7c138da619155785bfbb2909fc0f`）を実行・再読した。本文、runner payload、canonical、manifest/handoffの実体は編集していない。

- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_chapter_schemas.py --json` は `chapters=106`、`normalized_chapters=106`、`errors=[]` で成功した。`review_gates` は `list=19`、`mapping=87`、handoffは `legacy=14`、`modern=91`、`terminal=1` と分類され、全て`CHAPTER-METADATA-NORMALIZED-1`へ正規化可能である。
- checkerは、旧`next_chapter_id/title`と新`next_chapter: {id,title}`を同一の読み取り側契約へ写し、終端106章を許容し、片側欠落・旧新混在・status欠落を検査する。rawファイルの形式差は残るが、意味を変更せず正規化する仕様とerrors=0が実証されたため、以前のmanifest/handoff schema driftは構造ゲート上 **解消済み** と判定する。
- `./tools/validate_book`もexit 0（106章）で、schema checker追加による本文・実験入力・source semantic・`measured`状態の昇格はない。runner SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`、canonical SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`、execution snapshot SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`（既記載値）に変更はない。

### 更新後のP判定と learner-ready

**P0=0、P1=3領域、P2=1領域。`learner-ready`は不可（保留）。**

P1は (1) 全631 source rowの公式資料・採用版・節・本文claimの独立semantic sign-off、(2) FPGA任意経路のreference board・tool・bitstream・timing・board UART gate、(3) 全106章・13巻・全体の独立意味sign-offである。metadata schemaの正規化はこれらを解除しない。

残るP2は、candidate/sourceおよびartifactのclaim-bearing locator粒度不足である。review_gatesとhandoffの形式差は、正規化契約・106/106・errors=0によりP2から外した。ページmetadata P2も前節の全107 hash一致で解消済みである。

schema checkerは集計・表示の読み手側契約であり、raw manifest/handoffを一括書換せず、runner payloadやsource semanticを変えない。このため現状の完成・学習開始可能判定は上げず、次の一手はclaim-level locator、全source semantic、FPGA任意経路、章→巻→全体sign-offを閉じることである。

## 2026-09-04 現行追補（claim-bearing locator追加後）

新設された任意フィールド `claim_locators` と、これを検査する `tools/verify_source_ledgers.py` の出力を、本文・演習・解答・manifest・handoff・artifactへ戻して独立に再確認した。今回も本文、sources.yml、manifest/handoff、runner、canonical、HTMLは編集していない。

- 現行 `reviews/source-ledger-verification-20260903.json` の SHA-256 は `cbb2f9b0f66c402a053da769c2a31ef020f0bb91be0f197f7e4372bc95285c6d`、生成日時は `2026-09-03T23:12:04Z`。全631行で、`metadata_ok/locator_ok/cited_in_ok=533/533/533`、明示locator `321/321/0`、`claim_locator_rows/ok/invalid=83/83/0`、`cited_in_empty=98`、URL `187/187`、local `365`、`missing_locator=0`、`semantic_review_pending=631` である。
- CH92のtokenize候補は、Python 3.14.7の公式 `tokenize` ページへ `tokenize.tokenize`、`tokenize.generate_tokens`、`tokenize.detect_encoding` の3アンカーを持つ。PEG候補も3.14.7 grammarの `full-grammar-specification` アンカーを持ち、本文の「CPythonとの比較でありMiniPyの完全実装・外部測定ではない」という境界、演習・解答の `cited_in` は現行行へ解決する。URLアンカーの存在検査は通るが、公式版・節の意味と本文claimの一致を自動証明するものではない。
- CH105のcontract rowは `book-spec/trace-registry.yml:1-71`、canonicalの該当範囲 `59509-59979` / `60001-60430`、execution snapshot `1-34`へ接続する。trace-atlas rowは `tools/trace_atlas.py:1-501`、trace-B `2-816`、C `2-20770`、D `2-398`、E `2-267`、F `2-279`、snapshot `1-34`へ接続し、CH105本文・manifest・演習・解答の引用も解決する。CH106統合contractはregistry `1-71`、canonical `60001-60430`、snapshot `1-34`へ接続する。全て実ファイルの行数内であり、推測された範囲外locatorは0件だった。
- これらの範囲は registryのtrace_id/parent/layer/sequence、B–Fのsource/AST/VM/object/host-boundary、artifact・registry・snapshotのlineageを辿るための機械的入口として十分具体化した。一方、checker自身が明記する通り、存在・行範囲の検査はclaimの意味、公式資料の版・節、artifact値の妥当性を推論しない。全631行の `semantic_review=pending` と `status=candidate`、およびB–Fの `measured=false` / measurement `not_run` は維持されている。
- `./tools/validate_book` は再実行して `validated global manifest and 106 written chapter(s)`（exit 0）だった。既確認のrunner 718/718、canonical 739、HTML導線・ページhash合格の値に今回のlocator追加による昇格はなく、lock/canonical/runner/snapshotのlineageも変わらない。

### claim-bearing locator後のP判定と learner-ready

**P0=0、P1=3領域、P2=0領域。`learner-ready`は不可（保留）。**

今回の追補で、前節まで残していた **claim-bearing locatorの構造的粒度P2は解消** と判定する。83行について全83件が具体的URLアンカーまたは実ファイル行範囲へ解決し、CH92・CH105/106・trace-B〜Fの本文claimから artifact/registry/snapshotへ戻る入口があるためである。任意フィールドを持たない残りのsource rowへ、存在しないclaim locatorを推測で補ってはいないので、この判定を全631行のsemantic passとは扱わない。

残るP1は (1) 全631 source rowの公式資料・採用版・節・本文claimの独立semantic sign-off、(2) FPGA任意経路を選ぶ場合のreference board・tool・bitstream・timing・board UART gate、(3) Prelude＋全106章・13巻・全体の独立意味sign-offである。P2を0へ下げても、`measured=false`、measurement `not_run`、candidate/semantic pendingを learner-ready の根拠へ昇格させない。

次の一手は、claim locatorの機械passを入口として、全sourceの版・節・意味を人手で確認し、FPGA任意経路の採用有無と実機証跡を別ゲートで決め、章→巻→全体のsemantic sign-offを完了することである。

## 2026-09-04 現行追補（全631 source rowの独立sign-off被覆完了後）

独立した確認セッションが、現行 `reviews/source-ledger-verification-20260903.json`（SHA-256 `deb86fb260d73ca99fa10e49510e39a881813bb5c9ebbea3be1aa0b477405be0`）の全631行を、3分割の sign-off YAML/Markdown として被覆した。`uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json` は、`source_rows=631`、`signoff_entries=631`、重複0、欠落0、形式エラー0を返した。機械監査の出力JSON SHA-256は `54e9dcba31630e3f37a6275a48f6e487f6e680758fb9ce60056ff976b0455530`、sign-off checker SHA-256は `e50d55fdee833e75a4cb5237d522cf23968c6a3bb514d563b28491ec05f7f8cb`、台帳checker SHA-256は `5b896ea8f4a2be796f5d25b564ff49ba1e169c86215a0d681343ab0416d40030` である。台帳checkerは入力行と集計が同じ場合に生成時刻を保持し、再実行でsign-offの系譜を不用意に切らない。

- [ordinal 1–200 sign-off](independent-source-signoff-001-200-20260904.md): verified 64 / accepted_boundary 40 / hold 96
- [ordinal 201–400 sign-off](independent-source-signoff-201-400-20260904.md): verified 145 / accepted_boundary 53 / hold 2
- [ordinal 401–631 sign-off](independent-source-signoff-401-631-20260904.md): verified 116 / accepted_boundary 94 / hold 21

全体合算は verified 325、accepted_boundary 187、hold 119、`coverage_complete=true`、`gate_complete=false` である。holdを完成済みと読み替えず、`semantic_review=pending` 631行を変更していない。従って出典の被覆ゲートは閉じたが、出典意味ゲートそのものは保留である。保留の主因は、採用版・節・主張対応が未確定な外部資料、または版・実体・supports・`cited_in`が空の候補行である。

同時に `./tools/build_html` を再実行し、現行HTMLは321文書、全href（`#fragment`含む）44,136件、欠落0、bad fragment 0を確認した。なお43,815件はfragmentを除外した旧集計である。目次には独立出典sign-offの3分類と被覆631/631、および監査・契約へのリンクを表示する。固定runner 718/718、canonical 739、全件`measured=false`、runner測定`not_run`の境界は変えていない。

FPGAについては ADR 0008（`docs/adr/0008-fpga-optional-add-on-path.md`）に従い、本リリースの選択経路をPC-onlyとする。基準board/tool/bitstream/timing/board UARTが未固定のFPGA任意追加経路は `candidate` / `not_built` のままで、PC-onlyの学習開始条件をブロックしない。ただし任意追加経路を後から検証済みとするには、同ADRの実機ゲートを別途閉じる必要がある。

### 現行判定

**P0=0、P1=2領域、P2=0領域。`learner-ready`は保留。**

P1は (1) hold 119行を含む全sourceの公式資料・採用版・節・本文claimの意味確認、(2) Prelude＋全106章・13巻・全体の独立意味sign-offである。PC-onlyを選択したため、FPGA実機ゲートは今回の基準経路のP1には数えないが、任意追加経路として未検証の境界を保持する。HTMLのリンク・ページ測定、runner/canonicalの構造整合、sign-off全行被覆は、これらの意味確認を代替しない。

次の作業は、hold行について本文の境界記述または公式資料の版・節・claim locatorを一行ずつ確定し、修正後に同じ独立セッションで再判定すること。その後、章→巻→全体の意味sign-offを別記録で閉じる。

## 現行追補：第5〜8章の出典追跡補正（2026-09-04）

第5〜8章の本文claim位置に合わせ、NIST/BIPM/OpenStax/MIT/Ioffe出典へ直接節または版locatorを追加し、CH5 S3/S6/S8とCH6 S2/S5の`cited_in`を本文の実際の使用位置へ補正した。機械監査は source rows=631、`claim_locator_rows/ok=113/113`、`cited_in_present/resolved=533/533`、`semantic_review_pending=631`。独立sign-offは保守的な判定を維持し、現行 `verified=325 / accepted_boundary=187 / hold=119`、`gate_complete=false` である。locatorの存在・到達性は意味確認を代替せず、hold行と全章・巻・全体の独立確認は継続する。

この補正後の台帳は `reviews/source-ledger-verification-20260903.json`（生成 `2026-09-04T01:40:37Z`、SHA-256 `deb86fb260d73ca99fa10e49510e39a881813bb5c9ebbea3be1aa0b477405be0`）を基準とする。HTMLは再ビルド後もPrelude＋106章＋companionの321文書を維持し、ローカルプレビューは `http://127.0.0.1:8765/` で確認できる。

## 2026-09-04 現行同期追補（ordinal 201–631 remaining-hold semantic pass）

現行 `reviews/source-ledger-verification-20260903.json` と3分割 sign-offを再読し、ordinal 201–631の残存holdを再確認した。source YAML、本文、manifest、runner、canonical、HTMLは変更していない。今回は、版・直接locator・`cited_in`が揃い始めたCH32/33を公式ページと本文へ戻して確認したが、必修claimの節単位意味証拠が不足するため、decisionを変更する行はなかった。

### 再判定した高優先行

- ordinal **202** / `manuscript/volume-04/chapter-32/sources.yml#3` / `src-32-systemverilog`：sources.ymlは`IEEE Std 1800-2023`、公式URL、claim locator、本文・演習・解答の`cited_in`を持つ。IEEE SAの公式ページはIEEE 1800-2023をActive Standardとして示し、SystemVerilogのsyntax/semanticsとbehavioral/RTL/gate-level abstractionを説明する。しかしCH32本文は`assign`、`always_comb`、vector幅、four-state、latch推論という具体的な言語claimを扱い、source row自身も「clause-level mapping remains pending semantic review」、`accessed_for_this_draft=false`としている。公式landing pageだけでは該当節の意味照合を閉じられないため **hold維持** とした（公式確認先: https://standards.ieee.org/ieee/1800/7743/、本文`manuscript/volume-04/chapter-32/chapter.txt:5-9,17-24,47-51`）。
- ordinal **208** / `manuscript/volume-05/chapter-33/sources.yml#4` / `src-33-ieee754`：sources.ymlは`IEEE 754-2019`、公式URL、本文・演習の`cited_in`を持つ。IEEE SAの公式ページはIEEE 754-2019をActive Standardとして、binary/decimal formats、arithmetic、exceptionsを説明する。一方CH33本文はbinary32の符号・指数・仮数幅、NaN/Infの具体的bit列、丸めを扱うが、このrowには`claim_locators`がなく、`accessed_for_this_draft=false`である。公式ページの概要だけでは必修claimを節単位で確認できないため **hold維持** とした（公式確認先: https://standards.ieee.org/ieee/754/6210/、本文`manuscript/volume-05/chapter-33/chapter.txt:15-29,31-35`）。

残るordinal 201–631のholdは上記2行と、CH85–90およびCH97–106の候補行である。後者は現行sources.ymlで版・実体・supports・`cited_in`またはlocatorが未確定であり、本文のtoy/候補/not_run境界だけから外部仕様・実装のverifiedへ昇格させなかった。従って、このpassで `verified` または `accepted_boundary` へ動かす明白な行は0件である。なお、CH32のVerilator/Yosys行やCH33のRISC-V行は現行sign-offですでにhold外だが、固定runnerの`not_run`/`measured=false`境界を実ツール・実機の測定済みと読み替えない点は継続する。

### 最新機械値と全体同期

- 現行ledgerは生成 `2026-09-04T02:51:52Z`、SHA-256 `885368a50c92ea21218dd1a983633afb7b00250c78e97ec43839d8448b02c3e0`、rows 631。機械値は metadata 533、locator 532、declared locator 321/321/0、claim locator 171/171/0、cited_in 631/631（present/resolved 533/533）、URL fetch 186/187、semantic pending 631である。
- `tools/check_source_signoff.py --json` 再実行は coverage complete、sign-off entries 631/631、missing 0、duplicate 0、errors 0、`gate_complete=false`。最新全体分類は `verified=344 / accepted_boundary=187 / hold=100`。対象ファイルの分類は ordinal 201–400が`145 / 53 / 2`、ordinal 401–631が`116 / 94 / 21`であり、今回の再判定によるdecision差分は0である。
- `tools/check_chapter_schemas.py --json` は `chapters=106`、normalized 106、review_gates `19/87`、handoff `legacy/modern/terminal=14/91/1`、errors 0。`./tools/validate_book`もexit 0で、構造ゲートは継続して閉じている。
- したがって **P0=0、P1=2領域、P2=2領域、`learner-ready`は保留** を維持する。P1は全sourceの意味sign-off（hold100を含む）とPrelude＋106章＋13巻の全体意味sign-off。P2はCH4 S3のbase URL fetch未成立（claim locator自体は機械pass）と、PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。source row decisionを変更せず、次の一手はCH32/33を含むhold行へ公式版・節・claim locator・本文引用を追加して独立再監査すること。

## 2026-09-04 現行統合追補（ledger 02:14:48Z・最終checker再実行後）

現行worktreeをもう一度読み取り専用で突合した。本文、global/local manifest、handoff、sources.yml、runner、canonical、HTML、lockは変更していない。変更は本報告へのこの追補だけである。

### 構造・巻境界・全体縦断

- `electron_to_python_chapter_manifest.yaml` は章ID 1–106を一意に持ち、`volumes=13`、`chapters=106`、learning orderは「Preludeの後に1から106まで昇順」。巻境界は V1=1–8、V2=9–16、V3=17–24、V4=25–32、V5=33–40、V6=41–48、V7=49–56、V8=57–64、V9=65–72、V10=73–80、V11=81–90（10章）、V12=91–98、V13=99–106で、global/localの`volume_title`・`chapter_in_volume`・titleは106/106一致した。
- Preludeのmanifest/本文/figures/sourcesはglobal preludeのrequired outputs 4/4を満たし、Preludeに章用のexercises/solutionsを要求する誤接続はない。全106章は`chapter.txt`、`manifest.yml`、`handoff.yml`、`exercises.txt`、`solutions.txt`、`figures.yml`、`sources.yml`が各106/106存在し、空ファイル0件だった。
- 全106 local manifestで必須metadata key（status、page target、依存、concept/derivation、artifact、experiment、exercise、source、bridge、acceptance test）が欠落0、`bridge_in`/`bridge_out`の空0。CH1→CH2…CH105→CH106はhandoffのnext id/titleが連続し、CH106は付録への終端として扱われる。schema checkerの現行値も`chapters=106`、`normalized_chapters=106`、`review_gates list/mapping=19/87`、handoff `legacy/modern/terminal=14/91/1`、`errors=[]`である。
- 章間bridgeは巻境界（8→9、16→17、24→25、32→33、40→41、48→49、56→57、64→65、72→73、80→81、90→91、98→99）で入力と次層の出力を直接読み合わせた。物理量→回路→量子/半導体→CMOS→CPU→OS→MiniPy→trace atlasという向きの逆転や、次章が未定義の前提を必須扱いする明白な矛盾は見つからなかった。
- registryの実体は concept 756（ID重複0）、symbol 474（ID重複0）、equation 280（ID重複0）、trace A–F 6（ID重複0）。local manifestからのequation reference 891件はregistryへ全て解決した。これは参照構造のpassであり、各概念・式の意味や公式資料のsemantic sign-offを意味しない。

### trace A–F、artifact、runner/canonical/lock

- `book-spec/trace-registry.yml` のA–F 6 entryと、Aのcross-layer/negative/executable、B/C/D/E/Fの現行JSONを実ファイルへ戻した。各JSONのchecksは全てtrue、`measured=false`、B=13 events、C=1010 events、D/E/F=8 eventsで、親IDの欠落は0だった。CH105 manifestはB–F各artifactをcanonical artifactとして参照し、CH106はtrace registry/atlasと未実行境界を受け取る。
- Dはfilesystemまでのhost operation後にblock device/physical storage=`not_run`、Eは供給stdinまででTTY=`not_applicable`・keyboard/device=`not_run`、Fはloopback socketまででpacket/device=`not_run`。成功したhost境界と下位未実行層を混同しない契約は本文・artifactで一致する。A–Cも教育用MiniPy/host要約であり、CPU cycle/cache/実機波形の測定ではない。
- `artifacts/runner/full-run-20260904.json` は結果718、unique 718、exit nonzero 0、artifact missing 0、全718 `measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。`execution-snapshot-20260904.json`も718/718、selected 16、全selected `not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。runner HTMLの`run-*`は718/718一意でJSONとの対応欠落0だった。
- `artifacts/canonical/index.json` は宣言/実体739/739、ID重複0、unmaterialized 0、`measured=true` 0、全件`measurement_policy=all entries explicitly measured=false`（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。`environment/lock.yml` SHAは `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`で、runner、adapter、trace atlas、A/B–F artifact、MiniPy、RV32/minios、registry、Dockerfileのlock hashは現行ファイルと全て一致した。

### HTML導線・分量

- `build/html`は321 HTML文書。全href 44,136件を解決し、local target欠落0、bad fragment 0。indexのchapter unique linkは106、Prelude linkは2（navと本文）で、runnerの全718 run IDとartifact linkも到達する。
- `tmp/page-counts.json`はPrelude 11頁、本文106章合計3,514頁、合算3,525頁、min/max 24/40、under24=0、over40=0。107行の保存HTML hashは現行HTMLと107/107一致（hash mismatch 0、JSON SHA `7d23c054d3913abf495b6679b35a38da312750a77422a3c87277d0b5a287a4ac`、測定script SHA `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`）。index status panelも現行source sign-off値 `327/187/117`、claim locator `171/171`を表示する。

### source sign-offと現行checker

- 現行 ledger `reviews/source-ledger-verification-20260903.json` は指定どおり生成 `2026-09-04T02:14:48Z`、SHA `470163ac42954cb9ad459e1b252a528cfd1c783581ad7e5ca079e35a7d4ffd2e`、rows 631。機械値は metadata 533、locator 532（うち descriptive 79）、declared locator 321/321/0、claim locator 171/171/0、cited_in 631/631（present/resolved 533/533、empty 98）、URL 187 rows・fetch 186、local 365、missing locator 0、semantic pending 631である。CH4 S3のbase ngspice URL fetch不成立がlocator 532/631・URL fetch186/187の具体的残件だが、同行の3 claim locatorは範囲検査171/171側で解決している。
- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json` は終了コード1（holdがあるため）だが、`signoff_entries/source_rows=631/631`、coverage complete、missing 0、duplicate 0、errors 0、gate complete=false。全体分類は verified 327 / accepted_boundary 187 / hold 117。本対象sign-off YAML（ordinal 401–631）は verified 116 / accepted_boundary 94 / hold 21で、source rowのdecisionは今回変更していない。
- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_chapter_schemas.py --json` と `./tools/validate_book` はともに終了コード0。schema正規化とglobal/local manifest・lock・HTML・runner/canonicalの構造ゲートは閉じたが、checkerのsource holdと全体意味sign-offは閉じていない。

### 現行判定

**P0=0、P1=2領域、P2=2領域。`learner-ready`は保留（不可）。**

- **P1-SEMANTIC:** 全631 source rowが`semantic_review=pending`で、全体checkerのhold 117行が残る。metadata/locator/claim locatorの存在検査は、公式版・節・本文claimの意味一致を証明しない。対象401–631のhold 21行も継続する。
- **P1-WHOLE:** Prelude＋106章＋13巻の構造・導線・artifact接続は閉じたが、章レビュー/巻レビューとは別の全体意味sign-offは未完であり、manifestの`unresolved_finding_blocks_completion=true`により完了宣言できない。
- **P2-URL:** CH4 S3のbase URL fetch未成立（claim locatorは範囲pass）を、再取得または利用不能の明示まで機械証跡の残件とする。
- **P2-OPTIONAL-BOUNDARY:** ADR 0008により基準経路はPC-onlyでFPGAを必修にしない。FPGAのboard/pin/clock/tool/bitstream/timing/board UART、およびtrace D/E/Fのblock・TTY/keyboard・packet/device下位層は未実行で、任意経路/追加証跡としては未検証のまま保持する。runner/canonicalのanalytic成功をこれらの実測へ昇格させない。

次の一手は、CH4 S3の取得境界を記録し、hold 117行について外部資料を必修claimにするか本文の非必修境界へ明示的に落とすかを決め、採用する行だけ公式版・節・実体・claim locator・cited_inを固定して独立再監査すること。その後、章→巻→全体の意味sign-offを別sessionで閉じる。本文、manifest、handoff、sources.yml、runner、canonical、HTML、lock、ledgerはこの追補で変更していない。

## 現行追補：独立出典再判定とHTML再測定後（2026-09-04）

独立出典確認セッションが、ordinal 21、32、64–139を再読し、版・直接claim locator・本文対応が揃う14行を `verified` へ更新した。現行 `tools/check_source_signoff.py --json` は `source_rows/signoff_entries=631/631`、`verified=339 / accepted_boundary=187 / hold=105`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false` を返す。全631行の `semantic_review=pending` と `measured=false` は維持される。

執筆側のHTML再生成後、Chrome headless＋Letterで全107文書を再測定した。`tmp/page-counts.json` は生成 `2026-09-04T02:49:47+00:00`、SHA-256 `08b2c89137f66acccb39064880e86e1e9a1e7688975b64dda6a2a4950f47d5f5`、Prelude 11頁、本文3,514頁、合算3,525頁、min/max 24/40、under24=0、HTML hash mismatch 0/107である。HTMLは321文書、内部リンク44,136件、欠落0、bad fragment 0、目次表示のsign-offも `339/187/105` へ同期した。

この最新状態でも、P0=0、P1はsource semantic hold 105行とPrelude＋106章・13巻・全体の意味sign-off未完、P2はCH4 S3のbase URL取得境界と、未選択FPGA・trace D/E/F下位層の未実行境界であり、`learner-ready` は保留である。ローカルプレビューは <http://127.0.0.1:8765/> で継続稼働中である。

## 2026-09-04 現行同期最終追補（ordinal 201–631 semantic pass）

直前の執筆側更新を含む現行worktreeへ、ordinal 201–631の残存holdを再照合した。今回の追加semantic passでdecisionを変更したsource rowは0件である。source YAML・本文・manifest・runner・canonical・HTMLは変更していない。

- 高優先のordinal 202（CH32 `src-32-systemverilog`）は、現行版 `IEEE Std 1800-2023`、公式URL、claim locator、本文/演習/解答の`cited_in`がある。公式IEEEページ（https://standards.ieee.org/ieee/1800/7743/）で標準の版・適用範囲は確認できるが、本文の`assign`、`always_comb`、vector幅、four-state、latch推論を規定するclause locatorは未指定で、source rowもclause-level mapping pending・access falseであるためhold維持。
- ordinal 208（CH33 `src-33-ieee754`）は、現行版 `IEEE 754-2019`、公式URL、本文/演習の`cited_in`がある。公式IEEEページ（https://standards.ieee.org/ieee/754/6210/）で標準の版・一般的なformat/arithmetic/exception範囲は確認できるが、本文のbinary32 field幅、NaN/Inf bit列、丸めclaimを結ぶ`claim_locators`がないためhold維持。
- その他の201–631 holdは、現行sources.ymlの版・実体・supports・locatorまたは`cited_in`が未確定、またはCH85–90/97–106の候補・未実行・任意境界である。本文の境界記述だけを外部仕様/実装のverifiedへ読み替えず、holdを維持した。

最終再実行値（この追補作成時点）は、ledger生成 `2026-09-04T02:51:52Z`、SHA-256 `885368a50c92ea21218dd1a983633afb7b00250c78e97ec43839d8448b02c3e0`、rows 631、claim locator 171/171、semantic pending 631。`tools/check_source_signoff.py --json` はsign-off 631/631、coverage complete、missing 0、duplicate 0、errors 0、`gate_complete=false`、全体 `verified=344 / accepted_boundary=187 / hold=100`。対象ordinal 201–400は `145 / 53 / 2`、401–631は `116 / 94 / 21`である。`check_chapter_schemas.py` は106/106・errors 0、`validate_book`はexit 0だった。

したがって判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留** を維持する。P1はhold 100行を含む全source意味sign-offとPrelude＋106章＋13巻の全体意味sign-off、P2はCH4 S3 base URL取得境界およびPC-only基準外のFPGA/trace D–F下位層である。次の一手はCH32/33を含むhold行へclause/section-level locatorと本文claim対応を追加して独立再監査すること。

## 2026-09-04 03:05Z 現行再実行同期（201–631追加semantic pass確定）

読み取り専用で同じ現行worktreeを再実行確認した。今回の追加semantic passでdecisionを変更したordinalは **0件**。ordinal 202（CH32/S3）と208（CH33/S4）は、公式IEEEの版・概要は確認できるものの、本文の必修claimへ結ぶ節単位locatorが不足するためholdを維持した。401–631の21 holdも、候補・版/実体/claim対応未確定・未実行境界を理由に維持した。source YAML、本文、manifest、runner、canonical、HTMLは変更していない。

- 現行ledger: rows=631、generated=`2026-09-04T02:51:52Z`、SHA-256=`885368a50c92ea21218dd1a983633afb7b00250c78e97ec43839d8448b02c3e0`。
- `check_source_signoff.py --json`: `source_rows/signoff_entries=631/631`、coverage complete、missing=0、duplicate=0、errors=0、`gate_complete=false`、`verified/accepted_boundary/hold=344/187/100`。対象201–400は`145/53/2`、401–631は`116/94/21`、対象合算は`261/147/23`。
- `check_chapter_schemas.py --json`: chapters/normalized=106/106、review_gates list/mapping=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0（106 chapters）。
- runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。execution snapshotはselected=16、全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。canonicalは739件、`measured=true`=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。lock SHAは`2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`。
- 現行page-countsはPrelude=11、本文=3514、合算=3525、min/max=24/40、under24=0、HTML hash mismatch=0、JSON SHA=`08b2c89137f66acccb39064880e86e1e9a1e7688975b64dda6a2a4950f47d5f5`、測定script SHA=`27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`。

判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留** を維持する。P1はsource意味sign-off（hold 100）とPrelude＋106章＋13巻＋全体の意味sign-off、P2はCH4 S3のbase URL取得境界およびPC-only基準外のFPGA/trace D–F下位層未実行境界である。構造・系譜・分量の機械ゲート通過は、未完の意味/実測ゲートを閉じる根拠にはしない。

## 2026-09-04 現行同期（独立出典再判定反映）

独立出典確認セッションがordinal 66、79を追加再判定し、現行sign-offは `verified=346 / accepted_boundary=187 / hold=98`（631/631被覆、errors 0、`gate_complete=false`）へ更新された。台帳は生成 `2026-09-04T02:51:52Z`、SHA-256 `885368a50c92ea21218dd1a983633afb7b00250c78e97ec43839d8448b02c3e0`。この全体統合レビューの機械確認値（106/106章、runner 718/718、canonical 739、Prelude 11頁・本文3,514頁・合算3,525頁、HTML hash mismatch 0）は維持される。

P0=0。P1はsource semanticのhold 98行とPrelude＋106章＋13巻＋全体の意味sign-off、P2はCH4 S3の取得境界およびPC-only基準外のFPGA・trace D/E/F下位層未実行境界であり、`learner-ready`は保留である。

ページ測定の現行 `tmp/page-counts.json` は生成 `2026-09-04T03:13:08+00:00`、SHA-256 `f6b8c9402a6ac6be87a735dabee62b656f19184f82b313dd28fc25bee10438a4` で、107/107 HTML hash一致（Prelude 11頁、本文3,514頁、合算3,525頁）を記録する。HTML内部リンクは44,136件、欠落0、bad fragment 0である。

## 2026-09-04 現行全体同期（ledger 03:35:39Z後）

現行worktreeを読み取り専用で再確認した。本文、manifest、handoff、sources.yml、runner、canonical、HTML、lockは変更していない。追加の意味昇格・decision変更は行っていない。

- 構造: global manifestはPrelude後の章ID 1–106を一意に保持し、13巻の境界は1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106。localの必須7ファイルは106/106存在・空0、Preludeのrequired outputsは4/4、全handoffの隣接next idは0不一致。schema checkerはchapters/normalized=106/106、review_gates list/mapping=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。
- trace/artifact境界: trace registry A–Fは6件。各trace JSONのchecksはtrue、B=13 events、C=1010、D/E/F=8、全件`measured=false`。Dはfilesystemより下のblock/physical storage、EはTTY・keyboard/device、Fはpacket/deviceを`not_run`または`not_applicable`として明示し、成功したhost操作を下位層の実測へ昇格させていない。
- runner/canonical/lock: runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。snapshotは718/718、selected=16、全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。lock SHAは`2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`で、記録された21 file hashesに不一致0。
- HTML/分量: HTMLは321文書、href=44,136、local target欠落0、bad fragment 0、indexの章リンク106・Preludeリンク2。`tmp/page-counts.json`は現行実体と107/107 hash一致、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、JSON SHA `4719f892fdd1aa17126a0319475411cfd24bc5eb4b2fb18ec406c04ea88d5990`、測定script SHA `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`。index表示のclaim locatorも172/172、sign-off表示は369/187/75である。
- source gate: 現行ledgerはrows=631、generated=`2026-09-04T03:35:39Z`、SHA `49a56cca47685055d019e14fae73974d90b6653019ed71d480d1a0e1efc5af2e`、claim locator=172/172、semantic pending=631。sign-off checkerは631/631被覆、missing=0、duplicate=0、errors=0、`gate_complete=false`、verified/accepted_boundary/hold=369/187/75。今回の対象201–631では、CH32 ordinal 202とCH33 ordinal 208をhold維持し、401–631のhold 21も維持した。
- FPGA契約: ADR 0008に従い基準経路はPC-only。FPGAは任意追加経路であり、基準board・pin/clock制約・tool version・bitstream・timing・board UART証跡が揃うまで`candidate`/`not_built`。固定runner・host tool・MiniPy・minios教育モデルをFPGA/物理測定の代替としない。なお、本文・演習・解答の接続はmanifest/source/handoffの構造的整合を確認したが、source意味sign-offおよび実験測定の完了を意味しない。

判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1はhold 75行を含むsource意味sign-offと、Prelude＋106章＋13巻＋全体の独立意味sign-off。P2はCH4 S3のbase URL取得境界、およびPC-only基準外のFPGA・trace D/E/F下位層未実行境界である。構造・導線・hash・runner/canonicalの機械passは、未完の意味sign-offや実測へ昇格しない。

## 2026-09-04 現行同期（CH20–26 POSIX 7行反映後）

独立source reviewerによるordinal 143、147、151、155、159、165、171（CH20–26 POSIX row 7件）の`verified`昇格を現行worktreeで確認した。本追補セッションによる追加decision変更はなく、対象201–631（CH32 ordinal 202、CH33 ordinal 208、401–631のcandidate hold 21件を含む）の判定も維持した。本文、manifest、handoff、sources.yml、runner、canonical、HTML、lockは変更していない。

- 現行source checker: `source_rows/signoff_entries=631/631`、coverage complete、missing=0、duplicate=0、errors=0、`gate_complete=false`、`verified/accepted_boundary/hold=376/187/68`。ledgerはgenerated=`2026-09-04T03:35:39Z`、SHA-256=`49a56cca47685055d019e14fae73974d90b6653019ed71d480d1a0e1efc5af2e`、claim locator=172/172、semantic pending=631。
- 構造・runner/canonical/HTMLの既確認値は不変。global 106章・13巻、schema errors 0、runner 718/718（全件`not_run`）、canonical 739（measured true=0）、HTML 321文書・href 44,136・欠落0・bad fragment 0、page-count Prelude 11/本文3,514/合算3,525・107/107 hash一致を維持する。index表示はsign-off `376/187/68`へ同期済み。

判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1はhold 68行を含む全sourceの意味sign-offと、Prelude＋106章＋13巻＋全体の独立意味sign-off。P2はCH4 S3のbase URL取得境界、およびPC-only基準外のFPGA・trace D/E/F下位層未実行境界である。7件の出典昇格は意味ゲートを前進させたが、`gate_complete=false`を解除するものではない。

## 2026-09-04 現行同期（CH17–19更新・401–631境界受理反映後）

現行worktreeを読み取り専用で再確認した。CH17–19のMIT直接PDF/CH18 S4更新、および401–631の21 candidate holdから`accepted_boundary`への反映後、source decisionの現在値を取得した。本追補での追加decision変更はなく、本文、manifest、handoff、sources.yml、runner、canonical、HTML、lockは変更していない。

- source checker: `source_rows/signoff_entries=631/631`、coverage complete、missing=0、duplicate=0、errors=0、`gate_complete=false`、`verified/accepted_boundary/hold=377/208/46`。ledger generated=`2026-09-04T04:30:31Z`、SHA-256=`da9fda19fe1b06d8c6810dc0fa5f515071054444930556d04873c58ec5d15ce7`、claim locator=172/172、semantic pending=631。対象201–400はverified145/accepted_boundary53/hold2、401–631は116/115/0である。
- 構造: global 106章・13巻、volume ranges `1–8/9–16/17–24/25–32/33–40/41–48/49–56/57–64/65–72/73–80/81–90/91–98/99–106`、local必須7ファイル106/106・空0、Prelude required outputs 4/4、handoff隣接不一致0。schema checkerは106/106、review_gates 19/87、handoff 14/91/1、errors 0。`validate_book`はexit 0。
- trace/runner/canonical/lock: trace A–Fのchecksは全てtrue、B=13、C=1010、D/E/F=8 events、全trace`measured=false`。runnerは718/718 success・全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）、canonicalは739・unmaterialized=0・measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）、lock SHA `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`。
- HTML/ページ: HTML 321文書・href 44,136・local target欠落0・bad fragment 0、index章リンク106・Preludeリンク2。`tmp/page-counts.json`はPrelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 hash一致、JSON SHA `4719f892fdd1aa17126a0319475411cfd24bc5eb4b2fb18ec406c04ea88d5990`、測定script SHA `27e06fb5c7f41dd57e4f980a1ea24ef0d15b18fa685d4f9295738c00b8f45c0f`。ただしHTML index status panelは`verified=377 / accepted_boundary=187 / hold=67`で、現行checkerの`377/208/46`より21件古い。この表示差はpage hash/linkの不整合ではなく、sign-off表示の同期漏れである。
- FPGA: ADR 0008どおり基準経路はPC-only。FPGAのboard/pin/clock/tool/bitstream/timing/board UARTは未固定で、任意追加経路は`candidate`/`not_built`のまま。trace D/E/Fのblock/TTY・keyboard/packet/device下位層も`not_run`/`not_applicable`であり、host操作やanalytic artifactを実測へ昇格させない。

判定は **P0=0、P1=2領域、P2=3領域、`learner-ready`保留**。P1はhold 46行を含むsource意味sign-offとPrelude＋106章＋13巻＋全体の独立意味sign-off。P2はCH4 S3のbase URL取得境界、PC-only基準外のFPGA/trace D–F下位層未実行境界、および現行source sign-off（377/208/46）に追随していないHTML index status panelである。HTMLの再生成後、index表示だけを再確認し、ページ測定・内部リンクを同じsnapshotへ保つことが次の具体的作業となる。

## 2026-09-04 現行同期（HTML status/page再同期後）

`./tools/build_html`再実行と全107文書のページ再測定後を読み取り確認した。HTML index status panelは現行source checkerの`verified=377 / accepted_boundary=208 / hold=46`へ同期し、前回検出した21件の表示漏れP2は解消した。今回の統合確認で本文、source YAML、manifest、handoff、runner、canonical、HTML、lockへの追加変更は行っていない。

- source checkerは`source_rows/signoff_entries=631/631`、coverage complete、missing/duplicate/errors=0/0/0、`gate_complete=false`。ledgerはgenerated=`2026-09-04T04:30:31Z`、SHA-256=`da9fda19fe1b06d8c6810dc0fa5f515071054444930556d04873c58ec5d15ce7`、claim locator=172/172、semantic pending=631。
- `check_chapter_schemas.py --json`はchapters/normalized=106/106、review_gates=19/87、handoff=14/91/1、errors=0、`./tools/validate_book`はexit 0。global 106章・13巻の巻境界、Prelude required outputs 4/4、local必須成果物106/106、handoff隣接不一致0を維持する。
- trace A–Fは各checks true、B=13、C=1010、D/E/F=8 events、全件`measured=false`。runnerは718/718 success・全件`measurement_status=not_run`、canonicalは739・unmaterialized=0・measured=true=0、lockの現行hash一致を維持する。
- HTMLは321文書、href 44,136、local target欠落0、bad fragment 0、index章リンク106・Preludeリンク2。page-countsは生成=`2026-09-04T05:00:12+00:00`、SHA-256=`c74e8b2983306599d3934aecd687b0b55823359ae460cc8d8b9b6a9920050a58`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 hash一致。
- FPGAはADR 0008どおりPC-only基準経路で、FPGAの基準board/tool/bitstream/timing/board UARTは未固定の任意追加経路。trace D/E/F下位層も`not_run`/`not_applicable`であり、analytic/host境界を実測へ昇格させない。

最終判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1はhold 46行を含むsource意味sign-offとPrelude＋106章＋13巻＋全体の独立意味sign-off、P2はCH4 S3のbase URL取得境界およびPC-only基準外のFPGA/trace D–F下位層未実行境界である。HTML status表示・ページhash・導線は現行値へ再同期済みだが、未完の意味sign-off/実測ゲートを解除しない。

## 2026-09-04 現行同期（source sign-off 380/208/43 後）

直前の出典sign-off更新を含む現行worktreeを読み取り専用で再確認し、この追補以外のファイルは変更していない。HTML indexのstatus panelは `verified=380 / accepted_boundary=208 / hold=43`（被覆631/631）で現行checkerと一致する。`tools/check_source_signoff.py --json` は `source_rows/signoff_entries=631/631`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false` を返した。ledgerは生成 `2026-09-04T04:30:31Z`、SHA-256=`da9fda19fe1b06d8c6810dc0fa5f515071054444930556d04873c58ec5d15ce7`。claim locatorは172/172、semantic pendingは631である。

### 構造・学習順序・巻統合

- Prelude先行一周の後、global manifestは第1–106章を昇順に並べ、13巻の境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。
- local manifest/handoff、本文、演習、解答、figures、sourcesは106章分の既存構造を維持し、schema checkerはchapters/normalized=106/106、review_gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`もexit 0である。
- 巻境界を含む前章→次章のbridge、manifest/handoffのnext契約、concept/symbol/equation registryとtrace A–Fの既存整合は変わらない。これは構造・導線の確認であり、631 source rowのsemantic_review pendingを閉じるものではない。

### runner・canonical・trace・HTML

- runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。execution snapshotは718/718、selected=16、全selected `not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。
- canonical indexは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。trace A–Fは各checks=true、B=13、C=1010、D/E/F=8 events、全件`measured=false`。D/E/Fのblock・TTY/device・packet/device下位境界は`not_run`/`not_applicable`のままである。
- HTMLは321文書、内部href=44,136、欠落0、bad fragment 0。indexの章リンク106、Preludeリンク2、source sign-off表示は380/208/43である。`tmp/page-counts.json`は生成 `2026-09-04T05:00:12+00:00`、SHA-256=`c74e8b2983306599d3934aecd687b0b55823359ae460cc8d8b9b6a9920050a58`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致。HTML表示漏れのP2は解消済みである。
- environment lockの既存SHA・runner/canonical/trace/registry等のhash整合と、PC-onlyを基準経路とするADR 0008の契約は維持する。FPGAはboard/pin/clock/tool/bitstream/timing/board UARTの証跡を要する任意追加経路であり、未選択・未構築である。

### 現行判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。**

- **P1-SEMANTIC:** source sign-offは `380/208/43` だが `gate_complete=false`。hold行を含む公式版・節・本文claimの意味照合と、Prelude＋106章＋13巻＋全体の独立意味sign-offが未完である。
- **P1-WHOLE:** 構造、巻境界、handoff、runner/canonical、HTML導線は閉じているが、機械的passを全体意味・実測完了へ昇格できない。
- **P2-URL:** CH4 S3のbase URL取得境界は、claim locatorの範囲検査passとは別に、取得可否の明示または再取得が必要である。
- **P2-OPTIONAL-BOUNDARY:** ADR 0008のPC-only基準外となるFPGAおよびtrace D/E/F下位層（block/physical、TTY/keyboard、packet/device）は未実行。host/analytic成功を物理測定へ読み替えない。

従って、HTML表示同期後も learner-ready 宣言は保留する。次の完了条件は、残存holdについて公式版・節・本文claim locatorを固定し、source semantic sign-offと全体意味sign-offを別証跡で閉じることである。本文、manifest、handoff、sources.yml、runner、canonical、HTML、lock、ledgerはこの追補で変更していない。

## 2026-09-04 現行同期（CH8/CH9 cited_in境界狭小化後）

執筆側が変更した3箇所の `cited_in` を、現行本文・演習・解答、sources.yml、取得済み公式資料、対応する独立sign-offへ再突合した。変更は次のとおりで、いずれも引用範囲を狭める修正である。

- ledger ordinal 60（CH8 S4）は `chapter.txt:204` から `chapter.txt:206-214` へ変更。本文206–214は電場/端子電圧、寸法・接触、温度・照明・湿度、DC/過渡/AC、物性値/資料値/仮定/測定の区別を比較条件として列挙する。MIT 6.002の現行locatorは回路抽象化・抵抗モデルの入口であり、この5条件を直接定義する節ではない。また取得本文はFall 2000講義由来で、sources.ymlのSpring 2007表記と一致しない。現行decision `hold` は妥当で、accepted_boundary/verifiedへの変更は不要。
- ledger ordinal 62（CH8 S6）は `chapter.txt:101` から `chapter.txt:103-113` へ変更。103–113は緩和時間模型が衝突時刻・原子配置・量子状態・相互作用を隠し、結晶周期性・不純物・強電場・界面を量子/統計/半導体物性へ引き渡す境界を明示する。OpenStax Volume 3の9.4–9.6 locator（自由電子模型、バンドと限界、半導体/ドーピング）とこの境界claimが対応し、現行sign-offの `verified` を維持する。ただし式(8.7)や実測値をこのrowへ帰属させない境界も維持する。
- ledger ordinal 67（CH9 S4）は `chapter.txt:3.4` を削除し `chapter.txt:6.2-6.3` のみに変更。6.2–6.3は分布線路の電磁場エネルギー/Poynting収支、TEM近似、放射・高次モード・損失・分散を捨てる条件を扱うが、sources.ymlのOpenStax 16.2 locatorは404で、現行16.2は平面波の一般説明に留まり、伝送線路固有の直接節ではない（Poyntingの直接locatorは別row）。現行decision `hold` を維持し、accepted_boundaryへの変更は不要。

semantic decisionの変更は0件。現行 `tools/check_source_signoff.py --json` は `source_rows/signoff_entries=631/631`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false`、`verified=381 / accepted_boundary=208 / hold=42`。ledgerは生成 `2026-09-04T05:34:59Z`、SHA-256=`f4f96ddc1f5ec8437c3a203546b6ada68452edbaee667c129efe1b0f76480f8e`、claim locator=172/172、semantic pending=631である。CH8 S6は既にverified、CH8 S4/CH9 S4はholdのままであり、sign-offのdecision集合にこの再確認による変更はない。

構造・runner/canonical/trace・ページ測定の既確認値は維持される（global 106章・13巻、schema errors=0、runner 718/718 successかつ全件`not_run`、canonical 739かつmeasured=true=0、trace A–F checks=true、HTML 321文書・href 44,136・欠落0・bad fragment 0、page-counts Prelude=11/本文=3,514/合算=3,525、min/max=24/40、107/107 hash一致、`tmp/page-counts.json` SHA=`c74e8b2983306599d3934aecd687b0b55823359ae460cc8d8b9b6a9920050a58`）。ただしHTML indexの表示は現時点で `380/208/43` のままでchecker `381/208/42` と不一致であり、表示同期をP2残件として記録する。ADR 0008のPC-only基準経路、FPGA任意経路、trace D/E/F下位層未実行境界も変更しない。

判定は **P0=0、P1=2領域、P2=3領域、`learner-ready`保留**。P1はsource semantic hold 42行を含む全体意味sign-off、P2はCH4 S3 base URL取得境界、HTML indexのsign-off表示同期、PC-only基準外のFPGA/trace D–F下位層未実行境界である。次の具体的作業は、HTMLを新ledgerのsign-off値へ再生成・再検証し、CH8 S4/CH9 S4の不足する版・直接節locatorを補って独立再監査することである。本文、manifest、handoff、sources.yml、runner、canonical、HTML、lock、ledger自体はこのレビュー追補で変更していない。

## 2026-09-04 最終現行同期（HTML sign-off表示再生成後）

HTML再生成後の現行worktreeを読み取り確認した。indexの独立出典sign-off表示は `verified=381 / accepted_boundary=208 / hold=42` となり、`tools/check_source_signoff.py --json` の全体値と一致する。前節で記録したHTML表示差分P2は解消済みであり、この追補で本文、manifest、handoff、sources.yml、runner、canonical、HTML、lock、ledgerは変更していない。

- ledgerは生成 `2026-09-04T05:34:59Z`、SHA-256=`f4f96ddc1f5ec8437c3a203546b6ada68452edbaee667c129efe1b0f76480f8e`、rows=631、claim locator=172/172、semantic pending=631。
- source checkerは `source_rows/signoff_entries=631/631`、coverage complete、missing=0、duplicate=0、errors=0、`gate_complete=false`、`verified/accepted_boundary/hold=381/208/42`。
- global manifest/13巻/106章、Prelude、schema/handoff、trace A–F、runner 718/718（全件`not_run`）、canonical 739（measured=true=0）、HTML 321文書・href 44,136・欠落0・bad fragment 0は既確認値を維持する。page-countsもPrelude=11、本文=3,514、合算=3,525、min/max=24/40、107/107 hash一致、SHA=`c74e8b2983306599d3934aecd687b0b55823359ae460cc8d8b9b6a9920050a58`である。
- ADR 0008に従うPC-only基準経路、FPGA任意追加経路、trace D/E/F下位層の`not_run`/`not_applicable`境界は変更しない。

最終判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留**。P1はhold 42行を含むsource semantic sign-offとPrelude＋106章＋13巻＋全体の独立意味sign-off、P2はCH4 S3 base URL取得境界およびPC-only基準外のFPGA/trace D–F下位層未実行境界である。HTML表示差分は解消したが、`gate_complete=false`のためlearner-ready宣言は行わない。

## 2026-09-04 06:04Z ページ測定metadataの最終同期

現行HTMLを固定Chrome条件で全107文書再測定し、Prelude 11頁、本文3,514頁、合算3,525頁、最小24頁・最大40頁・24頁未満0章、107/107 HTML hash一致を確認した。`tmp/page-counts.json` は生成 `2026-09-04T06:04:51+00:00`、SHA-256 `8717ffa4f634a3346566cbcab8ba7e35828a733e26ade0f32d114a837e3b69e9`。HTMLは321文書、href 44,136、local target欠落0、bad fragment 0である。

現行source checkerは `381/208/42`（verified/accepted_boundary/hold）、631/631被覆、形式エラー0、`gate_complete=false`。runner 718/718成功（全件 `not_run`）、canonical 739（全件 `measured=false`）と、ADR 0008に基づくPC-only基準経路・未構築FPGA任意経路の境界を維持する。判定は **P0=0、P1=2領域、P2=2領域、`learner-ready`保留** であり、今回の再測定は未完のsource意味・全体意味・実測ゲートを解除しない。

## 2026-09-04 現行全体統合同期（source semantic再監査・06:31 ledger後）

最新の独立出典再監査後のworktreeを、Prelude＋106章・13巻の構造、章間handoff、trace A–F、runner/canonical/lock、HTML導線、PC-only/FPGA境界へ再突合した。本文・manifest・handoff・sources.yml・runner・canonical・HTML・lockは変更せず、このレビュー追補のみを追加した。

- source sign-offは `verified=387 / accepted_boundary=208 / hold=36`、被覆 `631/631`、`errors=[]`、`gate_complete=false`。`tools/check_source_signoff.py --json` の現行値は ledger生成 `2026-09-04T06:31:26Z`、SHA-256=`ed09d9c66a3a4945ebe8d1dad2fd8b2ebcdabeeff23b6eaa96fbcc66e960a842`、claim locator `172/172`、semantic pending `631` と一致する。
- global manifestは章数106を保持し、Prelude後の学習順序と13巻の既存境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）に変更なし。schema checkerはchapters/normalized `106/106`、review gates `19/87`、handoff `legacy/modern/terminal=14/91/1`、errors 0。`./tools/validate_book`はexit 0である。Preludeのrequired outputs、全章の本文・演習・解答・manifest・handoff・figures・sourcesの接続も既確認値を維持する。
- trace A–Fは各JSONのchecks=true、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。Dはfilesystemより下のblock/physical、EはTTY/keyboard/device、Fはpacket/deviceを`not_run`/`not_applicable`として保持し、host操作を下位層の実測へ昇格させていない。runnerは718/718 success・failed=0・全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）、execution snapshotは718件・selected_results 16件・全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。
- canonical indexは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。environment lockの既存runner/canonical/trace/registry hash整合と、ADR 0008のPC-only基準経路・FPGA任意追加経路契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡は未完で、基準経路をブロックしない任意候補のままである。
- HTML再生成後の現行導線は321文書、内部href 44,136件、欠落0、bad fragment 0、index章リンク106、Preludeリンク2で、indexのsign-off表示も `387/208/36` に同期している。`tmp/page-counts.json`は生成 `2026-09-04T06:47:54+00:00`、SHA-256=`04dbca8964757f7647189621049b55f78189033da3e91633c8f1762df438f8c1`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致。ページ導線・表示の不整合は今回確認されなかった。

### 現行判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。**

- **P1-SEMANTIC:** hold 36行を含むsourceの公式版・節・本文claim意味照合と、Prelude＋106章＋13巻＋全体の独立semantic sign-offが未完であり、`gate_complete=false`を維持する。
- **P1-WHOLE:** global/local manifest、巻境界、handoff、trace/artifact、runner/canonical、HTML導線の構造的整合は確認済みだが、構造passを学習内容の意味完了・外部実行・実測へ読み替えられない。
- **P2-URL:** CH4 S3 base URLの取得境界は、claim locatorの範囲検査passとは別に再取得または利用不能の明示が必要である。
- **P2-OPTIONAL-BOUNDARY:** PC-only基準外のFPGAおよびtrace D/E/F下位層は未実行。任意経路であり基準学習順序を妨げないが、実機完了の証跡ではない。

従って learner-ready 宣言は保留する。次の完了条件は、残存holdの意味sign-offと全体sign-offを閉じ、CH4 URL境界を記録し、必要な場合のみFPGA/trace下位層を別ゲートで実行することである。

## 2026-09-04 現行全体統合同期（07:16 ledger・07:34 page-counts後）

最終出典反映後の現行worktreeを独立に再確認した。Prelude＋106章・13巻の順序/境界、本文・演習・解答・manifest・handoff、trace A–F、runner/canonical/lock、HTML導線、ADR 0008のPC-only/FPGA境界に、前追補からの構造的な破綻は見つからない。今回の変更はこのレビュー追補のみで、本文、source YAML、manifest、runner、canonical、HTML、lockは変更していない。

- source checkerは `verified=390 / accepted_boundary=208 / hold=33`、`source_rows/signoff_entries=631/631`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false`。ledgerは生成 `2026-09-04T07:16:26Z`、SHA-256=`7802765eb0bbdb682d62fe0b0b5b535780e9bca9c49673f385174af0ed2cd9cd`、claim locator=172/172、semantic pending=631である。
- global manifestはPrelude後の第1–106章と13巻の既存境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0、`./tools/validate_book`はexit 0。Preludeのrequired outputs、全章の本文・演習・解答・handoff/source接続も既確認値を維持する。
- trace A–Fは各checks=true、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`である。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。execution snapshotはexperiment 718、selected_results 16、全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。
- canonical indexは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。environment lockのrunner/canonical/trace/registry hash整合は既確認値を維持する。ADR 0008によりPC-onlyが基準経路で、FPGAはboard/pin/clock/tool/bitstream/timing/board UARTが未完の任意追加候補である。
- HTMLは321文書、href=44,136、local target欠落0、bad fragment 0、index章リンク106、Preludeリンク2。`tmp/page-counts.json`は生成 `2026-09-04T07:34:42+00:00`、SHA-256=`d52e32b6161d574796f0d564d032daa03e99811dfcabf7d5bc43408d1e983af4`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致。HTML indexのsign-off表示は現時点で `389/208/34` であり、checkerの `390/208/33` と1行ずれているため、導線自体はpassだが表示同期をP2として残す。

### 現行判定

**P0=0、P1=2領域、P2=3領域、`learner-ready`保留。**

- **P1-SEMANTIC:** hold 33行を含むsourceの公式版・節・本文claim意味照合と、Prelude＋106章＋13巻＋全体の独立意味sign-offが未完であり、`gate_complete=false`を維持する。
- **P1-WHOLE:** 章順序、巻境界、handoff、trace/artifact、runner/canonical、HTML導線の構造整合は閉じているが、機械的passを外部実行・実測・学習内容の意味完了へ昇格できない。
- **P2-URL:** CH4 S3 base URLの取得境界は、claim locator範囲passとは別に再取得または利用不能の明示が必要である。
- **P2-HTML-STATUS:** HTMLの文書・リンク・fragmentは正常だが、indexのsign-off表示を最新checkerの390/208/33へ同期する必要がある。
- **P2-OPTIONAL-BOUNDARY:** PC-only基準外のFPGAとtrace D/E/F下位層は未実行。任意経路であり基準順序は妨げないが、実機完了の証跡ではない。

従って learner-ready は保留する。次の具体的作業はHTML indexのstatusを最新sign-offへ再同期し、残存holdの意味sign-offと全体sign-offを閉じることである。

## 2026-09-04 現行全体統合同期（08:11 ledger・08:42 page-counts後）

最終出典反映後の現行worktreeを独立に再突合した。Prelude＋106章・13巻の構造と学習順、本文・演習・解答・manifest/handoff、trace A–F、runner/canonical/lock、HTML導線、ADR 0008のPC-only/FPGA境界に、構造上の新たな破綻はない。今回の変更は本追補だけであり、本文、source YAML、manifest、runner、canonical、HTML、lockは変更していない。

- source checkerは `verified=403 / accepted_boundary=208 / hold=20`、`source_rows/signoff_entries=631/631`、`coverage_complete=true`、`missing_ids=[]`、`duplicate_ids=[]`、`errors=[]`、`gate_complete=false`。ledgerは生成 `2026-09-04T08:11:43Z`、SHA-256=`fd9d8e4f15fc5c32bebe3e51a8fb52f38146e97bc9fc842595191ddd97b17c28`、claim locator=187/187、semantic pending=631である。
- global manifestはPrelude後の第1–106章を保持し、13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）と巻内/巻間handoffに変更なし。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0である。
- trace A–Fのchecksは全てtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fはblock/physical、TTY/keyboard/device、packet/device下位層を`not_run`/`not_applicable`として保持する。runnerは718/718 success・failed=0・全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）、execution snapshotは718件・selected_results 16件・全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。
- canonical indexは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。environment lockの既存hash整合と、ADR 0008に基づくPC-only基準経路・未構築FPGA任意追加経路を維持する。
- HTMLは321文書、全href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。なお43,815はfragmentを除外した旧集計である。`tmp/page-counts.json`は生成 `2026-09-04T08:42:02+00:00`、SHA-256=`457383a1c42835bf5645481be3640665852a868dc966667c727ae3a97c5093cf`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。indexの旧時点表示 `390/208/33` は後続の再生成で `403/208/20` へ同期済みであり、リンク・fragment passとは分離した過去の表示同期残件として記録する。

### 現行判定

**P0=0、P1=2領域、P2=3領域、`learner-ready`保留。**

- **P1-SEMANTIC:** hold 20行を含むsourceの公式版・節・本文claim意味照合と、Prelude＋106章＋13巻＋全体の独立semantic sign-offが未完であり、`gate_complete=false`を維持する。
- **P1-WHOLE:** 構造、学習順、巻境界、handoff、trace/artifact、runner/canonical、HTML導線は機械的に整合するが、外部実行・物理測定・意味完了を示すものではない。
- **P2-URL:** CH4 S3 base URLの取得境界はclaim locator範囲passとは別に再取得または利用不能の明示が必要である。
- **P2-HTML-STATUS（解消済み）:** 43,815はfragment除外の旧集計であり、最新定義のHTML本体は321文書/全href 44,136（fragment含む）/欠落0/bad fragment0。indexのsign-off表示も403/208/20へ同期済みで、現行P2には含めない。
- **P2-OPTIONAL-BOUNDARY:** PC-only基準外のFPGAおよびtrace D/E/F下位層は未実行。任意経路であり基準順序を妨げないが、実機完了の証跡ではない。

従って learner-ready は保留する。次の具体的作業はindex表示を最新sign-offへ同期し、残存holdの意味sign-offと全体sign-offを閉じることである。

## 2026-09-04 最終現行全体同期（07:53 page-counts・index再生成後）

目次の再生成と最終ページ測定後の現行worktreeを読み取り専用で再突合した。HTML indexのsign-off表示は `390/208/33` へ同期し、前追補のP2-HTML-STATUSは解消した。本文、source YAML、manifest、handoff、runner、canonical、HTML、lockは変更せず、このレビュー追補のみを追加した。

- source checkerは `verified=390 / accepted_boundary=208 / hold=33`、`source_rows/signoff_entries=631/631`、coverage complete、missing=0、duplicate=0、errors=0、`gate_complete=false`。ledgerは生成 `2026-09-04T07:16:26Z`、SHA-256=`7802765eb0bbdb682d62fe0b0b5b535780e9bca9c49673f385174af0ed2cd9cd`、claim locator=172/172、semantic pending=631である。
- global manifestはPrelude後の106章を13巻の既存境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）で保持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、Prelude、本文・演習・解答、manifest/handoff/sourceの既存接続も変化なし。
- trace A–Fはchecks=true、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/deviceは`not_run`/`not_applicable`境界を維持する。runnerは718/718 success・failed=0・全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）、snapshotは718件・selected_results 16件・全件`not_run`（SHA `ac641b49a5d391cc3078be262ddba3df0fa488f573ef05cffeee0a8585dae37a`）。
- canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。environment lockの既存hash整合と、ADR 0008のPC-only基準経路・FPGA任意追加経路（board/pin/clock/tool/bitstream/timing/board UART未完）は維持される。
- HTMLは321文書、href=44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。`tmp/page-counts.json`は生成 `2026-09-04T07:53:10+00:00`、SHA-256=`2e01f35048a63f4857f7d41290490bca2969264a53e33187a77d05ffb78284ae`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致。HTML導線・表示の不整合は今回確認されなかった。

### 現行判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。**

- **P1-SEMANTIC:** hold 33行を含むsourceの公式版・節・本文claim意味照合、およびPrelude＋106章＋13巻＋全体の独立semantic sign-offが未完である。
- **P1-WHOLE:** 構造・巻境界・handoff・trace/artifact・runner/canonical・HTML導線は機械的に整合するが、外部実行・物理測定・学習内容の意味完了を示すものではない。
- **P2-URL:** CH4 S3 base URLの取得境界はclaim locator範囲passとは別に再取得または利用不能の明示が必要である。
- **P2-OPTIONAL-BOUNDARY:** PC-only基準外のFPGAおよびtrace D/E/F下位層は未実行。任意経路であり基準学習順序を妨げないが、実機完了の証跡ではない。

`gate_complete=false`のため、learner-ready宣言は行わない。次の完了条件は残存holdの意味sign-offと全体sign-offを閉じ、CH4 URL境界を記録し、必要な場合のみFPGA/trace下位層を別ゲートで実行することである。

## 2026-09-04 最新現行同期（checker 403/208/20・全href 44,136）

最新のindex再生成後に、全体統合の表示値と機械検証値を再確認した。indexは `verified=403 / accepted_boundary=208 / hold=20` とcheckerへ一致している。HTMLの相対hrefはfragment（`#...`）を含む定義で `44,136`（321文書）、欠落0、bad fragment 0であり、前追補の43,815はfragmentを除外した集計なのでP2差分として扱わない。本文、source YAML、manifest、runner、canonical、HTMLは変更せず、本追補のみを追加した。

- source sign-offはcoverage `631/631`、errors=0、`gate_complete=false`。現行ledgerは生成 `2026-09-04T08:11:43Z`、SHA-256=`fd9d8e4f15fc5c32bebe3e51a8fb52f38146e97bc9fc842595191ddd97b17c28`。ページ測定は `tmp/page-counts.json`（生成 `2026-09-04T08:42:02+00:00`、SHA-256=`457383a1c42835bf5645481be3640665852a868dc966667c727ae3a97c5093cf`）でPrelude=11、本文=3,514、合算=3,525、107/107一致を維持する。
- Prelude＋106章・13巻の境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）、schema/handoff、runner 718/718（全件not_run）、canonical 739（unmaterialized=0、measured=true=0）、trace A–F、lock、HTML導線の機械的整合に新たな差分はない。PC-only基準とADR 0008のFPGA任意追加経路も維持する。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 20を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。HTML表示差は解消済みで、P2に数えない。`gate_complete=false`のため完成宣言は行わず、残holdの意味確認・全体sign-off・CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（CH12/CH20反映・checker 405/208/18）

CH12 S6およびCH20 S3の独立出典判定反映後、Prelude＋106章＋13巻の統合状態を現行ファイルへ再突合した。index表示は `verified=405 / accepted_boundary=208 / hold=18` でcheckerと一致し、source coverageは `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false` である。ledgerは生成 `2026-09-04T09:02:21Z`、SHA-256=`23e9509eeeaffb587a387519122a29131b67ea203389e1b9ee276d93e557e714`。本文、source YAML、manifest、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答、handoff、巻内/巻間導線の機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。このrunner/canonical/trace証跡は意味sign-offや物理測定の完了を意味しない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。`tmp/page-counts.json`は生成 `2026-09-04T09:24:50+00:00`、SHA-256=`f8f341f065ad64863066a2bf0e317213e64be276f516f93254620e75376aea5e`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致を確認した。HTML表示・リンク・ページ測定のP2差分はない。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡、およびtrace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 18行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。HTMLの321文書・44,136 href・欠落0/bad fragment 0はpassであり、過去のfragment除外集計との差分をP2に数えない。`gate_complete=false`のためlearner-ready宣言は行わず、残holdの意味確認、全体sign-off、CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（CH12 S5反映・checker 406/208/17）

CH12 S5のverified昇格後、測定完了した現行worktreeをPrelude＋106章＋13巻の統合ゲートへ再突合した。HTML indexは `verified=406 / accepted_boundary=208 / hold=17` とcheckerへ一致し、source coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false` を確認した。ledgerは生成 `2026-09-04T09:30:14Z`、SHA-256=`c2c686d5dcedd864b646197792f6e95efa1005f2d8f516efe4c0dc0a032fa594`。本文、source YAML、manifest、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答、handoff、巻内/巻間導線の機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。runner/canonical/traceは意味sign-offまたは物理測定完了の証跡ではない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2を独立集計でも確認した。`tmp/page-counts.json`は生成 `2026-09-04T09:48:50+00:00`、SHA-256=`d5935594030f130c287be3aa63cd899651be23335955a85507b33a1fd854c8bb`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡と、trace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 17行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。HTMLの321文書・44,136 href・欠落0/bad fragment 0とページ測定はpassであり、P2に数えない。`gate_complete=false`のためlearner-ready宣言は行わず、残holdの意味確認、全体sign-off、CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（source checker 410/208/13）

現行source sign-off更新後、Prelude＋106章＋13巻の統合状態を読み取り専用で再突合した。source checkerは `verified=410 / accepted_boundary=208 / hold=13`、coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false`。ledgerは生成 `2026-09-04T10:10:45Z`、SHA-256=`baf0667c3be9910198a82c3a4aa1e23226e37a6333b1af86a6eb173e4b7e3d8a`。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答・handoffの機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。これらは意味sign-offまたは物理測定完了の証跡ではない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。独立リンク監査でも同値を確認した。`tmp/page-counts.json`は生成 `2026-09-04T09:48:50+00:00`、SHA-256=`d5935594030f130c287be3aa63cd899651be23335955a85507b33a1fd854c8bb`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。一方、現行indexの表示は `406/208/17` でsource checkerの `410/208/13` より古く、HTML再生成後のsign-off表示同期が未完である。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡とtrace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=3領域、`learner-ready`保留。** P1は (1) hold 13行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) source checkerに対するHTML index sign-off表示の未同期（406/208/17対410/208/13）、(3) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。HTMLの文書・全href・欠落・fragment・ページ測定自体はpassである。`gate_complete=false`のためlearner-ready宣言は行わず、index再生成、残holdの意味確認、全体sign-off、CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（index再生成・checker 410/208/13）

先ほどの一時的なindex表示差を除き、build後の現行worktreeを再突合した。HTML indexは `verified=410 / accepted_boundary=208 / hold=13` とsource checkerへ同期済みで、source coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false` である。ledgerは生成 `2026-09-04T10:10:45Z`、SHA-256=`baf0667c3be9910198a82c3a4aa1e23226e37a6333b1af86a6eb173e4b7e3d8a`。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答・handoffの機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。これらは意味sign-offまたは物理測定完了の証跡ではない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2を独立リンク監査でも確認した。再build後の`tmp/page-counts.json`は生成 `2026-09-04T10:28:19+00:00`、SHA-256=`fe43aa82f2724910becdcbbb623eb4d266634ac2c94e9303446f747e45ea065a`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡とtrace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 13行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。index表示差は解消済みで、HTMLの321文書・44,136 href・欠落0/bad fragment 0、ページ測定107/107一致はP2ではない。`gate_complete=false`のためlearner-ready宣言は行わず、残holdの意味確認、全体sign-off、CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（source checker 418/208/5・測定完了）

ソース再監査・HTML再build・ページ測定の完了後、Prelude＋106章＋13巻の全体統合を再突合した。HTML indexは `verified=418 / accepted_boundary=208 / hold=5` とsource checkerへ一致し、coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false` である。ledgerは生成 `2026-09-04T10:51:40Z`、SHA-256=`398155589bcaae1a9347695d8c5d1e6af83ad20852d67cb139fdc639831be477`。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答・handoffの機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。これらは意味sign-offまたは物理測定完了の証跡ではない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2を独立リンク監査でも確認した。`tmp/page-counts.json`は生成 `2026-09-04T11:11:53+00:00`、SHA-256=`fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡とtrace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 5行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH4 S3 base URLの取得境界、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。index表示、HTMLリンク、ページ測定は現行値で整合し、P2には含めない。`gate_complete=false`のためlearner-ready宣言は行わず、残holdの意味確認、全体sign-off、CH4 URL境界記録を完了条件として残す。

## 2026-09-04 最新現行同期（ledger 11:20:33Z・ngspice URL境界）

最新ledger/sign-off同期後の現行worktreeを、Prelude＋106章＋13巻の全体統合ゲートへ再突合した。source checkerは `verified=418 / accepted_boundary=208 / hold=5`、coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=false`。ledgerは生成 `2026-09-04T11:20:33Z`、SHA-256=`742baaa651eafcca831298a8af474aeea35a434abd7dae73fdf07a45906a6d68`。本文、manifest、source YAML、runner、canonicalの内容変更はなく、ledger同期後にHTML目次の状態表示を再生成し、本レビュー追補を追加した。

- URL監査はunique URL `78`、取得 `77/78`で、未取得の1件はSourceForge旧リリースのngspice-42 PDF（HTTP 403）である。公式旧リリース一覧の掲載と取得不能境界は記録済みであり、CH12 ngspiceのURL到達性を意味確認済み・target runtime ngspice-42.2の実行互換性・測定済みとは扱わない。機械ledger側もURL rows/fetched `187/186`、claim locator `189/189`、semantic pending=631を記録する。
- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0で、本文・演習・解答・handoffの機械的接続に新たな不整合はない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。これらは意味sign-offまたは物理測定完了の証跡ではない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。`tmp/page-counts.json`は生成 `2026-09-04T11:11:53+00:00`、SHA-256=`fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡とtrace D/E/F下位層の実行は未完であり、基準経路の完了と混同しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) hold 5行を含むsource semantic sign-off、(2) Prelude＋106章＋13巻の独立whole semantic sign-off。P2は (1) CH12 ngspice-42 SourceForge PDFのHTTP 403という取得境界（旧版公式掲載・不能状態を記録済み）、(2) PC-only基準外のFPGAおよびtrace D/E/F下位層の未実行境界である。CH4 URLを現行P2とは扱わない。HTML表示・リンク・ページ測定は整合している。`gate_complete=false`のためlearner-ready宣言は行わず、残holdの意味確認、全体sign-off、CH12 URL境界の明示的受理を完了条件として残す。

## 2026-09-04 最新現行同期（source semantic gate complete・423/208/0）

IEEE 1800/754の独立専門家監査反映後、Prelude先行一周＋106章＋13巻の全体状態を現行ファイルへ再突合した。source checkerは `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=true`。ledgerは生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`。source semantic gateは完了扱いにできるが、これだけで章・巻・全体の統合確認、外部domain実験、FPGA、実機測定を完了扱いにはしない。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビュー追補のみを追加した。

- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0。各章manifestのstatusはなお106/106件が`drafted_pending_*_and_independent_review`（artifact待ち5、runner待ち96、runner+SPICE待ち3、SPICE待ち2）であり、schema通過を章確認完了へ読み替えない。
- trace A–Fのchecksはtrue、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。D/E/Fのblock/physical、TTY/keyboard/device、packet/device下位層は`not_run`/`not_applicable`境界を維持する。runnerは718/718 success、failed=0、全件`measurement_status=not_run`（SHA `405a88a1b49faae8b97c0ec786588bfa547802ad0fb231c6a9ce7af6365c9d9e`）。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。固定runnerの解析・契約成功を外部domain実験または物理測定成功へ昇格させない。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。独立リンク監査でも同値を確認した。現行`tmp/page-counts.json`は生成 `2026-09-04T11:11:53+00:00`、SHA-256=`fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb`、Chrome `152.0.7977.76`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。indexのsource表示は423/208/0へ同期済み。
- URL取得の未成立1件はSourceForge旧ngspice-42 PDFのHTTP 403（unique URL 78、取得77/78）だが、公式旧版掲載・取得不能境界と代替PDFの意味確認を記録済みで、source gateは`hold=0`で閉じている。これはtarget runtime ngspice-42.2の実行互換性・測定済みの証跡ではない。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする契約を維持する。FPGAのboard/pin/clock/tool/bitstream/timing/board UART証跡は未完であり、実機経路を選択しない限り基準学習経路をブロックしない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** source semantic gate自体は完了し、P1は (1) 106章の章確認・13巻の巻統合確認・Prelude＋全体の独立whole sign-off、(2) 固定runnerが全件`not_run`である外部domain実験・必修実験再現の未完である。P2は (1) PC-only基準外のFPGA任意経路（未選択・未構築）、(2) trace D/E/F下位層を含む実機・物理測定（未実行）である。CH12 ngspice URLの403は境界記録済みでsource holdではない。`gate_complete=true`でも学習開始可能条件（章・巻・全体の独立確認と実験再現）を満たす証拠にはならないため、learner-ready宣言は行わない。

## 2026-09-04 最新現行同期（Docker固定runner再現・source gate complete）

Docker Desktop Linuxのlock固定imageから全718件を実再現した現行worktreeを、Prelude先行一周＋106章＋13巻の全体統合へ再突合した。source checkerは `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、missing=0、duplicate=0、errors=0、`gate_complete=true`。ledgerは生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`。source gate完了とrunner再現成功は記録できるが、章・巻・全体の独立意味確認、変更課題・故障診断、外部実測・FPGA・実機を完了扱いにはしない。本文、manifest、source YAML、HTMLは変更せず、本レビュー追補のみを追加した。

- runner `artifacts/runner/full-run-20260904.json` は `experiment_count=718`、success=718、fail=0、verification内訳 `contract_model_verified=548 / analytic_verified=127 / domain_verified=26 / educational_model_verified=17`、全718件`measurement_status=not_run`。runner SHA-256=`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`。execution snapshotは生成 `2026-09-04T12:13:21Z`、run artifact SHAは同じ`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`、image=`electron-to-python-runner:bookworm`、image id=`sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e`、SHA-256=`e1420aed3fafb90804b997b78411917a2ad120e8780551e3707d1edc60333ae0`である。
- global/local manifestはPrelude先行一周後の106章・13巻境界（1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106）を維持する。schema checkerはchapters/normalized=106/106、review gates=19/87、handoff legacy/modern/terminal=14/91/1、errors=0。`./tools/validate_book`はexit 0。各章manifest statusはなお独立review待ちで、機械schema通過を章・巻の意味確認完了とは読み替えない。
- trace A–Fはchecks=true、B=13 events、C=1010 events、D/E/F=8 events、全件`measured=false`。Docker runnerの成功はhost操作と解析・契約再現の証跡であり、trace D/E/F下位層のblock/physical、TTY/keyboard/device、packet/device測定を完了しない。canonicalは739件、unmaterialized=0、measured=true=0（SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。
- HTMLは321文書、相対href（`#fragment`含む）44,136、欠落0、bad fragment 0、index章リンク106、Preludeリンク2。`tmp/page-counts.json`は生成 `2026-09-04T11:11:53+00:00`、SHA-256=`fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb`、Prelude=11、本文=3,514、合算=3,525、min/max=24/40、under24=0、107/107 HTML hash一致である。indexのsource表示は423/208/0へ同期済み。
- ADR 0008に従いPC-onlyを基準学習経路、FPGAを任意追加経路とする。FPGAは未選択・未構築で、board/pin/clock/tool/bitstream/timing/board UART証跡は存在しない。CH12 ngspice-42旧版PDFのHTTP 403は取得不能境界として記録済みでsource gateを阻害しないが、target runtime互換性や測定済みを意味しない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** source semantic gateは `gate_complete=true` で閉じた。P1は (1) 章・巻・全体の独立意味確認（各章manifest statusが独立review待ち）、(2) 変更課題・故障診断および必修実験の学習者向け再現（runnerは全件successだが全件`measurement_status=not_run`）である。P2は (1) PC-only基準外のFPGA任意経路、(2) trace D/E/F下位層を含む実機・物理測定である。`gate_complete=true`はsource gateだけの状態であり、CONTEXTの学習開始可能条件を満たさないため、learner-ready宣言は行わない。

## 2026-09-04 最新現行同期（別session章ゲート反映・P1再分解）

最新の章別独立成果物を、既存の章別レビューの単純結合ではなく、全体統合の別ゲート証跡として現行worktreeへ突合した。`reviews/independent-chapter-confirmation-20260904.md` は Prelude＋CH1–56（Vol.1–7）を対象に、本文・演習・解答・manifest/handoff・artifact系譜を再確認し、章ローカル判定を **P0=0 / P1=0 / P2=0** としている。ただし同文書自身が、全718 runnerの`measurement_status=not_run`とCH57–106未確認を共有ゲートとして残しており、これを巻・全体完了とは扱わない。`reviews/chapters-57-106-cross-independent-review-20260904.md` はCH57–106（Vol.8–13）を対象に、局所判定を **P0=0 / P1=2系統 / P2=0** としている。その2系統は、CH99のMiniPy実装範囲とmanifestの`implemented`/`executed_analytic`表示のずれ、およびCH97–103のgeneric contract/analytic runnerをMiniPy/CPython実装検証と誤読し得る境界表示である。両文書は執筆側とは別sessionの章ゲートであり、source signoffや巻・全体signoffの代替ではない。

- source semantic gateは現行 `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、errors=0、`gate_complete=true`、ledger生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`。従ってsource gateを残存P1へ二重計上しない。
- Prelude先行一周＋106章＋13巻のmanifest境界、schema `106/106`、handoff `14/91/1`、`validate_book` exit 0、HTML 321文書・相対href（fragment含む）44,136・欠落0・bad fragment 0、page `11+3514=3525`・24–40・107/107 hash一致は整合している。しかし各章manifestのstatusはなお独立review待ちであり、今回の2つの章ゲートで巻内確認は進んだものの、13巻の巻統合確認とPrelude＋全体のwhole sign-offは未閉鎖である。
- runnerはDocker固定imageから `718/718 success`、failed=0（verification内訳 `contract548 / analytic127 / domain26 / educational17`）、全718件`measurement_status=not_run`。full-run SHA=`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`、execution snapshotは同run SHAを指す。canonicalは739件、`measured=true=0`。この成功は固定入力の契約・解析・教育模型の再現であり、必修の外部domain実験、変更課題・故障診断、実機測定の完了ではない。
- trace A–Fはchecks=true（B=13、C=1010、D/E/F=8 events）だが、全件`measured=false`。PC-only基準ではFPGAはADR 0008に従う任意追加経路であり、board/pin/clock/tool/bitstream/timing/UART証跡が未選択・未構築でも基準経路をブロックしない。一方、trace D/E/Fのblock・TTY/keyboard/device・packet/NIC/physical下位層は未実行境界である。

### 現行残存判定

**P0=0、P1=4領域、P2=2領域、`learner-ready`保留。** source semantic gateは完了済みで、残存P1を次の4領域へ分離する。

1. **巻・全体統合ゲート** — 別session章ゲートはPrelude＋CH1–56とCH57–106を覆うが、13巻の巻内/巻間統合確認およびPrelude＋106章のwhole sign-offは未完である。学習開始条件の「章・巻・全体の独立確認」を満たす証拠にはまだならない。
2. **CH99 MiniPy scope/status** — `manuscript/volume-13/chapter-99/manifest.yml:219-260` のE5/E7を`implemented`/`executed_analytic`とする表示と、`projects/minipy/runtime.py:424-426`および`machine-spec/minipy-language.md:36-38`のfinally/generator非対応範囲が不一致。実装するか、analytic/out-of-scopeへ明示的にそろえる必要がある。
3. **CH97–103 generic runner boundary** — `tools/experiment_driver.py:381-464`のdomain model/analytic fixture fallbackは、MiniPy/CPython受入実行ではない。章の実装検証と契約模型検証の表示を分離する必要がある。
4. **必修実験・変更/故障診断の実行境界** — runnerは718/718成功でも全件`not_run`で、canonicalも未測定。解析・契約再現を、外部domain、SPICE/RTL/QEMU/xv6、実CPU/OS、変更課題・故障診断の完了へ昇格できない。

P2は (1) PC-only基準外のFPGA任意経路（未選択・未構築）、(2) trace D/E/Fを含む実機・物理下位層の未実行である。これは基準経路の必須不足と混同しない。source `gate_complete=true`、HTML/ページ/構造監査の成功、runnerの固定再現成功はいずれも上記P1を閉じないため、`learner-ready`は宣言しない。次の最小手順は、13巻の巻統合→Prelude＋全体sign-offを別sessionで完了し、CH99/CH97–103の境界表示を修正または明示したうえで、必修実験・変更/故障診断の実行契約を確定することである。本文、source YAML、manifest、runner、canonical、HTMLは変更していない。

## 2026-09-04 最新現行同期（CH9–32独立レビュー反映・P2再評価）

`reviews/independent-chapters-09-32-20260904.md` を、Prelude＋CH1–56の別session章ゲートを補足する対象限定の独立確認として現行全体レビューへ反映した。同レビューはCH9–32（24章）について本文、manifest、演習、解答、handoff、runner、canonical、HTML、ページ測定を現物突合し、章ローカルを **P0=0 / P1=0 / P2=4** と判定している。4件はCH12、CH14、CH15、CH16冒頭の「domain未実行」と読める状態表現で、現行runnerの`domain_verified`または`contract_model_verified`（固定入力由来の解析・契約モデルは実行済み）と、外部domain/SPICE/分光・実測の`measurement_status=not_run`を同じ語で読ませる曖昧さである。本文の測定済み主張や必修経路破綻ではないため、4件ともP2に留め、P1へ繰り上げない。

- これは先行の`reviews/independent-chapter-confirmation-20260904.md`（Prelude＋CH1–56をP0=0/P1=0/P2=0）と重複してP1を増やすものではない。前者はCH1–56の広域章ゲート、今回の成果物はCH9–32の状態語彙を細かく再読した追補であり、より具体的な4文のP2候補を全体集計へ加える。CH9–32レビュー自身も第9〜32章のP1=0を維持している。
- CH9–32レビューのsource sign-offは対象141 rowsで`verified=108 / accepted_boundary=33 / hold=0`、全体source gateの現行 `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、`gate_complete=true`と整合する。accepted boundaryは外部tool、PDK、FPGA、planned/not-runをその状態で受理するもので、source gate完了を実験・測定完了へ昇格させない。
- 対象24 HTMLはhref 3,797件、欠落/fragment不良0、runner 115/115 artifactあり・hash不一致0、canonical 140/140 materialized・全件`measured=false`である。全体のHTML 321文書/44,136 href/欠落0/bad fragment0、page 11+3514=3525、全体runner 718/718 success・全件`measurement_status=not_run`、canonical 739・`measured=true=0`という既存証跡と矛盾しない。これらはP2-12/14/15/16の語彙修正判断を支持するが、外部domain実行の証拠ではない。

### 現行残存判定の更新

**P0=0、P1=4領域、P2=3領域（具体的finding 6件）、`learner-ready`保留。** P1の4領域（巻・全体統合、CH99 MiniPy scope/status、CH97–103 generic runner境界、必修実験・変更/故障診断の未実行）は前追補から変更しない。P2は次の3領域へ更新する。

1. **CH12/14/15/16の状態表現（4件）** — 固定runnerの入力由来解析・契約モデル実行済みと、外部domain tool/SPICE/分光・実測未実行を本文冒頭で明確に分離する。修正候補は各章レビューのP2-12-01〜P2-16-01に具体化されている。
2. **FPGA任意経路** — ADR 0008のPC-only基準経路外で、board/pin/clock/tool/bitstream/timing/board UART証跡は未選択・未構築。基準経路のP1とは分離する。
3. **trace D/E/Fの実機・物理下位層** — block、TTY/keyboard/device、packet/NIC/physicalの測定は未実行。trace artifactのchecks/events存在やhost operationを物理測定完了と扱わない。

以上により、先行の「P2=2領域」は今回の対象限定レビューで確認された4件の本文状態表現を含めて **P2=3領域・6件**へ更新する。source gate、章別P1、runner/page/HTMLの機械判定は変更しない。`learner-ready`は、13巻の巻統合とPrelude＋全体sign-off、CH99/CH97–103境界の処理、必修実験の契約確定が残るため保留である。本文、manifest、source YAML、runner、canonical、HTMLは変更していない。

## 2026-09-04 最新現行同期（境界表現修正・CH99/runner P1解消・ページ表示差）

本文・runner境界の修正後の現行worktreeを再読した。CH12/14/15/16は、各章冒頭で「固定入力から解析／契約モデルは実行済み」と「外部domain tool・SPICE・分光・実測は未実行（`measurement.status=not_run`）」を明記している（`manuscript/volume-02/chapter-12/chapter.txt:17`、`chapter-14/chapter.txt:17`、`chapter-15/chapter.txt:24`、`chapter-16/chapter.txt:19`）。従って前追補のP2-12/14/15/16の4件は、現行本文の意味境界で解消と判定し、P2へ残さない。

CH99も、`manuscript/volume-13/chapter-99/chapter.txt:7`で`book run`を一般frame/closure/exception/generator契約の再生と限定し、`contract_model_verified`/`analytic_verified`をMiniPy/CPython本体の実装受入ではないと明記している。`try/finally`とgeneratorは同章の概念・契約模型であり、必須MiniPy範囲とは別である。manifestのE5/E7（`manuscript/volume-13/chapter-99/manifest.yml:219-260`）に残る`command_status: implemented`/`status: executed_analytic`も、`tools/build_html.py:541-543`で入口・契約の用意と実装本体の受入を区別し、HTML runner欄は`入力由来契約モデル検証済み（実測なし）`と表示する。よって旧P1-CH99-MINIPY-SCOPEは、現行の明示的な契約境界により解消とする。

CH97/98/100/101/102/103も、固定入力の模型・契約再生とMiniPy/CPython本体、性能、外部実測を分離する説明を本文へ追加している。`tools/build_html.py:374`および`541-543`のラベルも同じ区別を反映し、CH97–103のgeneric contract/analytic runnerを実装受入と誤読させる旧P1-ANALYTIC-RUNNER-BOUNDARYは解消と判定する。これらの解消はrunnerの未実行を隠すものではなく、固定runnerが検証した層を正しく限定する変更である。

- source checkerは現行 `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、errors=0、`gate_complete=true`、ledger生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`。source gateに変更はない。
- `./tools/validate_book`はexit 0、schemaは106/106・errors=0、handoffはlegacy/modern/terminal=`14/91/1`。runner/canonicalの既存境界も維持され、runner 718/718 success・全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace A–F checks=true・全件`measured=false`である。固定runnerは外部domain実験・実装受入・物理測定の完了を意味しない。
- HTMLは321文書、現行ファイルを数えたhrefは44,137。`tmp/page-counts.json`は生成 `2026-09-04T13:04:41+00:00`、SHA-256=`b307a9e549caef13d06b293242c5756b31fccb5087843a0ad9fe34fab8b4b4fd`、Prelude=11、本文=3,515、合算=3,526、min/max=24/40、under24=0、rows=107である。保存JSONの各HTML SHAも107/107一致する。
- ただし現物の`build/html/index.html:41`のstatus panelは、ページ表示を「本文3514頁、合算3525頁」と記録しており、直後のChrome再測定JSON（本文3515、合算3526）と1頁ずれている。リンク自体は44,137 href、欠落0、bad fragment0で、章導線を壊す不整合ではないが、indexの分量metadata同期漏れとしてP2に残す。本文・manifest・source YAML・runner・canonicalは変更していない。
- ADR 0008に従いPC-onlyを基準経路、FPGAを任意追加経路とする。FPGAのboard/pin/clock/tool/bitstream/timing/UART証跡およびtrace D/E/F下位層の実機・物理測定は未実行である。

### 現行残存判定の更新

**P0=0、P1=2領域、P2=3領域（うち本文状態表現4件とCH99/CH97–103境界は解消、現存P2は1件の表示差＋2つの任意/実機境界）、`learner-ready`保留。** P1は、(1) 13巻の巻内/巻間統合とPrelude＋106章全体の独立whole sign-off、(2) 必修実験・変更課題・故障診断・外部実装の実行ゲート（runnerは718件すべて`not_run`）に限定する。source semantic gateとCH99/CH97–103の旧P1は残存P1へ計上しない。

P2は (1) `build/html/index.html`の本文/合算頁表示が最新`page-counts.json`より1頁古いmetadata同期漏れ、(2) PC-only基準外のFPGA任意経路、(3) trace D/E/Fのblock・TTY/keyboard/device・packet/NIC/physical下位層の未実行である。CH12/14/15/16の4件は本文修正により解消済みであり、HTMLのhref・fragment・保存HTML hashはpassである。index metadataを最新測定値へ再生成すればP2の表示差は閉じられるが、P1の巻/全体sign-offと必修実験未実行が残るため、`learner-ready`は引き続き保留する。

## 2026-09-04 最新現行同期（再build後のHTML表示同期・旧P1/P2除外）

再build後の現行HTMLを再確認した。`build/html/index.html:41` は最新ページ測定値の「先行一周11頁、本文3515頁、合算3526頁」を表示し、source sign-offも`verified=423 / accepted_boundary=208 / hold=0`へ同期している。indexにはPrelude＋CH1–56、CH9–32、CH57–106の3つの独立レビュー導線も追加されている。現行HTMLは321文書、全href（fragmentを含む）44,140、欠落0、bad fragment0であり、先行追補に記録した一時値（3514/3525、44,137）は再build前の履歴値として除外する。

- `tmp/page-counts.json`は生成 `2026-09-04T13:04:41+00:00`、SHA-256=`b307a9e549caef13d06b293242c5756b31fccb5087843a0ad9fe34fab8b4b4fd`、Chrome `152.0.7977.76`、Prelude=11、本文=3,515、合算=3,526、min/max=24/40、under24=0、107/107 HTML hash一致である。従って、前追補で記録したindexの1頁差P2は再buildにより解消済みとする。
- source checkerはcoverage `631/631`、errors=0、`gate_complete=true`を維持する。`./tools/validate_book`はexit 0、schema106/106、handoff legacy/modern/terminal=`14/91/1`。本文のCH12/14/15/16状態表現修正、CH99の契約模型とMiniPy/CPython受入の分離、CH97–103のgeneric runner境界説明はいずれも現行HTMLへ反映され、旧P2-12/14/15/16および旧P1-CH99/ANALYTIC-RUNNERは残存findingへ計上しない。
- runner/canonical/traceの境界は変わらない。runnerは718/718 success、全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace A–F checks=trueだが全件`measured=false`。これは契約・解析・教育模型の再現であって、外部実装受入、必修実験、実機測定の完了ではない。

### 最新判定

**P0=0、P1=2領域、P2=2領域、`learner-ready`保留。** P1は (1) 13巻の巻内/巻間統合とPrelude＋106章全体の独立whole sign-off、(2) 必修実験・変更課題・故障診断・外部実装の実行ゲート（runner全718件`not_run`）のみである。P2は (1) ADR 0008でPC-only基準外の任意FPGA経路、(2) trace D/E/Fのblock・TTY/keyboard/device・packet/NIC/physical下位層の未実行である。HTML表示・導線・ページ測定の同期差は解消済みで、CH12/14/15/16およびCH99/CH97–103の旧findingも除外した。source gateの完了、HTML/ページの整合、固定runner成功だけでは巻・全体sign-offと必修実験ゲートを閉じないため、`learner-ready`は保留する。本文、manifest、source YAML、runner、canonicalは変更していない。

## 2026-09-04 最終現行同期（13:07Z再build後確認）

再build（22:07 JST / 13:07 UTC）後のHTML実体を再確認した。`build/html/index.html:41` は本文=3,515頁、合算=3,526頁を表示し、追加3レビュー導線を含む現行HTMLは321文書・href=44,140、missing=0、bad fragment=0である。これは再build前の一時値（本文3,514、合算3,525、href 44,137）を訂正する最終値であり、page-countsの107/107 hash一致とも整合する。

source sign-offは `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、`gate_complete=true`。CH12/14/15/16の状態表現修正と、CH99/CH97–103の契約模型・MiniPy/CPython実装受入境界修正により、旧P2-12/14/15/16および旧CH99/generic-runner P1は残存findingへ計上しない。runnerは718/718 successだが全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace D/E/F下位層も未実行である。

最終判定は **P0=0 / P1=2領域 / P2=2領域 / `learner-ready`保留**。P1は巻・全体sign-offと必修実験・変更課題・故障診断・外部実装未実行、P2はPC-only基準外のFPGA任意経路とtrace D/E/F下位層である。本文・manifest・source YAML・runner・canonicalは変更していない。

## 2026-09-04 現行同期（13巻統合レビュー・13:56Z page-counts後）

新規の独立巻統合成果物 `reviews/volumes-01-13-integration-review-20260904-current.md` を現行worktreeへ突合した。これは過去の章別レビューの単純結合ではなく、Prelude先行一周、106章、13巻の役割・前後接続・境界表現・学習導線・runner/canonical/traceを巻単位で再確認した記録である。各巻の局所判定は **P0=0 / P1=0 / P2=0**（13巻合計）で、巻内の意味接続および巻間handoffの欠落は確認されなかった。

- 全体構造はglobal/local manifest `106/106`、13巻、schema `106/106`（errors=0）、handoff legacy/modern/terminal=`14/91/1`、`validate_book` exit 0。巻間handoffは8→9、16→17、24→25、32→33、40→41、48→49、56→57、64→65、72→73、80→81、90→91、98→99の12境界で整合し、Prelude→V1→…→V13の学習順序も一致する。章ごとの必須本文・演習・解答・artifactの接続欠落は確認されなかった。
- source sign-offは `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、errors=0、`gate_complete=true`。source ledger生成 `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`である。これは出典ゲートの完了であり、実験実行・実装受入・物理測定の完了とは分離して扱う。
- 固定imageのrunnerは `718/718 success`、fail=0（contract548 / analytic127 / domain26 / educational17）、全件 `measurement_status=not_run`。full-run SHA=`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`。canonicalは739件をmaterialize済みだが `measured=true=0`。trace A–Fはchecks/eventsの整合を満たす（Aは3 artifact、B=13、C=1010、D/E/F=8 events）一方、全件 `measured=false`である。
- PC-onlyの最小変更・故障診断アンカーは change `3/3`、fault `4/4`、artifact script `26/26` pass（実行成果物の `measured=false` 境界付き）。これは学習導線の縦断アンカーを確認するもので、106章すべての必修実験・変更課題・故障診断を完了した証拠ではない。
- HTMLは321文書、href（fragment含む）`44,143`、missing=0、bad fragment=0。indexのsource表示は423/208/0、ページ表示は先行一周11、本文3515、合算3526である。`tmp/page-counts.json`は生成 `2026-09-04T13:56:24+00:00`、SHA-256=`3546f417f8e36012924c0ca35084d585256f4efe6bf9811c8a836436ce8562c5`、min/max=24/40、under24=0、107/107 HTML hash一致。旧追補のhref=44,140および13:04Z page-countsは履歴値であり、現行判定には計上しない。lock/canonicalの同期も既存の検証済み状態を維持する。
- 境界表現は、固定runnerが検証した契約・解析・教育模型と、外部domain tool/SPICE/RTL/QEMU/xv6・実装受入・実機測定を分離している。ADR 0008に従いFPGAはPC-only基準経路外の任意追加経路であり、board/pin/clock/tool/bitstream/timing/UART証跡を未選択・未構築でも基準経路はブロックしない。trace D/E/Fのblock、TTY/keyboard/device、packet/NIC/physical下位層は同じく未実行境界である。

### 現行統合判定

**巻ローカルは P0=0 / P1=0 / P2=0。全体共有は P0=0 / P1=2領域 / P2=2領域、`learner-ready`保留。**

共有P1は、(1) 13巻の独立統合結果をPrelude＋106章の最終whole sign-offへ接続する別ゲート、(2) 必修実験・変更課題・故障診断・外部実装の実行ゲート（runner全718件が `not_run`）である。共有P2は、(1) FPGA任意経路、(2) trace D/E/F下位層の実機・物理測定未実行である。13巻局所P0/P1/P2=0/0/0、source gate complete、HTML/link/page pass、PC-onlyアンカー3/3+4/4+26/26 passはいずれも、全体の必修実験実行または最終whole sign-offを代替しない。したがって`learner-ready`は保留し、次の最小手順は全体別session sign-offを閉じたうえで、必修実験・変更/故障診断の実行契約と証跡を確定することである。本文、manifest、source YAML、runner、canonical、HTMLは変更していない。

## 2026-09-04 whole integration sign-off（範囲限定・現行artifact確認）

現行artifactを、構造・意味統合の範囲に限定して再確認した。対象はPrelude先行一周＋106章＋13巻、global/local manifest、章schemaとhandoff、本文・演習・解答の導線、source sign-off、runner lineage、canonical、trace A–F、HTMLである。`reviews/volumes-01-13-integration-review-20260904-current.md` の巻別判定（13巻局所 **P0=0 / P1=0 / P2=0**）とも突合し、現範囲では **whole integration sign-off: pass（範囲限定）** と記録する。

- 構造・学習順序はPrelude→CH1–106、13巻境界、global/local `106/106`、schema `106/106`・errors=0、handoff legacy/modern/terminal=`14/91/1`、巻間12境界で整合し、`./tools/validate_book` は exit 0。各章の本文・演習・解答・artifact参照、巻内/巻間のhandoff欠落はこのゲートでは検出しなかった。
- source gateは `verified=423 / accepted_boundary=208 / hold=0`、coverage `631/631`、errors=0、`gate_complete=true`。ledgerは `2026-09-04T11:50:54Z`、SHA-256=`117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741`。公式出典の意味照合を完了した範囲と、accepted boundaryとして受理した未実行・任意範囲を混同していない。
- runner lineageは固定Linux imageから `718/718 success`、failed=0、全件 `measurement_status=not_run`（contract548 / analytic127 / domain26 / educational17）。full-run SHA=`16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10`。canonicalは739件、unmaterialized=0、`measured=true=0`（index SHA=`61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f`）。したがってlineage・再現可能な契約/解析結果はpassだが、測定済みとは判定しない。
- trace A–Fは各checks=true、A=3 artifact、B=13 events、C=1010 events、D/E/F=8 events、全件 `measured=false`。A〜Cの教育・契約traceとD〜Fのhost入力/loopback境界を結び、D/E/Fのblock・TTY/keyboard/device・packet/NIC/physical下位層は未実行として明示されている。この意味境界の記録はpassだが、物理層実験のpassではない。
- HTMLは321文書、href（fragment含む）44,143、missing=0、bad fragment=0。index表示もsource `423/208/0`、ページ `11+3515=3526`に同期している。`tmp/page-counts.json`は `2026-09-04T13:56:24+00:00`、SHA-256=`3546f417f8e36012924c0ca35084d585256f4efe6bf9811c8a836436ce8562c5`、min/max=24/40、under24=0、107/107 hash一致である。

### 範囲外の未完了ゲートと最終判定

この範囲限定passは、必修実験の外部domain/SPICE/RTL/QEMU/xv6/CPython等の実行・測定、章固有の変更課題・故障診断、実装受入を完了したという意味ではない。runner全718件が `not_run`、canonical全739件が `measured=false`であるため、これらは共有 **P1（必修実験・変更・故障診断・外部実装の実行ゲート）** として残す。PC-onlyの最小アンカー（変更3/3、故障4/4、artifact script26/26）はpassだが、全章固有課題の代替ではない。

FPGAはADR 0008のとおりPC-only基準経路外の任意経路であり、board/pin/clock/tool/bitstream/timing/UART証跡を未選択・未構築のままでも本ゲートを阻害しない。trace D/E/Fの物理・下位デバイス測定も未実行であり、これらは共有 **P2（FPGA任意経路、trace D/E/F下位層）** として明示する。

以上より、現行の統合判定は **whole integration sign-off: pass（Prelude＋106章＋13巻の構造・意味境界・導線・lineage範囲に限定） / P0=0 / 共有P1=1領域 / 共有P2=2領域**。このpassは`learner-ready`宣言ではなく、必修実験・章固有変更/故障診断の実行ゲートが閉じるまで **`learner-ready`保留** とする。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-04 現行同期（chapter-learning-gate inventory 導線追加後）

目次再build後の現行HTMLを読み取り確認した。`build/html/index.html` に `reviews/chapter-learning-gate-inventory-20260904.md` と対応JSONへの導線が追加され、HTMLは321文書、href（fragment含む）44,145、missing=0、bad fragment=0である。indexのsource表示423/208/0とページ表示（先行一周11、本文3515、合算3526）も維持され、既存のwhole integration sign-off範囲に新たな不整合はない。

`tmp/page-counts.json`は前回確認値（生成 `2026-09-04T13:56:24+00:00`、SHA-256=`3546f417f8e36012924c0ca35084d585256f4efe6bf9811c8a836436ce8562c5`、107/107 hash一致）から変化なし。runner/canonical/trace境界も同一で、runner 718/718 success・全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace A–F checks=true・全件`measured=false`である。

判定は維持する。**whole integration sign-off: pass（範囲限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（必修外部実験・測定、章固有の変更・故障診断、実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。inventory導線の追加は学習ゲートの可視性を高めるが、未実行の必修実験・測定を完了扱いにはしない。本文、manifest、source YAML、runner、canonicalは変更せず、本レビューartifactのみを追記した。

## 2026-09-04 現行同期（学習ゲート inventory schema・negative model 12件化後）

`artifacts/learning-contract/chapter-learning-gate-inventory-20260904.json` と対応レビューを現物確認した。106章の宣言値は experiments=718、acceptance_tests=699、negative_tests=459で、acceptance結果行は699/699（実行済み0、全件`not_run`）、negative結果行は459/459（教育モデル検証12、`not_run`447、`measured=true` 0）である。今回のschemaはacceptance/negativeごとの結果行（test_id、status、measured、evidence等）を保持し、manifest negativeの教育モデル検証は12/12 passとして記録されているが、章別の全acceptance/negative実行を意味しない。章別change/fault execution rowsは0で、別artifactのPC-only最小アンカー（change 3/3、fault 4/4、artifact script 26/26）とも区別される。inventory自身の`learner_ready=false`、`measured=false`、境界説明はwhole sign-offの範囲限定契約と整合する。

- 目次再build後のHTMLは321文書、href（fragment含む）44,145、missing=0、bad fragment=0。`build/html/index.html`でinventory Markdown/JSONへの2導線、source sign-off 423/208/0、ページ先行一周11・本文3515・合算3526を確認した。
- runner/canonical/traceは不変で、runner 718/718 success・全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace A–F checks=true（A=3 artifact、B=13、C=1010、D/E/F=8 events）・全件`measured=false`。固定契約/解析/教育モデルの検証と、外部domain・物理測定を昇格させずに表示する境界は保たれている。

従って判定は維持する。**whole integration sign-off: pass（Prelude＋106章＋13巻の構造・意味境界・inventory導線・lineage範囲に限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance 699件、negative残447件、章固有change/fault、必修外部実験・測定・実装受入の未完） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。negative model 12/12 passとinventory schema追加は未実行ゲートの可視化・境界明示であり、執筆側の全体合格宣言やlearner-readyへ昇格させない。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-04 現行同期（acceptance構造検査239件反映後）

`artifacts/learning-contract/chapter-acceptance-results-20260904.json` と `artifacts/learning-contract/chapter-learning-gate-inventory-20260904.json` を突合した。acceptance 699件の結果行は、`structural_contract_verified=239`、`failed=0`、`not_run=460`、`measured=true=0`である。239件は本文・manifest等の構造契約検査に限定され、実験、外部domain、測定、または学習者ゲートの合格へ昇格しない。inventoryの宣言・結果行にもこの境界が反映され、negativeは459件中、教育モデル12件、未実行447件、章別change/fault execution rowsは0のままである。

- `chapter-acceptance-results` はschema v1、全699行を保持し、statusは structural_contract_verified 239件／not_run 460件。artifact自身の`measured=false`・`learner_ready=false`と「structural_contract_verified is not an experiment, external-tool, measurement, or learner-interaction pass」の境界を確認した。
- 再build後のHTMLは321文書、href（fragment含む）44,147、missing=0、bad fragment=0。目次のinventory Markdown/JSON導線、source sign-off 423/208/0、ページ先行一周11・本文3515・合算3526を確認した。
- runner/canonical/traceの境界は維持され、runner 718/718 success・全件`measurement_status=not_run`、canonical739・`measured=true=0`、trace A–F checks=true・全件`measured=false`である。固定構造検査・教育モデルの pass は、外部domain/測定・章固有変更/故障診断・実装受入の証拠ではない。

判定は変更しない。**whole integration sign-off: pass（範囲限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance未実行460件、negative未実行447件、章固有change/fault、必修外部実験・測定・実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。今回の239件構造検査は、統合導線と残存未実行行を明確化したが、執筆側の合格宣言へ昇格させない。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-05 現行同期（acceptance構造検査拡張後）

現行 `chapter-acceptance-results-20260904.json` と学習ゲートinventory、再build済みHTMLを読み取り突合した。acceptance 699件は `structural_contract_verified=261`、failed=0、not_run=438、`measured=true=0`。inventoryの `acceptance_executed_rows=0` は、構造契約検査を実験実行として数えていないためであり、JSONの構造検査261件と矛盾しない。negativeは教育モデル12件、not_run 447件、inventoryの `learner_ready=false`を維持する。

HTML目次は構造検査261件・実行済み0件を表示し、321文書、href 44,147、missing=0、bad fragment=0、ページは先行一周11・本文3515・合算3526である。本文・manifestには今回のacceptance集計に伴う変更を確認しておらず、変更はレビュー同期の記録に限定した。

判定は変更しない。**whole integration sign-off: pass（範囲限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance構造検査外の実行438件、negative未実行447件、章固有change/fault、必修外部実験・測定・実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。261件の構造検査は実験・学習者ゲートの合格へ昇格させない。source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-05 現行同期（CH99 cleanup-only MiniPy実装・manifest scope後）

CH99の現行実体を、`projects/minipy/runtime.py:426-455`、`tools/test_minipy_runtime.py`、`machine-spec/minipy-language.md:30,38`、`manuscript/volume-13/chapter-99/manifest.yml:219-262`および本文の実行境界へ戻って確認した。`python3 tools/test_minipy_runtime.py` は `minipy runtime acceptance: 20 cases passed`。この20件にはcleanup専用の`try/finally`（正常終了と例外伝播後のcleanup）を含むが、`except ... finally`併用、`finally`内のreturn、generator実装を受入した結果ではない。

- MiniPyの仕様はcleanup専用`try/finally`を必須範囲とし、`except ... finally`と`finally`内returnを対象外、generatorを必須範囲外と明記する。従って今回のruntime変更は、cleanup-only subsetのhost参照実装と20ケースの境界確認として受理できる。
- CH99のmanifest実験5（finally cleanup）と実験7（generator suspension）は、現行でも `command_status: contract_model_only`、`execution_scope: contract_model_only_not_minipy`、`status: executed_analytic`、`measured: false`である。これはbook runnerが一般契約模型を再生し、MiniPy本体・CPython・外部domainを実測しないという本文境界（`chapter.txt:7,80-100`）と整合する。runtime 20件passを、実験5/7の外部実行またはchapter acceptance完了へ昇格させない。
- 現行 `validate_book` はexit 0、runnerは718/718 success・failed=0・全件`measurement_status=not_run`、canonicalは739件・materialized739・`measured=true=0`。lockは`canonical_index_sha256=781da074e530761d4c9fb8373835ed950c3485618b1aac736bf7a6a248d6614e`、`minipy_runtime_sha256=945f682f33477e0493244db7c88608eff2a81f381d0397fd0d7ae2d9a9e258d3`で、現行canonical/runtimeのsha256と一致する。
- HTMLは321文書、href（fragment含む）44,147、missing=0、bad fragment=0、index表示はsource423/208/0、ページ11/3515/3526。runner/canonical/traceの`not_run`/`measured=false`境界は維持される。

この再確認でCH99について新たなP0/P1/P2を追加しない。判定は **whole integration sign-off: pass（Prelude＋106章＋13巻の構造・意味境界・lineage範囲に限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance・negativeの未実行、章固有change/fault、必修外部実験・測定・実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。20ケースのruntime passはcleanup-only実装の範囲証跡であり、CH99本文の完了宣言、全章学習ゲート、外部/物理実験の完了を意味しない。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-05 現行同期（CH99本文のruntime境界反映・ページ再測定後）

CH99本文の現行差分を再確認した。`chapter.txt:7` はcleanup専用`try/finally`のみ参照runtimeで実装・テスト済み、generatorは契約模型と明記し、実験5の`chapter.txt:80-85`もrunnerの契約模型と参照runtimeテストを分離している。実験7の`chapter.txt:97-102`は引き続きgenerator契約模型・`measurement.status=not_run`である。従って本文はcleanup-onlyの実装範囲を明示したが、CH99全体またはgeneratorの完了宣言へ拡張していない。

- `tmp/page-counts.json`は生成 `2026-09-04T15:49:26+00:00`、SHA-256=`d1d20c3ac0c4fdc5510bbd30c2c60ab7c04dee2e890784e36f70c8fd0b6b319b`、Prelude=11、本文=3,516、合算=3,527、min/max=24/40、under24=0、107行である。HTML indexも本文3516・合算3527を表示し、href=44,147、missing=0、bad fragment=0を維持する。
- runnerは718/718 success・failed=0・全件`measurement_status=not_run`、canonicalは739件・materialized739・`measured=true=0`。lockの`canonical_index_sha256=781da074e530761d4c9fb8373835ed950c3485618b1aac736bf7a6a248d6614e`および`minipy_runtime_sha256=945f682f33477e0493244db7c88608eff2a81f381d0397fd0d7ae2d9a9e258d3`は現行ファイルのsha256と一致し、`validate_book`はexit 0である。

判定は維持する。**whole integration sign-off: pass（範囲限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance・negativeの未実行、章固有change/fault、必修外部実験・測定・実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。CH99本文のページ増加とcleanup-only境界の明示は統合記録へ反映したが、実験5/7の契約模型、runnerの`not_run`、外部domain/物理層未実行を完了扱いにはしない。source YAML、manifest、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。

## 2026-09-05 現行同期（Docker固定runner再実行・runtime/canonical lineage更新後）

Docker daemon復旧後の固定runner再実行結果を現物確認した。`artifacts/runner/full-run-20260904.json` は `718/718 success`、failed=0、全件`measurement_status=not_run`で、SHA-256=`52374aac59aa2330e10232dd96deb71ea146a2de87531df0828a46af510dc4ef`。`./tools/validate_book`はexit 0で、canonical/runner lineage mismatch=0として検査を通過している。

- 現行`projects/minipy/runtime.py` SHA-256=`02db5ee8fd5838665448e6fc5f9c9e5738cb3ae334709df9759e9c57fb9a5109`、`artifacts/canonical/index.json` SHA-256=`781da074e530761d4c9fb8373835ed950c3485618b1aac736bf7a6a248d6614e`。canonicalは739件、materialized=739、`measured=true=0`である。
- `environment/lock.yml` の`minipy_runtime_sha256`および`canonical_index_sha256`は上記現行値と一致する。従って再実行後のhash/lineage同期はpassだが、固定入力の契約・解析・教育モデル再現であり、外部domain実験や物理測定の実行passではない。

この再同期でP0/P1/P2を変更しない。**whole integration sign-off: pass（範囲限定） / 13巻局所P0/P1/P2=0/0/0 / 全体P0=0 / 共有P1=1（acceptance・negativeの未実行、章固有change/fault、必修外部実験・測定・実装受入） / 共有P2=2（FPGA任意経路、trace D/E/F物理下位層） / `learner-ready`保留**。runner再実行成功とlineage mismatch=0は、`not_run`および`measured=false`の境界を閉じず、source gateやCH99 cleanup-onlyの範囲証跡を全体学習完了へ昇格させない。本文、manifest、source YAML、runner、canonical、HTMLは変更せず、本レビューartifactのみを追記した。
