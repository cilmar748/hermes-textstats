import json
import subprocess
import sys

import pytest


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "hermes_textstats.cli", *args],
        check=False,
        capture_output=True,
        text=True,
    )


def test_cli_prints_human_readable_summary():
    result = run_cli("Hermes builds packages.")

    assert result.returncode == 0
    assert "Words: 3" in result.stdout
    assert "Sentences: 1" in result.stdout
    assert "Reading time: 0.01 minutes" in result.stdout


def test_cli_prints_json_summary():
    result = run_cli("--json", "Hermes builds packages.")

    assert result.returncode == 0
    assert json.loads(result.stdout) == {
        "characters": 23,
        "characters_no_spaces": 21,
        "words": 3,
        "sentences": 1,
        "average_word_length": pytest.approx(20 / 3),
        "reading_time_minutes": 0.015,
    }


def test_cli_rejects_empty_input():
    result = run_cli("   ")

    assert result.returncode == 2
    assert "text must not be empty" in result.stderr
