"""Text statistics helpers for Python and the terminal."""

from __future__ import annotations

import re
from typing import Any

_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")
_SENTENCE_END_RE = re.compile(r"[.!?]+")


def _words(text: str) -> list[str]:
    return _WORD_RE.findall(text)


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


def analyze_text(text: str) -> dict[str, Any]:
    """Return a stable summary of text statistics."""
    return {
        "characters": count_characters(text),
        "characters_no_spaces": count_characters(text, include_spaces=False),
        "words": count_words(text),
        "sentences": count_sentences(text),
        "average_word_length": average_word_length(text),
        "reading_time_minutes": estimate_reading_time(text),
    }


__all__ = [
    "analyze_text",
    "average_word_length",
    "count_characters",
    "count_sentences",
    "count_words",
    "estimate_reading_time",
]
