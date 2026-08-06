# SAM Mersenne Prime Search

## Concept

SAM treats a Mersenne candidate as a relationship between two orbiting objects
inside a closed 2D sphere.

One orbit carries the candidate's reciprocal history: not only where the
recurrence lands, but the direction it traveled and the echoes it leaves. The
second orbit is a prime ruler built from the exponent's position among
neighboring prime marks. Because the sphere is closed, forward and reciprocal
motion remain parts of the same continuous geometry instead of being discarded
at an edge.

The two orbits do not tick at only one scale. Beats sit inside larger beats,
and alignments return as echoes. Those meetings produce an ordered set of
places to look for a factor. SAM therefore searches by relationship and rhythm
instead of walking blindly through possible factors.

The sphere and its beats do not assign primality. Each proposed contact is
handed to exact modular arithmetic. A confirmed factor assigns compositeness;
without one, the candidate remains unresolved and proceeds to Lucas--Lehmer.

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
| [SLCMP0](candidates/SLCMP0.csv) | $143{,}000{,}000<p\leq143{,}100{,}000$ | 1,858 |
| [SLCMP01](candidates/SLCMP01.csv) | $143{,}100{,}000<p\leq143{,}200{,}000$ | 1,226 |
| [SLCMP02](candidates/SLCMP02.csv) | $143{,}200{,}000<p\leq143{,}300{,}000$ | 1,119 |
| [SLCMP03](candidates/SLCMP03.csv) | $143{,}300{,}000<p\leq143{,}400{,}000$ | 1,225 |
| [SLCMP04](candidates/SLCMP04.csv) | $143{,}400{,}000<p\leq143{,}500{,}000$ | 1,244 |
| [SLCMP05](candidates/SLCMP05.csv) | $143{,}500{,}000<p\leq143{,}600{,}000$ | 956 |
| [SLCMP06](candidates/SLCMP06.csv) | $143{,}600{,}000<p\leq143{,}700{,}000$ | 780 |
| [SLCMP07](candidates/SLCMP07.csv) | $143{,}700{,}000<p\leq143{,}800{,}000$ | 1,360 |
| [SLCMP08](candidates/SLCMP08.csv) | $143{,}800{,}000<p\leq143{,}900{,}000$ | 1,042 |
| [SLCMP09](candidates/SLCMP09.csv) | $143{,}900{,}000<p\leq144{,}000{,}000$ | 1,327 |
| [SLCMP11](candidates/SLCMP11.csv) | $145{,}000{,}000<p\leq145{,}250{,}000$ | 3,108 |
| [SLCMP12](candidates/SLCMP12.csv) | $145{,}250{,}000<p\leq145{,}500{,}000$ | 3,932 |
| [SLCMP13](candidates/SLCMP13.csv) | $145{,}500{,}000<p\leq145{,}750{,}000$ | 3,972 |
| [SLCMP14](candidates/SLCMP14.csv) | $145{,}750{,}000<p\leq146{,}000{,}000$ | 2,320 |
| [SLCMP15](candidates/SLCMP15.csv) | $146{,}000{,}000<p\leq146{,}250{,}000$ | 461 |
| [SLCMP16](candidates/SLCMP16.csv) | $146{,}250{,}000<p\leq146{,}500{,}000$ | 687 |
| [SLCMP17](candidates/SLCMP17.csv) | $146{,}500{,}000<p\leq146{,}750{,}000$ | 2,916 |
| [SLCMP18](candidates/SLCMP18.csv) | $146{,}750{,}000<p\leq147{,}000{,}000$ | 3,391 |
| [SLCMP19](candidates/SLCMP19.csv) | $147{,}000{,}000<p\leq147{,}250{,}000$ | 2,088 |
| [SLCMP20](candidates/SLCMP20.csv) | $147{,}250{,}000<p\leq147{,}500{,}000$ | 244 |
| [SLCMP21](candidates/SLCMP21.csv) | $147{,}500{,}000<p\leq147{,}750{,}000$ | 523 |
| [SLCMP22](candidates/SLCMP22.csv) | $147{,}750{,}000<p\leq148{,}000{,}000$ | 1 |
| [SLCMP23](candidates/SLCMP23.csv) | $148{,}000{,}000<p\leq148{,}250{,}000$ | 551 |
| [SLCMP24](candidates/SLCMP24.csv) | $148{,}250{,}000<p\leq148{,}500{,}000$ | 4,610 |
| [SLCMP25](candidates/SLCMP25.csv) | $148{,}500{,}000<p\leq148{,}750{,}000$ | 4,527 |
| [SLCMP26](candidates/SLCMP26.csv) | $148{,}750{,}000<p\leq149{,}000{,}000$ | 4,447 |
| [SLCMP27](candidates/SLCMP27.csv) | $149{,}000{,}000<p\leq149{,}250{,}000$ | 4,485 |
| [SLCMP28](candidates/SLCMP28.csv) | $149{,}250{,}000<p\leq149{,}500{,}000$ | 4,591 |
| [SLCMP29](candidates/SLCMP29.csv) | $149{,}500{,}000<p\leq149{,}750{,}000$ | 4,630 |
| [SLCMP30](candidates/SLCMP30.csv) | $149{,}750{,}000<p\leq150{,}000{,}000$ | 4,409 |
| [SLCMP31](candidates/SLCMP31.csv) | $150{,}000{,}000<p\leq150{,}250{,}000$ | 4,533 |
| [SLCMP32](candidates/SLCMP32.csv) | $150{,}250{,}000<p\leq150{,}500{,}000$ | 4,567 |
| **Total** |  | **77,130** |

Each export link opens its number-only candidate roster. Every exponent remains
a primality-unassigned search input.

## Exact test

Lucas--Lehmer is the final decision. For a prime exponent, it repeatedly
applies square-minus-two in arithmetic modulo the Mersenne candidate for
exactly (p-2) steps. A terminal zero assigns primality; a nonzero terminal
residue assigns compositeness.

```bash
python3 -m unittest discover -s tests -v
python3 src/mersenne_search.py 31
python3 verification/validate_repository.py
```

This is a SAM Research Project repository. The
[`SAM Public Stewardship Pledge`](STEWARDSHIP_PLEDGE.md) applies. Code is
Apache-2.0; documentation is CC BY 4.0. See [`LICENSE.md`](LICENSE.md).
