# 独立章確認 artifact（Prelude＋第1–56章）

生成時刻: 2026-09-04T12:26:07Z  
確認者: 執筆セッションとは別の独立確認セッション  
ゲート: 本artifactは章内容・学習導線の確認であり、source signoff（出典の版・locator判定）とは別ゲートである。

## 1. 範囲と判定規則

対象は `manuscript/prelude` と Vol.1–7（CH1–56）の現行worktreeである。各章について本文、演習、解答、manifest、figures、sources、handoff、実行artifact、変更課題・故障診断、解析/契約runnerと未実行境界を、既存の範囲レビューを再利用しつつ現行ファイルで再確認した。

CH57–106、Vol.8–13の章単位確認は本artifactの対象外であり、未確認として残す。source YAMLや本文・manifestはこの確認では変更していない。

P0は学習内容を直ちに誤らせる破綻、P1は必修契約・導線を阻害する不整合、P2は表示・追跡上の修正候補とした。過去レビューに記録された修正前findingは、現行ファイルで修正を確認できた場合は残存findingに数えない。

## 2. 現行証拠スナップショット

| 検査 | 現行結果 |
|---|---|
| `./tools/validate_book` | exit 0、`validated global manifest and 106 written chapter(s)` |
| `check_chapter_schemas.py --json` | exit 0、chapters=106、normalized=106、errors=[]、handoff legacy=14 / modern=91 / terminal=1 |
| `test_domain_models.py` | exit 0、failures=0、representative_cases=625、modeled=536、inline_input_fallback=true |
| 固定runner full sweep | 718/718成功、failed=0、全718件 `measurement_status=not_run` |
| CH1–56 runner | 318件、exit 0=318、`not_run`=318 |
| canonical index | 739 entries、CH1–56は344 entries、materialized欠落0、lineage SHA不一致0、`measured=true` 0 |
| HTML page-count | 106章、Prelude 11頁、本文3,514頁、Prelude込み3,525頁、24–40頁、under_24=0、107 rows |
| HTML SHA照合 | `tmp/page-counts.json`の107 rowsと現行HTMLの不一致0 |
| source signoff（別ゲート） | verified=423、accepted_boundary=208、hold=0、coverage_complete=true、errors=[]。本章判定には流用していない。 |

固定runnerの現行記録は `artifacts/runner/full-run-20260904.json` であり、下表の現行SHAを採用する。

| 証拠 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260904.json` | `16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10` |
| `artifacts/canonical/index.json` | `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f` |
| `tmp/page-counts.json` | `fd002a1ddcabda4968e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb` |
| `environment/lock.yml` | `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c` |

注: 上の行は現行実体への `sha256sum` 再計算を二重確認して固定した。runnerの `kind=locked_runner_full_sweep` と `measurement_policy` は、固定Linux Dockerでの解析・契約・教育モデル再現であって、物理測定ではないことを明記している。lock記載のimageは `electron-to-python-runner:bookworm`、`linux/amd64`、digest `sha256:daccf702550ab50463e74c97dad0bdf26f4dd1d8a97a30849901065312ce1d8e` である。

## 3. 機械的な横断確認

読み取り専用のPyYAML/JSON/正規表現集計で、CH1–56について次を確認した。

- 56章すべてにmanifestの `required_outputs`（本文、manifest、handoff、演習、解答、図、出典）が存在し、空ファイルは0。
- manifestのfigure/source ID欠落0、required canonical artifactの実体欠落0。
- manifestの演習ID、`exercises.txt`の `## E*`、`solutions.txt`の `## E*` の不一致・重複0。
- handoffの次章edgeはCH1→2からCH56→57まで56/56が連続。旧direct形14件とmodern nested形42件はschemaが受理する形であり、次章IDの誤りは0。
- 変更・故障診断・反例・負のテストを示す本文/演習/解答の語彙は56/56章にあり、未実行境界（`not_run`、未実行、実測ではない等）も56/56章にある。この語彙集計は存在確認であり、意味判定は下記の再読で行った。
- CH1–56のrunner artifactは全件実体あり、full-run記録のSHAと実体SHAが一致。canonicalのrunner lineage 718件も現行runner SHAと一致し、canonical実体の欠落・実測trueは0。

