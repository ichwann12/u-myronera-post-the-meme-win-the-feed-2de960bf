"""Generate meme.png for the make.fun "Post the Meme, Win the Feed" bounty.

Classic top-text / bottom-text meme, 1080x1080, drawn entirely with PIL:
dark navy gradient, a subtle circuit-board motif, a small robot face in the
middle, bold white text with a black outline, and a make.fun wordmark.

Deterministic: fixed random seed, no network, no wall clock. Two runs
produce byte-identical output.
"""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "meme.png"

W, H = 1080, 1080
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP_LINES = ["MY AGENT ENTERED", "THE BOUNTY"]
BOTTOM_LINES = ["THE JUDGE IS", "ALSO AN AI"]
WORDMARK = "make.fun"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def draw_gradient(draw):
    top = (11, 16, 38)
    bottom = (20, 27, 61)
    for y in range(H):
        draw.line([(0, y), (W, y)], fill=lerp(top, bottom, y / H))


def draw_circuits(draw, rng):
    # Faint right-angle traces with nodes, seeded so output is stable.
    for _ in range(26):
        x = rng.randint(0, W)
        y = rng.randint(0, H)
        length = rng.randint(60, 220)
        horizontal = rng.random() < 0.5
        color = (34, 211, 238, 26)
        if horizontal:
            draw.line([(x, y), (x + length, y)], fill=color, width=2)
            draw.ellipse([x + length - 5, y - 5, x + length + 5, y + 5],
                         outline=color, width=2)
        else:
            draw.line([(x, y), (x, y + length)], fill=color, width=2)
            draw.ellipse([x - 5, y + length - 5, x + 5, y + length + 5],
                         outline=color, width=2)
        draw.ellipse([x - 4, y - 4, x + 4, y + 4], outline=color, width=2)


def draw_robot(draw):
    # Small robot face in the middle band: rounded head, antenna, glowing eyes.
    cx, cy = W // 2, 505
    head_w, head_h = 300, 220
    x0, y0 = cx - head_w // 2, cy - head_h // 2
    x1, y1 = cx + head_w // 2, cy + head_h // 2
    # Antenna
    draw.line([(cx, y0 - 55), (cx, y0)], fill=(34, 211, 238), width=6)
    draw.ellipse([cx - 14, y0 - 72, cx + 14, y0 - 44],
                 fill=(34, 211, 238))
    # Head
    draw.rounded_rectangle([x0, y0, x1, y1], radius=42,
                           outline=(34, 211, 238), width=6)
    # Eyes
    for ex in (cx - 70, cx + 70):
        draw.ellipse([ex - 28, cy - 40, ex + 28, cy + 16],
                     fill=(34, 211, 238))
        draw.ellipse([ex - 12, cy - 28, ex + 12, cy - 4],
                     fill=(11, 16, 38))
    # Smile
    draw.arc([cx - 55, cy + 25, cx + 55, cy + 85], start=15, end=165,
             fill=(34, 211, 238), width=6)
    # Side bolts
    for bx in (x0 - 14, x1 + 14):
        draw.ellipse([bx - 10, cy - 10, bx + 10, cy + 10],
                     outline=(34, 211, 238), width=4)


def draw_centered_text(draw, lines, font, y_start, line_gap, stroke):
    y = y_start
    for line in lines:
        w = draw.textlength(line, font=font)
        draw.text(((W - w) / 2, y), line, font=font, fill=(255, 255, 255),
                  stroke_width=stroke, stroke_fill=(0, 0, 0))
        y += font.size + line_gap
    return y


def main():
    rng = random.Random(42)
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img, "RGBA")
    draw_gradient(draw)
    draw_circuits(draw, rng)
    draw_robot(draw)

    top_font = ImageFont.truetype(FONT_PATH, 92)
    draw_centered_text(draw, TOP_LINES, top_font, 72, 8, 7)

    bottom_font = ImageFont.truetype(FONT_PATH, 92)
    draw_centered_text(draw, BOTTOM_LINES, bottom_font, 792, 8, 8)

    mark_font = ImageFont.truetype(FONT_PATH, 44)
    w = draw.textlength(WORDMARK, font=mark_font)
    draw.text(((W - w) / 2, 1008), WORDMARK, font=mark_font,
              fill=(148, 163, 184), stroke_width=2, stroke_fill=(0, 0, 0))

    img.save(OUT, "PNG")
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
