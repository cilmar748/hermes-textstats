# User Guide

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

## Output Fields

- `characters`: total characters, including spaces and punctuation.
- `characters_no_spaces`: total characters excluding whitespace.
- `words`: simple English-style word count.
- `sentences`: sentence count from `.`, `?`, and `!`; unpunctuated non-empty text counts as one sentence.
- `average_word_length`: average length of detected words.
- `reading_time_minutes`: estimated minutes at 200 words per minute.
