# DIVE Verification Checklist

Use this file before saying that `hermes-textstats` works in DIVE.

## Setup in DIVE

Open a DIVE terminal in JupyterLab or VSCode/code-server. Clone or copy the
repository into a project folder, then enter it:

```bash
cd ~/projects/hermes-textstats
```

If the repo is cloned from GitHub, use the main branch:

```bash
git checkout main
```

## 1. Run Tests

```bash
python3 -m pytest tests/ -v
```

Expected result:

```text
22 passed
```

## 2. Run the CLI

```bash
PYTHONPATH=src python3 -m hermes_textstats.cli "Hermes helps students publish Python packages from DIVE."
```

Expected result:

```text
Characters: 56
Characters without spaces: 49
Words: 8
Sentences: 1
Paragraphs: 1
Longest sentence: 8 words
Average word length: 6.00
Lexical diversity: 1.00
Reading time: 0.04 minutes
```

## 3. Check JSON Output

```bash
PYTHONPATH=src python3 -m hermes_textstats.cli --json "Hermes helps students publish Python packages from DIVE."
```

Expected result:

```text
{"average_word_length": 6.0, "characters": 56, "characters_no_spaces": 49, "lexical_diversity": 1.0, "longest_sentence_words": 8, "paragraphs": 1, "reading_time_minutes": 0.04, "sentences": 1, "words": 8}
```

## 4. Check Markdown Report

```bash
PYTHONPATH=src python3 -m hermes_textstats.cli --report "Hermes helps students publish Python packages from DIVE."
```

Expected result:

- The output starts with `# Text Statistics Report`.
- The table includes `Words`, `Paragraphs`, `Longest sentence`, and
  `Lexical diversity`.

## 5. Check File Input

```bash
printf "First paragraph.\n\nSecond paragraph." > reflection.txt
PYTHONPATH=src python3 -m hermes_textstats.cli --file reflection.txt
```

Expected result:

- The output includes `Paragraphs: 2`.

## 6. Check pydoc

```bash
PYTHONPATH=src python3 -m pydoc hermes_textstats
```

Expected result:

- The page starts with `Turn short text into clear statistics from Python or the terminal.`
- The function list includes `analyze_text`, `count_words`, `count_sentences`,
  `count_paragraphs`, `count_characters`, `average_word_length`,
  `estimate_reading_time`, `longest_sentence_length`, `lexical_diversity`, and
  `format_markdown_report`.

## 7. Build the Package

```bash
python3 -m build
```

Expected result:

```text
Successfully built hermes_textstats-0.1.1.tar.gz and hermes_textstats-0.1.1-py3-none-any.whl
```

If `build` is missing:

```bash
python3 -m pip install build
python3 -m build
```

## 8. Check the Distribution Files

```bash
python3 -m twine check dist/*
```

Expected result:

```text
Checking dist/hermes_textstats-0.1.1-py3-none-any.whl: PASSED
Checking dist/hermes_textstats-0.1.1.tar.gz: PASSED
```

If `twine` is missing:

```bash
python3 -m pip install twine
python3 -m twine check dist/*
```

## Verification Note

Do not write that this project is verified in DIVE until the checks above pass
inside DIVE. Before that, write that it is locally verified and DIVE verification
is prepared.
