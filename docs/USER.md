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
from hermes_textstats import analyze_text

print(analyze_text("This is a short sentence."))
```

