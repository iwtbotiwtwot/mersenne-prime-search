#!/usr/bin/env python3
"""Build the complete public candidate CSV from number-only SLCMP exports."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidates"
OUTPUT = CANDIDATES / "ALL_CANDIDATES.csv"
NAME = re.compile(r"SLCMP(\d+)\.csv")


def roster_key(path: Path) -> int:
    match = NAME.fullmatch(path.name)
    if match is None:
        raise ValueError(f"unexpected roster name: {path.name}")
    return int(match.group(1))


def main() -> None:
    sources = sorted(
        (path for path in CANDIDATES.glob("SLCMP*.csv") if NAME.fullmatch(path.name)),
        key=roster_key,
    )
    if any(roster_key(path) == 10 for path in sources):
        raise RuntimeError("SLCMP10 is outside the public export boundary")
    if not sources:
        raise RuntimeError("no public SLCMP rosters found")

    rows: list[tuple[int, str]] = []
    seen: set[int] = set()
    for source in sources:
        for line_number, text in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            value = text.strip()
            if not value:
                continue
            try:
                exponent = int(value)
            except ValueError as error:
                raise RuntimeError(f"{source.name}:{line_number}: expected one integer") from error
            if exponent in seen:
                raise RuntimeError(f"duplicate exponent {exponent} in {source.name}")
            seen.add(exponent)
            rows.append((exponent, source.stem))

    rows.sort()
    temporary = OUTPUT.with_suffix(".csv.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("exponent", "source_export"))
        writer.writerows(rows)
    temporary.replace(OUTPUT)
    print(f"PASS: {len(rows):,} unique candidates from {len(sources)} public exports")


if __name__ == "__main__":
    main()
