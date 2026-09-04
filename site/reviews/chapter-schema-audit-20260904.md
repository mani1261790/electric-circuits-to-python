# 章メタデータ schema 監査（2026-09-04）

`book-spec/chapter-metadata-schema.md` の `CHAPTER-METADATA-NORMALIZED-1` に従い、現行の106章を読み取り専用で正規化できるか確認した。

実行コマンド:

```text
uv run --with 'PyYAML==6.0.3' --no-project python3 tools/check_chapter_schemas.py --json
```

結果:

```json
{
  "chapters": 106,
  "normalized_chapters": 106,
  "review_gate_shapes": {"list": 19, "mapping": 87},
  "handoff_shapes": {"legacy": 14, "modern": 91, "terminal": 1},
  "errors": []
}
```

旧形式の `review_gates`（第1〜19章）と、旧形式の `next_chapter_id/title` を含むhandoffを、ファイルを書き換えずに共通の読み取り投影へ変換できた。途中章の次章ID・題名はglobal manifestと一致し、第106章の「付録と継続学習」だけは番号のない終端handoffとして扱った。第20〜24章を含む全handoffで `handoff_status` の欠落はない。

`tools/validate_book` にも、レビューゲートの型、handoffの旧形式組、`handoff_status`、第106章の終端例外を検査するチェックを追加し、`validated global manifest and 106 written chapter(s)` を再確認した。

この監査はschemaの読み取り互換性を固定するもので、manifestのrunner payload、本文、出典のsemantic判定、外部domain・FPGA・物理測定、章・巻・全体の意味sign-offを完了扱いにしない。

追補: `handoff_status` を非空文字列としても検査するようcheckerと`validate_book`を強化した。再実行結果は同じく106/106、errors=0で、現行checker SHA-256は `5b391cf3eb9b4c130780a75b94b360df8471bd71f1ad69850d800a008567ac13`、validator SHA-256は `8d9e3f748dd447061b1fa45a2f8b6be2f9f7b31e09e8e838e299b85de6cbe07c` である。
