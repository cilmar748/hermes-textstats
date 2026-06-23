"""Turn short text into clear statistics from Python or the terminal.

hermes-textstats is a DIVE-ready package I built while testing the Hermes Agent
workflow for a Python package project. It takes a short text input and reports
counts such as words, sentences, paragraphs, characters, average word length,
lexical diversity, longest sentence length, and estimated reading time.
"""

from __future__ import annotations

import re
from typing import Any

_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")
_SENTENCE_END_RE = re.compile(r"[!?]+|(?<!\d)\.+|\.(?=\s|$)")
_PARAGRAPH_SPLIT_RE = re.compile(r"\n\s*\n")


def _words(text: str) -> list[str]:
    return _WORD_RE.findall(text)


def _sentence_chunks(text: str) -> list[str]:
    stripped = text.strip()
    if not stripped:
        return []

    chunks = [chunk.strip() for chunk in _SENTENCE_END_RE.split(stripped)]
    return [chunk for chunk in chunks if chunk]


def count_words(text: str) -> int:
    """Return the number of simple English-style words in text."""
    return len(_words(text))


def count_sentences(text: str) -> int:
    """Return a simple sentence count based on ending punctuation."""
    stripped = text.strip()
    if not stripped:
        return 0

    ended_sentences = _SENTENCE_END_RE.findall(stripped)
    if ended_sentences:
        return len(ended_sentences)

    return 1


def count_paragraphs(text: str) -> int:
    """Return the number of non-empty paragraphs separated by blank lines."""
    stripped = text.strip()
    if not stripped:
        return 0

    return sum(1 for paragraph in _PARAGRAPH_SPLIT_RE.split(stripped) if paragraph.strip())


def count_characters(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters, optionally excluding whitespace."""
    if include_spaces:
        return len(text)

    return sum(1 for character in text if not character.isspace())


def average_word_length(text: str) -> float:
    """Return the average length of words in text, or 0.0 for no words."""
    words = _words(text)
    if not words:
        return 0.0

    return sum(len(word) for word in words) / len(words)


def estimate_reading_time(text: str, words_per_minute: int = 200) -> float:
    """Return estimated reading time in minutes."""
    if words_per_minute <= 0:
        raise ValueError("words_per_minute must be positive")

    return count_words(text) / words_per_minute


def longest_sentence_length(text: str) -> int:
    """Return the word count of the longest detected sentence."""
    sentence_lengths = [count_words(sentence) for sentence in _sentence_chunks(text)]
    if sentence_lengths:
        return max(sentence_lengths)

    return 0


def lexical_diversity(text: str) -> float:
    """Return unique word ratio using case-insensitive simple words."""
    words = [word.lower() for word in _words(text)]
    if not words:
        return 0.0

    return len(set(words)) / len(words)


def analyze_text(text: str) -> dict[str, Any]:
    """Return a stable summary of text statistics."""
    return {
        "characters": count_characters(text),
        "characters_no_spaces": count_characters(text, include_spaces=False),
        "words": count_words(text),
        "sentences": count_sentences(text),
        "paragraphs": count_paragraphs(text),
        "average_word_length": average_word_length(text),
        "reading_time_minutes": estimate_reading_time(text),
        "longest_sentence_words": longest_sentence_length(text),
        "lexical_diversity": lexical_diversity(text),
    }


def format_markdown_report(text: str) -> str:
    """Return a Markdown table report for text statistics."""
    summary = analyze_text(text)
    rows = [
        ("Characters", str(summary["characters"])),
        ("Characters without spaces", str(summary["characters_no_spaces"])),
        ("Words", str(summary["words"])),
        ("Sentences", str(summary["sentences"])),
        ("Paragraphs", str(summary["paragraphs"])),
        ("Longest sentence", f"{summary['longest_sentence_words']} words"),
        ("Average word length", f"{summary['average_word_length']:.2f}"),
        ("Lexical diversity", f"{summary['lexical_diversity']:.2f}"),
        ("Reading time", f"{summary['reading_time_minutes']:.2f} minutes"),
    ]

    lines = [
        "# Text Statistics Report",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {label} | {value} |" for label, value in rows)
    return "\n".join(lines)


__all__ = [
    "analyze_text",
    "average_word_length",
    "count_characters",
    "count_paragraphs",
    "count_sentences",
    "count_words",
    "estimate_reading_time",
    "format_markdown_report",
    "lexical_diversity",
    "longest_sentence_length",
]
