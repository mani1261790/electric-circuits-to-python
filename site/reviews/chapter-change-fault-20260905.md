# 第9〜60章 change/fault 教育モデル実行記録

確認日: 2026-09-05（Asia/Tokyo）

`tools/run_chapter_change_fault.py` を標準ライブラリだけで実行し、第9〜60章について、章の演習参照に対応する「基準入力 → 条件変更 → 故障入力」を1組ずつ記録した。結果の機械台帳は [`chapter-change-fault-20260905.json`](../artifacts/learning-contract/chapter-change-fault-20260905.json) である。前半の第9〜12章host補助記録は同じ台帳へ統合し、第13〜16章の量子・バンド入口、第17〜20章の半導体基礎、第21〜24章のMOS・CMOS入口、第25〜28章の論理電圧・ゲート・遅延・レイアウト入口、第29〜32章のビット・NAND・論理合成・HDL入口、第33〜36章の有限幅算術・ALU・帰還入口、第37〜40章のlatch・setup/hold・FSM・clock/reset入口、第41〜44章のSRAM・DRAM/ECC・memory array・stored-program入口、第45〜48章のRV32I・assembly・datapath・memory map入口、第49〜52章のtrap・boot・性能・pipeline入口、第53〜56章のhazard・branch prediction・cache・Sv32入口に続いて、第57〜60章のcoherence・atomic・out-of-order・speculation入口を追加した。

| 章 | 教育モデル | 基準 | 変更 | 故障 | measured |
|---:|---|---:|---:|---:|---:|
| 9 | 分布線路・集中RC | pass | pass | pass | false |
| 10 | 2節点抵抗網の節点解析 | pass | pass | pass | false |
| 11 | RC解析ステップ応答 | pass | pass | pass | false |
| 12 | RC周波数応答・線路反射 | pass | pass | pass | false |
| 13 | 無限量子井戸の準位 | pass | pass | pass | false |
| 14 | 矩形障壁トンネル尺度 | pass | pass | pass | false |
| 15 | 二準位Fermi–Dirac占有 | pass | pass | pass | false |
| 16 | tight-binding帯幅・ギャップ | pass | pass | pass | false |
| 17 | 真性キャリア密度 | pass | pass | pass | false |
| 18 | 完全イオン化の電荷中性 | pass | pass | pass | false |
| 19 | 電子・正孔drift電流 | pass | pass | pass | false |
| 20 | 急峻p-n接合空乏近似 | pass | pass | pass | false |
| 21 | 理想MOS酸化膜容量 | pass | pass | pass | false |
| 22 | 長チャネルNMOS平方則 | pass | pass | pass | false |
| 23 | 速度飽和・DIBL補正 | pass | pass | pass | false |
| 24 | CMOS静的切替点 | pass | pass | pass | false |
| 25 | 論理電圧・雑音余裕 | pass | pass | pass | false |
| 26 | CMOSゲート接続契約 | pass | pass | pass | false |
| 27 | 1次遅延・動的電力 | pass | pass | pass | false |
| 28 | レイアウトpitch・面積 | pass | pass | pass | false |
| 29 | low/high/undefined状態集合 | pass | pass | pass | false |
| 30 | NAND真理値・段数 | pass | pass | pass | false |
| 31 | NAND合成コスト | pass | pass | pass | false |
| 32 | SystemVerilog幅・select契約 | pass | pass | pass | false |
| 33 | 有限幅signed/unsigned解釈 | pass | pass | pass | false |
| 34 | 固定幅ripple加算 | pass | pass | pass | false |
| 35 | logical shift契約 | pass | pass | pass | false |
| 36 | 相補双安定feedback | pass | pass | pass | false |
| 37 | level-sensitive D latch | pass | pass | pass | false |
| 38 | setup/hold safe window | pass | pass | pass | false |
| 39 | register next-state | pass | pass | pass | false |
| 40 | ring period・reset edge | pass | pass | pass | false |
| 41 | SRAM read/write cell | pass | pass | pass | false |
| 42 | DRAM retention/refresh | pass | pass | pass | false |
| 43 | bank address decode | pass | pass | pass | false |
| 44 | PC branch・r0保護 | pass | pass | pass | false |
| 45 | RV32I field encoding | pass | pass | pass | false |
| 46 | aligned stack frame | pass | pass | pass | false |
| 47 | single-cycle next PC | pass | pass | pass | false |
| 48 | RV32edu memory map | pass | pass | pass | false |
| 49 | trap cause・mepc | pass | pass | pass | false |
| 50 | reset vector・UART | pass | pass | pass | false |
| 51 | critical path・CPI | pass | pass | pass | false |
| 52 | pipeline fill/flush | pass | pass | pass | false |
| 53 | RAW forwarding・stall | pass | pass | pass | false |
| 54 | branch misprediction penalty | pass | pass | pass | false |
| 55 | cache mapping | pass | pass | pass | false |
| 56 | Sv32 VA→PA translation | pass | pass | pass | false |
| 57 | MESI sharer/writer | pass | pass | pass | false |
| 58 | compare-and-swap | pass | pass | pass | false |
| 59 | issue width・dependency | pass | pass | pass | false |
| 60 | speculative cache observation | pass | pass | pass | false |

