"""Rebuild flipbook1/pages-data.js from the canonical page JPGs.

The JPGs stay the source. pages-data.js is the local double-click copy:
data URIs so WebGL can upload textures over file://. GitHub Pages does
not load this file.
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "flipbook1" / "manifest.js"
OUT = ROOT / "flipbook1" / "pages-data.js"


def page_list():
    text = MANIFEST.read_text(encoding="utf-8")
    match = re.search(r'"pages"\s*:\s*(\[[^\]]+\])', text)
    if not match:
        raise SystemExit("manifest.js has no pages list")
    return json.loads(match.group(1))


def main():
    pages = page_list()
    lines = ["var PAGE_DATA = {"]
    last = len(pages) - 1
    for i, rel in enumerate(pages):
        path = ROOT / rel.replace("/", "\\")
        if not path.is_file():
            raise SystemExit("missing page file: " + rel)
        raw = path.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        comma = "" if i == last else ","
        lines.append('  "%s": "data:image/jpeg;base64,%s"%s' % (rel, b64, comma))
    lines.append("};")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print("wrote %s (%d pages, %d bytes)" % (OUT.name, len(pages), OUT.stat().st_size))


if __name__ == "__main__":
    main()
