#!/usr/bin/env python3
"""Build the frozen public SAM MP-S8/MP-S9 export bundle.

The source repository remains outside this public checkout. Inputs are passed
explicitly, verified against the frozen source hashes, reduced to allowlisted
fields, and written without private paths or host metadata.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "exports" / "SAM_MP_S8_MP_S9_V1"
BUNDLE_ID = "SAM_MP_S8_MP_S9_V1"
EXPECTED_S8_SHA256 = "6def5e390613c19eef5156f86f1d7fc2e5d2d409e41a76b7191cdbb12649ba5a"
EXPECTED_S8_SEMANTIC_SHA256 = (
    "d88ca1f1246d5af0cce164f89afd89b5fb6642d7da2fe5b9d5b40bf50b0c485c"
)
EXPECTED_S9_SHA256 = "187dd2b45dd696085b860c1abcea19ccf8a52bf1ec430d3f76fc65095211413f"
EXPECTED_S9_SEMANTIC_SHA256 = (
    "6ca3190ff30f67b83fc114761472192436373974e195ded1e63ff2fe0b20e4e4"
)
EXPECTED_AGGREGATE = {
    "base2_prp_survivor_count": 654344,
    "canonical_base_object_count": 200,
    "deduplicated_shell_k_count": 10122,
    "echo_depth_max": 127,
    "echo_depth_min": 0,
    "exact_factor_assignment_count": 0,
    "first_unresolved_exponent": 143000029,
    "input_exponent_count": 1858,
    "primality_unassigned_count": 1858,
    "q_max_bits": 168,
    "q_min_bits": 40,
    "scheduled_k_count_p_mod_4_1": 9595,
    "scheduled_k_count_p_mod_4_3": 9595,
    "small_sieve_survivor_count": 4017974,
    "tested_opportunity_count": 17827510,
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def require_equal(observed: Any, expected: Any, label: str) -> None:
    if observed != expected:
        raise ValueError(f"{label} mismatch: {observed!r} != {expected!r}")


def validate_sources(
    s8_path: Path,
    s8: dict[str, Any],
    s9_path: Path,
    s9: dict[str, Any],
) -> list[dict[str, Any]]:
    require_equal(file_sha256(s8_path), EXPECTED_S8_SHA256, "MP-S8 file SHA-256")
    require_equal(file_sha256(s9_path), EXPECTED_S9_SHA256, "MP-S9 file SHA-256")
    require_equal(
        s8.get("campaign_id"),
        "SLC_MERSENNE_RH_FIRST_SINGULARITY_SHELL_MP_S8_V1",
        "MP-S8 campaign",
    )
    require_equal(
        s8.get("result_semantic_sha256"),
        EXPECTED_S8_SEMANTIC_SHA256,
        "MP-S8 semantic SHA-256",
    )
    require_equal(s8.get("aggregate"), EXPECTED_AGGREGATE, "MP-S8 aggregate")
    require_equal(
        s9.get("campaign_id"),
        "SLC_MERSENNE_LUCAS_LEHMER_MP_S9_V1",
        "MP-S9 campaign",
    )
    require_equal(
        s9.get("progress_semantic_sha256"),
        EXPECTED_S9_SEMANTIC_SHA256,
        "MP-S9 semantic SHA-256",
    )
    require_equal(s9.get("status"), "CHECKPOINTED_IN_PROGRESS", "MP-S9 status")
    require_equal(
        s9.get("assignment"),
        "PRIMALITY_UNASSIGNED_TEST_IN_PROGRESS",
        "MP-S9 assignment",
    )
    require_equal(s9.get("selection_index_1_based"), 1196, "owner selection")
    require_equal(s9.get("exponent"), 143064041, "owner-selected exponent")
    require_equal(s9.get("completed_iterations"), 110, "MP-S9 progress")
    require_equal(s9.get("terminal_iteration"), 143064039, "MP-S9 terminal")
    require_equal(s9.get("terminal_residue_zero"), None, "MP-S9 terminal residue")

    records = s8.get("records")
    if not isinstance(records, list):
        raise ValueError("MP-S8 records must be a list")
    require_equal(len(records), 1858, "MP-S8 record count")

    exponents: set[int] = set()
    for index, row in enumerate(records, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"MP-S8 row {index} is not an object")
        exponent = int(row["exponent"])
        if exponent in exponents:
            raise ValueError(f"duplicate MP-S8 exponent: {exponent}")
        if not is_prime(exponent):
            raise ValueError(f"nonprime MP-S8 exponent: {exponent}")
        exponents.add(exponent)
        require_equal(row.get("factor_q"), "", f"MP-S8 row {index} factor")
        require_equal(
            row.get("status"),
            "RADIX2_FIRST_SINGULARITY_SHELL_EXHAUSTED_PRIMALITY_UNASSIGNED",
            f"MP-S8 row {index} status",
        )

    require_equal(records[1195]["exponent"], 143064041, "selection 1196 mapping")
    return records


def write_roster(path: Path, records: list[dict[str, Any]]) -> None:
    fieldnames = (
        "selection_index_1_based",
        "exponent",
        "public_state",
        "source_status",
        "scheduled_shell_count",
        "tested_opportunity_count",
        "small_sieve_survivor_count",
        "base2_prp_survivor_count",
        "factor_q",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for index, row in enumerate(records, start=1):
            writer.writerow(
                {
                    "selection_index_1_based": index,
                    "exponent": row["exponent"],
                    "public_state": "SEARCH_INPUT",
                    "source_status": row["status"],
                    "scheduled_shell_count": row["scheduled_shell_count"],
                    "tested_opportunity_count": row["tested_opportunity_count"],
                    "small_sieve_survivor_count": row["small_sieve_survivor_count"],
                    "base2_prp_survivor_count": row["base2_prp_survivor_count"],
                    "factor_q": row["factor_q"],
                }
            )


def build_bundle(
    s8_path: Path,
    s9_path: Path,
    output: Path,
    created_utc: str,
) -> None:
    if not created_utc.endswith("Z") or "T" not in created_utc:
        raise ValueError("--created-utc must be an RFC 3339 UTC value ending in Z")

    s8 = read_json(s8_path)
    s9 = read_json(s9_path)
    records = validate_sources(s8_path, s8, s9_path, s9)
    output.mkdir(parents=True, exist_ok=True)

    summary_path = output / "campaign_summary.json"
    roster_path = output / "candidate_roster.csv"
    selection_path = output / "owner_selection_1196.json"
    readme_path = output / "README.md"
    manifest_path = output / "manifest.json"

    summary = {
        "schema": "PUBLIC_SAM_MP_S8_SUMMARY_V1",
        "bundle_id": BUNDLE_ID,
        "assigns_primality": False,
        "public_state": "SEARCH_INPUT",
        "source_campaign": s8["campaign_id"],
        "source_file_sha256": EXPECTED_S8_SHA256,
        "source_semantic_sha256": EXPECTED_S8_SEMANTIC_SHA256,
        "aggregate": s8["aggregate"],
        "exact_bridge": s8["exact_bridge"],
        "determination": (
            "Exact factors assign compositeness. Every no-factor row remains "
            "primality-unassigned and proceeds to an exact candidate test."
        ),
    }
    write_json(summary_path, summary)
    write_roster(roster_path, records)

    checkpoint = dict(s9["checkpoint"])
    selection = {
        "schema": "PUBLIC_SAM_MP_S9_PROGRESS_V1",
        "bundle_id": BUNDLE_ID,
        "assigns_primality": False,
        "public_state": "LLT_IN_PROGRESS",
        "selection_index_1_based": 1196,
        "exponent": 143064041,
        "mersenne_object": "2^143064041-1",
        "source_campaign": s9["campaign_id"],
        "source_file_sha256": EXPECTED_S9_SHA256,
        "source_semantic_sha256": EXPECTED_S9_SEMANTIC_SHA256,
        "completed_iterations": s9["completed_iterations"],
        "terminal_iteration": s9["terminal_iteration"],
        "terminal_residue_zero": None,
        "source_assignment": s9["assignment"],
        "engine": s9["engine"],
        "self_tests": s9["self_tests"],
        "checkpoint_receipt": checkpoint,
        "checkpoint_binary_included": False,
        "checkpoint_boundary": (
            "The public bundle preserves the exact checkpoint hashes and "
            "progress receipt, but not the 17,883,276-byte binary state."
        ),
    }
    write_json(selection_path, selection)

    readme_path.write_text(
        """# Frozen SAM MP-S8 / MP-S9 export

