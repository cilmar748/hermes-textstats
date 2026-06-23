# hermes-textstats Specification

## Purpose

`hermes-textstats` helps students and developers inspect short text snippets
from Python code, notebooks, files, or the terminal.

## User Stories

- As a Python user, I want importable text-statistics functions so I can reuse
  them in notebooks, scripts, and assignments.
- As a terminal user, I want a CLI summary so I can inspect text without writing
  Python code.
- As a DIVE/JupyterHub user, I want file input and a Markdown report so I can
  analyze a draft and reuse the result in a notebook or screenshot.
- As a package maintainer, I want tests and packaging metadata so I can publish
  safely to TestPyPI and PyPI.

## Public API

- `count_words(text: str) -> int`
- `count_sentences(text: str) -> int`
- `count_paragraphs(text: str) -> int`
- `count_characters(text: str, include_spaces: bool = True) -> int`
- `average_word_length(text: str) -> float`
- `estimate_reading_time(text: str, words_per_minute: int = 200) -> float`
- `longest_sentence_length(text: str) -> int`
- `lexical_diversity(text: str) -> float`
- `analyze_text(text: str) -> dict`
- `format_markdown_report(text: str) -> str`

## CLI

- `hermes-textstats "some text"` prints a human-readable summary.
- `hermes-textstats --file draft.txt` reads text from a UTF-8 text file.
- `hermes-textstats --json "some text"` prints JSON.
- `hermes-textstats --report "some text"` prints a Markdown report.
- Empty or whitespace-only input exits with a clear error message.

## Acceptance Criteria

- All public API functions handle punctuation and extra whitespace.
- Empty text returns zero counts for count-style functions.
- `average_word_length("")` returns `0.0`.
- `estimate_reading_time` raises `ValueError` when `words_per_minute <= 0`.
- `lexical_diversity("")` returns `0.0`.
- `longest_sentence_length("")` returns `0`.
- CLI JSON output is valid JSON and has the same keys as `analyze_text`.
- CLI file input rejects being combined with direct text input.
- Package builds into both a wheel and a source distribution.

## Non-Goals

- No natural-language processing dependencies.
- No language-specific tokenization beyond simple English-style words.
- No network calls.
