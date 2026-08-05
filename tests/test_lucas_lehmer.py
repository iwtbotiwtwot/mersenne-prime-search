from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mersenne_search import is_prime_exponent, lucas_lehmer  # noqa: E402


class PrimeExponentTests(unittest.TestCase):
    def test_prime_exponents(self) -> None:
        for exponent in (2, 3, 5, 7, 13, 17, 19, 31):
            with self.subTest(exponent=exponent):
                self.assertTrue(is_prime_exponent(exponent))

    def test_nonprime_exponents(self) -> None:
        for exponent in (-1, 0, 1, 4, 9, 21, 25):
            with self.subTest(exponent=exponent):
                self.assertFalse(is_prime_exponent(exponent))


class LucasLehmerTests(unittest.TestCase):
    def test_known_mersenne_primes(self) -> None:
        for exponent in (2, 3, 5, 7, 13, 17, 19, 31):
            with self.subTest(exponent=exponent):
                receipt = lucas_lehmer(exponent)
                self.assertTrue(receipt.is_mersenne_prime)
                self.assertEqual(receipt.final_residue, 0)

    def test_known_composites_with_prime_exponents(self) -> None:
        for exponent in (11, 23, 29):
            with self.subTest(exponent=exponent):
                receipt = lucas_lehmer(exponent)
                self.assertFalse(receipt.is_mersenne_prime)
                self.assertNotEqual(receipt.final_residue, 0)

    def test_receipt_shape(self) -> None:
        receipt = lucas_lehmer(31)
        self.assertEqual(receipt.exponent, 31)
        self.assertEqual(receipt.candidate_bits, 31)
        self.assertEqual(receipt.iterations, 29)
        self.assertEqual(receipt.algorithm, "Lucas-Lehmer exact integer recurrence")

    def test_rejects_composite_exponent(self) -> None:
        with self.assertRaises(ValueError):
            lucas_lehmer(9)


if __name__ == "__main__":
    unittest.main()
