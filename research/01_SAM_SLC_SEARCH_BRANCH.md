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
made. No source bundle has yet been exported into this public repository.

## Initial research questions

1. Can the existing SLC curriculum be exported as a compact, reproducible,
   non-private manifest?
2. Which fields are candidate-selection inputs, and which are diagnostic
   sidecars only?
3. Does an SLC ordering change time-to-candidate or work allocation against a
   declared baseline without changing the exact acceptance test?
4. Which reciprocal-history and directional-Weil fields should be applied
   retroactively to the Mersenne search surface?
