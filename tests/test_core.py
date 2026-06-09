import pytest

from hermes_textstats import (
    analyze_text,
    average_word_length,
    count_characters,
    count_sentences,
    count_words,
    estimate_reading_time,
)


def test_count_words_handles_punctuation_and_whitespace():
    text = "  Hermes helps: build, test, and publish Python packages!  "

    assert count_words(text) == 8


def test_count_words_returns_zero_for_empty_text():
    assert count_words("") == 0
    assert count_words("   \n\t ") == 0


def test_count_sentences_handles_common_end_marks():
    text = "Hermes builds packages. Does it test them? Yes!"

    assert count_sentences(text) == 3


def test_count_sentences_treats_unpunctuated_text_as_one_sentence():
    assert count_sentences("Hermes can read short text") == 1


def test_count_sentences_returns_zero_for_empty_text():
    assert count_sentences("") == 0
    assert count_sentences("   ") == 0


def test_count_characters_can_include_or_exclude_spaces():
    text = "Hi there"

    assert count_characters(text) == 8
    assert count_characters(text, include_spaces=False) == 7


def test_average_word_length_ignores_punctuation():
    text = "Hi there, Hermes!"

    assert average_word_length(text) == pytest.approx(13 / 3)


def test_average_word_length_returns_zero_for_empty_text():
    assert average_word_length("") == 0.0


def test_estimate_reading_time_uses_word_count_and_rate():
    text = "one two three four five"

    assert estimate_reading_time(text, words_per_minute=10) == pytest.approx(0.5)


def test_estimate_reading_time_rejects_non_positive_rate():
    with pytest.raises(ValueError, match="words_per_minute must be positive"):
        estimate_reading_time("some text", words_per_minute=0)


def test_analyze_text_returns_stable_summary_keys():
    text = "Hermes builds packages. It runs tests!"

    assert analyze_text(text) == {
        "characters": 38,
        "characters_no_spaces": 34,
        "words": 6,
        "sentences": 2,
        "average_word_length": pytest.approx(31 / 6),
        "reading_time_minutes": pytest.approx(6 / 200),
    }
