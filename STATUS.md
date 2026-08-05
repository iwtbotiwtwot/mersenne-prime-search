# Status

**Repository state:** `RESEARCH_EXPORT_V0.2.0`

**Exact baseline:** `LUCAS_LEHMER_INSTALLED`

**SAM/SLC interface:** `FROZEN_EXPORT_SAM_MP_S8_MP_S9_V1` + `SLCMP01` + `SLCMP02`

**New-prime claim:** `NONE`

## Installed

- Exact integer Lucas–Lehmer recurrence for prime exponents.
- Known-result regression tests.
- Compact JSON execution receipts.
- A typed boundary between exact primality testing and SAM/SLC candidate work.
- A manifest schema for future frozen, allowlisted exports.
- A deterministic public-safe export generator.
- The complete 1,858-row MP-S8 unresolved candidate roster.
- The MP-S8 aggregate and exact radix-2 first-singularity bridge.
- The MP-S9 selection-1196 checkpoint receipt at 110 of 143,064,039
  Lucas--Lehmer iterations.
- The compact public MP-S0--S9 research lineage.
- A public stewardship pledge.
- Post-run alias `SLCMP0` for the frozen MP-S8/MP-S9 origin bundle.
- Post-run alias `SLCMP01` for the completed MP-S10 Run 01 derivative:
  1,226 primality-unassigned search inputs over
  `143100000 < p <= 143200000`.
- Post-run alias `SLCMP02` for the completed MP-S10 Run 02 derivative:
  1,119 primality-unassigned search inputs over
  `143200000 < p <= 143300000`.

## Active branch

The intended research-development branch is `research/mersenne-search-v1`.
Stable bootstrap material is retained on `main`.

## Not yet installed

- Distributed checkpointing or long-run worker coordination.
- Trial-factor, probable-prime, or GPU acceleration stages.
- A production-scale exact engine for the 1,858-row queue.
- The MP-S9 binary checkpoint in the public bundle.
- A candidate passing the repository's new-result publication sequence.
- MP-S10 Run 03 (`SLCMP03`) and later sequential bands.

Nothing in the current state assigns primality to selection 1196 or claims
discovery of a new Mersenne prime.
