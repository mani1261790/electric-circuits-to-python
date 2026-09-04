# 第9〜32章 独立レビュー（2026-09-04）

## 位置づけ

執筆セッションとは別の専門家役セッションとして、現行worktreeの第9〜32章を読み合わせた。対象は本文`chapter.txt`、`manifest.yml`、`exercises.txt`、`solutions.txt`、`figures.yml`、`sources.yml`、`handoff.yml`、章別runner artifact、`artifacts/runner/full-run-20260904.json`、`artifacts/canonical/index.json`、HTML、ページ測定、環境lockである。既存の第9〜16章、第17〜24章、第25〜32章の部分レビューは履歴・修正点の把握に参照したが、判定は現行ファイルと現行hashを優先した。

本文、manifest、演習、解答、figure/source、handoff、runner、canonical、HTMLは変更していない。このファイルだけを新規作成した。

## 結論

章ローカルの現行判定は次の通りである。

| 判定 | 件数 | 内容 |
|---|---:|---|
| P0 | 0 | 直ちに学習経路を壊す定義・式・誤った測定表示は見つからない |
| P1 | 0 | 第9〜32章内で、修正なしには学習を止める未解決findingは見つからない |
| P2 | 4 | 第12、14、15、16章冒頭のrunner/domain状態表現が現行artifactとずれる |

大きな局所P1は確認されなかった。第32章の過去の`sv_decoder` source不整合、第21〜23章の`C_ox`/`phi_ms`連鎖、第9〜16章の古いrunner未実行表記、第25〜27章の古い状態表記は、現行本文・manifest・runner・canonical・HTMLでは修正済みと判定する。

ただし、書籍全体としての`learner-ready`は不可である。対象章の固定runnerは全件成功しているが測定欄は全件`not_run`であり、外部domain tool、実回路、シリコン、FPGAの成果を含まない。また、このレビュー単独では13巻の巻統合、全106章の全体統合、全体の最終独立判定を完了扱いにしない。

## 機械的な再確認

現行の次の検査を読み取り中心で実行した。

