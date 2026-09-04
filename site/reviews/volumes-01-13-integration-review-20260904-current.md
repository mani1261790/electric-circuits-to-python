# 第I〜XIII巻 独立意味統合レビュー（現行）

確認日時: 2026-09-04 22:30 JST  
確認者: 執筆セッションとは別の巻統合確認セッション  
対象: Prelude（先行一周）、106章、13巻、global/local manifest、handoff、本文、演習・解答、実験・canonical artifact、trace A〜F、runner、HTML、完成境界

## 結論

Preludeの地図を入口に、第1章から第106章までを番号順に読む一本の学習経路は維持されている。13巻の章範囲、巻内の役割、隣接巻へ渡す入力、用語の再利用、handoff、実験・artifact・演習・解答の参照関係を現行ファイルへ戻って突合した。各巻の「巻内／巻間の意味接続」について、現行の局所P0/P1/P2は確認しなかった。

これは、固定入力からのモデル再生やファイルの存在を、外部実験・実機測定・章合格へ昇格させた判定ではない。source sign-offは別ゲートとして `verified=423 / accepted_boundary=208 / hold=0`、`coverage=631/631`、`gate_complete=true` まで閉じているが、全718実験の測定欄、canonical artifactの測定欄、章manifestの独立確認待ち状態は別に残る。

今回の巻統合判定は **13巻すべて P0=0 / P1=0 / P2=0（巻の役割・接続・境界・導線という対象範囲）**。教材全体の完成判定は **P0=0 / P1=2領域 / P2=2領域、`learner-ready`保留** とする。共有P1は、(1) Prelude＋106章＋13巻を含む別sessionのwhole sign-off、(2) 全章の必修実験・章固有の変更課題／故障診断・外部実装の完了である。共有P2は、(1) PC-only基準外のFPGA任意経路、(2) trace D/E/Fのdevice・physical下位層である。

本文、manifest、sources.yml、runner、canonical、HTMLは変更していない。このファイルだけを新規作成した。

## 判定の範囲と読み方

巻のP判定は、各章の式をもう一度章別レビューへ分解して合算するものではなく、次の接続を巻単位で確認した結果である。

- Prelude → CH1 → CH106 の学習順と、巻境界（CH8/16/24/32/40/48/56/64/72/80/90/98/106）。`next_parallel_bridge` は先の層を予告する参照であり、学習順を飛ばす任意経路ではない。
- 巻の最初の章が要求する前巻の概念と、最後の章が次巻へ渡す概念・artifact・状態欄。特に `source_kind`、`status`、`measured`、`not_run` の意味を、モデル結果・実装・測定で混同しないこと。
- `handoff.yml` の次章ID・題名・役割、`manifest.yml` の `bridge_in`／`bridge_out`、実験ID・required artifact、演習ID・解答見出し。
- 物理量 → 回路 → 量子・半導体 → CMOS・論理 → CPU・OS → 言語処理系という用語の型変換。電圧・電荷・命令・仮想アドレス・Python objectを同一の値として渡していないこと。
- 固定runner、canonical、trace、HTMLは「何が存在するか」「何が固定モデルとして確認されたか」「何が未測定か」を分離して読むこと。

## 現行の機械的な証跡

読み取り専用に次を再確認した。

