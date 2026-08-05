# Agent instructions

This is a public exact-computation repository of the SAM Research Project.

## Repository preflight

Before any Mersenne commit, sync, push, branch, or pull-request operation,
verify that the working repository and `origin` are:

`https://github.com/iwtbotiwtwot/mersenne-prime-search.git`

Do not publish Mersenne work to the `SAM_Research_Project` remote.

1. Keep exact primality decisions separate from candidate ranking or sidecars.
2. Do not describe an SLC score, schedule, coordinate, or prediction as a
   primality result.
3. Preserve exact inputs, code revision, final residue, and receipt hashes for
   every promoted run.
4. Never replace or silently edit a published receipt. Corrections are new
   artifacts that identify the superseded record.
5. Do not claim a new Mersenne prime from an exploratory or unreplicated run.
6. Treat imported SAM/SLC data as versioned, frozen, allowlisted input.
7. Keep the repository free of private paths, credentials, and unreviewed
   source-repository internals.

The repository's claim states and execution sequence are defined in
`docs/RESULT_POLICY.md` and `docs/SEARCH_PROTOCOL.md`.
