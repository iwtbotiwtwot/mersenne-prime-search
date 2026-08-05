#!/usr/bin/env python3
"""Build deterministic, public-safe exports from completed MP-S10 runs.

Each supported source run has a frozen profile below. Adding SLCMP02--10
requires a new profile with independently checked source hashes and counts;
the reduction and privacy boundary remain shared.
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
CLASSIFICATION = "The test result suggests the concept is possible."
CAMPAIGN_ID = "SLC_MERSENNE_TEN_BAND_EXCAVATION_MP_S10_V1"
SOURCE_FIELDS = (
    "queue_id",
    "queue_rank",
    "shell_survivor_rank",
    "exponent",
    "mersenne_object",
    "screen_status",
    "shell_status",
    "screen_schedule_count",
    "shell_schedule_count",
    "shell_tested_opportunity_count",
    "external_status_at_snapshot",
    "assignment_snapshot_utc",
    "sam_distribution_status",
    "assignee",
    "assignment_utc",
    "result_status",
    "result_reference",
    "notes",
)
PUBLIC_FIELDS = (
    "candidate_id",
    "candidate_rank",
    "exponent",
    "mersenne_object",
    "public_state",
    "screen_status",
    "shell_status",
    "screen_schedule_count",
    "shell_schedule_count",
    "shell_tested_opportunity_count",
)

PROFILES: dict[str, dict[str, Any]] = {
    "SLCMP01": {
        "run_id": "MP-S10-R01",
        "run_number": 1,
        "interval": {"exclusive_lower": 143100000, "inclusive_upper": 143200000},
        "candidate_count": 1226,
        "first_exponent": 143100049,
        "last_exponent": 143198791,
        "files": {
            "RUN_CONTRACT.json": "475b23bec22371eeaf4a6e3afcebb053b24dd80a7309d42755bb3d03d3ed664e",
            "source/SOURCE_MANIFEST.json": "6c7cb0e4c427afa2a860bdf590879bdd64e3e6e96dead83eb2613d8bf829cd62",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "e6cb53e06c2b0b8092d2b816e6875630baf62980c61cda69c8b0490947dc93e6",
            "release/RUN_COMPLETE.json": "2656ec0339d250875ef24dbaa0c33d420b027ee6354c89fde520812153a8c634",
            "release/FINAL_VALIDATION.json": "44d595454b108f9e42603ab9db21425656c8188850a0618144a440b20e214a09",
            "release/FINAL_CANDIDATES.csv": "c9f48698796d2961b2aa24d689ace10e83e6124a9470b2c147a1715504f202ef",
            "release/RELEASE_MANIFEST.json": "5c894f61e782097796d638d4b262168df388b576c6ae8bf928aa7b90d84353b2",
        },
    },
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path.name}")
    return value


def write_object(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_equal(observed: Any, expected: Any, label: str) -> None:
    if observed != expected:
        raise ValueError(f"{label} mismatch: {observed!r} != {expected!r}")


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def validate_source(
    source_run: Path, export_id: str, profile: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, str]]]:
    for relative, expected in profile["files"].items():
        require_equal(file_sha256(source_run / relative), expected, f"{relative} SHA-256")

    contract = read_object(source_run / "RUN_CONTRACT.json")
    complete = read_object(source_run / "release/RUN_COMPLETE.json")
    validation = read_object(source_run / "release/FINAL_VALIDATION.json")
    release_manifest = read_object(source_run / "release/RELEASE_MANIFEST.json")

    for value, label in ((contract, "contract"), (complete, "completion")):
        require_equal(value.get("campaign_id"), CAMPAIGN_ID, f"{label} campaign")
        require_equal(value.get("run_id"), profile["run_id"], f"{label} run id")
    require_equal(contract.get("run_number"), profile["run_number"], "run number")
    require_equal(contract.get("interval"), profile["interval"], "contract interval")
    require_equal(complete.get("interval"), profile["interval"], "completion interval")
    require_equal(complete.get("status"), "PASS", "completion status")
    require_equal(validation.get("status"), "PASS", "validation status")
    require_equal(validation.get("check_count"), 33, "validation check count")
    require_equal(validation.get("passed_check_count"), 33, "passed check count")
    require_equal(
        validation.get("final_candidate_count"), profile["candidate_count"], "candidate count"
    )
    require_equal(release_manifest.get("status"), "FROZEN_COMPLETE", "release status")

    with (source_run / "release/FINAL_CANDIDATES.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        reader = csv.DictReader(handle)
        require_equal(tuple(reader.fieldnames or ()), SOURCE_FIELDS, "source CSV fields")
        rows = list(reader)
    require_equal(len(rows), profile["candidate_count"], "source roster count")

    seen: set[int] = set()
    for rank, row in enumerate(rows, start=1):
        exponent = int(row["exponent"])
        require_equal(int(row["queue_rank"]), rank, f"row {rank} queue rank")
        require_equal(row["queue_id"], f"MP-S10-R{profile['run_number']:02d}-{rank:04d}", f"row {rank} id")
        require_equal(row["mersenne_object"], f"2^{exponent}-1", f"row {rank} object")
        require_equal(row["sam_distribution_status"], "UNALLOCATED", f"row {rank} distribution")
        require_equal(
            row["external_status_at_snapshot"],
            "NO_RECORDED_FACTOR_PRP_OR_LL_RESULT_AND_NO_ACTIVE_GIMPS_ASSIGNMENT",
            f"row {rank} snapshot status",
        )
        for private_field in (
            "assignee", "assignment_utc", "result_status", "result_reference", "notes"
        ):
            require_equal(row[private_field], "", f"row {rank} {private_field}")
        if exponent in seen or not is_prime(exponent):
            raise ValueError(f"invalid or duplicate prime exponent: {exponent}")
        seen.add(exponent)
    require_equal(int(rows[0]["exponent"]), profile["first_exponent"], "first exponent")
    require_equal(int(rows[-1]["exponent"]), profile["last_exponent"], "last exponent")
    require_equal(complete["aggregate"]["final_active_candidate_count"], len(rows), "aggregate count")
    require_equal(complete["final_candidates_file_sha256"], profile["files"]["release/FINAL_CANDIDATES.csv"], "roster custody hash")
    return complete, validation, rows


def write_roster(path: Path, export_id: str, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PUBLIC_FIELDS, lineterminator="\n")
        writer.writeheader()
        for rank, row in enumerate(rows, start=1):
            writer.writerow(
                {
                    "candidate_id": f"{export_id}-{rank:04d}",
                    "candidate_rank": rank,
                    "exponent": row["exponent"],
                    "mersenne_object": row["mersenne_object"],
                    "public_state": "SEARCH_INPUT",
                    "screen_status": row["screen_status"],
                    "shell_status": row["shell_status"],
                    "screen_schedule_count": row["screen_schedule_count"],
                    "shell_schedule_count": row["shell_schedule_count"],
                    "shell_tested_opportunity_count": row["shell_tested_opportunity_count"],
                }
            )


def build_bundle(source_run: Path, export_id: str, output: Path) -> None:
    profile = PROFILES[export_id]
    complete, validation, rows = validate_source(source_run, export_id, profile)
    output.mkdir(parents=True, exist_ok=True)
    roster_path = output / "candidate_roster.csv"
    summary_path = output / "aggregate_summary.json"
    receipt_path = output / "source_receipt.json"
    readme_path = output / "README.md"
    manifest_path = output / "manifest.json"

    write_roster(roster_path, export_id, rows)
    summary = {
        "schema": "PUBLIC_SLCMP_RUN_SUMMARY_V1",
        "bundle_id": export_id,
        "post_run_name": export_id,
        "source_campaign": CAMPAIGN_ID,
        "source_run": profile["run_id"],
        "interval": profile["interval"],
        "completed_utc": complete["completed_utc"],
        "classification": CLASSIFICATION,
        "assigns_primality": False,
        "public_state": "SEARCH_INPUT",
        "aggregate": complete["aggregate"],
        "candidate_boundary": (
            "The 1,226 rows survived the completed local screens and the frozen status "
            "triage. They remain primality-unassigned search inputs."
        ),
    }
    write_object(summary_path, summary)
    receipt = {
        "schema": "PUBLIC_SLCMP_SOURCE_RECEIPT_V1",
        "bundle_id": export_id,
        "source_campaign": CAMPAIGN_ID,
        "source_run": profile["run_id"],
        "source_files": [
            {"object": relative, "sha256": digest}
            for relative, digest in profile["files"].items()
        ],
        "semantic_hashes": {
            key: complete[key]
            for key in (
                "run_contract_semantic_sha256",
                "source_manifest_semantic_sha256",
                "screen_result_semantic_sha256",
                "screen_validation_semantic_sha256",
                "official_snapshot_manifest_semantic_sha256",
                "triage_result_semantic_sha256",
                "final_validation_semantic_sha256",
                "run_complete_semantic_sha256",
            )
        },
        "independent_validation": {
            "status": validation["status"],
            "passed_check_count": validation["passed_check_count"],
            "check_count": validation["check_count"],
            "final_candidate_exponents_semantic_sha256": validation[
                "final_candidate_exponents_semantic_sha256"
            ],
        },
        "raw_external_responses_included": False,
        "private_assignment_metadata_included": False,
    }
    write_object(receipt_path, receipt)
    readme_path.write_text(
        f"""# {export_id} frozen candidate export