| 対象 | 現行値 | 意味の限定 |
|---|---:|---|
| global/local manifest | 106/106章、ID・title・volume・chapter_in_volumeの不一致0 | local manifestはglobal indexの代替ではなく、章固有の契約を持つ |
| 巻境界 | 13巻、範囲は 1–8 / 9–16 / 17–24 / 25–32 / 33–40 / 41–48 / 49–56 / 57–64 / 65–72 / 73–80 / 81–90 / 91–98 / 99–106 | V11だけ10章、他は8章 |
| spine | 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 90, 98, 106 | 各巻の出口確認点 |
| 必須章ファイル | 7種 × 106章、欠落0 | 本文、manifest、handoff、演習、解答、図、出典 |
| handoff schema | legacy/modern/terminal = 14/91/1、errors=0 | 途中105 edgeは連続、CH106は番号なし終端 |
| chapter schema / validate | normalized=106、review gates list/mapping=19/87、`validate_book` exit 0 | schema通過は意味sign-offや測定完了ではない |
| declared experiments | 718 | manifestの実験契約数、測定済み件数ではない |
| declared canonical artifacts | 739 | manifest上の成果物レコード数 |
| source sign-off | verified 423 / accepted_boundary 208 / hold 0、coverage 631/631 | source semantic gateは完了。機械ledgerの`semantic_review_pending=631`とは別の表示欄 |
| source ledger | 生成 `2026-09-04T11:50:54Z`、SHA `117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741` | rows 631、metadata/locator 533/533、declared locator 321/321、claim locator 190/190 |
| fixed runner | 718/718 success、fail 0、全件 `measurement_status=not_run` | contract/analytic/domain/educational modelの固定再生であり、外部実験・実測ではない |
| runner verification内訳 | contract 548 / analytic 127 / domain 26 / educational 17 | `domain_verified`も外部SPICE、RTL、QEMU、FPGA、実機測定を意味しない |
| canonical index | 739/739 materialized、`measured=true` 0、SHA `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f` | `status=executed_analytic` は解析系artifactの状態 |
| runner artifact | SHA `16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10` | Docker固定imageからの再現結果 |
| environment lock | SHA `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c`、base `debian:bookworm` linux/amd64、runner image digest固定 | canonical index、runner adapter、MiniPy runtime等のlock参照を検査 |
| page measurement | Prelude 11 / 本文 3515 / 合算 3526、min/max 24/40、under24=0、107/107 hash一致 | `tmp/page-counts.json` 生成 `2026-09-04T13:04:41+00:00`、SHA `b307a9e549caef13d06b293242c5756b31fccb5087843a0ad9fe34fab8b4b4fd` |

`check_chapter_schemas.py` は `chapter schema audit: 106 chapters, normalized=106, errors=0`、`validate_book.py` は `validated global manifest and 106 written chapter(s)` を返した。各章の演習見出しとsolutions見出しはmanifestのID列と一致し、全13巻で不一致0だった。各章本文には変更・故障診断語彙と、未実行・実測境界の語彙があるが、語彙の存在だけで章合格とは扱わない。

用語・数式・traceの正本も参照した。`book-spec/concept-registry.yml` は756 entries、`symbol-registry.yml` は474 entries、`equation-registry.yml` は280 entries、`trace-registry.yml` はA〜Fの6 entriesであり、`validate_book`の重複・導入順検査は通過した。これは用語IDと導入位置の整合を示すが、各概念を全章で同じ意味に使ったことの自動証明ではない。巻別の本文再読では、物理量、回路量、CPU状態、OS状態、Python objectを同じ所有者・単位の値として無断で渡すhandoffは見つからなかった。

既存の別session章artifact（`reviews/independent-chapter-confirmation-20260904.md`、`reviews/independent-chapters-09-32-20260904.md`、`reviews/chapters-57-106-cross-independent-review-20260904.md`）は対象範囲と修正履歴の照合にのみ使い、判定表を単純連結していない。巻の入口・出口、manifest/handoffの現行値、本文の境界表現へ戻って再確認した。特にCH12/14/15/16は固定runnerの解析・契約モデルと外部domain／実測`not_run`を分け、CH99およびCH97–103は一般契約模型とMiniPy／CPython実装受入を分けているため、旧状態表現・generic runnerの誤読を現行P1/P2へ繰り越していない。

HTMLは `build/html` の321文書、現行indexの本文3515・合算3526・source sign-off 423/208/0を確認した。プロジェクトで継続しているリンク監査の報告値は相対href 44,140、欠落0、bad fragment 0である。本セッションのDOM直接集計では、indexに現行のPC-only変更・故障診断のMarkdown/JSON導線が追加されているため、生のhref出現数は44,142となった（追加2件を含め欠落0、bad fragment 0）。これはリンク破損ではなく集計対象の差であり、P2には分類しない。`build_html`を本タスクから再実行してHTMLを変更することはしていない。

