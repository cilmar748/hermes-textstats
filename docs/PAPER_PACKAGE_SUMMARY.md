# Paper Package Summary

## One-line Summary

`hermes-textstats` is a DIVE-ready Python package that turns short text, files,
and notebook drafts into clear writing statistics.

## Motivation and Use Cases

I built this package as a concrete example of using Hermes Agent with git to
create a Python package that can be tested, documented, and published. The use
case is simple on purpose but easy to explain: a student working in
DIVE/JupyterHub can paste a short paragraph from an assignment, quiz
explanation, README file, or reflection and immediately see word count, sentence
count, paragraph count, lexical diversity, longest sentence length, character
count, average word length, and estimated reading time. This gives the
grant/paper a concrete student output, not only a description of an agent
workflow.

## Achievements

- Published `hermes-textstats` version `0.1.0` on real PyPI.
- Prepared version `0.1.1` with file input, Markdown report output, paragraph
  count, longest sentence length, and lexical diversity.
- Verified clean install from PyPI.
- Verified both Python import and command-line usage.
- Added tests, user guide, developer guide, DIVE verification notes, paper
  notes, notebook demo, CLI screencap, and workflow diagram.

## Package Name

The name `hermes-textstats` keeps credit to Hermes because the package was built
through the Hermes Agent workflow. The `textstats` part says what the package
does directly, so a user can understand the purpose before opening the code.

## Demo Evidence

- CLI demo transcript: `docs/assets/hermes-textstats-demo.txt`
- Compact showcase screencap: `docs/assets/hermes-textstats-showcase.png`
- CLI screencap-style image: `docs/assets/hermes-textstats-demo.png`
- Workflow diagram: `docs/assets/hermes-textstats-workflow.svg`
- Notebook demo: `notebooks/demo.ipynb`

## Visuals

![Hermes textstats showcase](assets/hermes-textstats-showcase.png)
![Hermes textstats workflow](assets/hermes-textstats-workflow.svg)

## Current Status

The package is published on real PyPI. Version `0.1.1` is prepared as the next
improvement release:

https://pypi.org/project/hermes-textstats/

The `0.1.1` release candidate passes local tests, builds into wheel and source
distribution files, and passes `twine check`. After uploading, the final check
is to install version `0.1.1` back from PyPI and verify both Python import and
the `hermes-textstats` command-line interface.
