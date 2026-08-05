# Exact baseline

For an exponent $p$, define the Mersenne number

$$
M_p=2^p-1.
$$

If $M_p$ is prime, then $p$ must be prime. Prime $p$ is necessary but not
sufficient: for example, $M_{11}=2047=23\cdot89$.

For prime $p>2$, the Lucas–Lehmer sequence is

$$
s_0=4,\qquad s_{k+1}=s_k^2-2 \pmod{M_p}.
$$

Then $M_p$ is prime if and only if $s_{p-2}=0$. The repository implementation
uses exact Python integers and records the final residue. For $p=2$, $M_2=3$
is handled directly.

## Baseline role

This recurrence is the exact decision surface. Candidate generators and
ranking systems can reduce or reorder the work queue, but their outputs do not
replace the recurrence and are not themselves evidence that $M_p$ is prime.

The bootstrap regression set includes:

- passing exponents: 2, 3, 5, 7, 13, 17, 19, 31;
- failing prime exponents: 11, 23, 29; and
- invalid composite-exponent inputs.
