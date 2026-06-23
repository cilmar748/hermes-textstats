from __future__ import annotations

from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "hermes-textstats-showcase.png"
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hermes_textstats import analyze_text

WIDTH = 1600
HEIGHT = 900

BG = "#f8fafc"
INK = "#0f172a"
MUTED = "#475569"
BLUE = "#2563eb"
CYAN = "#0891b2"
GREEN = "#16a34a"
AMBER = "#d97706"
CARD = "#ffffff"
LINE = "#cbd5e1"
TERMINAL = "#111827"
TERMINAL_TEXT = "#d1fae5"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
    ]
    for name in names:
        path = Path(name)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def rounded(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str | None = None, width: int = 2) -> None:
    draw.rounded_rectangle(xy, radius=24, fill=fill, outline=outline, width=width)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, size: int, fill: str = INK, bold: bool = False) -> None:
    draw.text(xy, value, font=font(size, bold), fill=fill)


def centered(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], value: str, size: int, fill: str = INK, bold: bool = False) -> None:
    fnt = font(size, bold)
    bbox = draw.textbbox((0, 0), value, font=fnt)
    x = box[0] + (box[2] - box[0] - (bbox[2] - bbox[0])) / 2
    y = box[1] + (box[3] - box[1] - (bbox[3] - bbox[1])) / 2
    draw.text((x, y), value, font=fnt, fill=fill)


def pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int], label: str, color: str) -> int:
    fnt = font(28, True)
    bbox = draw.textbbox((0, 0), label, font=fnt)
    w = bbox[2] - bbox[0] + 44
    h = 52
    x, y = xy
    draw.rounded_rectangle((x, y, x + w, y + h), radius=26, fill=color)
    draw.text((x + 22, y + 10), label, font=fnt, fill="#ffffff")
    return w


def main() -> None:
    sample = "Hermes helps students build, test, document, and publish Python packages from DIVE."
    stats = analyze_text(sample)

    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Header
    text(draw, (80, 56), "Hermes TextStats", 74, INK, True)
    text(draw, (84, 142), "A DIVE-ready Python package for short text, files, and notebook drafts.", 34, MUTED)

    x = 84
    for label, color in [
        ("v0.1.1 ready", BLUE),
        ("22 tests passed", GREEN),
        ("CLI + File + Report", CYAN),
    ]:
        x += pill(draw, (x, 210), label, color) + 18

    # Left workflow card
    rounded(draw, (80, 310, 700, 780), CARD, LINE)
    text(draw, (122, 350), "Agentic package workflow", 38, INK, True)
    text(draw, (122, 405), "DIVE/JupyterHub -> Hermes Agent -> git -> PyPI", 26, MUTED)

    steps = [
        ("1", "Build", "src layout, CLI, public API", BLUE),
        ("2", "Improve", "file input, Markdown report, writing metrics", GREEN),
        ("3", "Document", "user guide, developer guide, paper notes", CYAN),
        ("4", "Publish", "PyPI release with verified install", AMBER),
    ]
    y = 470
    for number, title, desc, color in steps:
        draw.ellipse((122, y, 178, y + 56), fill=color)
        centered(draw, (122, y, 178, y + 56), number, 26, "#ffffff", True)
        text(draw, (202, y - 2), title, 30, INK, True)
        text(draw, (202, y + 34), desc, 24, MUTED)
        y += 78

    # Right terminal/demo card
    rounded(draw, (750, 310, 1520, 780), TERMINAL, "#1f2937")
    text(draw, (790, 350), "Published package demo", 38, "#f8fafc", True)
    text(draw, (790, 405), "$ pip install hermes-textstats==0.1.1", 26, TERMINAL_TEXT)
    text(draw, (790, 450), "$ hermes-textstats --report --file reflection.txt", 26, TERMINAL_TEXT)

    output = [
        f"Characters: {stats['characters']}",
        f"Words: {stats['words']}",
        f"Sentences: {stats['sentences']}",
        f"Paragraphs: {stats['paragraphs']}",
        f"Longest sentence: {stats['longest_sentence_words']} words",
        f"Average word length: {stats['average_word_length']:.2f}",
        f"Lexical diversity: {stats['lexical_diversity']:.2f}",
        f"Reading time: {stats['reading_time_minutes']:.2f} minutes",
    ]
    y = 500
    for line in output:
        text(draw, (820, y), line, 23, "#e5e7eb")
        y += 33

    # Bottom proof strip
    draw.rounded_rectangle((80, 812, 1520, 858), radius=23, fill="#e0f2fe")
    centered(
        draw,
        (80, 812, 1520, 858),
        "PyPI: https://pypi.org/project/hermes-textstats/",
        26,
        "#075985",
        True,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
