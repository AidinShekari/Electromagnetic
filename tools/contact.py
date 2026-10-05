#!/usr/bin/env python3
"""QA helper: render a PDF to contact sheets (2 x 2 pages per sheet) for visual inspection.
Usage: python3 tools/contact.py book.pdf outdir [dpi]"""
import subprocess, sys, tempfile, glob, os
from PIL import Image, ImageDraw
pdf, out = sys.argv[1], sys.argv[2]
dpi = sys.argv[3] if len(sys.argv) > 3 else "55"
os.makedirs(out, exist_ok=True)
with tempfile.TemporaryDirectory() as t:
    subprocess.run(["pdftoppm", "-r", dpi, "-png", pdf, f"{t}/p"], check=True)
    pages = sorted(glob.glob(f"{t}/p-*.png"))
    for k in range(0, len(pages), 4):
        ims = [Image.open(p) for p in pages[k:k + 4]]
        w, h = ims[0].size
        sheet = Image.new("RGB", (2 * w + 6, 2 * h + 6), "gray")
        for i, im in enumerate(ims):
            sheet.paste(im, ((i % 2) * (w + 6), (i // 2) * (h + 6)))
            ImageDraw.Draw(sheet).text(((i % 2) * (w + 6) + 4, (i // 2) * (h + 6) + 2), str(k + i + 1), fill="red")
        sheet.save(f"{out}/sheet-{k // 4 + 1:02d}.png")
print(len(pages), "pages")