第9章は線路長を1.0 mから0.1 mへ変更して `κ` の変化を確認し、`C'=0` を入力契約エラーとして検出した。第10章は接地抵抗を変更して節点電圧が変わることと、零抵抗入力の検出を確認した。第11章は `R` を変更して時定数が変わることと、非正の `C` の検出を確認した。第12章は終端を50 Ωから1 kΩへ変更して反射係数が変わることと、ナイキスト条件違反の検出を確認した。第13章は井戸幅の変更で準位が変わることと、非整数・零の量子数を拒否する入力契約を確認した。第14章は障壁幅の変更で指数減衰尺度が変わることと、`E>=V0` の境界を検出した。第15章は温度変更で占有率が変わることと、`T=0` を有限温度モデルの外側として検出した。第16章は二サイト準位差の変更でギャップが変わることと、零格子定数を検出した。第17章は温度変更で真性キャリア密度が変わることと、負の状態密度を検出した。第18章はドナー濃度変更で多数キャリアが変わることと、負の濃度を検出した。第19章は電場変更でdrift電流が変わることと、負の移動度を検出した。第20章は内蔵電位変更で空乏幅が変わることと、非正の誘電率を検出した。第21章は酸化膜厚変更で `C_ox` が変わることと、零膜厚を検出した。第22章はゲート電圧変更で平方則電流が変わることと、しきい値以下を検出した。第23章は電場変更で速度飽和補正が変わることと、非正の飽和速度を検出した。第24章は `β_n` 変更で切替点が変わることと、零電源を検出した。第25章は電源電圧変更で雑音余裕が変わることと、零電源を検出した。第26章は入力段数変更で真理値表・直列段数が変わることと、零段数を検出した。第27章は負荷容量変更で遅延が変わることと、負荷容量の符号違反を検出した。第28章は配線間隔変更でpitchが変わることと、零間隔を検出した。第29章はしきい値幅変更でundefined領域が変わることと、順序違反を検出した。第30章はNAND入力段数変更で真理値表行数が変わることと、零段数を検出した。第31章は積項・リテラル変更でNANDコストが変わることと、不正な積項数を検出した。第32章はRTLデータ幅変更で入力ベクトル数契約が変わることと、零幅を検出した。第33章はビット幅変更でsigned解釈が変わることと、零幅を検出した。第34章は加数変更で固定幅和が変わることと、零幅を検出した。第35章はshift量変更で結果が変わることと、幅外shiftを検出した。第36章はloop gain変更で安定状態数が変わることと、非相補初期状態を検出した。第37章はラッチ入力変更で保持出力が変わることと、clock mode欠落を検出した。第38章はsetup時間変更でsafe windowが変わることと、零clock periodを検出した。第39章はload data変更でnext stateが変わることと、零幅を検出した。第40章は反転段遅延変更で発振周期が変わることと、零遅延を検出した。第41章はSRAM書込みでread bitが変わることと、非binary cellを検出した。第42章はrefresh周期変更で余裕が変わることと、retention超過を検出した。第43章はアドレス変更でbankが変わることと、配列外アドレスを検出した。第44章はbranch条件変更でnext PCが変わることと、r0書込みを検出した。第45章はrd変更で命令語が変わることと、x31超えのレジスタを検出した。第46章はcall depth変更でstack pointerが変わることと、未整列frameを検出した。第47章はbranch条件変更でnext PCが変わることと、未整列PCを検出した。第48章はアドレス変更でmemory regionが変わることと、負のアドレスを検出した。第49章はtrap cause変更でmcauseが変わることと、未知causeを検出した。第50章はreset vector変更でfirst fetchが変わることと、未整列resetを検出した。第51章はcritical path変更でcycle timeが変わることと、零CPIを検出した。第52章はflush数変更で総cycleが変わることと、零stageを検出した。第53章はproducer/consumer timing変更でstallが変わることと、負cycleを検出した。第54章はmisprediction数変更でpenaltyが変わることと、過大mispredictionを検出した。第55章はline size変更でoffsetが変わることと、零line sizeを検出した。第56章はPTEのPPN変更でphysical addressが変わることと、invalid PTEを検出した。第57章はreader/writer数変更でMESI状態が変わることと、複数writerを検出した。第58章はCAS current変更でsuccessが変わることと、非CAS操作を検出した。第59章はissue width変更でissue cycleが変わることと、零幅を検出した。第60章はsecret bit変更でcache observationが変わることと、非binary secretを検出した。

この証跡は、章ごとの変更・故障をモデルコードで再現できるという限定的な実装確認である。学習者が本文を読み、同じ操作を自力で行い、説明・再挑戦まで通過したことは記録しない。また、外部tool、固定Linux target、FPGA、実回路・実機測定、独立専門家AIレビュー、第13章以降、106章全体の学習ゲートへは昇格させない。従って `learner-ready=false` と `measured_true=0` は維持する。