- `./tools/validate_book` — 終了コード0、`validated global manifest and 106 written chapter(s)`。
- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_chapter_schemas.py` — `106 chapters, normalized=106, errors=0`。handoff形状はlegacy 14、modern 91、terminal 1、review gate形状はlist 19、mapping 87。
- `uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json` — source row 631、sign-off entry 631、`verified=423`、`accepted_boundary=208`、`hold=0`、missing/duplicate/errorなし、coverage complete、gate complete。
- 対象章のHTMLリンク監査 — 第9〜32章24文書、href 3,797件、存在しないリンクまたはfragment 0件。
- 対象章のrunner artifactとfull-run記載 — 115件すべてartifactあり、終了コード0、記録hashと実ファイルhashの不一致0件。
- 対象章のcanonical tree — 140件すべてmaterialized、tree hash不一致0件、全件`measured=false`。
- 対象章のmanifest equation ID、required artifact ID、canonical artifact ID — 未解決ID 0件。
- handoff — 第9→10→…→32→33の連続経路、章タイトル、次章入力の構造欠落なし。

source sign-offは出典状態の意味を独立に確認するゲートであり、外部実験や物理測定の完了を意味しない。`accepted_boundary`はplanned、not-run、任意経路、local仕様などをその状態のまま受理した行である。従って、sign-off完了をもってFPGA、SPICE、実回路、測定の実行済みとは扱わない。

## runner、canonical、PC-only／外部／FPGAの境界

`artifacts/runner/full-run-20260904.json`は全718件中718件が終了コード0、失敗0である。全体の検証分類は`contract_model_verified=548`、`analytic_verified=127`、`domain_verified=26`、`educational_model_verified=17`、測定は718件すべて`measurement_status=not_run`である。ここで`domain_verified`は固定runnerが入力由来のdomain式・契約モデルを検査したという意味で、外部solver、SPICE、計測器、実物試料を意味しない。

対象115件の内訳は次の通りである。

| 章 | 件数 | analytic | contract model | domain | 測定 |
|---:|---:|---:|---:|---:|---|
| 9 | 1 | 0 | 0 | 1 | 1 not_run |
| 10 | 1 | 0 | 0 | 1 | 1 not_run |
| 11 | 1 | 0 | 0 | 1 | 1 not_run |
| 12 | 1 | 0 | 0 | 1 | 1 not_run |
| 13 | 1 | 0 | 1 | 0 | 1 not_run |
| 14 | 1 | 0 | 1 | 0 | 1 not_run |
| 15 | 1 | 0 | 1 | 0 | 1 not_run |
| 16 | 1 | 0 | 1 | 0 | 1 not_run |
| 17 | 1 | 0 | 1 | 0 | 1 not_run |
| 18 | 1 | 0 | 1 | 0 | 1 not_run |
| 19 | 1 | 0 | 1 | 0 | 1 not_run |
| 20 | 8 | 0 | 8 | 0 | 8 not_run |
| 21 | 8 | 0 | 8 | 0 | 8 not_run |
| 22 | 8 | 0 | 8 | 0 | 8 not_run |
| 23 | 8 | 0 | 8 | 0 | 8 not_run |
| 24 | 8 | 0 | 8 | 0 | 8 not_run |
| 25 | 8 | 1 | 7 | 0 | 8 not_run |
| 26 | 8 | 7 | 1 | 0 | 8 not_run |
| 27 | 8 | 7 | 1 | 0 | 8 not_run |
| 28 | 8 | 8 | 0 | 0 | 8 not_run |
| 29 | 8 | 6 | 2 | 0 | 8 not_run |
| 30 | 8 | 6 | 2 | 0 | 8 not_run |
| 31 | 8 | 6 | 2 | 0 | 8 not_run |
| 32 | 8 | 6 | 2 | 0 | 8 not_run |

canonical indexでは対象140 entryがすべて`materialized=true`、`status=executed_analytic`、`measured=false`である。これは解析・契約再生のlineageがあることを示すが、SPICE、Verilator、Yosys、FPGA、実回路、分光、Hall測定などの実行結果ではない。

第11章にはホストngspice-47のRC/RLC外部tool出力、第24章にはホストngspice-47のCMOS VTC出力、第32章にはホスト上のIcarus／Verilator／Yosys出力が別系統の`artifacts/external/host-20260902/`にある。しかしこれらは固定runnerの`measurement=not_run`と別の外部tool証拠であり、`physical_measurement=false`の範囲を超えない。第28章のopen PDK、レイアウト後抽出、実製造は発展経路である。第32章のFPGAは任意経路で、現行対象にboard制約、bitstream、board上の波形、実機測定はない。採用リリースがPC-onlyである限り、これらは必修pathの欠陥ではないが、FPGA path完了とは表示できない。

## 数式・説明・代表値の読み合わせ

本文の式、単位、仮定、代表case、expectedの向き、解答を突合した。以下の値は本文またはmanifestの入力から再現できる代表的な検査点であり、測定値ではない。

### 第9〜16章

| 章 | 独立に確認した要点 | 判定 |
|---:|---|---|
| 9 | `t_prop=ell/v_p`（1 mで5 ns、1 cmで50 ps）、`kappa=t_prop/t_rise`、`v_p=1/sqrt(L'C')`、`Z_0=sqrt(L'/C')`。`R'=50 Ω/m, L'=250 nH/m, G'=0, C'=100 pF/m`から`R_lumped=50 Ω, C_lumped=100 pF, tau=5 ns, Z0=50 Ω`。`chapter.txt:5-33,76-166,173-281`。 | P0/P1なし |
| 10 | 制御体積からKCL、Faraday積分から条件付きKVL、MNA。電流源caseの`V1=2.75 V, V2=2.50 V, I12=0.25 mA`、浮いた電圧源caseの残差・電力符号。`chapter.txt:3-79,109-161,163-311,445-470`。 | P0/P1なし |
| 11 | `tau=RC=1 ms`、RC充電`3.1606 V/4.9663 V`、放電`1.8394 V`、RLCの`alpha=500 1/s, omega0=1e4 rad/s, omega_d=9987.492... rad/s`。陽Euler、初期条件、SPICEと測定の分離。`chapter.txt:3-45,119-263,265-390`。 | P0/P1なし |
| 12 | `f_c=1/(2pi RC)=159.1549 Hz`、`|H(100 Hz)|=0.846733`、`|H(f_c)|=0.707107`、`|H(1 kHz)|=0.157177`、熱雑音RMS約`128.7 nV`、`Gamma(1 kΩ)=0.904762`、伝搬5 ns。FFTの窓・bin・帯域、反射、測定器負荷を分離。`chapter.txt:3-17,23-185,187-252`。 | **P2-12-01** |
| 13 | Coulomb/Larmorの古典限界、無限井戸`E_n=n^2E_1`、`E1≈6.0247e-20 J≈0.3760 eV`、`E2≈1.504 eV`、`E3≈3.384 eV`、有限差分と境界・単位・質量の負のテスト。`chapter.txt:3-41,84-224`。 | P0/P1なし |
| 14 | Born確率と規格化、Schrodinger方程式、固有状態と重ね合わせ、有限障壁の`kappa≈2.81e9 1/m`、`exp(-2kappa a)≈3.7e-3`、前因子付き・矩形式約`1.4e-2`の区別、Crank–Nicolsonのノルム。`chapter.txt:3-17,19-232`。 | **P2-14-01** |
| 15 | Pauliの一粒子状態数え上げ、`f(E)=1/(exp((E-mu)/(kBT))+1)`、`E0=0,E1=0.10 eV,g0=g1=2,T=300 K,mu=0.050 eV`から`f0≈0.8737,f1≈0.1263,N≈2`、有限温度の二分法と`T=0`境界。`chapter.txt:3-24,26-187`。 | **P2-15-01** |
| 16 | 周期ポテンシャル、Bloch条件、`E(k)=epsilon-2t cos(ka)`、幅`4|t|`、二サイトgap、DOSのper-cell/totalとスピン係数、有限差分/Bloch位相。`chapter.txt:3-19,23-233`。 | **P2-16-01** |

### 第17〜24章

| 章 | 独立に確認した要点 | 判定 |
|---:|---|---|
| 17 | `E_g=E_c-E_v`、電子・正孔の符号、`n_i=p_i=sqrt(N_cN_v)exp[-E_g/(2kBT)]`、指定caseの`n_i≈6.5e9 cm^-3`。DOS、非縮退近似、`rho=e(p-n)`、温度境界を分離。`chapter.txt:5-29,61-243`。 | P0/P1なし |
| 18 | `n=N_c exp[-(E_c-E_F)/(kBT)]`、`p=N_v exp[-(E_F-E_v)/(kBT)]`、電荷中性、完全イオン化、二分法、donor caseの`n≈1e16 cm^-3,p≈4.3e3 cm^-3,E_c-E_F≈0.205 eV`。`chapter.txt:5-28,57-197`。 | P0/P1なし |
| 19 | 電子・正孔のdrift/diffusion符号、Einstein関係、連続の式、SRHとgross生成/再結合の分離。`E=100 V/m`のcaseで`J_n≈1.60e3 A/m²,J_p≈8.01e1 A/m²`。`chapter.txt:5-22`以降。 | P0/P1なし |
| 20 | `rho_total=q(p+N_D^+-n-N_A^-)`、Poisson、空乏幅、`V_bi`、最大電場、容量、Schottky–Mottとオーミック接触。前章のキャリア・イオン電荷の符号を引き継ぐ。`chapter.txt:5-76`以降。 | P0/P1なし |
| 21 | `C_ox=epsilon_ox/t_ox`、`V_FB=phi_ms-Q_ox/C_ox`、`V_G=V_FB+psi_s-Q_s/C_ox`、p型の`Q_s<0,psi_s>0`、`phi_F/phi_s/phi_ms`導出、低周波・高周波C–Vの範囲。旧CODATA/`phi_ms`問題は現行連鎖で解消。`chapter.txt:13-117`以降。 | P0/P1なし |
| 22 | `Q_inv=-C_ox[V_GS-V_th-V(x)]`、linear/saturationの領域、`V_DS,sat=V_OV`、nMOS端子符号、`V_GS<=V_th`で強反転式を使わない境界。`chapter.txt:13-91`以降。 | P0/P1なし |
| 23 | channel-length modulation、velocity saturation、DIBL、body effect、subthreshold、遅延を別の補正として扱う。`I_D=I_D,sat(1+lambda V_DS)`、`I_D≈W|Q_inv|v_sat`の適用範囲。`chapter.txt:19-75`以降。 | P0/P1なし |
| 24 | pMOSの`V_SG/V_SD`、nMOS/pMOS電流の向き、`I_p-I_n=0`、対称caseの`V_M=0.5 V`、理想模型のrail境界、静的と過渡KCL。`chapter.txt:5-77`以降。 | P0/P1なし |

### 第25〜32章

| 章 | 独立に確認した要点 | 判定 |
|---:|---|---|
| 25 | `V_OH/V_OL/V_IH/V_IL`の保証境界、`NML=V_IL-V_OL`、`NMH=V_OH-V_IH`、VTC傾きと過渡KCLを区別。runner/SPICE/測定の状態表記は現行artifactに同期済み。`chapter.txt:1-45,72-199`以降。 | P0/P1/P2なし |
| 26 | NANDのPDN直列/PUN並列、NORの双対、伝送ゲート、NAND-XOR、真理値契約と電圧波形の分離。`source_kind=analytic_prediction`とSPICE/測定のplanned/not_runを分ける。`chapter.txt:1-33,140-168`以降。 | P0/P1/P2なし |
| 27 | `t_pHL/t_pLH`の判定規約、`C_load=C_intrinsic+N_fanout C_in+C_wire`、`C_load dV_out/dt=I_PUN-I_PDN`、`E_charge=C V^2`と`E_stored=1/2 C V^2`の区別。`chapter.txt:1-57`以降。 | P0/P1/P2なし |
| 28 | 層・mask・工程の一般模型、DRCのwidth/spacing/enclosure/overlap、LVSの接続同値、寄生抽出とpost-layout SPICE、PDKを任意発展経路に限定。`chapter.txt:1-61`以降。 | P0/P1/P2なし |
| 29 | 物理状態の集合、`V_OL<=V_IL`と`V_IH<=V_OH`、判定閾値、条件付き誤り、PMF、有限標本とClopper–Pearson上限。E1〜E10の10問構成はschemaの許容範囲内で、E11/E12を欠くことは欠陥ではない。`chapter.txt:1-80`以降。 | P0/P1/P2なし |
| 30 | Boolean演算、NANDだけのNOT/AND/OR、NAND netlist依存順、未定義wire・循環・二重駆動・アナログ値の負のテスト。runner結果とSPICE/測定の非同一性。`chapter.txt:1-62`以降。 | P0/P1/P2なし |
| 31 | 真理値表→積和形→NAND netlist、`F=A+BC`、gate/depth/fan-outと遅延見積りの分離、同値性とSPICE/測定の区別。`chapter.txt:1-69`以降。 | P0/P1/P2なし |
| 32 | `assign`と`always_comb`、MUX、decoder、Verilator/Yosys/形式検証の証拠分離、X/Z/latch/libraryの負のテスト。decoder代表sourceは4本の明示的assignで、本文の`no variable-index shift or pmux`契約と一致。`chapter.txt:1-55`以降。 | P0/P1/P2なし |

## 未解決の局所finding

### P2-12-01: 第12章冒頭のdomain状態表現

位置: `manuscript/volume-02/chapter-12/chapter.txt:17`。同じ文に「`book run 12 1`も解析adapterは実行済みだがdomain処理は未実行」とある。現行`artifacts/runner/chapter-012/experiment-01.json`は終了コード0、`verification.status=domain_verified`、`measurement.status=not_run`で、入力由来の周波数応答・雑音・伝送線路式を計算している。外部SPICEや実測が未実行という意味なら妥当だが、「domain処理未実行」は固定runnerの計算も未実行と読める。

修正候補（本文は変更していない）: 「固定runnerの入力由来解析／契約モデルは実行済み。外部domain tool、SPICE、実測は未実行（`measurement.status=not_run`）」のように層を限定する。`analytic_prediction`、runner、SPICE、measurementを同じ波形列へ上書きしないという後段の説明は維持する。

### P2-14-01: 第14章冒頭のdomain状態表現

位置: `manuscript/volume-02/chapter-14/chapter.txt:17`。現行artifactは終了コード0、`contract_model_verified`、`measurement.status=not_run`で、無限井戸・有限障壁・固有状態・Crank–Nicolsonの入力由来契約を実行済みである。分光器による測定値を含まないという境界は正しいため、P1ではなく状態表現のP2とした。

修正候補: 「固定runnerの入力由来契約モデルは実行済み。外部domain／分光測定は未実行」と書き、`contract_model_verified`を測定結果へ昇格させない。

### P2-15-01: 第15章冒頭のdomain状態表現

位置: `manuscript/volume-02/chapter-15/chapter.txt:24`。現行artifactは終了コード0、`contract_model_verified`、`measurement.status=not_run`で、Pauli・Fermi–Dirac二準位caseの構造とexpectedを保存している。本文の「実在原子の分光測定ではない」は正しいが、「domain処理未実行」は入力由来契約モデルを未実行と誤読させる。

修正候補: 固定runnerの契約モデル実行済みと、実在原子・外部solver・分光測定未実行を別欄として明記する。

### P2-16-01: 第16章冒頭のdomain状態表現

位置: `manuscript/volume-02/chapter-16/chapter.txt:19`。現行artifactは終了コード0、`contract_model_verified`、`measurement.status=not_run`で、tight-binding、二サイトgap、DOS、Bloch境界の入力由来契約を確認している。実固体の測定スペクトルを含まないという前半の境界は正しい。

修正候補: 第14、15章と同じく「固定runnerの入力由来契約モデルは実行済み。外部固体domain、実スペクトル測定は未実行」と整理する。

いずれも周辺節、manifest、runner artifactが解析／契約／外部／測定の区別を補っており、現状で測定済みと偽る主張はない。そのため4件はP2であり、P0/P1へ繰り上げない。修正する場合は本文、対応HTML、必要ならpage-count metadataを同じ変更で再生成し、再hashする。

## 過去の局所P1／P2の現行再判定

- 第9〜16章の旧P2（第10章・第13章・第15章のrunner未作成／未実行）は、現行本文とHTMLで固定runner実行済み・測定not_runへ修正済み。第15章解答の旧「runnerがまだ実行されない」表記も修正済み。
- 第17〜19章の旧P2（冒頭の状態表記）は、現行本文で「固定runnerの入力由来契約モデルまで実行済み」「外部domain tool・実測は未実行」「measurement.status=not_run」となっている。
- 第21章の旧P1（CODATA 2022の`epsilon_0`から`C_ox`への値連鎖）は、現行第21〜23章本文、manifest、解答、runnerで`C_ox=0.0034531332493319996 F/m²`と後続値が統一されている。
- 第21章の旧P1（`phi_ms`再現性）は、現行本文に`phi_F=V_T ln(N_A/n_i)`、`phi_s=chi+E_g/2+phi_F`、`phi_ms=phi_m-phi_s`、eVと電圧差の対応がある。
- 第25〜27章の旧P2（plannedとrunner実行済みの混在）は、現行本文で固定runner実行済み、SPICE／測定not_runへ整理されている。
- 第32章の旧P1（`sv_decoder`代表sourceが可変添字で、明示的assign契約と矛盾）は、現行manifest `:96-108,526-563`、runner artifactで4本の`assign y[0]`〜`y[3]`、8行table、`source_contract=explicit_assign_all_outputs`へ統一されている。runnerの10 computed checksと3 contract checksは全てtrueで、外部SystemVerilog実行・測定の証明ではない。

## 演習、解答、実験見出し、変更、故障診断、再挑戦

対象24章の`exercises.txt`と`solutions.txt`をIDと内容の両方で突合した。

- 第9〜28章、第30〜32章はE1〜E12の対応があり、本文の到達点、manifestの代表case、expected観測と解答の方向が一致する。
- 第29章はE1〜E10で、schemaの許容範囲（8〜15問）内である。E11/E12がないことは欠陥ではない。
- 各章に、値または条件を一つだけ変える小変更、変更後の再挑戦、負のテストまたは故障診断、source/statusの境界を扱う導線がある。特に第9〜19章は単位・初期条件・境界・solver・測定区別、第20〜24章は符号・電荷・端子・threshold・VTC、第25〜32章は論理構造・幅・wire・latch・library・source_kindを故障として分類する。
- 章内の補助線／実験見出しは、入力、固定条件、期待値、観測状態、診断、再挑戦の順を保持している。expectedが文章の契約である場合も、測定値とは表示していない。
- 実行済み固定runnerの存在と、教材上の「外部toolをまだ実行しない」という予定は、外部domain／物理測定が未実行という意味で整合する。ただしP2-12-01〜16-01の4文だけは、固定runnerまで未実行と読めるため修正候補に残した。

## 図、出典、handoff

対象のfigure宣言と実体参照を突合した。第9章は5図、第10〜32章は各6図で、宣言参照の未解決はない。ただし全対象figureは現行記録で`status=planned`、`measured=false`、`accessed_for_this_draft=false`である。図を実測済みとして扱う根拠はない。

対象source rowは141行で、現行独立source sign-offの対応は`verified=108`、`accepted_boundary=33`、`hold=0`である。第9〜24章は全行verified、第25章は4 verified／2 accepted_boundary、第26章は4 verified／2 accepted_boundary、第27〜31章は全行accepted_boundary、第32章は4 verified／1 accepted_boundaryである。accepted boundaryの多くはplanned、local仕様、任意のSPICE／PDK／FPGA経路を明示するための行であり、外部実行結果や測定結果を表さない。source sign-off全体はcoverage complete／no holdだが、このレビューは出典の状態と本文の境界を確認するもので、未実行の外部経路を実行済みへ昇格させない。

handoffは第9→10→11→12→13→14→15→16→17、以降第32→33の主経路を確認し、並行して第11／12から第17、第14／15／16から後続章へ渡る量を確認した。代表的には、`R' L' G' C'`、KCL/KVL、RC/RLCの状態、FFT／反射、量子井戸の`E_n`・境界・規格化、縮退・占有、k・DOS、キャリア`n,p`、MOSの`C_ox`・threshold、CMOSの論理契約、HDL decoderの幅・順序が後続入力へつながる。`handoff_status`は独立レビュー待ち／planned系のプロセス状態として残るため、今回の局所確認を巻統合完了とは扱わない。

## 現行hashとHTMLページ

識別hashは正しさそのものを証明しないが、レビュー対象を固定するため記録する。

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260904.json` | `16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10` |
| `artifacts/canonical/index.json` | `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f` |
| `environment/lock.yml` | `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c` |
| `tmp/page-counts.json` | `fd002a1ddcabda496e0e5a2fc9a03718158d067521cf4e3e5ddb755ded2e8cb` |
| `reviews/source-ledger-verification-20260903.json` | `117420e9a3ceebdcacf83f58dc2271ec96781f75224f59d99291e03ac53ac741` |
| `reviews/source-semantic-signoff-verification-20260904.json` | `b1150835254cef1a5f7aa63836a2aea255232232dfbb8f9cc76ee1c626a19174` |

