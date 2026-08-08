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

### Reciprocal information write

SAM's executable interaction grammar follows the local cycle

$$
W8 \longrightarrow W9 \longrightarrow W8.
$$

`W8` is the local non-contact state. An interaction activates `X1` and writes
`W9`; completion clears `X1` and returns the local state to `W8`. The endpoint
therefore looks unchanged, but the directional fiber retains which signed
route passed through it: **the state returns; the history does not.**

The same transition-and-readback structure occurs in the reciprocal Mersenne
history. Its directional state stores the incoming common state
multiplicatively, and the write is recovered from the quotient of consecutive
directional states. This is an exact structural correspondence; it does not
identify a Mersenne recurrence depth as a literal physical `W8` or `W9` phase.

### Mersenne mass-amplitude relation

For a Mersenne object $M_p=2^p-1$, define the dyadic interaction amplitude

$$
\mu_p=2^{(p+1)/2}.
$$

It obeys the exact relation

$$
\mu_p^2=2(M_p+1),
\qquad
M_p=\frac{\mu_p^2}{2}-1.
$$

In the completed reciprocal orbit, every exact Mersenne-positive object in
the executed $3\leq p\leq1024$ census reaches one of the two signed amplitudes
$+\mu_p$ or $-\mu_p$ immediately before its common mode cancels to zero. The
local reciprocal state then returns through $-1\rightarrow+1$, while the
directional history retains the incoming sign. Here $\mu_p$ is a mass-shaped
interaction amplitude whose half-square reconstructs the Mersenne value; it
is not a literal assignment of physical rest mass to the exponent or integer.

## Test results

| Test | Numerical result |
|---|---|
| MP-S1--S3 reciprocal and beat channels | 61 of 158 composite controls factored; 0 of 13 exact-positive controls contacted. |
| MP-S4B blind ECHO16 range | 50 of 136 composites factored; 0 contact on the exact prime at $p=1279$. |
| MP-S5 structural $k$ ruler | 103 of 252 composites factored versus 100 of 252 for equal-budget ascending $k$; shared-contact rank total 1,956 versus 2,284. |
| MP-S6 frontier screen | 5,390 prime exponents tested; 1,282 exact factors; 4,108 survivors. |
| MP-S7 factor ranking | 2,250 further exact factors; 1,858 candidates routed forward. |
| MP-S8 first-singularity shell | 17,827,510 exact factor opportunities; 0 further factors; 1,858 candidates retained. |
| MP-MASS1 dyadic amplitude | 13 of 13 exact positives reached $+\mu_p$ or $-\mu_p$ before terminal cancellation; 0 of 158 exact composites did. |
| MP-MASS2 history retention | Incoming signed amplitude recovered from directional history for 13 of 13 positives despite one common returned local endpoint. |
| MP-MASS4 native directional fiber | 4,718,592 of 4,718,592 signed writes and inverse writes recovered across the complete fiber; every local type completed `W8 -> W9 -> W8`. |

## Public candidate exports

