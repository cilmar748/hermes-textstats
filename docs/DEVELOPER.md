# Developer Guide

## Project Layout

- `src/hermes_textstats/` contains the importable package and CLI.
- `tests/` contains pytest tests.
- `SPEC.md` describes the expected behavior.
- `README.md` is the PyPI-facing project description.
- `docs/` contains user, developer, DIVE, and paper notes.
- `notebooks/demo.ipynb` is the notebook-style demo.

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

The private remote is `https://github.com/cilmar748/hermes-textstats`.
Use git commits as checkpoints before upload or release steps.

## Agent Handoff Notes

Future AI agents should start by reading `SPEC.md`, `README.md`, this developer
guide, and the tests. The public behavior is intentionally small, so changes
should normally begin with a test in `tests/`, then an implementation update in
`src/hermes_textstats/`, then documentation updates if the behavior changed.

Keep the package dependency-free unless there is a strong reason. The package is
meant to be easy to inspect, build, and run in DIVE/JupyterHub.

## Cleanup and Refactor Checklist

Before publishing a new version:

1. Read the current tests and make sure they still match `SPEC.md`.
2. Remove duplicated logic only if it makes the code easier to read.
3. Run `python -m pytest tests/ -v`.
4. Run `python -m build`.
5. Run `python -m twine check dist/*`.
6. Install the wheel in a clean environment and run the CLI once.