## Preludeと全体導線

Prelude「電気からPythonまでの地図」は第1章より前に置かれ、20–30分の全層見取り図である。`interaction_required=false`、`exercise_required=false`で、`print(1 + 2)`を電荷・場・回路・CPU・OS・処理系へ一度通すが、ここで106章の学習を済ませたとは扱わない。本文・manifestの配置は番号を変えず、学習順は **Prelude → CH1 → CH2 → … → CH106** である。

CH1のtrace Aが、AST／bytecode／system call／RV32I／UARTを「同じもの」とせず観測層の違いとして開く。V1以降は、下位の物理・回路の量を、条件付きの模型と上位契約へ順に縮約する。V13では逆向きに、Python object・MiniPy・rv32edu・minios・UARTのtraceを通して全層を照合し、CH106で現代PCへの写像と未実装境界を整理する。これは短縮課程ではなく、各巻を順に通過するための先行一周である。

## 13巻の独立統合結果

各行の「局所判定」は、当該巻の役割、入口・出口、境界表現、学習導線、artifact／演習／解答の接続についての判定である。実験実行・測定・全体完成の残件は、巻ごとに重複計上せず、後段の共有ゲートへまとめた。

| 巻 | 章範囲・規模 | 巻の役割と学習導線 | 前巻から受けるもの → 次巻へ渡すもの | 実験 / canonical | manifest statusの現状 | 局所P0/P1/P2 |
|---:|---|---|---|---:|---|---|
| I | CH1–8、8章 | Preludeの縦断図をCH1のtrace Aと抽象化台帳へ分解し、電荷・電場・電位・電流から導電率・抵抗へ進む | Prelude → 物理量・電磁場 → V2の分布／集中回路、量子・物質への入口 | 11 / 36 | artifact+independent待ち5、runner+independent待ち3 | 0 / 0 / 0 |
| II | CH9–16、8章 | 電磁場を回路模型へ縮約する条件を確認し、時間・雑音から古典論の破綻、波動関数、Pauli/Fermi、Bloch・bandへ進む | V1の電位・電流・導電率・抽象化境界 → V3のband、gap、DOS、occupancy、キャリア | 8 / 41 | runner+independent待ち8 | 0 / 0 / 0 |
| III | CH17–24、8章 | bandと占有を電子・正孔キャリア、drift/diffusion、接合、MOS、CMOS inverterの電圧伝達へ接続する | V2のband・Fermi・温度・量子状態 → V4のVTC、noise margin、threshold、power | 43 / 41 | runner+independent待ち8 | 0 / 0 / 0 |
| IV | CH25–32、8章 | 連続電圧をlogic levelへ再構成し、NAND、組合せ論理、HDL、simulation、synthesis、formal verificationへ進む | V3のVTC／VDD／threshold／寄生・雑音 → V5のHDL vector、幅、検証契約、有限幅算術 | 64 / 58 | runner+independent待ち8 | 0 / 0 / 0 |
| V | CH33–40、8章 | 二進表現・符号・有限幅から加算器、ALU、帰還、latch/flip-flop、FSM、clock/resetへ進む | V4の論理・幅・検証 → V6のclock、reset、register file、memory array | 64 / 56 | runner待ち4、SPICE+independent待ち2、runner+SPICE+independent待ち2 | 0 / 0 / 0 |
| VI | CH41–48、8章 | SRAM/DRAM/ROM/flashとmemory arrayを経て、stored-program、RV32I、assembly、datapath、control、memory map、UART MMIOへ進む | V5のclock/reset/loadとHDL → V7のdecode/control、bus、memory map、UART、trap契約 | 64 / 56 | runner+SPICE+independent待ち1、runner+independent待ち7 | 0 / 0 / 0 |
| VII | CH49–56、8章 | trap・interrupt・privilegeからrv32edu、pipeline、cache、virtual address、page table、TLBへ進む | V6のcontrol/decode/MMIO → V8のtranslation後physical access、coherence、boot | 64 / 56 | runner+independent待ち8 | 0 / 0 / 0 |
| VIII | CH57–64、8章 | multicore/cache coherence、atomic、OoO、trust、bus/DMA、power/clock/temperatureを経てreset vector・firmware・boot chainへ進む | V7のTLB後のmemory access → V9のstorage block/controller、input/output、network device trace | 64 / 62 | runner+independent待ち8 | 0 / 0 / 0 |
| IX | CH65–72、8章 | 永続storageとcontroller、keyboard/TTY、UART/framebuffer/GPU、networkから、assembler、object/ELF、linker、loader、dynamic linkingへ進む | V8のboot/address空間・latency/trace → V10のprocess image、ABI、code/data/stack/register | 64 / 64 | runner+independent待ち8 | 0 / 0 / 0 |
| X | CH73–80、8章 | Cの抽象機械とABIからlexer/parser/IR/codegen、debugger/bootstrap、kernel mode、system call、process/schedulerへ進む | V9のloader imageとsource_kind/measured境界 → V11のper-process memory view、page table、OS policy | 64 / 56 | runner+independent待ち8 | 0 / 0 / 0 |
| XI | CH81–90、10章 | address space、page fault、COW、kernel allocator、thread/lock、filesystem、TTY、socketを、xv6とminiosの統合へまとめる | V10のprocess/context switch/kernel stackとV7のtranslation → V12のprocess、FD、system call観測点 | 80 / 78 | runner+independent待ち10 | 0 / 0 / 0 |
| XII | CH91–98、8章 | syntax/semantics、tokenizer、PEG、AST、symbol table、bytecode、VM、object identity、GC、integer/string/list/dictへ進む | V11のprocess/FD/syscallとV9のprocess image → V13のruntime/object、state、operation、error、source_kind | 64 / 64 | runner+independent待ち8 | 0 / 0 / 0 |
| XIII | CH99–106、8章 | function/closure/exception/generator、module/I/O、GIL、adaptive interpreterを経て、MiniPy仕様・compiler・RISC-V port・trace atlas・現代PC mappingを統合する | V12のobject/runtime boundary → 付録・継続学習へhash、contract、未実装境界、再現commandを渡す | 64 / 71 | runner+independent待ち8 | 0 / 0 / 0 |

