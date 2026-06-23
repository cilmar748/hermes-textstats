"""Command-line interface for hermes-textstats."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import analyze_text, format_markdown_report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hermes-textstats",
        description="Show simple statistics for a text snippet.",
    )
    parser.add_argument("text", nargs="?", help="Text to analyze.")
    parser.add_argument(
        "--file",
        type=Path,
        help="Read text to analyze from a UTF-8 text file.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Print the summary as JSON.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a Markdown report.",
    )
    return parser


def _read_text(args: argparse.Namespace, parser: argparse.ArgumentParser) -> str:
    if args.text is not None and args.file is not None:
        parser.error("use either text or --file, not both")

    if args.file is not None:
        try:
            return args.file.read_text(encoding="utf-8")
        except OSError as error:
            parser.error(f"could not read file: {error}")

    if args.text is None:
        parser.error("text or --file is required")

    return args.text


def main(argv: list[str] | None = None) -> int:
    """Run the hermes-textstats command-line interface."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    text = _read_text(args, parser)

    if args.as_json and args.report:
        parser.error("use either --json or --report, not both")

    if not text.strip():
        parser.error("text must not be empty")

    if args.report:
        print(format_markdown_report(text))
        return 0

    summary = analyze_text(text)
    if args.as_json:
        print(json.dumps(summary, sort_keys=True))
        return 0

    print(f"Characters: {summary['characters']}")
    print(f"Characters without spaces: {summary['characters_no_spaces']}")
    print(f"Words: {summary['words']}")
    print(f"Sentences: {summary['sentences']}")
    print(f"Paragraphs: {summary['paragraphs']}")
    print(f"Longest sentence: {summary['longest_sentence_words']} words")
    print(f"Average word length: {summary['average_word_length']:.2f}")
    print(f"Lexical diversity: {summary['lexical_diversity']:.2f}")
    print(f"Reading time: {summary['reading_time_minutes']:.2f} minutes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
