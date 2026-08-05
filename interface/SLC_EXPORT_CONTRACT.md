# SLC export contract

SLC remains in the private/source SAM Research Project repository. This public
repository accepts only deliberate, frozen export bundles.

## Required bundle contents

Each export must contain:

1. a manifest conforming to
   `schemas/mersenne_export_manifest.schema.json`;
2. a declared source campaign and version;
3. an allowlist of included files and fields;
4. SHA-256 hashes for every exported file;
5. a type declaration for candidate, scheduler, and diagnostic fields; and
6. an explicit statement that the bundle does not assign primality.

## Excluded by default

- absolute local paths;
- credentials or host metadata;
- unrelated SAM research artifacts;
- mutable pointers without a frozen referenced object;
- undocumented fitted values; and
- claims not present in the source result.

## Authority

Imported sidecars may order or annotate exact work. The Lucas–Lehmer receipt
remains the primality authority for each Mersenne candidate.