### 巻境界の意味確認

12個の巻間edgeは `(8,9)`, `(16,17)`, `(24,25)`, `(32,33)`, `(40,41)`, `(48,49)`, `(56,57)`, `(64,65)`, `(72,73)`, `(80,81)`, `(90,91)`, `(98,99)` である。各edgeのhandoffは、legacy形式（`next_chapter_id`/`next_chapter_title`）またはmodern形式（`next_chapter: {id,title,...}`）を正規化したとき、次章IDと題名がglobal/local manifestと一致する。第106章だけは付録・継続学習を指す番号なし終端で、途中章の欠落ではない。

巻をまたぐ用語の所有者は次のように変わる。

- V1→V2: 電流密度・導電率・抵抗は、分布場を端子模型へ縮約する条件を伴って渡す。
- V2→V3: 一粒子準位・Fermi占有・周期系のbandを、半導体のキャリア数・輸送・接合へ渡す。
- V3→V4: MOS/CMOSの連続電圧、VTC、しきい値、寄生、powerをlogic level・noise margin・HDLへ渡す。
- V4→V5: Boolean/HDLの論理と幅を、有限幅表現・算術・時系列状態・resetへ渡す。
- V5→V6: clock/reset/loadとregisterを、記憶素子・ISA・datapath・memory mapへ渡す。
- V6→V7: decode/control、UART MMIO、memory mapを、trap・interrupt・privilege・TLBへ渡す。
- V7→V8: virtual-to-physical accessとcache policyを、coherence・bus・firmware・bootへ渡す。
- V8→V9: boot後のdevice/storage/input/output観測点を、toolchainとloaderのprocess imageへ渡す。
- V9→V10: ELF/loaderのcode/data/stack/registerとABI観測点を、Cの抽象機械・kernel entryへ渡す。
- V10→V11: process・context switch・scheduler・kernel stackを、address space・paging・concurrency・OS serviceへ渡す。
- V11→V12: process・FD・syscallと権限境界を、syntaxからruntime/objectへ渡す。
- V12→V13: object identity・GC・bytecode/VMの状態を、function/closure・MiniPy・全層traceへ渡す。