`{export_id}` is the public post-run name for completed MP-S10 Run 01 over
`143100000 < p <= 143200000`.

**{CLASSIFICATION}**

The source run screened 5,275 prime exponents, found 1,327 exact structural
factors, routed 2,165 further recorded-factor assignments, executed 17,107,885
deep-shell opportunities without another factor, and completed frozen status
triage to this 1,226-row candidate roster. Independent reconstruction passed
33/33 checks.

Every exported row is `SEARCH_INPUT` and remains primality-unassigned. This
bundle is not an external assignment, reservation, submission, Lucas--Lehmer
result, or new-prime claim. Raw external responses, usernames, assignees, local
paths, and private host metadata are not included.
""",
        encoding="utf-8",
    )

    exported = (readme_path, summary_path, roster_path, receipt_path)
    manifest = {
        "schema_version": "1.0.0",
        "bundle_id": export_id,
        "source_campaign": CAMPAIGN_ID,
        "source_revision": complete["run_complete_semantic_sha256"],
        "created_utc": complete["completed_utc"],
        "assigns_primality": False,
        "field_types": {
            "candidate_id": "candidate",
            "candidate_rank": "scheduler",
            "exponent": "candidate",
            "mersenne_object": "candidate",
            "public_state": "candidate",
            "screen_status": "diagnostic",
            "shell_status": "diagnostic",
            "screen_schedule_count": "scheduler",
            "shell_schedule_count": "scheduler",
            "shell_tested_opportunity_count": "diagnostic",
        },
        "files": [
            {"path": path.name, "sha256": file_sha256(path)} for path in exported
        ],
    }
    write_object(manifest_path, manifest)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-run", required=True, type=Path)
    parser.add_argument("--export-id", choices=sorted(PROFILES), default="SLCMP01")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output or ROOT / "exports" / args.export_id
    build_bundle(args.source_run.resolve(), args.export_id, output.resolve())
    print(f"wrote frozen export: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
