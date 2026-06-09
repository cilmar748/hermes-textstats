# Developer Guide

## Project Layout

- `src/hermes_textstats/` contains the importable package and CLI.
- `tests/` contains pytest tests.
- `SPEC.md` describes the expected behavior.
- `README.md` is the PyPI-facing project description.

## Local Checks

```bash
python -m pip install -e ".[test]"
python -m pytest tests/ -v
python -m build
python -m twine check dist/*
```

## Release Flow

1. Run the full test suite.
2. Build distributions with `python -m build`.
3. Validate distributions with `python -m twine check dist/*`.
4. Upload to TestPyPI.
5. Install from TestPyPI in a clean environment.
6. Upload the same verified version to PyPI.

## GitHub

The planned private remote is `https://github.com/cilmar748/hermes-textstats`.
Create it after the local implementation and package checks pass.
