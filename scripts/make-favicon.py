"""Draws the favicon set into public/.

    python3 scripts/make-favicon.py          # dithered moon
    python3 scripts/make-favicon.py mono     # "dm" monogram on an ink tile

Makes favicon.svg (32px grid), favicon.ico (16 + 32px) and apple-touch-icon.png
(180px). Standard library only: the PNGs are written by hand.
"""

import math
import struct
import zlib
from pathlib import Path

INK = (0x2A, 0x2A, 0x28)
PAPER = (0xE2, 0xE0, 0xD9)
LIGHT = (0.75, -0.35, 0.56)  # from the upper right, a little in front
PUBLIC = Path(__file__).resolve().parent.parent / 'public'


def moon(n):
    """An n x n grid of INK, PAPER or None (transparent)."""
    r = n / 2 - (1.5 if n >= 32 else 0.75)
    c = n / 2
    gray = [[None] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            dx, dy = (x + 0.5 - c) / r, (y + 0.5 - c) / r
            d = dx * dx + dy * dy
            if d <= 1:
                z = math.sqrt(1 - d)
                b = max(0.0, dx * LIGHT[0] + dy * LIGHT[1] + z * LIGHT[2])
                gray[y][x] = 255 * (0.08 + 0.92 * b**0.8)

    # Atkinson dithering, the same as the images on the site
    grid = [[None] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            v = gray[y][x]
            if v is None:
                continue
            out = 255 if v >= 128 else 0
            err = (v - out) / 8
            for ddx, ddy in ((1, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (0, 2)):
                nx, ny = x + ddx, y + ddy
                if 0 <= nx < n and ny < n and gray[ny][nx] is not None:
                    gray[ny][nx] += err
            grid[y][x] = PAPER if out else INK

    # an ink rim so the lit side shows on light tab bars
    for y in range(n):
        for x in range(n):
            if r - 1 <= math.hypot(x + 0.5 - c, y + 0.5 - c) <= r + 0.2:
                grid[y][x] = INK
    return grid


def monogram():
    """A pixel "dm", paper on an ink tile with rounded corners, on a 16px grid."""
    n = 16
    grid = [[INK] * n for _ in range(n)]
    for x, y in ((0, 0), (1, 0), (0, 1), (n - 1, 0), (n - 2, 0), (n - 1, 1)):
        for gx, gy in ((x, y), (x, n - 1 - y)):
            grid[gy][gx] = None
    d = ['...#', '...#', '.###', '#..#', '#..#', '.###']
    m = ['##.#.', '#.#.#', '#.#.#', '#.#.#', '#.#.#']
    for j, row in enumerate(d):
        for i, ch in enumerate(row):
            if ch == '#':
                grid[5 + j][2 + i] = PAPER
    for j, row in enumerate(m):
        for i, ch in enumerate(row):
            if ch == '#':
                grid[6 + j][8 + i] = PAPER
    return grid


def to_svg(grid):
    n = len(grid)
    hexc = lambda rgb: '#%02x%02x%02x' % rgb
    rects = []
    for y, row in enumerate(grid):
        x = 0
        while x < n:  # one rect per run of same-colored pixels
            px, w = row[x], 1
            while x + w < n and row[x + w] == px:
                w += 1
            if px:
                rects.append(f'<rect x="{x}" y="{y}" width="{w}" height="1" fill="{hexc(px)}"/>')
            x += w
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges">\n'
        + '\n'.join(rects)
        + '\n</svg>\n'
    )


def to_png(grid, scale=1, size=None, background=None):
    """RGBA PNG; the grid is scaled up by whole pixels and centered in size x size."""
    n = len(grid)
    size = size or n * scale
    off = (size - n * scale) // 2
    bg = (*background, 255) if background else (0, 0, 0, 0)
    rows = []
    for Y in range(size):
        row = bytearray([0])  # filter: none
        for X in range(size):
            gx, gy = (X - off) // scale, (Y - off) // scale
            px = grid[gy][gx] if 0 <= gx < n and 0 <= gy < n and X >= off and Y >= off else None
            row += bytes((*px, 255) if px else bg)
        rows.append(bytes(row))
    chunk = lambda kind, data: struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    return (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
        + chunk(b'IDAT', zlib.compress(b''.join(rows), 9))
        + chunk(b'IEND', b'')
    )


def to_ico(pngs):
    """An .ico holding PNG images (fine in every current browser)."""
    header = struct.pack('<HHH', 0, 1, len(pngs))
    entries, data = b'', b''
    offset = 6 + 16 * len(pngs)
    for size, png in pngs:
        entries += struct.pack('<BBBBHHII', size % 256, size % 256, 0, 0, 1, 32, len(png), offset + len(data))
        data += png
    return header + entries + data


if __name__ == '__main__':
    import sys

    if sys.argv[1:] == ['mono']:
        small = monogram()
        big, ico32, touch = small, to_png(small, scale=2), to_png(small, scale=10, size=180, background=INK)
    else:
        big, small = moon(32), moon(16)
        ico32 = to_png(big)
        # iOS fills transparency with black, so the touch icon sits on paper
        touch = to_png(big, scale=4, size=180, background=PAPER)
    (PUBLIC / 'favicon.svg').write_text(to_svg(big))
    (PUBLIC / 'favicon.ico').write_bytes(to_ico([(16, to_png(small)), (32, ico32)]))
    (PUBLIC / 'apple-touch-icon.png').write_bytes(touch)
    print('wrote favicon.svg, favicon.ico, apple-touch-icon.png')
