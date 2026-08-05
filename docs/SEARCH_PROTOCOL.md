# Search protocol

The public search flow is deliberately typed:

1. **Exponent admission.** Admit a prime exponent $p$ from a declared source.
2. **Optional research annotation.** Join an allowlisted SAM/SLC sidecar by its
   stable exponent key. The sidecar may affect ordering, never truth value.
3. **Exact execution.** Run the Lucas–Lehmer recurrence for exactly $p-2$
   iterations when $p>2$.
4. **Receipt.** Preserve exponent, algorithm revision, iteration count, final
   residue, software revision, and execution-manifest hash.
5. **Replication.** Re-run a zero-residue candidate through an independently
   prepared execution path and compare exact outputs.
6. **Publication state.** Advance only according to `RESULT_POLICY.md`.

Optimizations may change representation, scheduling, checkpoint frequency, or
hardware use. They may not change the mathematical recurrence or silently
replace the final exact residue.
