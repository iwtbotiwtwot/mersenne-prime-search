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
    "SLCMP02": {
        "run_id": "MP-S10-R02",
        "run_number": 2,
        "interval": {"exclusive_lower": 143200000, "inclusive_upper": 143300000},
        "candidate_count": 1119,
        "first_exponent": 143202223,
        "last_exponent": 143299973,
        "files": {
            "RUN_CONTRACT.json": "9ffdaa73b8ca1d86c2ea0677f23d2ae92a2c3d573777edb89fccac4bdc27cb79",
            "source/SOURCE_MANIFEST.json": "fdf392cc69296a0a785126e86a607d5f479fee717af45a6ae5dfc667a0e326c7",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "62e6bd1475771357eb524a442d496ae105a8c15000bfa08368e4fdab80e61e4b",
            "release/RUN_COMPLETE.json": "76299a5c856f9c9f71189cbd8ccb75768d5546d7e51782abd255989744ab3c70",
            "release/FINAL_VALIDATION.json": "43918b80a7fe1588bd0c64f745800180354cb1259c3645da21a38fd9f1785cf2",
            "release/FINAL_CANDIDATES.csv": "5e14ef740fb6b072cf5f530ca15b635fec568f4c79c8ffb2415629831362ac26",
            "release/RELEASE_MANIFEST.json": "c7bc38f936117c123c225b279f0fa8a10a22a37f4da27791bb39244f6f8a5eba",
        },
    },
    "SLCMP03": {
        "run_id": "MP-S10-R03",
        "run_number": 3,
        "interval": {"exclusive_lower": 143300000, "inclusive_upper": 143400000},
        "candidate_count": 1225,
        "first_exponent": 143300093,
        "last_exponent": 143399819,
        "files": {
            "RUN_CONTRACT.json": "a2ce173f3fb5aeb8bc2347f28b24071c71378ffaa0ef5ab96c2b318fcb04f563",
            "source/SOURCE_MANIFEST.json": "43f0fdf127e92b79394fa6ba4237653e676b033580a04baf7693429e363fb6f3",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "06ab9249f89c4b650a497699ed8cf8d0739850bb50b05be13c1db40b35a3cba1",
            "release/RUN_COMPLETE.json": "9115231c59e038376ef4c00bd96420b01ffb73589bc1f8cb8807debd5f514228",
            "release/FINAL_VALIDATION.json": "a6935a1810d58707fe0729d92a68cddb518665aaae004030aec6b99bd620bead",
            "release/FINAL_CANDIDATES.csv": "b53e516400ed8414100038e490a4ac06262cd2e69acfae2db98e55d50d1caf0d",
            "release/RELEASE_MANIFEST.json": "b157cae5203c745f306df5e8cb650033b748cefaab6436ba12088f3db2e18d81",
        },
    },
    "SLCMP04": {
        "run_id": "MP-S10-R04",
        "run_number": 4,
        "interval": {"exclusive_lower": 143400000, "inclusive_upper": 143500000},
        "candidate_count": 1244,
        "first_exponent": 143400077,
        "last_exponent": 143499929,
        "files": {
            "RUN_CONTRACT.json": "75b04e3ed350b43029cc3855ec44902a061beadb215edf5ce8d4cc3d0e48762d",
            "source/SOURCE_MANIFEST.json": "1ca85c58a92b0ac335281d77917ebb7f34903e4c6f89f112c5afb4fc57a3489d",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "59647a274553c1b811dcd6ac412e5d878c9036e2b2165830d67b9569e706afea",
            "release/RUN_COMPLETE.json": "a9bab91091b9c5b0affa2fe4bd5ea91057efff65125764b85e6cf16c99889276",
            "release/FINAL_VALIDATION.json": "bf5807f02e112b7118d241ec1652dfb9c2632225f1fe91518a72d274bf4ea466",
            "release/FINAL_CANDIDATES.csv": "a451671fd0134ca21f275c0876af5fce80379dd5f7874cd9687e3decd314a57b",
            "release/RELEASE_MANIFEST.json": "148b2b0af48c6f668f4277c6dbdb9fada4955273ba368a5d41e4b6e9225224d9",
        },
    },
    "SLCMP05": {
        "run_id": "MP-S10-R05",
        "run_number": 5,
        "interval": {"exclusive_lower": 143500000, "inclusive_upper": 143600000},
        "candidate_count": 956,
        "first_exponent": 143500003,
        "last_exponent": 143597021,
        "files": {
            "RUN_CONTRACT.json": "e9b1b51815436701319e719174064881072d2a79ac5c0d0eabca447d5aa7705e",
            "source/SOURCE_MANIFEST.json": "52f1d4527c138129e2ad963c6dd50d4f19f8158cfb4a284c50b7e2e6be887b31",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "05b7e26a10211cb491bdbb9b5fbbfe4f3ae48c59a613d7fbfc626108ef70851d",
            "release/RUN_COMPLETE.json": "70e22ec8a1eb23a16a9a6f05a69dd26eea45d013cd32045ac2623eb4f4436b61",
            "release/FINAL_VALIDATION.json": "d53f6fc695af356843a18c0637584be9aa4950b70864f61cf4fb4b04057b90ac",
            "release/FINAL_CANDIDATES.csv": "d030b8824b32fdf51a86488ef30cb8d0eeddc78789c6ec960011805f0008e190",
            "release/RELEASE_MANIFEST.json": "b01b364608f6adcbe82ca4360e989368938aa185482082b684988a338ebcee83",
        },
    },
    "SLCMP06": {
        "run_id": "MP-S10-R06",
        "run_number": 6,
        "interval": {"exclusive_lower": 143600000, "inclusive_upper": 143700000},
        "candidate_count": 780,
        "first_exponent": 143607547,
        "last_exponent": 143699191,
        "files": {
            "RUN_CONTRACT.json": "094b80f0c5c07560efe4003d9c05b11c17abbbd79ada5e65451a9f6a3d817068",
            "source/SOURCE_MANIFEST.json": "dd1e3478dbc88ec95a969d0ca36754dbca266b776744eb31b9479cb039080d56",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "69de08fe4caf15738c0806d0fec90a4e6af07cd14138f6170552996bcc400daf",
            "release/RUN_COMPLETE.json": "0c0103fd7fc5cd1d7d3c173bece13254313f7b34cc64f660f490fec9a3976de3",
            "release/FINAL_VALIDATION.json": "8b886f8311d9868e281a77b92f97aee86e77eab0259a525269152f867c9fb9ad",
            "release/FINAL_CANDIDATES.csv": "6514fbca64bd38fde1715d04a616db1b79ce843b58ad534eedb767dfbf7f3e01",
            "release/RELEASE_MANIFEST.json": "5d48eb36664a3b2c151b76383751a30e5b2212f24f92360c1248642ebc62f776",
        },
    },
    "SLCMP07": {
        "run_id": "MP-S10-R07",
        "run_number": 7,
        "interval": {"exclusive_lower": 143700000, "inclusive_upper": 143800000},
        "candidate_count": 1360,
        "first_exponent": 143700239,
        "last_exponent": 143799949,
        "files": {
            "RUN_CONTRACT.json": "ee38d55d8d4e46a2b274c7c66baa2e585f703277ace2fbe99c2113a8cbc4766d",
            "source/SOURCE_MANIFEST.json": "42f12e6ae3cbdf3dbdec0a8fd2b1eb0c0dc61526731200e60e7e3ac6239fb1f2",
            "source/OFFICIAL_SNAPSHOT_MANIFEST.json": "ef543c68dbd9fdadf445547877292104a073beb9a402db905f673dd561901b73",
            "release/RUN_COMPLETE.json": "b627f7f91ef906437cf7876ab569333d3aae085693a4f2aa5dcde4ce46d31681",
            "release/FINAL_VALIDATION.json": "2a0f7d8c4e11b88d91916638180af3cc0f54ab025e1acef20be0356548e27930",
            "release/FINAL_CANDIDATES.csv": "ab3d7baad93e267aa21408802ec2fd3dbdc62b8bd7ee6ca183d97fac9a95405b",
            "release/RELEASE_MANIFEST.json": "a75a39358bbd24955992f499556fb4af82bb9300550b68cb46fab9a1e16b6a3e",
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
            f"The {profile['candidate_count']:,} rows survived the completed local screens and the frozen status "
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

`{export_id}` is the public post-run name for completed {profile['run_id']} over
`{profile['interval']['exclusive_lower']} < p <= {profile['interval']['inclusive_upper']}`.

**{CLASSIFICATION}**

The source run screened {complete['aggregate']['prime_exponent_count']:,} prime exponents, found
{complete['aggregate']['screen_factor_count']:,} exact structural factors, routed
{complete['aggregate']['official_factor_elimination_count']:,} further recorded-factor assignments,
executed {complete['aggregate']['shell_tested_opportunity_count']:,} deep-shell opportunities,
and completed frozen status triage to this {profile['candidate_count']:,}-row candidate roster.
Independent reconstruction passed 33/33 checks.

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
