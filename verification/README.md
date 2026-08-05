# Verification

Run both checks before publishing a change:

```bash
python3 verification/validate_repository.py
python3 -m unittest discover -s tests -v
```

The structural validator checks required public surfaces, JSON syntax, private
path or credential markers, trailing whitespace, frozen-export allowlists,
file hashes, all 1,858 prime-exponent rows, aggregate counts, and the typed
selection-1196 progress state. The unit suite exercises the exact recurrence
against known Mersenne-prime and composite cases and independently rechecks the
public export.