同じ文字列を別層の物理量として再利用する箇所では、本文のmodel limitとhandoffの`must_not_assume`が所有者・単位・成立条件を留める。特に「解析予測」「固定runner出力」「実測」は各巻の演習・解答・artifactで別欄のままである。

巻の境界表現の代表確認として、V1のCH8は導電率・抵抗・電力を条件付きの物質模型としてV2へ渡し、V2のCH12/14/15/16は解析・契約モデルと外部domain／分光／固体測定を分離する。V3のCH24は連続電圧からlogicへの条件を残し、V4〜V8はRTL、CPU、MMU、deviceを同じ`verified`語で実測と混同しない。V9〜V11はloader、OS、socketのhost境界とtarget／physical下位層を区別し、V12〜V13はCPython/MiniPyのscope、contract model、実装受入を分離する。これらは巻間で受け渡す用語の所有者を保つための境界であり、未実行を隠すための表現ではない。

## 実験、変更、故障診断、artifactの接続

全章で必要ファイルが存在し、manifestのexperiment IDとrunner result、canonical artifact ID、exercise IDとsolutions見出しを確認できる。canonicalの巻別数はmanifestの宣言値であり、indexは739件の一つのartifact集合としてmaterializeされている。

固定runnerの成功は、各巻の実験カードにある入力、期待値、契約、解析adapter、教育モデルを再現できることを示す。検証statusの意味は以下の通りである。

- `contract_model_verified`: 入力・期待値・artifact参照の契約を固定値で再生した。
- `analytic_verified`: 解析式またはanalytic fixtureを固定値で再生した。
- `domain_verified`: 実行可能な教育／章固有モデルの値を再生した場合があるが、外部SPICE、RTL、QEMU、実装機器の測定を意味しない。
- `educational_model_verified`: MiniPy、minios、rv32eduなど、チェックイン済み教育モデルの実行を区別する。

PC-only変更・故障診断の最小縦断は、別artifact `artifacts/learning-contract/pc-only-change-fault-20260904.json`で変更3/3、故障4/4、章PC側artifact 26/26がpassしている。しかしこれは各巻の全章固有の変更課題・故障診断を閉じるものではない。全718 runner resultの測定欄はなお718/718 `not_run`であり、canonicalも739件すべて`measured=false`である。この差を「runnerが壊れている」とは分類せず、「必修学習契約の全件実行・変更・診断証跡が未完」と分類する。

## trace A〜FとFPGA境界

trace registryはA〜Fを同じ`trace_id`、event、parent、source referenceで結ぶ契約を持つ。現行artifactのチェックはすべてtrueである。

| trace | artifactの現行境界 | event数 | 判定 |
|---|---|---:|---|
| A | `print(1 + 2)`をAST、VM、RV32I、UARTへつなぐ教育・縮約trace。negative stack boundaryも保存 | 0（3 artifact） | checks pass、measured=false |
| B | MiniPy list/object graphの教育モデル | 13 | checks 10/10、measured=false |
| C | `sum(range(1000))`のloop／branch入力由来モデル | 1,010 | checks 10/10、measured=false |
| D | hostのregular file read。block device・physical storageではない | 8 | checks 13/13、host operationのみ |
| E | 供給stdinのhost operation。TTY・keyboard・USB deviceではない | 8 | checks 13/13、device measurementなし |
| F | host loopback TCP。packet capture・NIC・physical linkではない | 8 | checks 13/13、network lower layerなし |

