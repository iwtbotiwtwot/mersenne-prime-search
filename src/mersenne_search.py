#!/usr/bin/env python3
"""Exact Lucas–Lehmer baseline and compact receipt CLI."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import isqrt


@dataclass(frozen=True)
class LucasLehmerReceipt:
    """Exact result for one prime exponent."""

    algorithm: str
    exponent: int
    candidate_bits: int
    iterations: int
    final_residue: int
    is_mersenne_prime: bool


def is_prime_exponent(exponent: int) -> bool:
    """Return whether ``exponent`` is prime by exact trial division."""

    if exponent < 2:
        return False
    if exponent % 2 == 0:
        return exponent == 2
    for divisor in range(3, isqrt(exponent) + 1, 2):
        if exponent % divisor == 0:
            return False
    return True


def lucas_lehmer(exponent: int) -> LucasLehmerReceipt:
    """Run the exact Lucas–Lehmer test for a prime exponent.

    A composite exponent cannot produce a Mersenne prime, so it is rejected
    before the recurrence. Python integers preserve exact arithmetic.
    """

    if not is_prime_exponent(exponent):
        raise ValueError("the Lucas–Lehmer baseline requires a prime exponent >= 2")

    mersenne = (1 << exponent) - 1
    if exponent == 2:
        iterations = 0
        residue = 0
    else:
        iterations = exponent - 2
        residue = 4
        for _ in range(iterations):
            residue = (residue * residue - 2) % mersenne

    return LucasLehmerReceipt(
        algorithm="Lucas-Lehmer exact integer recurrence",
        exponent=exponent,
        candidate_bits=exponent,
        iterations=iterations,
        final_residue=residue,
        is_mersenne_prime=residue == 0,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the exact Lucas–Lehmer test for a prime exponent."
    )
    parser.add_argument("exponent", type=int, help="prime exponent p in 2^p - 1")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        receipt = lucas_lehmer(args.exponent)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(asdict(receipt), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
