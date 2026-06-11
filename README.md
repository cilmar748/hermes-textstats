# hermes-textstats

`hermes-textstats` is a small Python package for text statistics. It provides
importable functions and a command-line interface for word counts, sentence
counts, character counts, average word length, and reading-time estimates.

## Installation

```bash
python -m pip install hermes-textstats
```

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

- [Paper notes](docs/PAPER_NOTES.md) records what I built, what Hermes helped
  with, and what is already verified.
- [DIVE verification](docs/DIVE_VERIFICATION.md) lists the commands to run in
  DIVE before saying the package is verified there.
- [Demo transcript](docs/assets/hermes-textstats-demo.txt) shows the package
  running from the command line.
- [Demo screencap](docs/assets/hermes-textstats-demo.png) is a screencap-style
  image made from the real CLI output.

See `docs/ACCOUNT_SETUP.md` before publishing to TestPyPI, PyPI, or Telegram.