This allowlisted bundle installs the 1,858 prime-exponent rows that remained
primality-unassigned after the completed MP-S8 radix-2 first-singularity shell.
The source campaign executed 17,827,510 shell opportunities and assigned zero
new factors.

Owner selection 1196 resolves to exponent 143064041. Its exact Lucas--Lehmer
test is checkpointed after 110 of 143,064,039 iterations and is represented by
the public state `LLT_IN_PROGRESS`.

The bundle assigns no primality. The candidate roster, scheduler fields, and
checkpoint diagnostics cannot replace a completed exact residue. The binary
checkpoint is not included; its file and state hashes remain in the progress
receipt for custody.
""",
        encoding="utf-8",
    )

    exported = (readme_path, summary_path, roster_path, selection_path)
    manifest = {
        "schema_version": "1.0.0",
        "bundle_id": BUNDLE_ID,
        "source_campaign": (
            "SLC_MERSENNE_RH_FIRST_SINGULARITY_SHELL_MP_S8_V1 + "
            "SLC_MERSENNE_LUCAS_LEHMER_MP_S9_V1"
        ),
        "source_revision": (
            f"MP-S8:{EXPECTED_S8_SEMANTIC_SHA256};"
            f"MP-S9:{EXPECTED_S9_SEMANTIC_SHA256}"
        ),
        "created_utc": created_utc,
        "assigns_primality": False,
        "field_types": {
            "exponent": "candidate",
            "public_state": "candidate",
            "source_status": "diagnostic",
            "scheduled_shell_count": "scheduler",
            "tested_opportunity_count": "scheduler",
            "small_sieve_survivor_count": "diagnostic",
            "base2_prp_survivor_count": "diagnostic",
            "checkpoint_receipt": "diagnostic",
        },
        "files": [
            {
                "path": path.name,
                "sha256": file_sha256(path),
            }
            for path in exported
        ],
    }
    write_json(manifest_path, manifest)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mp-s8-result", required=True, type=Path)
    parser.add_argument("--mp-s9-progress", required=True, type=Path)
    parser.add_argument("--created-utc", required=True)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    build_bundle(
        args.mp_s8_result.resolve(),
        args.mp_s9_progress.resolve(),
        args.output.resolve(),
        args.created_utc,
    )
    print(f"wrote frozen export: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
