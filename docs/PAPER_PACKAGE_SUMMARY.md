# Paper Package Summary

## One-line Summary

`hermes-textstats` is a small Python package for checking basic text statistics
from Python, the terminal, or a notebook.

## Motivation and Use Cases

I built this package as a concrete example of using Hermes Agent with git to
create a Python package that can be tested, documented, and published. The use
case is simple on purpose: a student working in DIVE/JupyterHub can paste a
short paragraph from an assignment, quiz explanation, README file, or reflection
and get word count, sentence count, character count, average word length, and
estimated reading time. This gives the project a real package output while also
showing the steps of the agentic coding workflow.

## Package Name

The name `hermes-textstats` keeps credit to Hermes because the package was built
through the Hermes Agent workflow. The `textstats` part says what the package
does directly, so a user can understand the purpose before opening the code.

## Demo Evidence

- CLI demo transcript: `docs/assets/hermes-textstats-demo.txt`
- CLI screencap-style image: `docs/assets/hermes-textstats-demo.png`
- Workflow diagram: `docs/assets/hermes-textstats-workflow.svg`
- Notebook demo: `notebooks/demo.ipynb`

## Visual Diagram

![Hermes textstats workflow](assets/hermes-textstats-workflow.svg)

## Current Status

The package has passing local tests, builds into wheel and source distribution
files, and passes `twine check`. The next publishing step is uploading the
current `0.1.0` release to TestPyPI with a private TestPyPI API token, then
installing it back from TestPyPI to verify the published package.
