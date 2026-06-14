# User Guide

## What This Package Is For

`hermes-textstats` is for quick checks on short text. For example, a student can
check a reflection paragraph, a quiz explanation, a README section, or a short
answer draft inside DIVE/JupyterHub.

## Command Line

```bash
hermes-textstats "This is a short sentence."
```

Use JSON output when another program should read the result:

```bash
hermes-textstats --json "This is a short sentence."
```

## Python API

```python
from hermes_textstats import analyze_text, estimate_reading_time

text = "This is a short sentence."
print(estimate_reading_time(text))
print(analyze_text(text))
```

## Notebook Demo

Open `notebooks/demo.ipynb` to see the same package used in a notebook-style
workflow. This is the easiest demo format for DIVE/JupyterHub because the input
text, code, and output can stay in one place.

## Output Fields

- `characters`: total characters, including spaces and punctuation.
- `characters_no_spaces`: total characters excluding whitespace.
- `words`: simple English-style word count.
- `sentences`: sentence count from `.`, `?`, and `!`; unpunctuated non-empty text counts as one sentence.
- `average_word_length`: average length of detected words.
- `reading_time_minutes`: estimated minutes at 200 words per minute.
