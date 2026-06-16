# hermes-textstats

`hermes-textstats` is a small Python package for text statistics. It provides
importable functions and a command-line interface for word counts, sentence
counts, character counts, average word length, and reading-time estimates.

The name connects the package to the Hermes Agent workflow used in the course.
The package itself is intentionally small: it gives students a concrete package
that can be built, tested, documented, and published from DIVE/JupyterHub.

## Motivation

When I write short text for assignments, quiz explanations, README files, or
project reflections, I sometimes want quick feedback about length without
opening another tool. This package gives a simple example: a student can paste a
paragraph into Python, a notebook, or the terminal and immediately see word
count, sentence count, character count, and estimated reading time.

Example use cases:

- checking the length of a reflection paragraph before submitting it;
- measuring a short quiz explanation inside DIVE/JupyterHub;
- using a small package project to practice the Hermes Agent + git + PyPI
  workflow.

## Installation

```bash
python -m pip install hermes-textstats
```

Published package: https://pypi.org/project/hermes-textstats/0.1.0/

## Quick Start

```python
from hermes_textstats import analyze_text, count_words

text = "Hermes helps me build, test, and publish Python packages."
print(count_words(text))
summary = analyze_text(text)
print(summary)
```

```bash
hermes-textstats "Hermes helps me build, test, and publish Python packages."
hermes-textstats --json "Hermes helps me build, test, and publish Python packages."
```

## API

- `count_words(text)`
- `count_sentences(text)`
- `count_characters(text, include_spaces=True)`
- `average_word_length(text)`
- `estimate_reading_time(text, words_per_minute=200)`
- `analyze_text(text)`

## Development

```bash
python -m pip install -e ".[test]"
python -m pytest tests/ -v
python -m build
python -m twine check dist/*
```

## Project Notes

- [Paper package summary](docs/PAPER_PACKAGE_SUMMARY.md) contains the one-line
  summary, short motivation paragraph, and visual evidence for TALE 2026 notes.
- [Paper notes](docs/PAPER_NOTES.md) records what I built, what Hermes helped
  with, and what is already verified.
- [DIVE verification](docs/DIVE_VERIFICATION.md) lists the commands to run in
  DIVE before saying the package is verified there.
- [Notebook demo](notebooks/demo.ipynb) demonstrates the Python API in a
  notebook-style workflow.
- [Demo transcript](docs/assets/hermes-textstats-demo.txt) shows the package
  running from the command line.
- [Demo screencap](docs/assets/hermes-textstats-demo.png) is a screencap-style
  image made from the real CLI output.
- [Workflow diagram](docs/assets/hermes-textstats-workflow.svg) shows how DIVE,
  Hermes Agent, git, tests, docs, and TestPyPI/PyPI connect.

See `docs/ACCOUNT_SETUP.md` for the account/token steps used for TestPyPI,
PyPI, and Telegram setup.