`tmp/page-counts.json`はprelude 11頁、本文合計3,514頁、prelude込み3,525頁、最小24頁、最大40頁、24頁未満0、106章・107行を記録する。対象24章のHTMLは記録hashと実ファイルhashが全件一致した。

| 章 | 頁 | HTML SHA-256 |
|---:|---:|---|
| 9 | 28 | `c748c9ba11e6eb5941129686e94a896f3846f32f4d9f29c1e45ca62227eb557b` |
| 10 | 31 | `a3470368e2c970555f75bf5d2cda9b3974a105da2cf9fe182b9dc0fe5e03e324` |
| 11 | 29 | `49af9df629fcf37a2c0fdcb697f6ce61126c54c2e0e456b5b2c386aefd4c2c40` |
| 12 | 25 | `a29e2f2766f33198459e53397b4299d220ba1680e5a68c1dddc22e4c0f1e8cc7` |
| 13 | 24 | `063ed16c106c6cbd3df6109d51bd68c577a73d4976fb97f37fd02285863f4a82` |
| 14 | 25 | `1404422901558c4f9d43eca661578fb9660571303d87d06b84fb9639089a84d7` |
| 15 | 24 | `2f662a9fbe492c3083166f51103c5cb9de5b0716ba62766e123dc0044247875e` |
| 16 | 24 | `0a60d3d68f4ee24d86e46ed8a1d1d656701d95c0928db35891f68be0a8742dbd` |
| 17 | 25 | `137b8b0491b3f3948f4e8d5929143aad4f86d6b3ea1b70c6fe44f1731a95a395` |
| 18 | 24 | `fc4b907c4e1c1f55a7959e30ff76ced745ee8baf4291989a0d6a8ff3ed44527c` |
| 19 | 25 | `8879361005fea6452d5f52f1eb3b500cbf7e2b13079cfe22bb7d6e44b8fdace3` |
| 20 | 33 | `711d1c9d4c916495a74294aea9446ad0a95b3e7b9f0898c84122f9f73d0c485a` |
| 21 | 36 | `bc3efa4cbf5ee96cbd84acce8f4dcf252932dfc45d43965ad553f58ca57a18e6` |
| 22 | 29 | `a441a4a793c5ea0cccc12998d558373a50335b90c20170299658a90ca56a5947` |
| 23 | 34 | `c7ca6ed87e6206e955ac29e5d82676162fd35935bc96875d4223b357aae5e778` |
| 24 | 35 | `77353cd03150dbae22d0ca0fe71bb219d59a0996fd00f1696e6da20e73c90152` |
| 25 | 40 | `07ec5b7862afe58487d4be3a4e159055716b103bd3ff1e670dd5e9b63cedba7d` |
| 26 | 34 | `596f70d27534dae96ed0f160fee43c800c84aa179291e6fe7adc5bde16d455b6` |
| 27 | 35 | `f91bbb6e95b1a68d4287f5872ea65400bc1ce28e4ac955157bb74dd377f86416` |
| 28 | 35 | `b05ea0f8155ba8f82c0017c2ac5275a4bfb2df18f757e93f0a3a722e25013f10` |
| 29 | 37 | `004469b21c507d6207d2ae7199c9feb64ae48ae051dafdba888f9e043ec1f475` |
| 30 | 33 | `56cc09edf49237c043889f6e11c47399cf659dd2c41aea9b4b19d0c6daf85c6e` |
| 31 | 36 | `f51599514a6dd235aaabdd68e81521ac4aca9887ab9a3de9a3f066118bad6325` |
| 32 | 34 | `cd3e932d78d0884dfbd4c9cbc193b6259b68b1a68191cf1b9f4c129641e8a17a` |

