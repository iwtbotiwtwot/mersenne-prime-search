# Mersenne Prime Search

An exact, reproducible Mersenne-prime search repository with two deliberately
separate lanes:

1. a public Lucas–Lehmer baseline that decides candidates of the form
   $M_p=2^p-1$ for prime exponents $p$; and
2. a SAM/SLC research branch that may propose, order, or annotate exponents,
   but does not assign primality.

## Current status

The repository is at **bootstrap v0.1.0**. It contains a tested exact
Lucas–Lehmer implementation and the public interface for future frozen SLC
exports. It does **not** contain a new-prime claim.

For prime $p>2$, the baseline starts with $s_0=4$ and computes

$$
s_{k+1}=s_k^2-2 \pmod{M_p}
$$

for $p-2$ iterations. The candidate $M_p$ is prime exactly when the final
residue is zero. The case $p=2$ is handled directly.

## Quick start

The code uses only the Python standard library.

```bash
python3 -m unittest discover -s tests -v
python3 src/mersenne_search.py 31
python3 verification/validate_repository.py
```

The CLI emits a compact JSON receipt containing the exponent, bit length,
iteration count, final residue, and result. It intentionally does not print a
potentially enormous decimal candidate.

## Research boundary

The exact Lucas–Lehmer lane is the primality authority in this repository.
SAM/SLC may contribute candidate generation, ranking, scheduling, reciprocal
history, directional-Weil coordinates, or other typed sidecars. Those objects
remain hypotheses or search-control data until an exact candidate test is
executed and preserved.

The source SAM installation currently records a completed Mersenne curriculum
with 13,818 ordinary-prime exponent sidecars and 13,972 prime-power channel
receipts. That installation explicitly made no primality assignment. This
repository carries the same boundary.

## Repository map

- [`src/mersenne_search.py`](src/mersenne_search.py): exact baseline and CLI.
- [`tests/`](tests): known prime and composite regression cases.
- [`research/00_BASELINE.md`](research/00_BASELINE.md): mathematical baseline.
- [`research/01_SAM_SLC_SEARCH_BRANCH.md`](research/01_SAM_SLC_SEARCH_BRANCH.md):
  typed research lane.
- [`docs/SEARCH_PROTOCOL.md`](docs/SEARCH_PROTOCOL.md): candidate-to-receipt flow.
- [`docs/RESULT_POLICY.md`](docs/RESULT_POLICY.md): precise public claim states.
- [`interface/SLC_EXPORT_CONTRACT.md`](interface/SLC_EXPORT_CONTRACT.md): frozen
  export boundary.
- [`schemas/mersenne_export_manifest.schema.json`](schemas/mersenne_export_manifest.schema.json):
  machine-readable manifest schema.

## Stewardship

This repository is a project of the SAM Research Project. Any award or prize
received because of work published here is covered by the
[`SAM Public Stewardship Pledge`](STEWARDSHIP_PLEDGE.md).

## License

Code is released under Apache-2.0. Documentation is released under CC BY 4.0.
See [`LICENSE.md`](LICENSE.md).
