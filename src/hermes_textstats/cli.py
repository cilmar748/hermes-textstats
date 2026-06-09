"""Command-line interface for hermes-textstats."""

from __future__ import annotations

import argparse
import json

from . import analyze_text


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hermes-textstats",
        description="Show simple statistics for a text snippet.",
    )
    parser.add_argument("text", help="Text to analyze.")
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Print the summary as JSON.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the hermes-textstats command-line interface."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if not args.text.strip():
        parser.error("text must not be empty")

    summary = analyze_text(args.text)
    if args.as_json:
        print(json.dumps(summary, sort_keys=True))
        return 0

    print(f"Characters: {summary['characters']}")
    print(f"Characters without spaces: {summary['characters_no_spaces']}")
    print(f"Words: {summary['words']}")
    print(f"Sentences: {summary['sentences']}")
    print(f"Average word length: {summary['average_word_length']:.2f}")
    print(f"Reading time: {summary['reading_time_minutes']:.2f} minutes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
