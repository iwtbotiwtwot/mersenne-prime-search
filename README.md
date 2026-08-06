# SAM Mersenne Prime Search

SAM searches the exact Mersenne factor coordinate

$$
q=2kp+1,
\qquad
q\mid 2^p-1 \iff \operatorname{ord}_q(2)=p.
$$

The structural search orders $k$; exact modular arithmetic certifies every
factor. A candidate with no factor remains unresolved until an exact
Lucas--Lehmer test assigns primality.

## Test results

| Test | Numerical result |
|---|---|
| MP-S1--S3 reciprocal and beat channels | 61 of 158 composite controls factored; 0 of 13 exact-positive controls contacted. |
| MP-S4B blind ECHO16 range | 50 of 136 composites factored; 0 contact on the exact prime at $p=1279$. |
| MP-S5 structural $k$ ruler | 103 of 252 composites factored versus 100 of 252 for equal-budget ascending $k$; shared-contact rank total 1,956 versus 2,284. |
| MP-S6 frontier screen | 5,390 prime exponents tested; 1,282 exact factors; 4,108 survivors. |
| MP-S7 factor ranking | 2,250 further exact factors; 1,858 candidates routed forward. |
| MP-S8 first-singularity shell | 17,827,510 exact factor opportunities; 0 further factors; 1,858 candidates retained. |

## Public candidate exports

| Export | Exponent band | Candidates |
|---|---:|---:|
| [SLCMP0](exports/SAM_MP_S8_MP_S9_V1/RESULTS.md) | $143{,}000{,}000<p\leq143{,}100{,}000$ | 1,858 |
| [SLCMP01](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP01/RESULTS.md) | $143{,}100{,}000<p\leq143{,}200{,}000$ | 1,226 |
| [SLCMP02](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP02/RESULTS.md) | $143{,}200{,}000<p\leq143{,}300{,}000$ | 1,119 |
| [SLCMP03](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP03/RESULTS.md) | $143{,}300{,}000<p\leq143{,}400{,}000$ | 1,225 |
| [SLCMP04](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP04/RESULTS.md) | $143{,}400{,}000<p\leq143{,}500{,}000$ | 1,244 |
| [SLCMP05](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP05/RESULTS.md) | $143{,}500{,}000<p\leq143{,}600{,}000$ | 956 |
| [SLCMP06](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP06/RESULTS.md) | $143{,}600{,}000<p\leq143{,}700{,}000$ | 780 |
| [SLCMP07](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP07/RESULTS.md) | $143{,}700{,}000<p\leq143{,}800{,}000$ | 1,360 |
| [SLCMP08](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP08/RESULTS.md) | $143{,}800{,}000<p\leq143{,}900{,}000$ | 1,042 |
| [SLCMP09](https://github.com/iwtbotiwtwot/mersenne-prime-search/blob/research/mersenne-search-v1/exports/SLCMP09/RESULTS.md) | $143{,}900{,}000<p\leq144{,}000{,}000$ | 1,327 |
| **Total** |  | **12,137** |

Each export page places its complete candidate roster directly below its
numerical result. Every row is a primality-unassigned search input.

## Exact test

For prime $p>2$, Lucas--Lehmer starts at $s_0=4$ and performs

$$
s_{j+1}=s_j^2-2 \pmod{2^p-1}
$$

for $p-2$ iterations. The number is prime exactly when the terminal residue is
zero.

```bash
python3 -m unittest discover -s tests -v
python3 src/mersenne_search.py 31
python3 verification/validate_repository.py
```

The full research sequence is recorded in
[`research/02_SAM_MERSENNE_LINEAGE.md`](research/02_SAM_MERSENNE_LINEAGE.md).

This is a SAM Research Project repository. The
[`SAM Public Stewardship Pledge`](STEWARDSHIP_PLEDGE.md) applies. Code is
Apache-2.0; documentation is CC BY 4.0. See [`LICENSE.md`](LICENSE.md).
