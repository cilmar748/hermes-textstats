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
from hermes_textstats import analyze_text

summary = analyze_text("Hermes helps me build, test, and publish Python packages.")
print(summary)
```

```bash
hermes-textstats "Hermes helps me build, test, and publish Python packages."
hermes-textstats --json "Hermes helps me build, test, and publish Python packages."
```

## Development

```bash
python -m pip install -e ".[test]"
python -m pytest tests/ -v
python -m build
python -m twine check dist/*
```