## 共有P1と最終判定

この範囲の局所P0/P1は0であるが、次の共有ゲートはこのartifactでは解除しない。

1. 固定runner 115件は再現可能な解析／契約結果で、測定115件ではない。外部domain tool、外部SPICE／RTL、FPGA、実回路、シリコン、分光などを必要とするcaseは、各artifactに`not_run`または任意／planned境界が残る。
2. 第28章のPDK／レイアウト後SPICE、第32章のSystemVerilog／Verilator／Yosys／形式検証／FPGAは、PC-onlyの必修pathと任意の外部pathを分けている。外部pathを完了扱いするには版、コマンド、条件、ログ、出力、必要ならboard／bitstream／測定を別artifactに固定する必要がある。
3. source sign-offは現行全体でcoverage complete、hold 0だが、`accepted_boundary`はplanned・local・任意・not-runの境界を受理した状態であり、外部実験や測定を代替しない。
4. 第9〜32章の局所確認をもって、13巻統合、全106章統合、全体の学習順・trace・未解決finding統合を完了扱いにしない。親タスク側で巻／全体reviewを別artifactとして最終確認する必要がある。

従って、現行の第9〜32章については **局所 P0=0 / P1=0 / P2=4**、書籍全体の **learner-ready=不可** と判定する。残る局所修正候補はP2-12-01〜16-01の4文であり、本文を直す場合も、固定runnerの入力由来モデル、外部tool、FPGA、実測の境界を明示した上でHTMLとhashを再生成する。