したがってtrace B〜Fはartifact欠落やrunner failureではない。D/E/Fの下位device・physical層が未実行であることも、本文・trace artifactの境界欄に明示されている。これはPC-only基準経路の意味説明を壊すP1ではなく、完成時に物理経路まで主張する場合の共有P2境界である。

FPGAは `book-spec/book.toml` とglobal manifestで `required=false`、`fpga=optional`、selected release path=`pc_only` と固定されている。基準board、pin、clock、tool version、bitstream、timing、board UARTの証跡がない現状は、任意追加経路を未選択・未構築とする正しい状態である。FPGAを必修へ昇格させない限り、PC-onlyの学習経路をブロックしない。

## 現行P判定と残課題

### 巻ごとの判定

13巻とも、巻の意味統合対象（役割、前後接続、境界表現、学習順、handoff、演習／解答／artifact接続）で **P0=0 / P1=0 / P2=0**。これはsource semantic gate、固定runner、外部domain、実機測定、whole sign-offを含めて完了したという意味ではない。

### 教材全体の共有判定

**P0=0。** 章番号・巻境界・handoff・必要ファイル・artifactの系譜・HTML導線に、教材全体を直ちに破壊する不整合はない。

**P1=2領域。**

1. **Prelude＋106章＋13巻のwhole sign-off** — 本ファイルは13巻の独立意味統合記録だが、completion contractが要求する章確認・巻確認・whole確認を一つの完了宣言へまとめる別sessionの最終ゲートは残る。各章manifestのstatusも106/106が `drafted_pending_*_and_independent_review` のままで、schema通過や既存章レビューartifactを自動的に合格へ書き換えない。
2. **必修実験と章固有の変更・故障診断・外部実装** — PC-onlyの最小縦断変更／故障診断はpassしているが、718件の実験は固定入力の契約・解析・教育モデル再生で、測定欄718件すべて`not_run`。SPICE、Verilator/Yosys、QEMU/xv6、CPythonの対象観測、実CPU性能、実装受入、章ごとの変更／故障診断を完了した証拠ではない。

**P2=2領域。**

1. **FPGA任意経路** — ADR／scopeのPC-only基準外。boardとtool lock、synthesis/place-and-route/timing、bitstream、board UARTの証跡は未選択・未構築であるため、任意追加経路としてのみ残る。
2. **trace D/E/Fの下位層** — regular file、stdin、loopback TCPのhost operationはartifactへ保存済みだが、block storage、TTY/keyboard/USB、packet/NIC/physical linkは未実行。A〜Fのchecks passやevent数は、この下位層の測定済みを意味しない。

`source sign-off gate_complete=true`、HTMLの欠落0/bad fragment0、ページhash107/107、runner 718/718 success、canonical materialized 739件は、上のP1を閉じる証拠ではない。従って `learner-ready` は **保留**。完了には、全体統合の別session sign-offと、必修実験・変更・故障診断の対象・版・入力・出力・provenanceを明確にした実行記録が必要である。FPGAとD/E/F物理下位層は、基準経路と別の任意／物理ゲートとして扱う。

## 次の最小手順

1. 本ファイルを13巻の巻統合artifactとしてwhole-review sessionへ渡し、Prelude、全章、全巻、trace、source sign-off、runner/canonical、HTMLを重複なく一つのcompletion判定へ統合する。
2. PC-onlyで必修とする章固有の実験・小さな変更・故障診断を、固定版・入力・artifact・結果・失敗境界つきで選別実行する。既にpassした最小縦断を、718件全件の実測済みと表現しない。
3. 任意FPGAを実施する場合だけ、基準boardとtool versionを固定し、synthesis/place-and-route/timing/bitstream/board UARTを独立artifactへ保存する。実施しない場合はPC-only releaseの任意未選択表示を維持する。
4. D/E/Fを物理層まで拡張する場合だけ、block/TTY/NIC/packet/physicalの観測対象と測定器を固定する。現行host traceをその結果へ昇格させない。
