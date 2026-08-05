from __future__ import annotations

import csv
import hashlib
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "exports" / "SAM_MP_S8_MP_S9_V1"
SLCMP01_EXPORT = ROOT / "exports" / "SLCMP01"
SLCMP02_EXPORT = ROOT / "exports" / "SLCMP02"
SLCMP03_EXPORT = ROOT / "exports" / "SLCMP03"
SLCMP04_EXPORT = ROOT / "exports" / "SLCMP04"
SLCMP05_EXPORT = ROOT / "exports" / "SLCMP05"
SLCMP06_EXPORT = ROOT / "exports" / "SLCMP06"
sys.path.insert(0, str(ROOT / "src"))

from mersenne_search import is_prime_exponent  # noqa: E402


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


class PublicExportTests(unittest.TestCase):
    def test_manifest_hashes(self) -> None:
        manifest = json.loads((EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SAM_MP_S8_MP_S9_V1")
        for row in manifest["files"]:
            target = EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])

    def test_candidate_roster(self) -> None:
        with (EXPORT / "candidate_roster.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1858)
        self.assertEqual(len({row["exponent"] for row in rows}), 1858)
        self.assertEqual(int(rows[1195]["exponent"]), 143064041)
        for row in rows:
            with self.subTest(exponent=row["exponent"]):
                self.assertTrue(is_prime_exponent(int(row["exponent"])))
                self.assertEqual(row["public_state"], "SEARCH_INPUT")
                self.assertEqual(row["factor_q"], "")

    def test_owner_selection_is_in_progress(self) -> None:
        selection = json.loads(
            (EXPORT / "owner_selection_1196.json").read_text(encoding="utf-8")
        )
        self.assertFalse(selection["assigns_primality"])
        self.assertEqual(selection["public_state"], "LLT_IN_PROGRESS")
        self.assertEqual(selection["exponent"], 143064041)
        self.assertEqual(selection["completed_iterations"], 110)
        self.assertEqual(selection["terminal_iteration"], 143064039)
        self.assertIsNone(selection["terminal_residue_zero"])
        self.assertFalse(selection["checkpoint_binary_included"])

    def test_slcmp01_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP01_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP01")
        for row in manifest["files"]:
            target = SLCMP01_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP01_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["classification"], "The test result suggests the concept is possible.")
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 1226)
        with (SLCMP01_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1226)
        self.assertEqual(rows[0]["exponent"], "143100049")
        self.assertEqual(rows[-1]["exponent"], "143198791")
        self.assertEqual(len({row["exponent"] for row in rows}), 1226)
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")

    def test_slcmp02_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP02_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP02")
        for row in manifest["files"]:
            target = SLCMP02_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP02_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 1119)
        with (SLCMP02_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1119)
        self.assertEqual(rows[0]["exponent"], "143202223")
        self.assertEqual(rows[-1]["exponent"], "143299973")
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")

    def test_slcmp03_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP03_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP03")
        for row in manifest["files"]:
            target = SLCMP03_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP03_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 1225)
        with (SLCMP03_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1225)
        self.assertEqual(rows[0]["exponent"], "143300093")
        self.assertEqual(rows[-1]["exponent"], "143399819")
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")

    def test_slcmp04_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP04_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP04")
        for row in manifest["files"]:
            target = SLCMP04_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP04_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 1244)
        with (SLCMP04_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1244)
        self.assertEqual(rows[0]["exponent"], "143400077")
        self.assertEqual(rows[-1]["exponent"], "143499929")
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")

    def test_slcmp05_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP05_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP05")
        for row in manifest["files"]:
            target = SLCMP05_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP05_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 956)
        with (SLCMP05_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 956)
        self.assertEqual(rows[0]["exponent"], "143500003")
        self.assertEqual(rows[-1]["exponent"], "143597021")
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")

    def test_slcmp06_manifest_and_roster(self) -> None:
        manifest = json.loads((SLCMP06_EXPORT / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["assigns_primality"])
        self.assertEqual(manifest["bundle_id"], "SLCMP06")
        for row in manifest["files"]:
            target = SLCMP06_EXPORT / row["path"]
            self.assertTrue(target.is_file())
            self.assertEqual(file_sha256(target), row["sha256"])
        summary = json.loads((SLCMP06_EXPORT / "aggregate_summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["aggregate"]["final_active_candidate_count"], 780)
        with (SLCMP06_EXPORT / "candidate_roster.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 780)
        self.assertEqual(rows[0]["exponent"], "143607547")
        self.assertEqual(rows[-1]["exponent"], "143699191")
        for row in rows:
            self.assertTrue(is_prime_exponent(int(row["exponent"])))
            self.assertEqual(row["public_state"], "SEARCH_INPUT")


if __name__ == "__main__":
    unittest.main()