## 追補: 第12・14・15・16章の状態表記修正後の再確認（2026-09-04）

親タスク側で上記4箇所の本文を修正したため、執筆セッションとは別の確認として、4章の本文、対応HTML、章別runner artifact、canonical entryを再読した。修正後の表記は次のようになっている。

- 第12章 `manuscript/volume-02/chapter-12/chapter.txt:17`: `book run 12 1`は固定入力から解析モデルを実行済み、外部domain tool・SPICE・実測は未実行、`measurement.status=not_run`。
- 第14章 `manuscript/volume-02/chapter-14/chapter.txt:17`: `book run 14 1`は固定入力から契約モデルを実行済み、外部domain solver・分光測定は未実行、`measurement.status=not_run`。
- 第15章 `manuscript/volume-02/chapter-15/chapter.txt:24`: `book run 15 1`は固定入力から契約モデルを実行済み、外部domain solver・実在原子の分光測定は未実行、`measurement.status=not_run`。
- 第16章 `manuscript/volume-02/chapter-16/chapter.txt:19`: `book run 16 1`は固定入力から契約モデルを実行済み、外部固体domain solver・実スペクトル測定は未実行、`measurement.status=not_run`。

対応するHTML `build/html/chapter-012.html`、`chapter-014.html`、`chapter-015.html`、`chapter-016.html`にも同じ境界が反映され、「domain処理は未実行」という旧表現の残存は確認されなかった。本文後段も固定runnerの契約再生と、図・外部tool・測定の未実行を分けている。

