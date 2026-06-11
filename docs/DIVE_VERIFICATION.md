# DIVE Verification Checklist

Use this file before saying that `hermes-textstats` works in DIVE.

## Setup in DIVE

Open a DIVE terminal in JupyterLab or VSCode/code-server. Clone or copy the
repository into a project folder, then enter it:

```bash
cd ~/projects/hermes-textstats
```

If the repo is cloned from GitHub, use the branch that contains the package
work:

```bash
git checkout codex/hermes-textstats
```

## 1. Run Tests

```bash
python3 -m pytest tests/ -v
```

Expected result:

```text
14 passed
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
Average word length: 6.00
Reading time: 0.04 minutes
```

## 3. Check JSON Output

```bash
PYTHONPATH=src python3 -m hermes_textstats.cli --json "Hermes helps students publish Python packages from DIVE."
```

Expected result:

```text
{"average_word_length": 6.0, "characters": 56, "characters_no_spaces": 49, "reading_time_minutes": 0.04, "sentences": 1, "words": 8}
```

## 4. Check pydoc

```bash
PYTHONPATH=src python3 -m pydoc hermes_textstats
```

Expected result:

- The page starts with `Count simple text statistics from Python or the terminal.`
- The function list includes `analyze_text`, `count_words`, `count_sentences`,
  `count_characters`, `average_word_length`, and `estimate_reading_time`.

## 5. Build the Package

```bash
python3 -m build
```

Expected result:

```text
Successfully built hermes_textstats-0.1.0.tar.gz and hermes_textstats-0.1.0-py3-none-any.whl
```

If `build` is missing:

```bash
python3 -m pip install build
python3 -m build
```

## 6. Check the Distribution Files

```bash
python3 -m twine check dist/*
```

Expected result:

```text
Checking dist/hermes_textstats-0.1.0-py3-none-any.whl: PASSED
Checking dist/hermes_textstats-0.1.0.tar.gz: PASSED
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

