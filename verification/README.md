# Verification

Run both checks before publishing a change:

```bash
python3 verification/validate_repository.py
python3 -m unittest discover -s tests -v
```

The structural validator checks required public surfaces, JSON syntax, private
path or credential markers, and trailing whitespace. The unit suite exercises
the exact Lucas--Lehmer recurrence against known prime and composite cases.