4章のrunner artifactは以下の通り再確認した。

| 章 | runner artifact | 終了 | verification | measurement |
|---:|---|---:|---|---|
| 12 | `artifacts/runner/chapter-012/experiment-01.json` | 0 | `domain_verified` | `not_run` |
| 14 | `artifacts/runner/chapter-014/experiment-01.json` | 0 | `contract_model_verified` | `not_run` |
| 15 | `artifacts/runner/chapter-015/experiment-01.json` | 0 | `contract_model_verified` | `not_run` |
| 16 | `artifacts/runner/chapter-016/experiment-01.json` | 0 | `contract_model_verified` | `not_run` |

4件とも`measured=false`で、artifactのscopeも`input-derived invariant; not external tool or physical measurement`である。canonical側も第12章6件、第14章6件、第15章5件、第16章6件が`materialized=true`、`status=executed_analytic`、`measured=false`で、runner artifact SHAとのlineage不一致は0件だった。従って、修正により「固定runnerまで未実行」と読める旧P2は解消したと判定する。

修正後の局所判定は次の通り更新する。

- P0: 0
- P1: 0
- **旧P2-12-01／14-01／15-01／16-01: 4件とも解消**
- 現行の第9〜32章ローカルP2: **0**

再確認時点でも、固定runner 115件は解析／契約モデルであり測定ではなく、4章を含む対象runnerの測定欄は`not_run`である。外部domain solver、SPICE、実在原子・固体の測定、FPGA、実回路を実行済みとは扱わない。この追補は4つの状態表記P2を解消するが、PC-only経路と任意FPGA／PDK経路、巻統合・全体統合、書籍全体の`learner-ready`共有判定は変更しない。

