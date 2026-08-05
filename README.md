# SAM Mersenne Prime Search

This project asks two different questions, in the correct order:

1. Can the reciprocal, prime-ruler, and beat structure developed by the SAM
   Research Project expose an exact factor of a Mersenne number?
2. If no factor is found, what does the exact Lucas--Lehmer test say?

The first question builds a structured search. The second assigns primality.
Keeping them separate lets the project use new mathematical structure without
confusing a promising candidate with a finished result.

## The object being searched

For a prime exponent $p$, the candidate is

$$
M_p=2^p-1.
$$

A proper prime factor $q$ of $M_p$ must occupy the exact coordinate

$$
q=2kp+1,
\qquad
q\mid M_p \iff \operatorname{ord}_q(2)=p.
$$

That turns factor search into a search over the integer coordinate $k$. The
SAM scheduler does not simply count upward through $k$. It builds structural
bases from the project's connector, harmony, transition, and ECHO16 objects,
then follows dyadic shells

$$
k=b2^e.
$$

Every contact is checked by exact modular arithmetic. A successful contact is
an exact factor certificate; exhausting the finite shell leaves that exponent
unresolved and available for further testing.

## Where the structure comes from

The clean-sheet search began with the quadratic unit

$$
x_n=(2+\sqrt3)^{2^n}=a_n+b_n\sqrt3,
\qquad
x_n^{-1}=a_n-b_n\sqrt3.
$$

Its common component reproduces the Lucas--Lehmer state,
$2a_n=s_n$, while its directional component $2b_n$ preserves the reciprocal
history that the usual scalar recurrence hides.

SAM then places the reciprocal action on a rational closed sphere using

$$
x=\tan(\chi/2),
\qquad J(x)=1/x,
\qquad T_m(x)=mx,
\qquad du=dx/x=d\chi/\sin\chi.
$$

Only prime marks are ruler objects. Adjacent prime marks form reversible cells,
and two additional norm-one voices let the search compare a Mersenne orbit
with its prime-ruler position and incoming prime transition:

$$
\beta_p=\frac{p+\sqrt3}{p-\sqrt3},
\qquad
\gamma_p=\beta_p\beta_{p^-}^{-1}.
$$

The resulting self, prime-mark, and transition channels search for modular
orbit collisions across shallow pulse depths and echo delays. Those collision
experiments led to the structural $k$ ruler used at the frontier.

## Test results

| Stage | Test and result |
|---|---|
| MP-S1 | Reciprocal-orbit collisions emitted exact factors for 52 of 158 composite controls and none of 13 exact-positive controls. **The test result suggests the concept is possible.** |
| MP-S2 | Two-object informational harmony emitted 37 composite factors, including five objects unresolved by MP-S1, and no exact-positive contact. **The test result suggests the concept is possible.** |
| MP-S3 | The adjacent-prime transition beat emitted four further exact factors and no exact-positive contact. **The test result suggests the concept is possible.** |
| MP-S4B | In the blind range $1024<p\leq2048$, ECHO16 factored 50 of 136 composite candidates and did not contact the exact prime at $p=1279$. **The test result suggests the concept is possible.** |
| MP-S5 | With 256 opportunities per exponent, the SAM structural ruler factored 103 of 252 composites versus 100 for the equal-budget ascending-$k$ control, reached shared contacts earlier, and found six exclusive factors beyond the control horizon. **The test result suggests strong contact with the concept.** |
| MP-S6 | Across all 5,390 prime exponents in $143{,}000{,}000<p\leq143{,}100{,}000$, the frontier screen assigned 1,282 exact factors and left 4,108 locally unfalsified candidates. **The test result suggests the concept is possible.** |
| MP-S7 | Decisive factor ranking assigned 2,250 further exact factors and routed 1,858 unresolved exponents forward. |
| MP-S8 | The first-singularity shell executed 17,827,510 exact factor opportunities, found no additional factor, and retained all 1,858 rows as primality-unassigned search inputs. |

**[Open the complete 1,858-candidate list](exports/SAM_MP_S8_MP_S9_V1/candidate_roster.csv)**

The list is the direct output of the completed MP-S8 screen. Each row is a
prime exponent near 143 million for which the installed finite factor searches
found no factor. `SEARCH_INPUT` means exactly that: the exponent remains a
candidate for continued factor search or exact Lucas--Lehmer testing.

The full stage-by-stage account is in
[`research/02_SAM_MERSENNE_LINEAGE.md`](research/02_SAM_MERSENNE_LINEAGE.md),
and the frozen bundle has its own
[`manifest and receipt guide`](exports/SAM_MP_S8_MP_S9_V1/README.md).

## Exact primality lane

For prime $p>2$, Lucas--Lehmer begins with $s_0=4$ and computes

$$
s_{j+1}=s_j^2-2 \pmod{M_p}
$$

for $p-2$ iterations. The candidate $M_p$ is prime exactly when the terminal
residue is zero. The case $p=2$ is handled directly.

Selection 1196 from the public roster is $p=143{,}064{,}041$. Its preserved
receipt records `LLT_IN_PROGRESS` after 110 of 143,064,039 iterations. The
repository currently assigns no new Mersenne-prime result.

## Run it

The exact baseline uses only the Python standard library.

```bash
python3 -m unittest discover -s tests -v
python3 src/mersenne_search.py 31
python3 verification/validate_repository.py
```

The CLI emits a compact JSON receipt with the exponent, bit length, iteration
count, final residue, and result. It avoids printing the enormous decimal
candidate itself.

## Repository map

- [`exports/SAM_MP_S8_MP_S9_V1/`](exports/SAM_MP_S8_MP_S9_V1/README.md): frozen
  1,858-row candidate export and selection-1196 progress receipt.
- [`research/02_SAM_MERSENNE_LINEAGE.md`](research/02_SAM_MERSENNE_LINEAGE.md):
  conceptual and experimental lineage.
- [`research/03_CANDIDATE_ADMISSION_REFERENCE.md`](research/03_CANDIDATE_ADMISSION_REFERENCE.md):
  meaning of each public candidate and result state.
- [`src/mersenne_search.py`](src/mersenne_search.py): exact Lucas--Lehmer
  baseline and CLI.
- [`docs/SEARCH_PROTOCOL.md`](docs/SEARCH_PROTOCOL.md): candidate-to-receipt
  execution flow.
- [`docs/RESULT_POLICY.md`](docs/RESULT_POLICY.md): public result states.
- [`interface/SLC_EXPORT_CONTRACT.md`](interface/SLC_EXPORT_CONTRACT.md): frozen
  export boundary.

## Stewardship and license

This is a SAM Research Project repository. Any award or prize received because
of work published here is covered by the
[`SAM Public Stewardship Pledge`](STEWARDSHIP_PLEDGE.md).

Code is released under Apache-2.0. Documentation is released under CC BY 4.0.
See [`LICENSE.md`](LICENSE.md).
