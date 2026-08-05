#!/usr/bin/env python3
"""Small dependency-free structural validator for the public repository."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from math import isqrt
from pathlib import Path
from typing import Any


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
    "research/02_SAM_MERSENNE_LINEAGE.md",
    "research/03_CANDIDATE_ADMISSION_REFERENCE.md",
    "interface/SLC_EXPORT_CONTRACT.md",
    "schemas/mersenne_export_manifest.schema.json",
    "tools/build_sam_mp_s8_export.py",
    "tools/build_slcmp_export.py",
    "exports/SAM_MP_S8_MP_S9_V1/README.md",
    "exports/SAM_MP_S8_MP_S9_V1/manifest.json",
    "exports/SAM_MP_S8_MP_S9_V1/campaign_summary.json",
    "exports/SAM_MP_S8_MP_S9_V1/candidate_roster.csv",
    "exports/SAM_MP_S8_MP_S9_V1/owner_selection_1196.json",
    "exports/SLCMP01/README.md",
    "exports/SLCMP01/manifest.json",
    "exports/SLCMP01/aggregate_summary.json",
    "exports/SLCMP01/candidate_roster.csv",
    "exports/SLCMP01/source_receipt.json",
    "exports/SLCMP02/README.md",
    "exports/SLCMP02/manifest.json",
    "exports/SLCMP02/aggregate_summary.json",
    "exports/SLCMP02/candidate_roster.csv",
    "exports/SLCMP02/source_receipt.json",
    "exports/SLCMP03/README.md",
    "exports/SLCMP03/manifest.json",
    "exports/SLCMP03/aggregate_summary.json",
    "exports/SLCMP03/candidate_roster.csv",
    "exports/SLCMP03/source_receipt.json",
    "exports/SLCMP04/README.md",
    "exports/SLCMP04/manifest.json",
    "exports/SLCMP04/aggregate_summary.json",
    "exports/SLCMP04/candidate_roster.csv",
    "exports/SLCMP04/source_receipt.json",
    "exports/SLCMP05/README.md",
    "exports/SLCMP05/manifest.json",
    "exports/SLCMP05/aggregate_summary.json",
    "exports/SLCMP05/candidate_roster.csv",
    "exports/SLCMP05/source_receipt.json",
    "exports/SLCMP06/README.md",
    "exports/SLCMP06/manifest.json",
    "exports/SLCMP06/aggregate_summary.json",
    "exports/SLCMP06/candidate_roster.csv",
    "exports/SLCMP06/source_receipt.json",
    "exports/SLCMP07/README.md",
    "exports/SLCMP07/manifest.json",
    "exports/SLCMP07/aggregate_summary.json",
    "exports/SLCMP07/candidate_roster.csv",
    "exports/SLCMP07/source_receipt.json",
    "exports/SLCMP08/README.md",
    "exports/SLCMP08/manifest.json",
    "exports/SLCMP08/aggregate_summary.json",
    "exports/SLCMP08/candidate_roster.csv",
    "exports/SLCMP08/source_receipt.json",
)
EXPORT = ROOT / "exports" / "SAM_MP_S8_MP_S9_V1"
SLCMP01_EXPORT = ROOT / "exports" / "SLCMP01"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def validate_export() -> list[str]:
    failures: list[str] = []
    manifest_path = EXPORT / "manifest.json"
    if not manifest_path.is_file():
        return ["missing frozen export manifest"]

    try:
        manifest = read_object(manifest_path)
    except (json.JSONDecodeError, ValueError) as error:
        return [f"invalid frozen export manifest: {error}"]

    required = {
        "schema_version",
        "bundle_id",
        "source_campaign",
        "created_utc",
        "assigns_primality",
        "files",
    }
    allowed = required | {"source_revision", "field_types"}
    missing = required - manifest.keys()
    extra = manifest.keys() - allowed
    if missing:
        failures.append(f"export manifest missing fields: {sorted(missing)}")
    if extra:
        failures.append(f"export manifest has extra fields: {sorted(extra)}")
    if manifest.get("schema_version") != "1.0.0":
        failures.append("export manifest schema version mismatch")
    if manifest.get("bundle_id") != "SAM_MP_S8_MP_S9_V1":
        failures.append("export bundle id mismatch")
    if manifest.get("assigns_primality") is not False:
        failures.append("export manifest must assign no primality")
    if not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
        str(manifest.get("created_utc", "")),
    ):
        failures.append("export created_utc is not canonical UTC")

    field_types = manifest.get("field_types", {})
    if not isinstance(field_types, dict) or any(
        value not in {"candidate", "scheduler", "diagnostic"}
        for value in field_types.values()
    ):
        failures.append("export field types are invalid")

    expected_files = {
        "README.md",
        "campaign_summary.json",
        "candidate_roster.csv",
        "owner_selection_1196.json",
    }
    listed_files: set[str] = set()
    file_rows = manifest.get("files", [])
    if not isinstance(file_rows, list) or not file_rows:
        failures.append("export manifest files must be a nonempty list")
        file_rows = []
    for row in file_rows:
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            failures.append(f"invalid export file row: {row!r}")
            continue
        relative = Path(str(row["path"]))
        digest = str(row["sha256"])
        if relative.is_absolute() or ".." in relative.parts:
            failures.append(f"unsafe export path: {relative}")
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            failures.append(f"invalid export SHA-256: {relative}")
            continue
        listed_files.add(relative.as_posix())
        target = EXPORT / relative
        if not target.is_file():
            failures.append(f"missing exported file: {relative}")
        elif file_sha256(target) != digest:
            failures.append(f"exported file hash mismatch: {relative}")
    if listed_files != expected_files:
        failures.append(
            f"export allowlist mismatch: {sorted(listed_files)} != "
            f"{sorted(expected_files)}"
        )

    try:
        summary = read_object(EXPORT / "campaign_summary.json")
        if summary.get("assigns_primality") is not False:
            failures.append("campaign summary assigns primality")
        if summary.get("public_state") != "SEARCH_INPUT":
            failures.append("campaign summary public state mismatch")
        aggregate = summary["aggregate"]
        expected_aggregate = {
            "input_exponent_count": 1858,
            "primality_unassigned_count": 1858,
            "exact_factor_assignment_count": 0,
            "tested_opportunity_count": 17827510,
            "small_sieve_survivor_count": 4017974,
            "base2_prp_survivor_count": 654344,
            "deduplicated_shell_k_count": 10122,
            "q_min_bits": 40,
            "q_max_bits": 168,
        }
        for key, expected in expected_aggregate.items():
            if aggregate.get(key) != expected:
                failures.append(f"campaign aggregate mismatch: {key}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        failures.append(f"invalid campaign summary: {error}")

    try:
        selection = read_object(EXPORT / "owner_selection_1196.json")
        expected_selection = {
            "assigns_primality": False,
            "public_state": "LLT_IN_PROGRESS",
            "selection_index_1_based": 1196,
            "exponent": 143064041,
            "completed_iterations": 110,
            "terminal_iteration": 143064039,
            "terminal_residue_zero": None,
            "checkpoint_binary_included": False,
        }
        for key, expected in expected_selection.items():
            if selection.get(key) != expected:
                failures.append(f"owner selection mismatch: {key}")
        if selection.get("source_assignment") != (
            "PRIMALITY_UNASSIGNED_TEST_IN_PROGRESS"
        ):
            failures.append("owner selection source assignment mismatch")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        failures.append(f"invalid owner selection receipt: {error}")

    try:
        with (EXPORT / "candidate_roster.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 1858:
            failures.append(f"candidate roster count mismatch: {len(rows)}")
        seen: set[int] = set()
        scheduled_total = 0
        tested_total = 0
        small_sieve_total = 0
        base2_prp_total = 0
        for index, row in enumerate(rows, start=1):
            exponent = int(row["exponent"])
            if int(row["selection_index_1_based"]) != index:
                failures.append(f"candidate index mismatch at row {index}")
            if exponent in seen or not is_prime(exponent):
                failures.append(f"invalid candidate exponent: {exponent}")
            seen.add(exponent)
            if row["public_state"] != "SEARCH_INPUT":
                failures.append(f"candidate state mismatch: {exponent}")
            if row["factor_q"]:
                failures.append(f"candidate unexpectedly has factor: {exponent}")
            scheduled_total += int(row["scheduled_shell_count"])
            tested_total += int(row["tested_opportunity_count"])
            small_sieve_total += int(row["small_sieve_survivor_count"])
            base2_prp_total += int(row["base2_prp_survivor_count"])
        if rows and int(rows[1195]["exponent"]) != 143064041:
            failures.append("selection 1196 roster mapping mismatch")
        expected_totals = {
            "scheduled": (scheduled_total, 17827510),
            "tested": (tested_total, 17827510),
            "small_sieve": (small_sieve_total, 4017974),
            "base2_prp": (base2_prp_total, 654344),
        }
        for label, (observed, expected) in expected_totals.items():
            if observed != expected:
                failures.append(f"candidate roster {label} total mismatch")
    except (OSError, KeyError, ValueError) as error:
        failures.append(f"invalid candidate roster: {error}")

    return failures


def validate_slcmp_export(export_id: str, candidate_count: int, first_exponent: str, last_exponent: str) -> list[str]:
    failures: list[str] = []
    export = ROOT / "exports" / export_id
    manifest_path = export / "manifest.json"
    if not manifest_path.is_file():
        return [f"missing {export_id} export manifest"]
    try:
        manifest = read_object(manifest_path)
        if manifest.get("bundle_id") != export_id:
            failures.append(f"{export_id} bundle id mismatch")
        if manifest.get("assigns_primality") is not False:
            failures.append(f"{export_id} assigns primality")
        listed = {row["path"]: row["sha256"] for row in manifest["files"]}
        expected = {"README.md", "aggregate_summary.json", "candidate_roster.csv", "source_receipt.json"}
        if set(listed) != expected:
            failures.append(f"{export_id} export allowlist mismatch")
        for relative, digest in listed.items():
            target = export / relative
            if not target.is_file() or file_sha256(target) != digest:
                failures.append(f"{export_id} file hash mismatch: {relative}")
        summary = read_object(export / "aggregate_summary.json")
        if summary.get("classification") != "The test result suggests the concept is possible.":
            failures.append(f"{export_id} classification mismatch")
        if summary.get("aggregate", {}).get("final_active_candidate_count") != candidate_count:
            failures.append(f"{export_id} candidate aggregate mismatch")
        receipt = read_object(export / "source_receipt.json")
        if receipt.get("independent_validation", {}).get("passed_check_count") != 33:
            failures.append(f"{export_id} independent validation mismatch")
        with (export / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != candidate_count:
            failures.append(f"{export_id} candidate roster count mismatch: {len(rows)}")
        seen: set[int] = set()
        for rank, row in enumerate(rows, start=1):
            exponent = int(row["exponent"])
            if int(row["candidate_rank"]) != rank or exponent in seen or not is_prime(exponent):
                failures.append(f"{export_id} invalid candidate row: {rank}")
            if row["public_state"] != "SEARCH_INPUT":
                failures.append(f"{export_id} state mismatch: {exponent}")
            seen.add(exponent)
        if rows and rows[0]["exponent"] != first_exponent:
            failures.append(f"{export_id} first exponent mismatch")
        if rows and rows[-1]["exponent"] != last_exponent:
            failures.append(f"{export_id} last exponent mismatch")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        failures.append(f"invalid {export_id} export: {error}")
    return failures


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

    failures.extend(validate_export())
    failures.extend(validate_slcmp_export("SLCMP01", 1226, "143100049", "143198791"))
    failures.extend(validate_slcmp_export("SLCMP02", 1119, "143202223", "143299973"))

    forbidden = ("/home/", "file://", "gho_", "github_pat_", "BEGIN OPENSSH")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {
            ".cff",
            ".csv",
            ".json",
            ".md",
            ".py",
            ".yaml",
            ".yml",
        }:
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
