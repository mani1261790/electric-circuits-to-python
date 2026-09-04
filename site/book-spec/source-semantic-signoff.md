# 出典semantic sign-off契約

この文書は、`sources.yml` の候補行を、執筆セッションとは別の確認セッションが
主張単位で確認した結果を記録するための契約である。機械的なURL取得やlocatorの
存在検査だけでは `verified` にならない。

## 入力

`reviews/independent-source-signoff-*.yml` を、出典台帳の分割範囲ごとに置く。
各ファイルは次の形をとる。

```yaml
schema: SOURCE-SEMANTIC-SIGNOFF-1
range: 1-200
reviewer_session: independent-source-review-001-200
source_ids:
  - key: manuscript/volume-01/chapter-01/sources.yml#1
    id: some-source-id
    decision: verified
    evidence:
      - path/to/file:12-24
      - https://example.invalid/spec#section
    note: 主張、採用版、節、本文引用位置を確認した。
```

`source_ids` は対象行を一度ずつ列挙する。`key` は現行ファイルの相対パスと
1始まりの行番号を `path#row` で表す安定な行キーであり、`id` は表示用に併記する。
同じ短いID（例: `S1`）が複数章で再利用されるため、IDだけを一意キーにしてはいけない。
`decision` は次の三値だけを許す。

- `verified`: 必修の本文主張を支える資料・版・節・本文引用位置を独立に確認した。
- `accepted_boundary`: 候補、planned、not-run、または任意経路であり、本文がその
  状態を明示していることを確認した。未実行の成功や実測を根拠にしない。
- `hold`: 資料の意味、版、節、実体、本文との対応のいずれかが未解決で、修正なしに
  完成ゲートを閉じられない。

`evidence` と `note` は必須で、確認者が読んだ具体的な入口を残す。確認者は本文の
執筆に参加していない別セッションでなければならない。`semantic_review` を推測で
変更せず、保留行を別の分類へ移す場合は、実際の修正後に再確認する。

台帳を参照する場合は、`ledger`（または互換名 `source_ledger`）と
`ledger_sha256`、必要に応じて`ledger_generated_at_utc`をsign-offへ記録する。
検査器は現在の台帳SHAと照合し、古い台帳に対する判定を現行行の合格として扱わない。

## 完成ゲートでの扱い

検査器は、全source IDの被覆、重複、許可されたdecision、確認者名、証跡を検査する。
`hold` が残る場合、または被覆が欠ける場合、全体sign-offは未完了である。
`accepted_boundary` は出典意味の確認を代替するものではないが、本文が候補・任意・
未実行を正しく表示している行を、実測済みと誤って扱わないための明示的な判定である。

現行台帳に対する検査は、authoring環境の依存を固定するため次で実行する。

```text
uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_source_signoff.py --json
```

検査器は `reviews/source-semantic-signoff-verification-20260904.json` と同名Markdownを更新し、
終了コード0は被覆完了かつ `hold=0` の場合だけ返す。

この契約を通過しても、固定runnerの `measurement=not_run`、FPGA任意経路、実回路・
物理測定、章・巻・全体の統合確認を完了扱いにはしない。それらは別ゲートである。
