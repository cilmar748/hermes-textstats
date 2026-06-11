# Paper Notes

## One-line Summary

`hermes-textstats` is a small Python package that counts basic statistics for a
short piece of text.

## Short Description

The package solves a simple problem: given a text string, it returns useful
counts without needing a notebook or a longer script. It can count words,
sentences, characters with and without spaces, average word length, and an
estimated reading time. It can be used from Python or from the terminal.

## What I Built

I built a Python package called `hermes-textstats`. The import name is
`hermes_textstats`, and the command-line command is `hermes-textstats`. The
package uses a `src/` layout, has a `pyproject.toml`, includes tests, and can be
built into a wheel and source distribution.

## What Hermes Helped With

Hermes Agent was used as the coding workflow. The work was broken into small
steps: package structure, tests, implementation, documentation, package build,
and verification. Git was used as the checkpoint system so each step could be
reviewed or reverted if needed.

## What Is Verified Locally

These checks have passed on my local machine:

- `python3 -m pytest tests/ -v` showed `14 passed`.
- The CLI printed text statistics from a real command.
- The JSON CLI output worked.
- `PYTHONPATH=src python3 -m pydoc hermes_textstats` showed the package summary
  and function list.
- `python -m build` created the wheel and source distribution.
- `twine check dist/*` passed for both distribution files.

## What Still Needs Tokens

The package is built locally and ready for TestPyPI/PyPI upload, but it is not
uploaded yet. Uploading needs private TestPyPI and PyPI API tokens. Those tokens
should not be saved in git.

## Connection to DIVE

The goal of the paper is to show Hermes being used in DIVE for students to
publish a package. This project is the package output from that workflow. The
course documentation describes Hermes inside the course environment through
JupyterLab and VSCode/code-server. I should only write that this exact project
is verified in DIVE after running the checklist in `docs/DIVE_VERIFICATION.md`
inside DIVE.

