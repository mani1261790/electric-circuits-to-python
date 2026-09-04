#!/usr/bin/env python3
"""Validate local links and publication boundaries in a built public site."""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del tag
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)
            if key == "id" and value:
                self.ids.add(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", type=Path, default=Path("build/public-site"))
    args = parser.parse_args()
    site = args.site.resolve()
    documents: dict[Path, LinkParser] = {}
    for path in sorted(site.rglob("*.html")):
        parsed = LinkParser()
        parsed.feed(path.read_text(encoding="utf-8"))
        documents[path] = parsed
    failures: list[str] = []
    local_links = 0
    for document, parsed in documents.items():
        for reference in parsed.links:
            split = urlsplit(reference)
            if split.scheme or split.netloc:
                continue
            local_links += 1
            target = document if not split.path else (document.parent / unquote(split.path)).resolve()
            if target != site and site not in target.parents:
                failures.append(f"escapes site: {document.relative_to(site)} -> {reference}")
                continue
            if not target.is_file():
                failures.append(f"missing: {document.relative_to(site)} -> {reference}")
                continue
            if split.fragment and target.suffix == ".html":
                target_parser = documents.get(target)
                if target_parser is None:
                    target_parser = LinkParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    documents[target] = target_parser
                if split.fragment not in target_parser.ids:
                    failures.append(f"bad fragment: {document.relative_to(site)} -> {reference}")
    forbidden = ["tmp/", "manuscript/", "sources/", "projects/"]
    leaked = [path.relative_to(site).as_posix() for path in site.rglob("*") if path.is_file() and any(path.relative_to(site).as_posix().startswith(prefix) for prefix in forbidden)]
    if leaked:
        failures.extend(f"forbidden publication path: {path}" for path in leaked)
    manifest = json.loads((site / "PUBLICATION-MANIFEST.json").read_text(encoding="utf-8"))
    result = {
        "html_documents": len(documents),
        "local_links": local_links,
        "files": sum(1 for path in site.rglob("*") if path.is_file()),
        "bytes": sum(path.stat().st_size for path in site.rglob("*") if path.is_file()),
        "manifest_source_file_count": manifest.get("source_file_count"),
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
