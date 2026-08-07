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
| [SLCMP33](candidates/SLCMP33.csv) | $150{,}500{,}000<p\leq150{,}750{,}000$ | 4,557 |
| [SLCMP34](candidates/SLCMP34.csv) | $150{,}750{,}000<p\leq151{,}000{,}000$ | 4,478 |
| [SLCMP35](candidates/SLCMP35.csv) | $151{,}000{,}000<p\leq151{,}250{,}000$ | 4,564 |
| [SLCMP36](candidates/SLCMP36.csv) | $151{,}250{,}000<p\leq151{,}500{,}000$ | 4,467 |
| [SLCMP37](candidates/SLCMP37.csv) | $151{,}500{,}000<p\leq151{,}750{,}000$ | 4,528 |
| [SLCMP38](candidates/SLCMP38.csv) | $151{,}750{,}000<p\leq152{,}000{,}000$ | 4,572 |
| [SLCMP39](candidates/SLCMP39.csv) | $152{,}000{,}000<p\leq152{,}250{,}000$ | 4,500 |
| [SLCMP40](candidates/SLCMP40.csv) | $152{,}250{,}000<p\leq152{,}500{,}000$ | 4,534 |
| [SLCMP41](candidates/SLCMP41.csv) | $152{,}500{,}000<p\leq152{,}750{,}000$ | 4,566 |
| [SLCMP42](candidates/SLCMP42.csv) | $152{,}750{,}000<p\leq153{,}000{,}000$ | 4,413 |
| [SLCMP43](candidates/SLCMP43.csv) | $153{,}000{,}000<p\leq153{,}250{,}000$ | 4,625 |
| [SLCMP44](candidates/SLCMP44.csv) | $153{,}250{,}000<p\leq153{,}500{,}000$ | 4,512 |
| [SLCMP45](candidates/SLCMP45.csv) | $153{,}500{,}000<p\leq153{,}750{,}000$ | 4,534 |
| [SLCMP46](candidates/SLCMP46.csv) | $153{,}750{,}000<p\leq154{,}000{,}000$ | 3,885 |
| [SLCMP47](candidates/SLCMP47.csv) | $154{,}000{,}000<p\leq154{,}250{,}000$ | 3,435 |
| [SLCMP48](candidates/SLCMP48.csv) | $154{,}250{,}000<p\leq154{,}500{,}000$ | 4,505 |
| [SLCMP49](candidates/SLCMP49.csv) | $154{,}500{,}000<p\leq154{,}750{,}000$ | 4,556 |
| [SLCMP50](candidates/SLCMP50.csv) | $154{,}750{,}000<p\leq155{,}000{,}000$ | 4,514 |
| [SLCMP51](candidates/SLCMP51.csv) | $155{,}000{,}000<p\leq155{,}250{,}000$ | 4,546 |
| [SLCMP52](candidates/SLCMP52.csv) | $155{,}250{,}000<p\leq155{,}500{,}000$ | 4,351 |
| [SLCMP53](candidates/SLCMP53.csv) | $155{,}500{,}000<p\leq155{,}750{,}000$ | 4,414 |
| [SLCMP54](candidates/SLCMP54.csv) | $155{,}750{,}000<p\leq156{,}000{,}000$ | 4,402 |
| [SLCMP55](candidates/SLCMP55.csv) | $156{,}000{,}000<p\leq156{,}250{,}000$ | 4,535 |
| [SLCMP56](candidates/SLCMP56.csv) | $156{,}250{,}000<p\leq156{,}500{,}000$ | 4,533 |
| [SLCMP57](candidates/SLCMP57.csv) | $156{,}500{,}000<p\leq156{,}750{,}000$ | 4,400 |
| [SLCMP58](candidates/SLCMP58.csv) | $156{,}750{,}000<p\leq157{,}000{,}000$ | 4,512 |
| [SLCMP59](candidates/SLCMP59.csv) | $157{,}000{,}000<p\leq157{,}250{,}000$ | 4,507 |
| [SLCMP60](candidates/SLCMP60.csv) | $157{,}250{,}000<p\leq157{,}500{,}000$ | 4,458 |
| [SLCMP61](candidates/SLCMP61.csv) | $157{,}500{,}000<p\leq157{,}750{,}000$ | 4,502 |
| [SLCMP62](candidates/SLCMP62.csv) | $157{,}750{,}000<p\leq158{,}000{,}000$ | 4,518 |
| [SLCMP63](candidates/SLCMP63.csv) | $158{,}000{,}000<p\leq158{,}250{,}000$ | 4,397 |
| [SLCMP64](candidates/SLCMP64.csv) | $158{,}250{,}000<p\leq158{,}500{,}000$ | 4,441 |
| [SLCMP65](candidates/SLCMP65.csv) | $158{,}500{,}000<p\leq158{,}750{,}000$ | 4,386 |
| [SLCMP66](candidates/SLCMP66.csv) | $158{,}750{,}000<p\leq159{,}000{,}000$ | 4,468 |
| [SLCMP67](candidates/SLCMP67.csv) | $159{,}000{,}000<p\leq159{,}250{,}000$ | 4,200 |
| [SLCMP68](candidates/SLCMP68.csv) | $159{,}250{,}000<p\leq159{,}500{,}000$ | 4,375 |
| [SLCMP69](candidates/SLCMP69.csv) | $159{,}500{,}000<p\leq159{,}750{,}000$ | 4,336 |
| [SLCMP70](candidates/SLCMP70.csv) | $159{,}750{,}000<p\leq160{,}000{,}000$ | 4,393 |
| [SLCMP71](candidates/SLCMP71.csv) | $160{,}000{,}000<p\leq160{,}250{,}000$ | 4,280 |
| [SLCMP72](candidates/SLCMP72.csv) | $160{,}250{,}000<p\leq160{,}500{,}000$ | 3,765 |
| [SLCMP73](candidates/SLCMP73.csv) | $160{,}500{,}000<p\leq160{,}750{,}000$ | 4,215 |
| [SLCMP74](candidates/SLCMP74.csv) | $160{,}750{,}000<p\leq161{,}000{,}000$ | 4,079 |
| [SLCMP75](candidates/SLCMP75.csv) | $161{,}000{,}000<p\leq161{,}250{,}000$ | 4,226 |
| [SLCMP76](candidates/SLCMP76.csv) | $161{,}250{,}000<p\leq161{,}500{,}000$ | 4,108 |
| [SLCMP77](candidates/SLCMP77.csv) | $161{,}500{,}000<p\leq161{,}750{,}000$ | 3,650 |
| [SLCMP78](candidates/SLCMP78.csv) | $161{,}750{,}000<p\leq162{,}000{,}000$ | 4,216 |
| [SLCMP79](candidates/SLCMP79.csv) | $162{,}000{,}000<p\leq162{,}250{,}000$ | 4,646 |
| [SLCMP80](candidates/SLCMP80.csv) | $162{,}250{,}000<p\leq162{,}500{,}000$ | 4,200 |
| [SLCMP81](candidates/SLCMP81.csv) | $162{,}500{,}000<p\leq162{,}750{,}000$ | 4,327 |
| [SLCMP82](candidates/SLCMP82.csv) | $162{,}750{,}000<p\leq163{,}000{,}000$ | 4,643 |
| [SLCMP83](candidates/SLCMP83.csv) | $163{,}000{,}000<p\leq163{,}250{,}000$ | 2,667 |
| [SLCMP84](candidates/SLCMP84.csv) | $163{,}250{,}000<p\leq163{,}500{,}000$ | 4,893 |
| [SLCMP85](candidates/SLCMP85.csv) | $163{,}500{,}000<p\leq163{,}750{,}000$ | 4,821 |
| [SLCMP86](candidates/SLCMP86.csv) | $163{,}750{,}000<p\leq164{,}000{,}000$ | 4,790 |
| [SLCMP87](candidates/SLCMP87.csv) | $164{,}000{,}000<p\leq164{,}250{,}000$ | 4,687 |
| [SLCMP88](candidates/SLCMP88.csv) | $164{,}250{,}000<p\leq164{,}500{,}000$ | 4,752 |
| [SLCMP89](candidates/SLCMP89.csv) | $164{,}500{,}000<p\leq164{,}750{,}000$ | 4,734 |
| [SLCMP90](candidates/SLCMP90.csv) | $164{,}750{,}000<p\leq165{,}000{,}000$ | 4,665 |
| [SLCMP91](candidates/SLCMP91.csv) | $165{,}000{,}000<p\leq165{,}250{,}000$ | 4,549 |
| [SLCMP92](candidates/SLCMP92.csv) | $165{,}250{,}000<p\leq165{,}500{,}000$ | 4,658 |
| [SLCMP93](candidates/SLCMP93.csv) | $165{,}500{,}000<p\leq165{,}750{,}000$ | 4,581 |
| [SLCMP94](candidates/SLCMP94.csv) | $165{,}750{,}000<p\leq166{,}000{,}000$ | 4,683 |
| [SLCMP95](candidates/SLCMP95.csv) | $166{,}000{,}000<p\leq166{,}250{,}000$ | 4,779 |
| [SLCMP96](candidates/SLCMP96.csv) | $166{,}250{,}000<p\leq166{,}500{,}000$ | 4,822 |
| [SLCMP97](candidates/SLCMP97.csv) | $166{,}500{,}000<p\leq166{,}750{,}000$ | 4,704 |
| [SLCMP98](candidates/SLCMP98.csv) | $166{,}750{,}000<p\leq167{,}000{,}000$ | 4,714 |
| [SLCMP99](candidates/SLCMP99.csv) | $167{,}000{,}000<p\leq167{,}250{,}000$ | 4,762 |
| [SLCMP100](candidates/SLCMP100.csv) | $167{,}250{,}000<p\leq167{,}500{,}000$ | 4,786 |
| [SLCMP101](candidates/SLCMP101.csv) | $167{,}500{,}000<p\leq167{,}750{,}000$ | 4,770 |
| [SLCMP102](candidates/SLCMP102.csv) | $167{,}750{,}000<p\leq168{,}000{,}000$ | 4,722 |
| [SLCMP103](candidates/SLCMP103.csv) | $168{,}000{,}000<p\leq168{,}250{,}000$ | 4,576 |
| [SLCMP104](candidates/SLCMP104.csv) | $168{,}250{,}000<p\leq168{,}500{,}000$ | 4,782 |
| [SLCMP105](candidates/SLCMP105.csv) | $168{,}500{,}000<p\leq168{,}750{,}000$ | 4,643 |
| [SLCMP106](candidates/SLCMP106.csv) | $168{,}750{,}000<p\leq169{,}000{,}000$ | 4,697 |
| [SLCMP107](candidates/SLCMP107.csv) | $169{,}000{,}000<p\leq169{,}250{,}000$ | 4,982 |
| [SLCMP108](candidates/SLCMP108.csv) | $169{,}250{,}000<p\leq169{,}500{,}000$ | 4,832 |
| [SLCMP109](candidates/SLCMP109.csv) | $169{,}500{,}000<p\leq169{,}750{,}000$ | 4,847 |
| [SLCMP110](candidates/SLCMP110.csv) | $169{,}750{,}000<p\leq170{,}000{,}000$ | 4,853 |
| [SLCMP111](candidates/SLCMP111.csv) | $170{,}000{,}000<p\leq170{,}250{,}000$ | 4,945 |
| [SLCMP112](candidates/SLCMP112.csv) | $170{,}250{,}000<p\leq170{,}500{,}000$ | 4,882 |
| [SLCMP113](candidates/SLCMP113.csv) | $170{,}500{,}000<p\leq170{,}750{,}000$ | 4,832 |
| [SLCMP114](candidates/SLCMP114.csv) | $170{,}750{,}000<p\leq171{,}000{,}000$ | 4,908 |
| [SLCMP115](candidates/SLCMP115.csv) | $171{,}000{,}000<p\leq171{,}250{,}000$ | 4,923 |
| [SLCMP116](candidates/SLCMP116.csv) | $171{,}250{,}000<p\leq171{,}500{,}000$ | 4,902 |
| [SLCMP117](candidates/SLCMP117.csv) | $171{,}500{,}000<p\leq171{,}750{,}000$ | 4,817 |
| [SLCMP118](candidates/SLCMP118.csv) | $171{,}750{,}000<p\leq172{,}000{,}000$ | 4,705 |
| [SLCMP119](candidates/SLCMP119.csv) | $172{,}000{,}000<p\leq172{,}250{,}000$ | 4,729 |
| [SLCMP120](candidates/SLCMP120.csv) | $172{,}250{,}000<p\leq172{,}500{,}000$ | 4,965 |
| [SLCMP121](candidates/SLCMP121.csv) | $172{,}500{,}000<p\leq172{,}750{,}000$ | 4,867 |
| [SLCMP122](candidates/SLCMP122.csv) | $172{,}750{,}000<p\leq173{,}000{,}000$ | 4,848 |
| [SLCMP123](candidates/SLCMP123.csv) | $173{,}000{,}000<p\leq173{,}250{,}000$ | 4,837 |
| [SLCMP124](candidates/SLCMP124.csv) | $173{,}250{,}000<p\leq173{,}500{,}000$ | 4,850 |
| [SLCMP125](candidates/SLCMP125.csv) | $173{,}500{,}000<p\leq173{,}750{,}000$ | 4,921 |
| [SLCMP126](candidates/SLCMP126.csv) | $173{,}750{,}000<p\leq174{,}000{,}000$ | 4,913 |
| [SLCMP127](candidates/SLCMP127.csv) | $174{,}000{,}000<p\leq174{,}250{,}000$ | 4,825 |
| [SLCMP128](candidates/SLCMP128.csv) | $174{,}250{,}000<p\leq174{,}500{,}000$ | 4,935 |
| [SLCMP129](candidates/SLCMP129.csv) | $174{,}500{,}000<p\leq174{,}750{,}000$ | 4,742 |
| [SLCMP130](candidates/SLCMP130.csv) | $174{,}750{,}000<p\leq175{,}000{,}000$ | 4,829 |
| [SLCMP131](candidates/SLCMP131.csv) | $175{,}000{,}000<p\leq175{,}250{,}000$ | 4,867 |
| [SLCMP132](candidates/SLCMP132.csv) | $175{,}250{,}000<p\leq175{,}500{,}000$ | 4,880 |
| [SLCMP133](candidates/SLCMP133.csv) | $175{,}500{,}000<p\leq175{,}750{,}000$ | 4,852 |
| [SLCMP134](candidates/SLCMP134.csv) | $175{,}750{,}000<p\leq176{,}000{,}000$ | 4,865 |
| [SLCMP135](candidates/SLCMP135.csv) | $176{,}000{,}000<p\leq176{,}250{,}000$ | 4,634 |
| [SLCMP136](candidates/SLCMP136.csv) | $176{,}250{,}000<p\leq176{,}500{,}000$ | 4,775 |
| [SLCMP137](candidates/SLCMP137.csv) | $176{,}500{,}000<p\leq176{,}750{,}000$ | 4,894 |
| [SLCMP138](candidates/SLCMP138.csv) | $176{,}750{,}000<p\leq177{,}000{,}000$ | 4,872 |
| [SLCMP139](candidates/SLCMP139.csv) | $177{,}000{,}000<p\leq177{,}250{,}000$ | 4,848 |
| [SLCMP140](candidates/SLCMP140.csv) | $177{,}250{,}000<p\leq177{,}500{,}000$ | 4,934 |
| [SLCMP141](candidates/SLCMP141.csv) | $177{,}500{,}000<p\leq177{,}750{,}000$ | 4,856 |
| [SLCMP142](candidates/SLCMP142.csv) | $177{,}750{,}000<p\leq178{,}000{,}000$ | 4,937 |
| [SLCMP143](candidates/SLCMP143.csv) | $178{,}000{,}000<p\leq178{,}250{,}000$ | 4,913 |
| [SLCMP144](candidates/SLCMP144.csv) | $178{,}250{,}000<p\leq178{,}500{,}000$ | 4,824 |
| [SLCMP145](candidates/SLCMP145.csv) | $178{,}500{,}000<p\leq178{,}750{,}000$ | 4,821 |
| [SLCMP146](candidates/SLCMP146.csv) | $178{,}750{,}000<p\leq179{,}000{,}000$ | 4,862 |
| [SLCMP147](candidates/SLCMP147.csv) | $179{,}000{,}000<p\leq179{,}250{,}000$ | 4,935 |
| [SLCMP148](candidates/SLCMP148.csv) | $179{,}250{,}000<p\leq179{,}500{,}000$ | 4,947 |
| [SLCMP149](candidates/SLCMP149.csv) | $179{,}500{,}000<p\leq179{,}750{,}000$ | 4,899 |
| [SLCMP150](candidates/SLCMP150.csv) | $179{,}750{,}000<p\leq180{,}000{,}000$ | 4,922 |
| [SLCMP151](candidates/SLCMP151.csv) | $180{,}000{,}000<p\leq180{,}250{,}000$ | 4,698 |
| [SLCMP152](candidates/SLCMP152.csv) | $180{,}250{,}000<p\leq180{,}500{,}000$ | 4,854 |
| [SLCMP153](candidates/SLCMP153.csv) | $180{,}500{,}000<p\leq180{,}750{,}000$ | 4,871 |
| [SLCMP154](candidates/SLCMP154.csv) | $180{,}750{,}000<p\leq181{,}000{,}000$ | 4,836 |
| [SLCMP155](candidates/SLCMP155.csv) | $181{,}000{,}000<p\leq181{,}250{,}000$ | 4,776 |
| [SLCMP156](candidates/SLCMP156.csv) | $181{,}250{,}000<p\leq181{,}500{,}000$ | 4,754 |
| [SLCMP157](candidates/SLCMP157.csv) | $181{,}500{,}000<p\leq181{,}750{,}000$ | 4,862 |
| [SLCMP158](candidates/SLCMP158.csv) | $181{,}750{,}000<p\leq182{,}000{,}000$ | 4,942 |
| [SLCMP159](candidates/SLCMP159.csv) | $182{,}000{,}000<p\leq182{,}250{,}000$ | 4,877 |
| [SLCMP160](candidates/SLCMP160.csv) | $182{,}250{,}000<p\leq182{,}500{,}000$ | 4,930 |
| [SLCMP161](candidates/SLCMP161.csv) | $182{,}500{,}000<p\leq182{,}750{,}000$ | 4,808 |
| [SLCMP162](candidates/SLCMP162.csv) | $182{,}750{,}000<p\leq183{,}000{,}000$ | 4,869 |
| [SLCMP163](candidates/SLCMP163.csv) | $183{,}000{,}000<p\leq183{,}250{,}000$ | 4,849 |
| [SLCMP164](candidates/SLCMP164.csv) | $183{,}250{,}000<p\leq183{,}500{,}000$ | 4,836 |
| [SLCMP165](candidates/SLCMP165.csv) | $183{,}500{,}000<p\leq183{,}750{,}000$ | 4,914 |
| [SLCMP166](candidates/SLCMP166.csv) | $183{,}750{,}000<p\leq184{,}000{,}000$ | 4,817 |
| [SLCMP167](candidates/SLCMP167.csv) | $184{,}000{,}000<p\leq184{,}250{,}000$ | 4,911 |
| [SLCMP168](candidates/SLCMP168.csv) | $184{,}250{,}000<p\leq184{,}500{,}000$ | 4,944 |
| [SLCMP169](candidates/SLCMP169.csv) | $184{,}500{,}000<p\leq184{,}750{,}000$ | 4,809 |
| [SLCMP170](candidates/SLCMP170.csv) | $184{,}750{,}000<p\leq185{,}000{,}000$ | 4,844 |
| [SLCMP171](candidates/SLCMP171.csv) | $185{,}000{,}000<p\leq185{,}250{,}000$ | 4,896 |
| [SLCMP172](candidates/SLCMP172.csv) | $185{,}250{,}000<p\leq185{,}500{,}000$ | 4,785 |
| [SLCMP173](candidates/SLCMP173.csv) | $185{,}500{,}000<p\leq185{,}750{,}000$ | 4,793 |
| [SLCMP174](candidates/SLCMP174.csv) | $185{,}750{,}000<p\leq186{,}000{,}000$ | 4,860 |
| [SLCMP175](candidates/SLCMP175.csv) | $186{,}000{,}000<p\leq186{,}250{,}000$ | 4,841 |
| [SLCMP176](candidates/SLCMP176.csv) | $186{,}250{,}000<p\leq186{,}500{,}000$ | 4,845 |
| [SLCMP177](candidates/SLCMP177.csv) | $186{,}500{,}000<p\leq186{,}750{,}000$ | 4,925 |
| [SLCMP178](candidates/SLCMP178.csv) | $186{,}750{,}000<p\leq187{,}000{,}000$ | 4,827 |
| [SLCMP179](candidates/SLCMP179.csv) | $187{,}000{,}000<p\leq187{,}250{,}000$ | 4,853 |
| [SLCMP180](candidates/SLCMP180.csv) | $187{,}250{,}000<p\leq187{,}500{,}000$ | 4,817 |
| [SLCMP181](candidates/SLCMP181.csv) | $187{,}500{,}000<p\leq187{,}750{,}000$ | 4,675 |
| **Total** |  | **771,285** |

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
