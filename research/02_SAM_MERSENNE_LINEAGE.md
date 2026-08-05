# SAM Mersenne search lineage

This document is the compact public map of the completed SAM Mersenne
research sequence. It reports the source campaign outcomes while preserving
the repository boundary:

```text
candidate structure and scheduling
    != exact primality assignment
    != independent confirmation
    != public new-prime claim
```

## Exact bridge

For prime exponent $p$,

$$
M_p=2^p-1=\Phi_p(2).
$$

A proper prime factor $q$ of $M_p$ has the coordinate

$$
q=2kp+1,
\qquad
q\mid M_p
\iff
\operatorname{ord}_q(2)=p.
$$

The SAM shell writes

$$
k=b2^e,
$$

so increasing echo depth advances $\log(q-1)$ by $\log 2$ at fixed structural
base $b$ and exponent $p$. A successful contact is an exact factor
certificate. Exhausting a finite shell leaves the candidate unresolved.

## From direct ranking to exact objects

The RH-aware M4 and M4A direct-ranking campaigns did not produce a stable
positive-ranking successor to their parent. For both campaigns, **The test
falsifies the concept**, scoped specifically to that direct-ranking objective.
The search then moved to exact reciprocal, orbit, beat, factor, and
cyclotomic objects.

## Clean-sheet sequence

| Stage | Exact object or campaign | Source outcome |
|---|---|---|
| MP-S0 | Reciprocal Lucas--Lehmer object | Reconstructed 80,358 states across 171 prime exponents and exposed the terminal reciprocal closure. No project classification. |
| MP-S0A | Rational closed-sphere operator | Installed stereographic coordinate, reciprocal reflection, integer action, and logarithmic traversal. No project classification. |
| MP-S0B | Prime-only spherical ruler | Installed 172 prime marks and 171 reversible adjacent-prime cells without emitting intervening composites as ruler objects. No project classification. |
| MP-S1 | Reciprocal-orbit collisions | Exact factors for 52 of 158 composite controls and none of 13 exact-positive controls. **The test result suggests the concept is possible.** |
| MP-S2 | Two-object informational harmony | Exact factors for 37 composites, including five unresolved by MP-S1; none of 13 exact-positive controls. **The test result suggests the concept is possible.** |
| MP-S3 | Adjacent-prime transition beat | Four further exact factors at exponents 79, 181, 547, and 619; no exact-positive control contact. **The test result suggests the concept is possible.** |
| MP-S4A | Candidate-local ECHO16 executable | Compiled the three factor channels into a deterministic checkpointable search executable; no new project classification. |
| MP-S4B | Blind range 1024 to 2048 | Exact factors for 50 of 136 composite candidates and none for the exact prime at exponent 1279. **The test result suggests the concept is possible.** |
| MP-S5 | SAM structural $k$ ruler | Factored 103 of 252 composites versus 100 for equal-budget ascending counting. **The test result suggests strong contact with the concept.** |
| MP-S6 | Frontier structural screen | Across 5,390 prime exponents near 143 million, assigned 1,282 exact factors and left 4,108 rows unfalsified by that screen. **The test result suggests the concept is possible.** |
| MP-S7 | Decisive factor ranking | Assigned 2,250 further exact factors and routed 1,858 rows to the unresolved queue. |
| MP-S8 | RH first-singularity shell | Executed 17,827,510 shell opportunities, tested $q$ objects from 40 to 168 bits, assigned zero new factors, and retained all 1,858 rows as unresolved search inputs. |
| MP-S9 | Owner-selected exact test | Selection 1196 maps to $p=143{,}064{,}041$; exact Lucas--Lehmer progress is checkpointed at iteration 110 of 143,064,039. State: `LLT_IN_PROGRESS`. |

The official factor-record audit associated with MP-S6 found that all 1,282
factor pairs were already recorded externally. That audit changed no exact
factor certificate and no campaign classification.

## Current public installation

The frozen
[SAM MP-S8 / MP-S9 export](../exports/SAM_MP_S8_MP_S9_V1/README.md)
contains:

- the complete 1,858-row candidate roster;
- the MP-S8 aggregate and exact cyclotomic bridge;
- the selection-1196 MP-S9 progress receipt;
- source and semantic hashes; and
- a manifest that assigns no primality.

The 17,883,276-byte MP-S9 binary checkpoint is not in the public bundle. Its
file and state hashes are preserved in the progress receipt. A later
production engine may consume the candidate, but only a completed exact
residue can advance its result state.