### runner内訳

| 範囲 | 実験数 | exit 0 | verificationの内訳 | measurement |
|---|---:|---:|---|---:|
| CH1–8 | 11 | 11 | contract 6 / domain 5 | not_run 11 |
| CH9–16 | 8 | 8 | contract 4 / domain 4 | not_run 8 |
| CH17–24 | 43 | 43 | contract 43 | not_run 43 |
| CH25–32 | 64 | 64 | contract 17 / analytic 47 | not_run 64 |
| CH33–40 | 64 | 64 | contract 58 / analytic 6 | not_run 64 |
| CH41–48 | 64 | 64 | contract 47 / analytic 11 / educational 4 / domain 2 | not_run 64 |
| CH49–56 | 64 | 64 | contract 51 / analytic 7 / educational 6 | not_run 64 |

## 4. 意味の再確認（既存レビューの現行追補を再利用）

再利用した範囲レビューは次の7件である。いずれも修正後の追補を優先し、初回の修正前findingを現行findingへ繰り越していない。

- `reviews/chapters-01-08-independent-review-20260903.md`
- `reviews/chapters-09-16-independent-review-20260903.md`
- `reviews/chapters-17-24-independent-review-20260903.md`
- `reviews/chapters-25-32-independent-review-20260903.md`
- `reviews/chapters-33-40-independent-review.md`
- `reviews/chapters-41-48-independent-review-20260903.md`
- `reviews/chapters-49-56-independent-review-20260903.md`

| 範囲 | 現行本文・演習・解答・導線の確認 | 局所判定 |
|---|---|---|
| Prelude | `prelude.txt` とmanifestの学習契約を確認。操作・演習を要求せず、`print(1 + 2)`を自然法則・模型・契約・実装へ過剰に同一視しない。図とsourceは未測定・将来artifactを区別する。 | P0=0 / P1=0 / P2=0 |
| CH1–8 | trace AのAST/bytecode/OS/CPU境界、CH5の静電誘導と分極、CH8の導電率予測を再読。CH1 `chapter.txt:218–244`のADD結果→UART依存、演習/解答の故障診断、各章の解析予測と測定not_run分離が現行artifactと一致。 | P0=0 / P1=0 / P2=0 |
| CH9–16 | 分布線路と集中近似、KCL/KVL・過渡、二準位統計、Bloch/tight-bindingを再読。`t_prop`等の数値は入力条件からの予測、演習/解答は境界条件・負のテスト・再挑戦を持ち、実測波形へ昇格していない。 | P0=0 / P1=0 / P2=0 |
| CH17–24 | キャリア符号、状態密度、ドーピング、drift/diffusion・再結合、p-n/MOS/CMOSの式とhandoffを再読。CH19 `chapter.txt:7–16`は電子/正孔の符号と予測・not_run境界を明示し、既存のCH17–24最終追補で数値系譜・状態表示の修正を確認済み。 | P0=0 / P1=0 / P2=0 |
| CH25–32 | process/noise、Boolean/NAND、真理値表、HDL/Verilator/Yosys境界を再読。CH32 `chapter.txt:5–17`は`assign`/`always_comb`/latchを分け、decoder代表sourceも本文の明示的assign契約へ同期済み。外部RTL実行・FPGA・実測とは呼んでいない。 | P0=0 / P1=0 / P2=0 |
| CH33–40 | binary/符号/浮動小数、datapath、ALU、control、register/FSMを再読。CH39 `chapter.txt:5–21`の幅・reset・illegal状態・変更診断はmanifest/演習/解答と整合し、analytic/contract runnerをRTL/formalの実行結果へ拡張していない。 | P0=0 / P1=0 / P2=0 |
| CH41–48 | memory array、cache前段、16-bit ISA、assembly、datapath、UART busを再読。CH44は手計算期待値・固定runner契約再生・formal/実CPU/実測を分離。演習の変更・負のテストとhandoffは現行manifestに対応する。 | P0=0 / P1=0 / P2=0 |
| CH49–56 | trap/CSR、boot ROM、pipeline/cache、VA/PTE/TLBを再読。CH50の`wstrb=0b1111`契約とCH56のfull VPN `0x401/0x402`表記は修正後本文・解答・artifactが一致する。`chapter-56/chapter.txt:5–21`はrv32eduのMMU非実装、Sv32は簡略模型、実MMU/QEMU/FPGA/latency未実行を明記する。 | P0=0 / P1=0 / P2=0 |

