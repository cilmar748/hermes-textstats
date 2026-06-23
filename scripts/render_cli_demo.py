from __future__ import annotations

from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPT = ROOT / "docs" / "assets" / "hermes-textstats-demo.txt"
OUT = ROOT / "docs" / "assets" / "hermes-textstats-demo.png"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for name in names:
        path = Path(name)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def main() -> None:
    raw_lines = TRANSCRIPT.read_text(encoding="utf-8").splitlines()
    lines: list[str] = []
    for line in raw_lines:
        if len(line) <= 94:
            lines.append(line)
        else:
            lines.extend(textwrap.wrap(line, width=94, subsequent_indent="  "))

    width = 1600
    line_height = 30
    title_height = 54
    padding = 34
    height = title_height + padding + line_height * len(lines) + padding

    img = Image.new("RGB", (width, height), "#111827")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, width, title_height), radius=14, fill="#1f2937")

    for index, color in enumerate(["#ef4444", "#f59e0b", "#22c55e"]):
        draw.ellipse((28 + index * 28, 20, 42 + index * 28, 34), fill=color)

    draw.text((112, 15), "hermes-textstats v0.1.1 demo", font=font(24), fill="#e5e7eb")

    y = title_height + 26
    body_font = font(22)
    for line in lines:
        fill = "#93c5fd" if line.startswith("$") else "#e5e7eb"
        draw.text((34, y), line, font=body_font, fill=fill)
        y += line_height

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