### 追補時の再識別hash

| 対象 | SHA-256 |
|---|---|
| `artifacts/runner/full-run-20260904.json` | `16522fa6af2fb4bc2df3569118c77562ead09cee1ab1c3ae25057c4c00fb2d10` |
| `artifacts/canonical/index.json` | `61bfae9157449838b91527b77945788771dc8fad9440a7d6b646ba2c661f973f` |
| `environment/lock.yml` | `2ba6efc73090f571d97c117ee5a17680d8f6d37738f66a4c3a9c0530d3231d1c` |
| `tmp/page-counts.json` | `b307a9e549caef13d06b293242c5756b31fccb5087843a0ad9fe34fab8b4b4fd` |

`tmp/page-counts.json`は修正後にprelude 11頁、本文3,515頁、prelude込み3,526頁、各章24〜40頁、24頁未満0を記録している。4章のHTML記録hashと実ファイルhashは全件一致した。

| 章 | 頁 | HTML SHA-256 |
|---:|---:|---|
| 12 | 25 | `ebe15e5a18e445cbc9b323dbad50a07594a4f8064e313a6a8ef396e3fe312098` |
| 14 | 25 | `165da948003fa1ecf21f1040158bfd8c79472cf5462ebd03fe94bd80c2a3cc0e` |
| 15 | 24 | `686823859ba9e9c8188655589b437ae668f0302b6a07cbad6823ddccf9e9d48f` |
| 16 | 24 | `b68e3b818e11e9501cbc664453af65db9ac33621e87d425f5ef6a6dc3135ec3b` |

`./tools/validate_book`も修正後に終了コード0で`validated global manifest and 106 written chapter(s)`を返した。以上により、最新スナップショットにおける本レビューの章ローカル判定は **P0=0 / P1=0 / P2=0** へ更新する。