CH33–56の意味確認では、本文の代表式・状態遷移・幅/符号/権限契約をmanifestの代表入力およびsolutionsの再計算と照合した。各章の変更課題・故障診断は「成功した実機実験」とは扱わず、負の入力・不変条件・診断記録を学習用契約として扱う。

CH33–40は二進表現→加算/ALU→帰還・順序回路→FSM/clock/reset、CH41–48はSRAM/DRAM/array→stored-program/ISA→assembly/datapath/control、CH49–56はtrap/boot→pipeline/cache→VA/PTE/TLBの8章ずつである。各8章について本文の中心契約、manifestの実験・required artifact、演習/解答の変更・負のテスト、handoffの次章入力を照合し、現行範囲レビューの局所P0/P1/P2=0を再確認した。

## 5. 未解決findingと境界記録（このartifactの完了を妨げる共有ゲート）

### F-CH-001 [P1] 外部domain・実測の未完了

固定Linux Docker runnerの718/718成功は、固定入力に対する解析、契約モデル、決定的domain、教育モデルの実行証拠である。全718件の `measurement_status` は `not_run`、canonical 739 entriesの `measured=true` は0である。したがって、実CPython/OSの全実行経路、SPICE波形、RTL/formal/Verilator/Yosysの外部経路、FPGA、実回路、実機MMU/性能/物理測定を完了扱いしない。次の最小条件は、必修とする外部経路ごとに対象版・入力・出力artifact・測定 provenanceを固定して実行するか、manifestで解析・教育モデルのみを明示的に採用し学習契約を再定義することである。

### F-CH-002 [P1] 本artifactの範囲外

CH57–106（Vol.8–13）の本文・演習・解答・manifest/handoff・章artifactの独立確認は、このartifactでは未実施である。したがってPrelude＋CH1–56の局所findingが0でも、106章全体、13巻統合、全体学習順・trace A–F・変更課題/故障診断の統合確認を完了とは判定しない。後続セッションでCH57–106を同じ機械＋意味手順で確認し、巻間handoffと全体ゲートを別artifactへ記録する必要がある。

### source signoffとの独立性（findingではない境界記録）

現行source checkerは `verified=423 / accepted_boundary=208 / hold=0` で完了しているが、これは本artifactの章内容判定の根拠ではない。逆に、この章確認のP0/P1/P2=0は、出典の意味・版・locatorを再確認済みへ昇格させるものでもない。両ゲートの証跡と判定を混ぜない。

## 6. 最終判定

対象範囲（Prelude＋CH1–56）の現行局所判定は **P0=0 / P1=0 / P2=0**。機械検査、本文・演習・解答・manifest/handoffの意味再読、runner/canonical/HTMLの系譜照合に、現行の章ローカル未解決findingはない。

ただし F-CH-001（外部domain・実測）とF-CH-002（CH57–106未確認）が残るため、教材全体の `learner-ready` は **不可**。本artifactは執筆セッション外の章確認であり、source signoffおよび固定runner再現ゲートの完了を、章・巻・全体の学習完了へ読み替えない。

## 7. 再現コマンド

```text
./tools/validate_book
uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_chapter_schemas.py --json
uv run --with 'PyYAML==6.0.3' --no-project python3 tools/test_domain_models.py
uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json
sha256sum artifacts/runner/full-run-20260904.json artifacts/canonical/index.json tmp/page-counts.json environment/lock.yml
```

上記4コマンドはすべてexit 0（source signoffの結果は別ゲート）である。読み取り専用の機械集計では、CH1–56のrequired output、figure/source参照、canonical実体、演習/解答ID、handoff次章edge、runner artifact SHA、canonical lineage、HTML SHAを再照合した。
