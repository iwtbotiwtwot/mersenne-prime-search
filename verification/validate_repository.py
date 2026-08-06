#!/usr/bin/env python3
"""Small dependency-free structural validator for the public repository."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "STATUS.md",
    "LICENSE",
    "STEWARDSHIP_PLEDGE.md",
    "src/mersenne_search.py",
    "tests/test_lucas_lehmer.py",
    "research/00_BASELINE.md",
    "research/01_SAM_SLC_SEARCH_BRANCH.md",
    "interface/SLC_EXPORT_CONTRACT.md",
    "schemas/mersenne_export_manifest.schema.json",
)


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    schema_path = ROOT / "schemas/mersenne_export_manifest.schema.json"
    if schema_path.is_file():
        try:
            json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"invalid JSON schema: {error}")

    forbidden = ("/home/", "file://", "gho_", "github_pat_", "BEGIN OPENSSH")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in forbidden:
            if marker in text:
                failures.append(f"forbidden public marker {marker!r}: {path.relative_to(ROOT)}")
        for number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                failures.append(f"trailing whitespace: {path.relative_to(ROOT)}:{number}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("repository validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
