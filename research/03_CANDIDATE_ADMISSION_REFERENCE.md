# Candidate admission and result stages

**Status:** research reference for owner rule-setting

This document separates the ordinary burden for admitting a Mersenne
candidate to computation from the later burden for publishing a positive
result. It does not change [`RESULT_POLICY.md`](../docs/RESULT_POLICY.md), add
a submission state, transmit an exponent, or announce a Mersenne prime.

## Four distinct stages

| Stage | Object | Minimum operational content |
|---|---|---|
| Candidate admission | Prime exponent proposed for factor, PRP, or Lucas--Lehmer work | Exact exponent, prime-exponent check, candidate identity, provenance, completed finite-screen receipts, and requested test |
| Production-test assignment | Candidate reserved or transmitted to a compute system | Candidate package plus assignment availability, accepted work type, execution capability, and result-return path |
| Positive computational result | Completed result presented for confirmation | Valid completed PRP probable-prime or Lucas--Lehmer zero result with algorithm and receipt custody |
| Confirmed discovery/public claim | Positive result presented as a new Mersenne prime | Independent reproduction and comparison with the current known-result record |

A candidate is admitted because its truth value remains open. Requiring the
result of the requested test before admission would erase the purpose of the
test.

## External workflow reference

The current GIMPS workflow starts from prime exponents, applies factor and
P-1 work, and then routes unresolved candidates to PRP or Lucas--Lehmer
testing. Its result table explicitly treats `NF`, `NF-PM1`, and `NF-ECM` as
no-factor states needing more testing. Assignment rules control resource and
return logistics. Independent verification occurs after an initial positive
result.

References:

- [GIMPS workflow](https://www.mersenne.org/various/works.php)
- [PrimeNet result types](https://www.mersenne.org/resulttypes/)
- [PrimeNet assignment rules](https://www.mersenne.org/thresholds/)
- [Independent verification example](https://www.mersenne.org/primes/?press=M82589933)

## Current SAM candidates

All 1,858 rows in the frozen MP-S8 export are:

- exact prime exponents;
- without an exact factor assignment in the completed exported screen;
- typed `SEARCH_INPUT` in the public roster; and
- explicitly not assigned prime or composite.

They therefore meet the mathematical candidate-admission burden for a
production queue. Actual external reservation still requires a current
availability and deduplication check.

Owner selection 1196 resolves to

$$
p=143{,}064{,}041,
\qquad
M_p=2^{143064041}-1.
$$

The candidate is submission-worthy for production testing under this staged
reference. Its public state is `LLT_IN_PROGRESS`: 110 of 143,064,039
Lucas--Lehmer iterations are preserved in the source progress receipt. No
terminal residue or primality assignment exists.

## Reserved owner decisions

The following remain outside this reference:

1. the repository label, if any, for submission to production testing;
2. which candidates are transmitted and in what order;
3. the receiving compute or assignment system;
4. required external-status fields;
5. credit, announcement, stewardship, and public-claim sequencing.

Those decisions require an explicit owner-approved policy update.
