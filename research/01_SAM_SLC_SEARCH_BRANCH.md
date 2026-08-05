# SAM/SLC search branch

The SAM/SLC branch investigates whether substrate-derived computation can
contribute useful structure to Mersenne-prime search while preserving an exact
and independent primality decision.

## Permitted roles

An imported SLC bundle may provide:

- candidate exponent generation;
- deterministic candidate ordering or scheduling;
- exact feature or coordinate sidecars;
- reciprocal-history or directional-history annotations;
- resource-allocation hypotheses; and
- frozen receipts from a completed source campaign.

## Hard type boundary

The following objects are not primality decisions:

- a candidate score or rank;
- a scheduler choice;
- a prime-spacing coordinate;
- a prime-power channel receipt;
- an RH/Weil sidecar; or
- agreement with a completed curriculum.

Every candidate promoted from this lane returns to the exact Lucas–Lehmer
lane. A zero final residue is recorded as an exact candidate-test result; any
public discovery claim follows the separate replication sequence in
`docs/RESULT_POLICY.md`.

## Current source context

The source SAM repository records 13,818 ordinary-prime exponent sidecars and
13,972 prime-power channel receipts for a completed Mersenne curriculum. The
installation states that no model was fitted and no primality assignment was
made.

The first frozen public bundle is now installed at
[`exports/SAM_MP_S8_MP_S9_V1`](../exports/SAM_MP_S8_MP_S9_V1/README.md).
It carries the 1,858 unresolved MP-S8 exponent rows and the MP-S9
selection-1196 progress receipt. The bundle assigns no primality. Its candidate
fields, scheduler fields, and diagnostics remain separately typed.

## Initial research questions

1. Which additional completed SLC campaigns merit compact, reproducible
   public bundles?
2. Does an SLC ordering change time-to-candidate or work allocation against a
   declared baseline without changing the exact acceptance test?
3. Which reciprocal-history and directional-Weil fields should be applied
   retroactively to the Mersenne search surface?
4. Which production engine should consume the installed 1,858-row queue?
