import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


def run_cli(*args):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
    return subprocess.run(
        [sys.executable, "-m", "hermes_textstats.cli", *args],
        check=False,
        capture_output=True,
        env=env,
        text=True,
    )


def test_cli_prints_human_readable_summary():
    result = run_cli("Hermes builds packages.")

    assert result.returncode == 0
    assert "Words: 3" in result.stdout
    assert "Sentences: 1" in result.stdout
    assert "Paragraphs: 1" in result.stdout
    assert "Lexical diversity: 1.00" in result.stdout
    assert "Reading time: 0.01 minutes" in result.stdout


def test_cli_prints_json_summary():
    result = run_cli("--json", "Hermes builds packages.")

    assert result.returncode == 0
    assert json.loads(result.stdout) == {
        "characters": 23,
        "characters_no_spaces": 21,
        "words": 3,
        "sentences": 1,
        "paragraphs": 1,
        "average_word_length": pytest.approx(20 / 3),
        "reading_time_minutes": 0.015,
        "longest_sentence_words": 3,
        "lexical_diversity": 1.0,
    }


def test_cli_rejects_empty_input():
    result = run_cli("   ")

    assert result.returncode == 2
    assert "text must not be empty" in result.stderr


def test_cli_reads_text_from_file(tmp_path):
    text_file = tmp_path / "reflection.txt"
    text_file.write_text("First paragraph.\n\nSecond paragraph.", encoding="utf-8")

    result = run_cli("--file", str(text_file))

    assert result.returncode == 0
    assert "Words: 4" in result.stdout
    assert "Paragraphs: 2" in result.stdout


def test_cli_prints_markdown_report():
    result = run_cli("--report", "Hermes builds packages.")

    assert result.returncode == 0
    assert result.stdout.startswith("# Text Statistics Report")
    assert "| Words | 3 |" in result.stdout


def test_cli_rejects_text_and_file_together(tmp_path):
    text_file = tmp_path / "reflection.txt"
    text_file.write_text("From a file.", encoding="utf-8")

    result = run_cli("--file", str(text_file), "From the command line.")

    assert result.returncode == 2
    assert "use either text or --file, not both" in result.stderr
