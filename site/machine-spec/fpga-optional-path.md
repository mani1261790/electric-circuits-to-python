# FPGA任意追加経路の仕様

この文書は、PC-onlyの必修経路を修了した後に、`rv32edu`をFPGAへ移すための任意経路を固定する。FPGAを使わない学習者の章合格、外部domain実験、物理測定の代わりにはならない。

## 1　この経路で追加する層

PC上のPython、解析模型、Verilator、Yosysの結果は、FPGA上の回路が同じ条件で動いたことを意味しない。任意経路では、次の変換を別々のartifactとして保存する。

```text
SystemVerilog RTL
  → synthesis netlist
  → place-and-route result
  → timing report
  → bitstream
  → board pin / clock / reset
  → UARTまたはlogic-analyzer observation
```

合成が成功しても配置配線やtimingを合格とはしない。bitstreamを書き込めても、UART文字列が得られたことと、指定したclock・reset・memory mapが検証されたことを一つにしない。

## 2　候補条件（未検証）

現在の候補は、章47・48のmanifestと揃えた次の値である。

| 項目 | 候補値 | 現在の状態 |
| --- | --- | --- |
| reference board | Lattice iCE40 HX8K | `candidate` |
| toolchain | Yosys 0.40 + nextpnr-ice40 | version／実行条件を固定前 |
| clock | P1, 10 MHz | `candidate` |
| reset_n | P2 | `candidate` |
| trace_valid または UART TX | P3 | top moduleに応じて選択 |
| bitstream | — | `not_built` |
| timing report | — | `not_generated` |
| board measurement | — | `none` |

候補値は、基準board、package、電源、pin制約、tool version、温度、clock sourceを固定した実行記録ができるまで、本文中で測定値や検証済み設定として扱わない。章64のboot経路では、ROM image hash、clock、UART出力、bitstream hashを追加で記録する。

## 3　必要なartifactと合格条件

任意経路を一つの実験として閉じるには、少なくとも次を同じcommitまたは内容hashで対応させる。

1. RTL source、top module、include、parameterのhash。
2. pin constraintとclock constraint。P1/P2/P3の用途を明記する。
3. synthesis logと生成netlist。未接続、latch、幅切捨て、未定義clockを診断する。
4. place-and-route logとtiming report。setup、hold、clock uncertainty、worst slackを保存する。
5. bitstreamのhashと書込みtoolの版。
6. boardの電源、clock、resetの状態、およびUART／logic analyzerの入力条件。
7. UART payloadまたは波形、取得時刻、測定器、sampling条件。

合格条件は「合成できた」だけではない。指定したpinへ有効なclock・resetが入り、timing reportが設定した制約を満たし、bitstream hashが書込み対象と一致し、同じimageから期待したUART traceを得たことを、各段の証拠で確認する。どれか一つが欠けたら、その段以降は `not_run_due_to_<stage>` と記録する。

## 4　PC-onlyとの境界

Verilatorのcycle traceはRTL simulatorの結果、Yosysのreportは合成toolの結果である。どちらもFPGA board上の電圧、温度、timing、UART信号を測ったものではない。逆にboard UARTが表示した文字列だけでは、sourceからimageまでの対応を証明できない。

そのため、通常の公開制作版ではこの経路を `candidate` / `not_built` と表示し、`measured=false`を維持する。基準学習者はPC-only経路だけで全層の説明、解析、テスト、変更課題へ進める。FPGAを選ぶ読者は、この文書のartifact表を埋めてから、該当章の独立確認を追加する。