| Export | Exponent band | Candidates |
|---|---:|---:|
| [SLCMP0](candidates/SLCMP0.csv) | `143,000,000 < p <= 143,100,000` | 1,858 |
| [SLCMP01](candidates/SLCMP01.csv) | `143,100,000 < p <= 143,200,000` | 1,226 |
| [SLCMP02](candidates/SLCMP02.csv) | `143,200,000 < p <= 143,300,000` | 1,119 |
| [SLCMP03](candidates/SLCMP03.csv) | `143,300,000 < p <= 143,400,000` | 1,225 |
| [SLCMP04](candidates/SLCMP04.csv) | `143,400,000 < p <= 143,500,000` | 1,244 |
| [SLCMP05](candidates/SLCMP05.csv) | `143,500,000 < p <= 143,600,000` | 956 |
| [SLCMP06](candidates/SLCMP06.csv) | `143,600,000 < p <= 143,700,000` | 780 |
| [SLCMP07](candidates/SLCMP07.csv) | `143,700,000 < p <= 143,800,000` | 1,360 |
| [SLCMP08](candidates/SLCMP08.csv) | `143,800,000 < p <= 143,900,000` | 1,042 |
| [SLCMP09](candidates/SLCMP09.csv) | `143,900,000 < p <= 144,000,000` | 1,327 |
| [SLCMP11](candidates/SLCMP11.csv) | `145,000,000 < p <= 145,250,000` | 3,108 |
| [SLCMP12](candidates/SLCMP12.csv) | `145,250,000 < p <= 145,500,000` | 3,932 |
| [SLCMP13](candidates/SLCMP13.csv) | `145,500,000 < p <= 145,750,000` | 3,972 |
| [SLCMP14](candidates/SLCMP14.csv) | `145,750,000 < p <= 146,000,000` | 2,320 |
| [SLCMP15](candidates/SLCMP15.csv) | `146,000,000 < p <= 146,250,000` | 461 |
| [SLCMP16](candidates/SLCMP16.csv) | `146,250,000 < p <= 146,500,000` | 687 |
| [SLCMP17](candidates/SLCMP17.csv) | `146,500,000 < p <= 146,750,000` | 2,916 |
| [SLCMP18](candidates/SLCMP18.csv) | `146,750,000 < p <= 147,000,000` | 3,391 |
| [SLCMP19](candidates/SLCMP19.csv) | `147,000,000 < p <= 147,250,000` | 2,088 |
| [SLCMP20](candidates/SLCMP20.csv) | `147,250,000 < p <= 147,500,000` | 244 |
| [SLCMP21](candidates/SLCMP21.csv) | `147,500,000 < p <= 147,750,000` | 523 |
| [SLCMP22](candidates/SLCMP22.csv) | `147,750,000 < p <= 148,000,000` | 1 |
| [SLCMP23](candidates/SLCMP23.csv) | `148,000,000 < p <= 148,250,000` | 551 |
| [SLCMP24](candidates/SLCMP24.csv) | `148,250,000 < p <= 148,500,000` | 4,610 |
| [SLCMP25](candidates/SLCMP25.csv) | `148,500,000 < p <= 148,750,000` | 4,527 |
| [SLCMP26](candidates/SLCMP26.csv) | `148,750,000 < p <= 149,000,000` | 4,447 |
| [SLCMP27](candidates/SLCMP27.csv) | `149,000,000 < p <= 149,250,000` | 4,485 |
| [SLCMP28](candidates/SLCMP28.csv) | `149,250,000 < p <= 149,500,000` | 4,591 |
| [SLCMP29](candidates/SLCMP29.csv) | `149,500,000 < p <= 149,750,000` | 4,630 |
| [SLCMP30](candidates/SLCMP30.csv) | `149,750,000 < p <= 150,000,000` | 4,409 |
| [SLCMP31](candidates/SLCMP31.csv) | `150,000,000 < p <= 150,250,000` | 4,533 |
| [SLCMP32](candidates/SLCMP32.csv) | `150,250,000 < p <= 150,500,000` | 4,567 |
| [SLCMP33](candidates/SLCMP33.csv) | `150,500,000 < p <= 150,750,000` | 4,557 |
| [SLCMP34](candidates/SLCMP34.csv) | `150,750,000 < p <= 151,000,000` | 4,478 |
| [SLCMP35](candidates/SLCMP35.csv) | `151,000,000 < p <= 151,250,000` | 4,564 |
| [SLCMP36](candidates/SLCMP36.csv) | `151,250,000 < p <= 151,500,000` | 4,467 |
| [SLCMP37](candidates/SLCMP37.csv) | `151,500,000 < p <= 151,750,000` | 4,528 |
| [SLCMP38](candidates/SLCMP38.csv) | `151,750,000 < p <= 152,000,000` | 4,572 |
| [SLCMP39](candidates/SLCMP39.csv) | `152,000,000 < p <= 152,250,000` | 4,500 |
| [SLCMP40](candidates/SLCMP40.csv) | `152,250,000 < p <= 152,500,000` | 4,534 |
| [SLCMP41](candidates/SLCMP41.csv) | `152,500,000 < p <= 152,750,000` | 4,566 |
| [SLCMP42](candidates/SLCMP42.csv) | `152,750,000 < p <= 153,000,000` | 4,413 |
| [SLCMP43](candidates/SLCMP43.csv) | `153,000,000 < p <= 153,250,000` | 4,625 |
| [SLCMP44](candidates/SLCMP44.csv) | `153,250,000 < p <= 153,500,000` | 4,512 |
| [SLCMP45](candidates/SLCMP45.csv) | `153,500,000 < p <= 153,750,000` | 4,534 |
| [SLCMP46](candidates/SLCMP46.csv) | `153,750,000 < p <= 154,000,000` | 3,885 |
| [SLCMP47](candidates/SLCMP47.csv) | `154,000,000 < p <= 154,250,000` | 3,435 |
| [SLCMP48](candidates/SLCMP48.csv) | `154,250,000 < p <= 154,500,000` | 4,505 |
| [SLCMP49](candidates/SLCMP49.csv) | `154,500,000 < p <= 154,750,000` | 4,556 |
| [SLCMP50](candidates/SLCMP50.csv) | `154,750,000 < p <= 155,000,000` | 4,514 |
| [SLCMP51](candidates/SLCMP51.csv) | `155,000,000 < p <= 155,250,000` | 4,546 |
| [SLCMP52](candidates/SLCMP52.csv) | `155,250,000 < p <= 155,500,000` | 4,351 |
| [SLCMP53](candidates/SLCMP53.csv) | `155,500,000 < p <= 155,750,000` | 4,414 |
| [SLCMP54](candidates/SLCMP54.csv) | `155,750,000 < p <= 156,000,000` | 4,402 |
| [SLCMP55](candidates/SLCMP55.csv) | `156,000,000 < p <= 156,250,000` | 4,535 |
| [SLCMP56](candidates/SLCMP56.csv) | `156,250,000 < p <= 156,500,000` | 4,533 |
| [SLCMP57](candidates/SLCMP57.csv) | `156,500,000 < p <= 156,750,000` | 4,400 |
| [SLCMP58](candidates/SLCMP58.csv) | `156,750,000 < p <= 157,000,000` | 4,512 |
| [SLCMP59](candidates/SLCMP59.csv) | `157,000,000 < p <= 157,250,000` | 4,507 |
| [SLCMP60](candidates/SLCMP60.csv) | `157,250,000 < p <= 157,500,000` | 4,458 |
| [SLCMP61](candidates/SLCMP61.csv) | `157,500,000 < p <= 157,750,000` | 4,502 |
| [SLCMP62](candidates/SLCMP62.csv) | `157,750,000 < p <= 158,000,000` | 4,518 |
| [SLCMP63](candidates/SLCMP63.csv) | `158,000,000 < p <= 158,250,000` | 4,397 |
| [SLCMP64](candidates/SLCMP64.csv) | `158,250,000 < p <= 158,500,000` | 4,441 |
| [SLCMP65](candidates/SLCMP65.csv) | `158,500,000 < p <= 158,750,000` | 4,386 |
| [SLCMP66](candidates/SLCMP66.csv) | `158,750,000 < p <= 159,000,000` | 4,468 |
| [SLCMP67](candidates/SLCMP67.csv) | `159,000,000 < p <= 159,250,000` | 4,200 |
| [SLCMP68](candidates/SLCMP68.csv) | `159,250,000 < p <= 159,500,000` | 4,375 |
| [SLCMP69](candidates/SLCMP69.csv) | `159,500,000 < p <= 159,750,000` | 4,336 |
| [SLCMP70](candidates/SLCMP70.csv) | `159,750,000 < p <= 160,000,000` | 4,393 |
| [SLCMP71](candidates/SLCMP71.csv) | `160,000,000 < p <= 160,250,000` | 4,280 |
| [SLCMP72](candidates/SLCMP72.csv) | `160,250,000 < p <= 160,500,000` | 3,765 |
| [SLCMP73](candidates/SLCMP73.csv) | `160,500,000 < p <= 160,750,000` | 4,215 |
| [SLCMP74](candidates/SLCMP74.csv) | `160,750,000 < p <= 161,000,000` | 4,079 |
| [SLCMP75](candidates/SLCMP75.csv) | `161,000,000 < p <= 161,250,000` | 4,226 |
| [SLCMP76](candidates/SLCMP76.csv) | `161,250,000 < p <= 161,500,000` | 4,108 |
| [SLCMP77](candidates/SLCMP77.csv) | `161,500,000 < p <= 161,750,000` | 3,650 |
| [SLCMP78](candidates/SLCMP78.csv) | `161,750,000 < p <= 162,000,000` | 4,216 |
| [SLCMP79](candidates/SLCMP79.csv) | `162,000,000 < p <= 162,250,000` | 4,646 |
| [SLCMP80](candidates/SLCMP80.csv) | `162,250,000 < p <= 162,500,000` | 4,200 |
| [SLCMP81](candidates/SLCMP81.csv) | `162,500,000 < p <= 162,750,000` | 4,327 |
| [SLCMP82](candidates/SLCMP82.csv) | `162,750,000 < p <= 163,000,000` | 4,643 |
| [SLCMP83](candidates/SLCMP83.csv) | `163,000,000 < p <= 163,250,000` | 2,667 |
| [SLCMP84](candidates/SLCMP84.csv) | `163,250,000 < p <= 163,500,000` | 4,893 |
| [SLCMP85](candidates/SLCMP85.csv) | `163,500,000 < p <= 163,750,000` | 4,821 |
| [SLCMP86](candidates/SLCMP86.csv) | `163,750,000 < p <= 164,000,000` | 4,790 |
| [SLCMP87](candidates/SLCMP87.csv) | `164,000,000 < p <= 164,250,000` | 4,687 |
| [SLCMP88](candidates/SLCMP88.csv) | `164,250,000 < p <= 164,500,000` | 4,752 |
| [SLCMP89](candidates/SLCMP89.csv) | `164,500,000 < p <= 164,750,000` | 4,734 |
| [SLCMP90](candidates/SLCMP90.csv) | `164,750,000 < p <= 165,000,000` | 4,665 |
| [SLCMP91](candidates/SLCMP91.csv) | `165,000,000 < p <= 165,250,000` | 4,549 |
| [SLCMP92](candidates/SLCMP92.csv) | `165,250,000 < p <= 165,500,000` | 4,658 |
| [SLCMP93](candidates/SLCMP93.csv) | `165,500,000 < p <= 165,750,000` | 4,581 |
| [SLCMP94](candidates/SLCMP94.csv) | `165,750,000 < p <= 166,000,000` | 4,683 |
| [SLCMP95](candidates/SLCMP95.csv) | `166,000,000 < p <= 166,250,000` | 4,779 |
| [SLCMP96](candidates/SLCMP96.csv) | `166,250,000 < p <= 166,500,000` | 4,822 |
| [SLCMP97](candidates/SLCMP97.csv) | `166,500,000 < p <= 166,750,000` | 4,704 |
| [SLCMP98](candidates/SLCMP98.csv) | `166,750,000 < p <= 167,000,000` | 4,714 |
| [SLCMP99](candidates/SLCMP99.csv) | `167,000,000 < p <= 167,250,000` | 4,762 |
| [SLCMP100](candidates/SLCMP100.csv) | `167,250,000 < p <= 167,500,000` | 4,786 |
| [SLCMP101](candidates/SLCMP101.csv) | `167,500,000 < p <= 167,750,000` | 4,770 |
| [SLCMP102](candidates/SLCMP102.csv) | `167,750,000 < p <= 168,000,000` | 4,722 |
| [SLCMP103](candidates/SLCMP103.csv) | `168,000,000 < p <= 168,250,000` | 4,576 |
| [SLCMP104](candidates/SLCMP104.csv) | `168,250,000 < p <= 168,500,000` | 4,782 |
| [SLCMP105](candidates/SLCMP105.csv) | `168,500,000 < p <= 168,750,000` | 4,643 |
| [SLCMP106](candidates/SLCMP106.csv) | `168,750,000 < p <= 169,000,000` | 4,697 |
| [SLCMP107](candidates/SLCMP107.csv) | `169,000,000 < p <= 169,250,000` | 4,982 |
| [SLCMP108](candidates/SLCMP108.csv) | `169,250,000 < p <= 169,500,000` | 4,832 |
| [SLCMP109](candidates/SLCMP109.csv) | `169,500,000 < p <= 169,750,000` | 4,847 |
| [SLCMP110](candidates/SLCMP110.csv) | `169,750,000 < p <= 170,000,000` | 4,853 |
| [SLCMP111](candidates/SLCMP111.csv) | `170,000,000 < p <= 170,250,000` | 4,945 |
| [SLCMP112](candidates/SLCMP112.csv) | `170,250,000 < p <= 170,500,000` | 4,882 |
| [SLCMP113](candidates/SLCMP113.csv) | `170,500,000 < p <= 170,750,000` | 4,832 |
| [SLCMP114](candidates/SLCMP114.csv) | `170,750,000 < p <= 171,000,000` | 4,908 |
| [SLCMP115](candidates/SLCMP115.csv) | `171,000,000 < p <= 171,250,000` | 4,923 |
| [SLCMP116](candidates/SLCMP116.csv) | `171,250,000 < p <= 171,500,000` | 4,902 |
| [SLCMP117](candidates/SLCMP117.csv) | `171,500,000 < p <= 171,750,000` | 4,817 |
| [SLCMP118](candidates/SLCMP118.csv) | `171,750,000 < p <= 172,000,000` | 4,705 |
| [SLCMP119](candidates/SLCMP119.csv) | `172,000,000 < p <= 172,250,000` | 4,729 |
| [SLCMP120](candidates/SLCMP120.csv) | `172,250,000 < p <= 172,500,000` | 4,965 |
| [SLCMP121](candidates/SLCMP121.csv) | `172,500,000 < p <= 172,750,000` | 4,867 |
| [SLCMP122](candidates/SLCMP122.csv) | `172,750,000 < p <= 173,000,000` | 4,848 |
| [SLCMP123](candidates/SLCMP123.csv) | `173,000,000 < p <= 173,250,000` | 4,837 |
| [SLCMP124](candidates/SLCMP124.csv) | `173,250,000 < p <= 173,500,000` | 4,850 |
| [SLCMP125](candidates/SLCMP125.csv) | `173,500,000 < p <= 173,750,000` | 4,921 |
| [SLCMP126](candidates/SLCMP126.csv) | `173,750,000 < p <= 174,000,000` | 4,913 |
| [SLCMP127](candidates/SLCMP127.csv) | `174,000,000 < p <= 174,250,000` | 4,825 |
| [SLCMP128](candidates/SLCMP128.csv) | `174,250,000 < p <= 174,500,000` | 4,935 |
| [SLCMP129](candidates/SLCMP129.csv) | `174,500,000 < p <= 174,750,000` | 4,742 |
| [SLCMP130](candidates/SLCMP130.csv) | `174,750,000 < p <= 175,000,000` | 4,829 |
| [SLCMP131](candidates/SLCMP131.csv) | `175,000,000 < p <= 175,250,000` | 4,867 |
| [SLCMP132](candidates/SLCMP132.csv) | `175,250,000 < p <= 175,500,000` | 4,880 |
| [SLCMP133](candidates/SLCMP133.csv) | `175,500,000 < p <= 175,750,000` | 4,852 |
| [SLCMP134](candidates/SLCMP134.csv) | `175,750,000 < p <= 176,000,000` | 4,865 |
| [SLCMP135](candidates/SLCMP135.csv) | `176,000,000 < p <= 176,250,000` | 4,634 |
| [SLCMP136](candidates/SLCMP136.csv) | `176,250,000 < p <= 176,500,000` | 4,775 |
| [SLCMP137](candidates/SLCMP137.csv) | `176,500,000 < p <= 176,750,000` | 4,894 |
| [SLCMP138](candidates/SLCMP138.csv) | `176,750,000 < p <= 177,000,000` | 4,872 |
| [SLCMP139](candidates/SLCMP139.csv) | `177,000,000 < p <= 177,250,000` | 4,848 |
| [SLCMP140](candidates/SLCMP140.csv) | `177,250,000 < p <= 177,500,000` | 4,934 |
| [SLCMP141](candidates/SLCMP141.csv) | `177,500,000 < p <= 177,750,000` | 4,856 |
| [SLCMP142](candidates/SLCMP142.csv) | `177,750,000 < p <= 178,000,000` | 4,937 |
| [SLCMP143](candidates/SLCMP143.csv) | `178,000,000 < p <= 178,250,000` | 4,913 |
| [SLCMP144](candidates/SLCMP144.csv) | `178,250,000 < p <= 178,500,000` | 4,824 |
| [SLCMP145](candidates/SLCMP145.csv) | `178,500,000 < p <= 178,750,000` | 4,821 |
| [SLCMP146](candidates/SLCMP146.csv) | `178,750,000 < p <= 179,000,000` | 4,862 |
| [SLCMP147](candidates/SLCMP147.csv) | `179,000,000 < p <= 179,250,000` | 4,935 |
| [SLCMP148](candidates/SLCMP148.csv) | `179,250,000 < p <= 179,500,000` | 4,947 |
| [SLCMP149](candidates/SLCMP149.csv) | `179,500,000 < p <= 179,750,000` | 4,899 |
| [SLCMP150](candidates/SLCMP150.csv) | `179,750,000 < p <= 180,000,000` | 4,922 |
| [SLCMP151](candidates/SLCMP151.csv) | `180,000,000 < p <= 180,250,000` | 4,698 |
| [SLCMP152](candidates/SLCMP152.csv) | `180,250,000 < p <= 180,500,000` | 4,854 |
| [SLCMP153](candidates/SLCMP153.csv) | `180,500,000 < p <= 180,750,000` | 4,871 |
| [SLCMP154](candidates/SLCMP154.csv) | `180,750,000 < p <= 181,000,000` | 4,836 |
| [SLCMP155](candidates/SLCMP155.csv) | `181,000,000 < p <= 181,250,000` | 4,776 |
| [SLCMP156](candidates/SLCMP156.csv) | `181,250,000 < p <= 181,500,000` | 4,754 |
| [SLCMP157](candidates/SLCMP157.csv) | `181,500,000 < p <= 181,750,000` | 4,862 |
| [SLCMP158](candidates/SLCMP158.csv) | `181,750,000 < p <= 182,000,000` | 4,942 |
| [SLCMP159](candidates/SLCMP159.csv) | `182,000,000 < p <= 182,250,000` | 4,877 |
| [SLCMP160](candidates/SLCMP160.csv) | `182,250,000 < p <= 182,500,000` | 4,930 |
| [SLCMP161](candidates/SLCMP161.csv) | `182,500,000 < p <= 182,750,000` | 4,808 |
| [SLCMP162](candidates/SLCMP162.csv) | `182,750,000 < p <= 183,000,000` | 4,869 |
| [SLCMP163](candidates/SLCMP163.csv) | `183,000,000 < p <= 183,250,000` | 4,849 |
| [SLCMP164](candidates/SLCMP164.csv) | `183,250,000 < p <= 183,500,000` | 4,836 |
| [SLCMP165](candidates/SLCMP165.csv) | `183,500,000 < p <= 183,750,000` | 4,914 |
| [SLCMP166](candidates/SLCMP166.csv) | `183,750,000 < p <= 184,000,000` | 4,817 |
| [SLCMP167](candidates/SLCMP167.csv) | `184,000,000 < p <= 184,250,000` | 4,911 |
| [SLCMP168](candidates/SLCMP168.csv) | `184,250,000 < p <= 184,500,000` | 4,944 |
| [SLCMP169](candidates/SLCMP169.csv) | `184,500,000 < p <= 184,750,000` | 4,809 |
| [SLCMP170](candidates/SLCMP170.csv) | `184,750,000 < p <= 185,000,000` | 4,844 |
| [SLCMP171](candidates/SLCMP171.csv) | `185,000,000 < p <= 185,250,000` | 4,896 |
| [SLCMP172](candidates/SLCMP172.csv) | `185,250,000 < p <= 185,500,000` | 4,785 |
| [SLCMP173](candidates/SLCMP173.csv) | `185,500,000 < p <= 185,750,000` | 4,793 |
| [SLCMP174](candidates/SLCMP174.csv) | `185,750,000 < p <= 186,000,000` | 4,860 |
| [SLCMP175](candidates/SLCMP175.csv) | `186,000,000 < p <= 186,250,000` | 4,841 |
| [SLCMP176](candidates/SLCMP176.csv) | `186,250,000 < p <= 186,500,000` | 4,845 |
| [SLCMP177](candidates/SLCMP177.csv) | `186,500,000 < p <= 186,750,000` | 4,925 |
| [SLCMP178](candidates/SLCMP178.csv) | `186,750,000 < p <= 187,000,000` | 4,827 |
| [SLCMP179](candidates/SLCMP179.csv) | `187,000,000 < p <= 187,250,000` | 4,853 |
| [SLCMP180](candidates/SLCMP180.csv) | `187,250,000 < p <= 187,500,000` | 4,817 |
| [SLCMP181](candidates/SLCMP181.csv) | `187,500,000 < p <= 187,750,000` | 4,675 |
| [SLCMP182](candidates/SLCMP182.csv) | `187,750,000 < p <= 188,000,000` | 4,555 |
| [SLCMP183](candidates/SLCMP183.csv) | `188,000,000 < p <= 188,250,000` | 4,858 |
| [SLCMP184](candidates/SLCMP184.csv) | `188,250,000 < p <= 188,500,000` | 4,894 |
| [SLCMP185](candidates/SLCMP185.csv) | `188,500,000 < p <= 188,750,000` | 4,839 |
| [SLCMP186](candidates/SLCMP186.csv) | `188,750,000 < p <= 189,000,000` | 4,885 |
| [SLCMP187](candidates/SLCMP187.csv) | `189,000,000 < p <= 189,250,000` | 4,905 |
| [SLCMP188](candidates/SLCMP188.csv) | `189,250,000 < p <= 189,500,000` | 4,873 |
| [SLCMP189](candidates/SLCMP189.csv) | `189,500,000 < p <= 189,750,000` | 4,915 |
| [SLCMP190](candidates/SLCMP190.csv) | `189,750,000 < p <= 190,000,000` | 4,943 |
| [SLCMP191](candidates/SLCMP191.csv) | `190,000,000 < p <= 190,250,000` | 4,773 |
| [SLCMP192](candidates/SLCMP192.csv) | `190,250,000 < p <= 190,500,000` | 4,795 |
| [SLCMP193](candidates/SLCMP193.csv) | `190,500,000 < p <= 190,750,000` | 4,639 |
| [SLCMP194](candidates/SLCMP194.csv) | `190,750,000 < p <= 191,000,000` | 4,828 |
| [SLCMP195](candidates/SLCMP195.csv) | `191,000,000 < p <= 191,250,000` | 4,799 |
| [SLCMP196](candidates/SLCMP196.csv) | `191,250,000 < p <= 191,500,000` | 4,613 |
| [SLCMP197](candidates/SLCMP197.csv) | `191,500,000 < p <= 191,750,000` | 4,524 |
| [SLCMP198](candidates/SLCMP198.csv) | `191,750,000 < p <= 192,000,000` | 4,625 |
| [SLCMP199](candidates/SLCMP199.csv) | `192,000,000 < p <= 192,250,000` | 4,359 |
| [SLCMP200](candidates/SLCMP200.csv) | `192,250,000 < p <= 192,500,000` | 4,068 |
| [SLCMP201](candidates/SLCMP201.csv) | `192,500,000 < p <= 192,750,000` | 1,112 |
| [SLCMP202](candidates/SLCMP202.csv) | `192,750,000 < p <= 193,000,000` | 149 |
| [SLCMP203](candidates/SLCMP203.csv) | `193,000,000 < p <= 193,250,000` | 732 |
| [SLCMP204](candidates/SLCMP204.csv) | `193,250,000 < p <= 193,500,000` | 4,937 |
| [SLCMP205](candidates/SLCMP205.csv) | `193,500,000 < p <= 193,750,000` | 4,960 |
| [SLCMP206](candidates/SLCMP206.csv) | `193,750,000 < p <= 194,000,000` | 4,931 |
| [SLCMP207](candidates/SLCMP207.csv) | `194,000,000 < p <= 194,250,000` | 4,939 |
| [SLCMP208](candidates/SLCMP208.csv) | `194,250,000 < p <= 194,500,000` | 4,991 |
| [SLCMP209](candidates/SLCMP209.csv) | `194,500,000 < p <= 194,750,000` | 4,972 |
| [SLCMP210](candidates/SLCMP210.csv) | `194,750,000 < p <= 195,000,000` | 4,971 |
| [SLCMP211](candidates/SLCMP211.csv) | `195,000,000 < p <= 195,250,000` | 4,883 |
| [SLCMP212](candidates/SLCMP212.csv) | `195,250,000 < p <= 195,500,000` | 4,889 |
| [SLCMP213](candidates/SLCMP213.csv) | `195,500,000 < p <= 195,750,000` | 4,852 |
| [SLCMP214](candidates/SLCMP214.csv) | `195,750,000 < p <= 196,000,000` | 4,991 |
| [SLCMP215](candidates/SLCMP215.csv) | `196,000,000 < p <= 196,250,000` | 4,803 |
| [SLCMP216](candidates/SLCMP216.csv) | `196,250,000 < p <= 196,500,000` | 4,826 |
| [SLCMP217](candidates/SLCMP217.csv) | `196,500,000 < p <= 196,750,000` | 4,950 |
| [SLCMP218](candidates/SLCMP218.csv) | `196,750,000 < p <= 197,000,000` | 5,006 |
| [SLCMP219](candidates/SLCMP219.csv) | `197,000,000 < p <= 197,250,000` | 4,908 |
| [SLCMP220](candidates/SLCMP220.csv) | `197,250,000 < p <= 197,500,000` | 5,056 |
| [SLCMP221](candidates/SLCMP221.csv) | `197,500,000 < p <= 197,750,000` | 4,835 |
| [SLCMP222](candidates/SLCMP222.csv) | `197,750,000 < p <= 198,000,000` | 4,947 |
| [SLCMP223](candidates/SLCMP223.csv) | `198,000,000 < p <= 198,250,000` | 4,914 |
| [SLCMP224](candidates/SLCMP224.csv) | `198,250,000 < p <= 198,500,000` | 5,014 |
| [SLCMP225](candidates/SLCMP225.csv) | `198,500,000 < p <= 198,750,000` | 4,902 |
| [SLCMP226](candidates/SLCMP226.csv) | `198,750,000 < p <= 199,000,000` | 4,909 |
| [SLCMP227](candidates/SLCMP227.csv) | `199,000,000 < p <= 199,250,000` | 4,924 |
| [SLCMP228](candidates/SLCMP228.csv) | `199,250,000 < p <= 199,500,000` | 4,924 |
| [SLCMP229](candidates/SLCMP229.csv) | `199,500,000 < p <= 199,750,000` | 4,982 |
| [SLCMP230](candidates/SLCMP230.csv) | `199,750,000 < p <= 200,000,000` | 5,039 |
| [SLCMP231](candidates/SLCMP231.csv) | `200,000,000 < p <= 200,250,000` | 5,019 |
| [SLCMP232](candidates/SLCMP232.csv) | `200,250,000 < p <= 200,500,000` | 4,909 |
| [SLCMP233](candidates/SLCMP233.csv) | `200,500,000 < p <= 200,750,000` | 5,005 |
| [SLCMP234](candidates/SLCMP234.csv) | `200,750,000 < p <= 201,000,000` | 4,887 |
| [SLCMP235](candidates/SLCMP235.csv) | `201,000,000 < p <= 201,250,000` | 4,990 |
| [SLCMP236](candidates/SLCMP236.csv) | `201,250,000 < p <= 201,500,000` | 4,888 |
| [SLCMP237](candidates/SLCMP237.csv) | `201,500,000 < p <= 201,750,000` | 4,998 |
| [SLCMP238](candidates/SLCMP238.csv) | `201,750,000 < p <= 202,000,000` | 4,780 |
| [SLCMP239](candidates/SLCMP239.csv) | `202,000,000 < p <= 202,250,000` | 4,943 |
| [SLCMP240](candidates/SLCMP240.csv) | `202,250,000 < p <= 202,500,000` | 4,991 |
| [SLCMP241](candidates/SLCMP241.csv) | `202,500,000 < p <= 202,750,000` | 4,905 |
| [SLCMP242](candidates/SLCMP242.csv) | `202,750,000 < p <= 203,000,000` | 4,855 |
| [SLCMP243](candidates/SLCMP243.csv) | `203,000,000 < p <= 203,250,000` | 5,008 |
| [SLCMP244](candidates/SLCMP244.csv) | `203,250,000 < p <= 203,500,000` | 4,974 |
| [SLCMP245](candidates/SLCMP245.csv) | `203,500,000 < p <= 203,750,000` | 4,965 |
| [SLCMP246](candidates/SLCMP246.csv) | `203,750,000 < p <= 204,000,000` | 5,004 |
| [SLCMP247](candidates/SLCMP247.csv) | `204,000,000 < p <= 204,250,000` | 5,024 |
| [SLCMP248](candidates/SLCMP248.csv) | `204,250,000 < p <= 204,500,000` | 4,965 |
| [SLCMP249](candidates/SLCMP249.csv) | `204,500,000 < p <= 204,750,000` | 5,052 |
| [SLCMP250](candidates/SLCMP250.csv) | `204,750,000 < p <= 205,000,000` | 5,024 |
| [SLCMP251](candidates/SLCMP251.csv) | `205,000,000 < p <= 205,250,000` | 4,860 |
| [SLCMP252](candidates/SLCMP252.csv) | `205,250,000 < p <= 205,500,000` | 5,072 |
| [SLCMP253](candidates/SLCMP253.csv) | `205,500,000 < p <= 205,750,000` | 4,943 |
| [SLCMP254](candidates/SLCMP254.csv) | `205,750,000 < p <= 206,000,000` | 4,994 |
| [SLCMP255](candidates/SLCMP255.csv) | `206,000,000 < p <= 206,250,000` | 5,031 |
| [SLCMP256](candidates/SLCMP256.csv) | `206,250,000 < p <= 206,500,000` | 4,951 |
| [SLCMP257](candidates/SLCMP257.csv) | `206,500,000 < p <= 206,750,000` | 4,897 |
| [SLCMP258](candidates/SLCMP258.csv) | `206,750,000 < p <= 207,000,000` | 5,014 |
| [SLCMP259](candidates/SLCMP259.csv) | `207,000,000 < p <= 207,250,000` | 4,972 |
| [SLCMP260](candidates/SLCMP260.csv) | `207,250,000 < p <= 207,500,000` | 4,937 |
| [SLCMP261](candidates/SLCMP261.csv) | `207,500,000 < p <= 207,750,000` | 5,061 |
| [SLCMP262](candidates/SLCMP262.csv) | `207,750,000 < p <= 208,000,000` | 4,981 |
| [SLCMP263](candidates/SLCMP263.csv) | `208,000,000 < p <= 208,250,000` | 4,980 |
| [SLCMP264](candidates/SLCMP264.csv) | `208,250,000 < p <= 208,500,000` | 4,900 |
| [SLCMP265](candidates/SLCMP265.csv) | `208,500,000 < p <= 208,750,000` | 4,967 |
| [SLCMP266](candidates/SLCMP266.csv) | `208,750,000 < p <= 209,000,000` | 4,929 |
| [SLCMP267](candidates/SLCMP267.csv) | `209,000,000 < p <= 209,250,000` | 4,927 |
| [SLCMP268](candidates/SLCMP268.csv) | `209,250,000 < p <= 209,500,000` | 5,032 |
| [SLCMP269](candidates/SLCMP269.csv) | `209,500,000 < p <= 209,750,000` | 4,933 |
| [SLCMP270](candidates/SLCMP270.csv) | `209,750,000 < p <= 210,000,000` | 4,817 |
| [SLCMP271](candidates/SLCMP271.csv) | `210,000,000 < p <= 210,250,000` | 4,867 |
| [SLCMP272](candidates/SLCMP272.csv) | `210,250,000 < p <= 210,500,000` | 5,006 |
| [SLCMP273](candidates/SLCMP273.csv) | `210,500,000 < p <= 210,750,000` | 4,979 |
| [SLCMP274](candidates/SLCMP274.csv) | `210,750,000 < p <= 211,000,000` | 4,951 |
| [SLCMP275](candidates/SLCMP275.csv) | `211,000,000 < p <= 211,250,000` | 4,929 |
| [SLCMP276](candidates/SLCMP276.csv) | `211,250,000 < p <= 211,500,000` | 4,984 |
| [SLCMP277](candidates/SLCMP277.csv) | `211,500,000 < p <= 211,750,000` | 4,934 |
| [SLCMP278](candidates/SLCMP278.csv) | `211,750,000 < p <= 212,000,000` | 4,873 |
| [SLCMP279](candidates/SLCMP279.csv) | `212,000,000 < p <= 212,250,000` | 4,875 |
| [SLCMP280](candidates/SLCMP280.csv) | `212,250,000 < p <= 212,500,000` | 4,921 |
| [SLCMP281](candidates/SLCMP281.csv) | `212,500,000 < p <= 212,750,000` | 4,999 |
| [SLCMP282](candidates/SLCMP282.csv) | `212,750,000 < p <= 213,000,000` | 5,085 |
| [SLCMP283](candidates/SLCMP283.csv) | `213,000,000 < p <= 213,250,000` | 4,891 |
| [SLCMP284](candidates/SLCMP284.csv) | `213,250,000 < p <= 213,500,000` | 4,852 |
| [SLCMP285](candidates/SLCMP285.csv) | `213,500,000 < p <= 213,750,000` | 4,828 |
| [SLCMP286](candidates/SLCMP286.csv) | `213,750,000 < p <= 214,000,000` | 4,956 |
| [SLCMP287](candidates/SLCMP287.csv) | `214,000,000 < p <= 214,250,000` | 4,976 |
| [SLCMP288](candidates/SLCMP288.csv) | `214,250,000 < p <= 214,500,000` | 4,916 |
| [SLCMP289](candidates/SLCMP289.csv) | `214,500,000 < p <= 214,750,000` | 5,076 |
| [SLCMP290](candidates/SLCMP290.csv) | `214,750,000 < p <= 215,000,000` | 4,947 |
| [SLCMP291](candidates/SLCMP291.csv) | `215,000,000 < p <= 215,250,000` | 4,968 |
| [SLCMP292](candidates/SLCMP292.csv) | `215,250,000 < p <= 215,500,000` | 5,032 |
| [SLCMP293](candidates/SLCMP293.csv) | `215,500,000 < p <= 215,750,000` | 4,888 |
| [SLCMP294](candidates/SLCMP294.csv) | `215,750,000 < p <= 216,000,000` | 5,008 |
| [SLCMP295](candidates/SLCMP295.csv) | `216,000,000 < p <= 216,250,000` | 4,963 |
| [SLCMP296](candidates/SLCMP296.csv) | `216,250,000 < p <= 216,500,000` | 5,081 |
| [SLCMP297](candidates/SLCMP297.csv) | `216,500,000 < p <= 216,750,000` | 4,884 |
| [SLCMP298](candidates/SLCMP298.csv) | `216,750,000 < p <= 217,000,000` | 5,055 |
| [SLCMP299](candidates/SLCMP299.csv) | `217,000,000 < p <= 217,250,000` | 4,998 |
| [SLCMP300](candidates/SLCMP300.csv) | `217,250,000 < p <= 217,500,000` | 5,036 |
| [SLCMP301](candidates/SLCMP301.csv) | `217,500,000 < p <= 217,750,000` | 4,919 |
| [SLCMP302](candidates/SLCMP302.csv) | `217,750,000 < p <= 218,000,000` | 4,919 |
| [SLCMP303](candidates/SLCMP303.csv) | `218,000,000 < p <= 218,250,000` | 5,060 |
| [SLCMP304](candidates/SLCMP304.csv) | `218,250,000 < p <= 218,500,000` | 4,978 |
| [SLCMP305](candidates/SLCMP305.csv) | `218,500,000 < p <= 218,750,000` | 4,955 |
| [SLCMP306](candidates/SLCMP306.csv) | `218,750,000 < p <= 219,000,000` | 5,009 |
| [SLCMP307](candidates/SLCMP307.csv) | `219,000,000 < p <= 219,250,000` | 4,962 |
| [SLCMP308](candidates/SLCMP308.csv) | `219,250,000 < p <= 219,500,000` | 4,923 |
| [SLCMP309](candidates/SLCMP309.csv) | `219,500,000 < p <= 219,750,000` | 4,912 |
| [SLCMP310](candidates/SLCMP310.csv) | `219,750,000 < p <= 220,000,000` | 4,924 |
| [SLCMP311](candidates/SLCMP311.csv) | `220,000,000 < p <= 220,250,000` | 4,924 |
| [SLCMP312](candidates/SLCMP312.csv) | `220,250,000 < p <= 220,500,000` | 4,916 |
| [SLCMP313](candidates/SLCMP313.csv) | `220,500,000 < p <= 220,750,000` | 4,935 |
| [SLCMP314](candidates/SLCMP314.csv) | `220,750,000 < p <= 221,000,000` | 5,006 |
| [SLCMP315](candidates/SLCMP315.csv) | `221,000,000 < p <= 221,250,000` | 5,036 |
| [SLCMP316](candidates/SLCMP316.csv) | `221,250,000 < p <= 221,500,000` | 5,046 |
| [SLCMP317](candidates/SLCMP317.csv) | `221,500,000 < p <= 221,750,000` | 4,982 |
| [SLCMP318](candidates/SLCMP318.csv) | `221,750,000 < p <= 222,000,000` | 4,988 |
| [SLCMP319](candidates/SLCMP319.csv) | `222,000,000 < p <= 222,250,000` | 5,028 |
| [SLCMP320](candidates/SLCMP320.csv) | `222,250,000 < p <= 222,500,000` | 4,934 |
| [SLCMP321](candidates/SLCMP321.csv) | `222,500,000 < p <= 222,750,000` | 4,961 |
| [SLCMP322](candidates/SLCMP322.csv) | `222,750,000 < p <= 223,000,000` | 5,107 |
| [SLCMP323](candidates/SLCMP323.csv) | `223,000,000 < p <= 223,250,000` | 4,974 |
| [SLCMP324](candidates/SLCMP324.csv) | `223,250,000 < p <= 223,500,000` | 4,985 |
| [SLCMP325](candidates/SLCMP325.csv) | `223,500,000 < p <= 223,750,000` | 4,944 |
| [SLCMP326](candidates/SLCMP326.csv) | `223,750,000 < p <= 224,000,000` | 5,011 |
| [SLCMP327](candidates/SLCMP327.csv) | `224,000,000 < p <= 224,250,000` | 5,117 |
| [SLCMP328](candidates/SLCMP328.csv) | `224,250,000 < p <= 224,500,000` | 4,974 |
| [SLCMP329](candidates/SLCMP329.csv) | `224,500,000 < p <= 224,750,000` | 4,923 |
| [SLCMP330](candidates/SLCMP330.csv) | `224,750,000 < p <= 225,000,000` | 4,983 |
| [SLCMP331](candidates/SLCMP331.csv) | `225,000,000 < p <= 225,250,000` | 4,983 |
| [SLCMP332](candidates/SLCMP332.csv) | `225,250,000 < p <= 225,500,000` | 4,894 |
| [SLCMP333](candidates/SLCMP333.csv) | `225,500,000 < p <= 225,750,000` | 4,920 |
| [SLCMP334](candidates/SLCMP334.csv) | `225,750,000 < p <= 226,000,000` | 5,080 |
| [SLCMP335](candidates/SLCMP335.csv) | `226,000,000 < p <= 226,250,000` | 4,894 |
| [SLCMP336](candidates/SLCMP336.csv) | `226,250,000 < p <= 226,500,000` | 4,974 |
| [SLCMP337](candidates/SLCMP337.csv) | `226,500,000 < p <= 226,750,000` | 4,970 |
| [SLCMP338](candidates/SLCMP338.csv) | `226,750,000 < p <= 227,000,000` | 4,943 |
| [SLCMP339](candidates/SLCMP339.csv) | `227,000,000 < p <= 227,250,000` | 4,929 |
| [SLCMP340](candidates/SLCMP340.csv) | `227,250,000 < p <= 227,500,000` | 5,023 |
| [SLCMP341](candidates/SLCMP341.csv) | `227,500,000 < p <= 227,750,000` | 4,963 |
| [SLCMP342](candidates/SLCMP342.csv) | `227,750,000 < p <= 228,000,000` | 4,999 |
| [SLCMP343](candidates/SLCMP343.csv) | `228,000,000 < p <= 228,250,000` | 4,966 |
| [SLCMP344](candidates/SLCMP344.csv) | `228,250,000 < p <= 228,500,000` | 4,962 |
| [SLCMP345](candidates/SLCMP345.csv) | `228,500,000 < p <= 228,750,000` | 5,019 |
| [SLCMP346](candidates/SLCMP346.csv) | `228,750,000 < p <= 229,000,000` | 4,965 |
| [SLCMP347](candidates/SLCMP347.csv) | `229,000,000 < p <= 229,250,000` | 4,692 |
| [SLCMP348](candidates/SLCMP348.csv) | `229,250,000 < p <= 229,500,000` | 4,780 |
| [SLCMP349](candidates/SLCMP349.csv) | `229,500,000 < p <= 229,750,000` | 4,848 |
| [SLCMP350](candidates/SLCMP350.csv) | `229,750,000 < p <= 230,000,000` | 4,917 |
| [SLCMP351](candidates/SLCMP351.csv) | `230,000,000 < p <= 230,250,000` | 4,939 |
| [SLCMP352](candidates/SLCMP352.csv) | `230,250,000 < p <= 230,500,000` | 4,987 |
| [SLCMP353](candidates/SLCMP353.csv) | `230,500,000 < p <= 230,750,000` | 5,047 |
| [SLCMP354](candidates/SLCMP354.csv) | `230,750,000 < p <= 231,000,000` | 4,939 |
| [SLCMP355](candidates/SLCMP355.csv) | `231,000,000 < p <= 231,250,000` | 5,064 |
| [SLCMP356](candidates/SLCMP356.csv) | `231,250,000 < p <= 231,500,000` | 5,101 |
| [SLCMP357](candidates/SLCMP357.csv) | `231,500,000 < p <= 231,750,000` | 4,845 |
| [SLCMP358](candidates/SLCMP358.csv) | `231,750,000 < p <= 232,000,000` | 5,045 |
| [SLCMP359](candidates/SLCMP359.csv) | `232,000,000 < p <= 232,250,000` | 4,942 |
| [SLCMP360](candidates/SLCMP360.csv) | `232,250,000 < p <= 232,500,000` | 5,054 |
| [SLCMP361](candidates/SLCMP361.csv) | `232,500,000 < p <= 232,750,000` | 5,004 |
| [SLCMP362](candidates/SLCMP362.csv) | `232,750,000 < p <= 233,000,000` | 4,938 |
| [SLCMP363](candidates/SLCMP363.csv) | `233,000,000 < p <= 233,250,000` | 4,901 |
| [SLCMP364](candidates/SLCMP364.csv) | `233,250,000 < p <= 233,500,000` | 5,054 |
| [SLCMP365](candidates/SLCMP365.csv) | `233,500,000 < p <= 233,750,000` | 5,063 |
| [SLCMP366](candidates/SLCMP366.csv) | `233,750,000 < p <= 234,000,000` | 5,024 |
| [SLCMP367](candidates/SLCMP367.csv) | `234,000,000 < p <= 234,250,000` | 4,950 |
| [SLCMP368](candidates/SLCMP368.csv) | `234,250,000 < p <= 234,500,000` | 4,948 |
| [SLCMP369](candidates/SLCMP369.csv) | `234,500,000 < p <= 234,750,000` | 4,936 |
| [SLCMP370](candidates/SLCMP370.csv) | `234,750,000 < p <= 235,000,000` | 4,961 |
| [SLCMP371](candidates/SLCMP371.csv) | `235,000,000 < p <= 235,250,000` | 4,934 |
| [SLCMP372](candidates/SLCMP372.csv) | `235,250,000 < p <= 235,500,000` | 4,964 |
| [SLCMP373](candidates/SLCMP373.csv) | `235,500,000 < p <= 235,750,000` | 4,949 |
| [SLCMP374](candidates/SLCMP374.csv) | `235,750,000 < p <= 236,000,000` | 4,869 |
| [SLCMP375](candidates/SLCMP375.csv) | `236,000,000 < p <= 236,250,000` | 5,013 |
| [SLCMP376](candidates/SLCMP376.csv) | `236,250,000 < p <= 236,500,000` | 4,910 |
| [SLCMP377](candidates/SLCMP377.csv) | `236,500,000 < p <= 236,750,000` | 4,965 |
| [SLCMP378](candidates/SLCMP378.csv) | `236,750,000 < p <= 237,000,000` | 4,960 |
| [SLCMP379](candidates/SLCMP379.csv) | `237,000,000 < p <= 237,250,000` | 4,994 |
| [SLCMP380](candidates/SLCMP380.csv) | `237,250,000 < p <= 237,500,000` | 4,906 |
| [SLCMP381](candidates/SLCMP381.csv) | `237,500,000 < p <= 237,750,000` | 5,009 |
| [SLCMP382](candidates/SLCMP382.csv) | `237,750,000 < p <= 238,000,000` | 4,962 |
| [SLCMP383](candidates/SLCMP383.csv) | `238,000,000 < p <= 238,250,000` | 4,922 |
| [SLCMP384](candidates/SLCMP384.csv) | `238,250,000 < p <= 238,500,000` | 5,005 |
| [SLCMP385](candidates/SLCMP385.csv) | `238,500,000 < p <= 238,750,000` | 5,042 |
| [SLCMP386](candidates/SLCMP386.csv) | `238,750,000 < p <= 239,000,000` | 4,948 |
| [SLCMP387](candidates/SLCMP387.csv) | `239,000,000 < p <= 239,250,000` | 4,903 |
| [SLCMP388](candidates/SLCMP388.csv) | `239,250,000 < p <= 239,500,000` | 5,031 |
| [SLCMP389](candidates/SLCMP389.csv) | `239,500,000 < p <= 239,750,000` | 4,944 |
| [SLCMP390](candidates/SLCMP390.csv) | `239,750,000 < p <= 240,000,000` | 4,950 |
| [SLCMP391](candidates/SLCMP391.csv) | `240,000,000 < p <= 240,250,000` | 4,950 |
| [SLCMP392](candidates/SLCMP392.csv) | `240,250,000 < p <= 240,500,000` | 4,976 |
| [SLCMP393](candidates/SLCMP393.csv) | `240,500,000 < p <= 240,750,000` | 5,064 |
| [SLCMP394](candidates/SLCMP394.csv) | `240,750,000 < p <= 241,000,000` | 4,939 |
| [SLCMP395](candidates/SLCMP395.csv) | `241,000,000 < p <= 241,250,000` | 5,003 |
| [SLCMP396](candidates/SLCMP396.csv) | `241,250,000 < p <= 241,500,000` | 4,981 |
| [SLCMP397](candidates/SLCMP397.csv) | `241,500,000 < p <= 241,750,000` | 4,942 |
| [SLCMP398](candidates/SLCMP398.csv) | `241,750,000 < p <= 242,000,000` | 5,021 |
| [SLCMP399](candidates/SLCMP399.csv) | `242,000,000 < p <= 242,250,000` | 4,878 |
| [SLCMP400](candidates/SLCMP400.csv) | `242,250,000 < p <= 242,500,000` | 4,956 |
| [SLCMP401](candidates/SLCMP401.csv) | `242,500,000 < p <= 242,750,000` | 4,847 |
| [SLCMP402](candidates/SLCMP402.csv) | `242,750,000 < p <= 243,000,000` | 4,964 |
| [SLCMP403](candidates/SLCMP403.csv) | `243,000,000 < p <= 243,250,000` | 4,985 |
| [SLCMP404](candidates/SLCMP404.csv) | `243,250,000 < p <= 243,500,000` | 4,985 |
| [SLCMP405](candidates/SLCMP405.csv) | `243,500,000 < p <= 243,750,000` | 4,976 |
| [SLCMP406](candidates/SLCMP406.csv) | `243,750,000 < p <= 244,000,000` | 5,029 |
| [SLCMP407](candidates/SLCMP407.csv) | `244,000,000 < p <= 244,250,000` | 4,911 |
| [SLCMP408](candidates/SLCMP408.csv) | `244,250,000 < p <= 244,500,000` | 4,963 |
| [SLCMP409](candidates/SLCMP409.csv) | `244,500,000 < p <= 244,750,000` | 5,041 |
| [SLCMP410](candidates/SLCMP410.csv) | `244,750,000 < p <= 245,000,000` | 5,010 |
| [SLCMP411](candidates/SLCMP411.csv) | `245,000,000 < p <= 245,250,000` | 4,985 |
| [SLCMP412](candidates/SLCMP412.csv) | `245,250,000 < p <= 245,500,000` | 5,057 |
| [SLCMP413](candidates/SLCMP413.csv) | `245,500,000 < p <= 245,750,000` | 4,886 |
| [SLCMP414](candidates/SLCMP414.csv) | `245,750,000 < p <= 246,000,000` | 5,027 |
| [SLCMP415](candidates/SLCMP415.csv) | `246,000,000 < p <= 246,250,000` | 4,881 |
| [SLCMP416](candidates/SLCMP416.csv) | `246,250,000 < p <= 246,500,000` | 4,877 |
| [SLCMP417](candidates/SLCMP417.csv) | `246,500,000 < p <= 246,750,000` | 5,062 |
| [SLCMP418](candidates/SLCMP418.csv) | `246,750,000 < p <= 247,000,000` | 4,896 |
| [SLCMP419](candidates/SLCMP419.csv) | `247,000,000 < p <= 247,250,000` | 5,003 |
| [SLCMP420](candidates/SLCMP420.csv) | `247,250,000 < p <= 247,500,000` | 5,029 |
| [SLCMP421](candidates/SLCMP421.csv) | `247,500,000 < p <= 247,750,000` | 4,897 |
| [SLCMP422](candidates/SLCMP422.csv) | `247,750,000 < p <= 248,000,000` | 4,946 |
| [SLCMP423](candidates/SLCMP423.csv) | `248,000,000 < p <= 248,250,000` | 4,990 |
| [SLCMP424](candidates/SLCMP424.csv) | `248,250,000 < p <= 248,500,000` | 4,936 |
| [SLCMP425](candidates/SLCMP425.csv) | `248,500,000 < p <= 248,750,000` | 5,012 |
| [SLCMP426](candidates/SLCMP426.csv) | `248,750,000 < p <= 249,000,000` | 4,885 |
| [SLCMP427](candidates/SLCMP427.csv) | `249,000,000 < p <= 249,250,000` | 5,098 |
| [SLCMP428](candidates/SLCMP428.csv) | `249,250,000 < p <= 249,500,000` | 4,945 |
| [SLCMP429](candidates/SLCMP429.csv) | `249,500,000 < p <= 249,750,000` | 5,047 |
| [SLCMP430](candidates/SLCMP430.csv) | `249,750,000 < p <= 250,000,000` | 4,981 |
| [SLCMP431](candidates/SLCMP431.csv) | `250,000,000 < p <= 250,250,000` | 4,882 |
| [SLCMP432](candidates/SLCMP432.csv) | `250,250,000 < p <= 250,500,000` | 4,915 |
| [SLCMP433](candidates/SLCMP433.csv) | `250,500,000 < p <= 250,750,000` | 4,891 |
| [SLCMP434](candidates/SLCMP434.csv) | `250,750,000 < p <= 251,000,000` | 4,989 |
| [SLCMP435](candidates/SLCMP435.csv) | `251,000,000 < p <= 251,250,000` | 4,903 |
| [SLCMP436](candidates/SLCMP436.csv) | `251,250,000 < p <= 251,500,000` | 4,785 |
| [SLCMP437](candidates/SLCMP437.csv) | `251,500,000 < p <= 251,750,000` | 4,940 |
| [SLCMP438](candidates/SLCMP438.csv) | `251,750,000 < p <= 252,000,000` | 4,948 |
| [SLCMP439](candidates/SLCMP439.csv) | `252,000,000 < p <= 252,250,000` | 5,028 |
| [SLCMP440](candidates/SLCMP440.csv) | `252,250,000 < p <= 252,500,000` | 4,994 |
| [SLCMP441](candidates/SLCMP441.csv) | `252,500,000 < p <= 252,750,000` | 5,062 |
| [SLCMP442](candidates/SLCMP442.csv) | `252,750,000 < p <= 253,000,000` | 4,920 |
| [SLCMP443](candidates/SLCMP443.csv) | `253,000,000 < p <= 253,250,000` | 4,932 |
| [SLCMP444](candidates/SLCMP444.csv) | `253,250,000 < p <= 253,500,000` | 5,159 |
| [SLCMP445](candidates/SLCMP445.csv) | `253,500,000 < p <= 253,750,000` | 5,018 |
| [SLCMP446](candidates/SLCMP446.csv) | `253,750,000 < p <= 254,000,000` | 4,975 |
| [SLCMP447](candidates/SLCMP447.csv) | `254,000,000 < p <= 254,250,000` | 4,944 |
| [SLCMP448](candidates/SLCMP448.csv) | `254,250,000 < p <= 254,500,000` | 4,874 |
| [SLCMP449](candidates/SLCMP449.csv) | `254,500,000 < p <= 254,750,000` | 4,993 |
| [SLCMP450](candidates/SLCMP450.csv) | `254,750,000 < p <= 255,000,000` | 4,924 |
| [SLCMP451](candidates/SLCMP451.csv) | `255,000,000 < p <= 255,250,000` | 4,912 |
| [SLCMP452](candidates/SLCMP452.csv) | `255,250,000 < p <= 255,500,000` | 5,026 |
| [SLCMP453](candidates/SLCMP453.csv) | `255,500,000 < p <= 255,750,000` | 5,017 |
| [SLCMP454](candidates/SLCMP454.csv) | `255,750,000 < p <= 256,000,000` | 5,031 |
| [SLCMP455](candidates/SLCMP455.csv) | `256,000,000 < p <= 256,250,000` | 4,942 |
| [SLCMP456](candidates/SLCMP456.csv) | `256,250,000 < p <= 256,500,000` | 4,862 |
| [SLCMP457](candidates/SLCMP457.csv) | `256,500,000 < p <= 256,750,000` | 4,947 |
| [SLCMP458](candidates/SLCMP458.csv) | `256,750,000 < p <= 257,000,000` | 5,052 |
| [SLCMP459](candidates/SLCMP459.csv) | `257,000,000 < p <= 257,250,000` | 4,995 |
| [SLCMP460](candidates/SLCMP460.csv) | `257,250,000 < p <= 257,500,000` | 5,083 |
| [SLCMP461](candidates/SLCMP461.csv) | `257,500,000 < p <= 257,750,000` | 4,963 |
| [SLCMP462](candidates/SLCMP462.csv) | `257,750,000 < p <= 258,000,000` | 5,035 |
| [SLCMP463](candidates/SLCMP463.csv) | `258,000,000 < p <= 258,250,000` | 4,979 |
| [SLCMP464](candidates/SLCMP464.csv) | `258,250,000 < p <= 258,500,000` | 4,940 |
| [SLCMP465](candidates/SLCMP465.csv) | `258,500,000 < p <= 258,750,000` | 5,022 |
| [SLCMP466](candidates/SLCMP466.csv) | `258,750,000 < p <= 259,000,000` | 4,966 |
| [SLCMP467](candidates/SLCMP467.csv) | `259,000,000 < p <= 259,250,000` | 4,880 |
| [SLCMP468](candidates/SLCMP468.csv) | `259,250,000 < p <= 259,500,000` | 5,005 |
| [SLCMP469](candidates/SLCMP469.csv) | `259,500,000 < p <= 259,750,000` | 4,938 |
| [SLCMP470](candidates/SLCMP470.csv) | `259,750,000 < p <= 260,000,000` | 4,880 |
| [SLCMP471](candidates/SLCMP471.csv) | `260,000,000 < p <= 260,250,000` | 4,981 |
| [SLCMP472](candidates/SLCMP472.csv) | `260,250,000 < p <= 260,500,000` | 4,967 |
| [SLCMP473](candidates/SLCMP473.csv) | `260,500,000 < p <= 260,750,000` | 4,946 |
| [SLCMP474](candidates/SLCMP474.csv) | `260,750,000 < p <= 261,000,000` | 4,962 |
| [SLCMP475](candidates/SLCMP475.csv) | `261,000,000 < p <= 261,250,000` | 4,924 |
| [SLCMP476](candidates/SLCMP476.csv) | `261,250,000 < p <= 261,500,000` | 5,008 |
| [SLCMP477](candidates/SLCMP477.csv) | `261,500,000 < p <= 261,750,000` | 4,965 |
| [SLCMP478](candidates/SLCMP478.csv) | `261,750,000 < p <= 262,000,000` | 4,961 |
| [SLCMP479](candidates/SLCMP479.csv) | `262,000,000 < p <= 262,250,000` | 5,061 |
| [SLCMP480](candidates/SLCMP480.csv) | `262,250,000 < p <= 262,500,000` | 4,953 |
| [SLCMP481](candidates/SLCMP481.csv) | `262,500,000 < p <= 262,750,000` | 5,004 |
| [SLCMP482](candidates/SLCMP482.csv) | `262,750,000 < p <= 263,000,000` | 4,969 |
| [SLCMP483](candidates/SLCMP483.csv) | `263,000,000 < p <= 263,250,000` | 4,938 |
| [SLCMP484](candidates/SLCMP484.csv) | `263,250,000 < p <= 263,500,000` | 4,858 |
| [SLCMP485](candidates/SLCMP485.csv) | `263,500,000 < p <= 263,750,000` | 4,822 |
| [SLCMP486](candidates/SLCMP486.csv) | `263,750,000 < p <= 264,000,000` | 5,057 |
| [SLCMP487](candidates/SLCMP487.csv) | `264,000,000 < p <= 264,250,000` | 4,847 |
| [SLCMP488](candidates/SLCMP488.csv) | `264,250,000 < p <= 264,500,000` | 4,963 |
| [SLCMP489](candidates/SLCMP489.csv) | `264,500,000 < p <= 264,750,000` | 4,923 |
| [SLCMP490](candidates/SLCMP490.csv) | `264,750,000 < p <= 265,000,000` | 5,074 |
| [SLCMP491](candidates/SLCMP491.csv) | `265,000,000 < p <= 265,250,000` | 4,932 |
| [SLCMP492](candidates/SLCMP492.csv) | `265,250,000 < p <= 265,500,000` | 4,953 |
| [SLCMP493](candidates/SLCMP493.csv) | `265,500,000 < p <= 265,750,000` | 4,939 |
| [SLCMP494](candidates/SLCMP494.csv) | `265,750,000 < p <= 266,000,000` | 4,944 |
| [SLCMP495](candidates/SLCMP495.csv) | `266,000,000 < p <= 266,250,000` | 4,927 |
| [SLCMP496](candidates/SLCMP496.csv) | `266,250,000 < p <= 266,500,000` | 4,830 |
| [SLCMP497](candidates/SLCMP497.csv) | `266,500,000 < p <= 266,750,000` | 4,948 |
| [SLCMP498](candidates/SLCMP498.csv) | `266,750,000 < p <= 267,000,000` | 4,985 |
| [SLCMP499](candidates/SLCMP499.csv) | `267,000,000 < p <= 267,250,000` | 5,075 |
| [SLCMP500](candidates/SLCMP500.csv) | `267,250,000 < p <= 267,500,000` | 4,913 |
| [SLCMP501](candidates/SLCMP501.csv) | `267,500,000 < p <= 267,750,000` | 5,015 |
| [SLCMP502](candidates/SLCMP502.csv) | `267,750,000 < p <= 268,000,000` | 5,080 |
| [SLCMP503](candidates/SLCMP503.csv) | `268,000,000 < p <= 268,250,000` | 4,960 |
| [SLCMP504](candidates/SLCMP504.csv) | `268,250,000 < p <= 268,500,000` | 4,985 |
| [SLCMP505](candidates/SLCMP505.csv) | `268,500,000 < p <= 268,750,000` | 4,948 |
| [SLCMP506](candidates/SLCMP506.csv) | `268,750,000 < p <= 269,000,000` | 4,972 |
| [SLCMP507](candidates/SLCMP507.csv) | `269,000,000 < p <= 269,250,000` | 5,047 |
| [SLCMP508](candidates/SLCMP508.csv) | `269,250,000 < p <= 269,500,000` | 4,945 |
| [SLCMP509](candidates/SLCMP509.csv) | `269,500,000 < p <= 269,750,000` | 4,951 |
| [SLCMP510](candidates/SLCMP510.csv) | `269,750,000 < p <= 270,000,000` | 4,859 |
| [SLCMP511](candidates/SLCMP511.csv) | `270,000,000 < p <= 270,250,000` | 4,951 |
| [SLCMP512](candidates/SLCMP512.csv) | `270,250,000 < p <= 270,500,000` | 4,965 |
| [SLCMP513](candidates/SLCMP513.csv) | `270,500,000 < p <= 270,750,000` | 4,920 |
| [SLCMP514](candidates/SLCMP514.csv) | `270,750,000 < p <= 271,000,000` | 4,945 |
| [SLCMP515](candidates/SLCMP515.csv) | `271,000,000 < p <= 271,250,000` | 4,997 |
| [SLCMP516](candidates/SLCMP516.csv) | `271,250,000 < p <= 271,500,000` | 5,029 |
| [SLCMP517](candidates/SLCMP517.csv) | `271,500,000 < p <= 271,750,000` | 4,955 |
| [SLCMP518](candidates/SLCMP518.csv) | `271,750,000 < p <= 272,000,000` | 4,928 |
| [SLCMP519](candidates/SLCMP519.csv) | `272,000,000 < p <= 272,250,000` | 4,913 |
| [SLCMP520](candidates/SLCMP520.csv) | `272,250,000 < p <= 272,500,000` | 4,985 |
| [SLCMP521](candidates/SLCMP521.csv) | `272,500,000 < p <= 272,750,000` | 4,959 |
| [SLCMP522](candidates/SLCMP522.csv) | `272,750,000 < p <= 273,000,000` | 4,873 |
| [SLCMP523](candidates/SLCMP523.csv) | `273,000,000 < p <= 273,250,000` | 4,950 |
| [SLCMP524](candidates/SLCMP524.csv) | `273,250,000 < p <= 273,500,000` | 5,061 |
| [SLCMP525](candidates/SLCMP525.csv) | `273,500,000 < p <= 273,750,000` | 4,909 |
| [SLCMP526](candidates/SLCMP526.csv) | `273,750,000 < p <= 274,000,000` | 4,976 |
| **Total** |  | **2,465,462** |

Each export link opens that test's complete candidate table. Every exponent
remains a primality-unassigned search input.

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
