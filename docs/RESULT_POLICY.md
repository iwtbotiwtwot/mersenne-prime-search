# Result policy

This repository uses precise public states so an exploratory signal is never
confused with an exact discovery result.

## States

- `SEARCH_INPUT`: admitted prime exponent, optionally with typed sidecars.
- `LLT_IN_PROGRESS`: exact recurrence has begun but is incomplete.
- `LLT_NONZERO_RESIDUE`: completed exact recurrence; candidate is composite.
- `LLT_ZERO_RESIDUE_CANDIDATE`: completed exact recurrence returned zero and
  the full receipt is awaiting independent reproduction.
- `INDEPENDENTLY_REPRODUCED`: a separate execution reproduced the zero residue
  and the compared receipts are public.
- `SUBMITTED_FOR_EXTERNAL_CONFIRMATION`: the reproduced result was sent to the
  relevant external verification or registration channel.
- `PUBLIC_NEW_PRIME_CLAIM`: the repository identifies the number as a new
  Mersenne prime and links the complete custody record.

An SLC prediction, rank, schedule, or sidecar cannot advance a result into an
LLT state. The current repository status is bootstrap only and contains no new
prime claim.
