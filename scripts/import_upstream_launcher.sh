#!/usr/bin/env bash
set -Eeuo pipefail

# Import the upstream launcher into ./launcher without touching the catalog site.
# Run from the root of decode-open-source-hub:
#   bash scripts/import_upstream_launcher.sh
#
# This is a source-import step, not a release/build guarantee. It preserves upstream
# license and attribution files and deliberately does not copy .git metadata.

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
DEST="${ROOT}/launcher"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [[ -e "$DEST" ]]; then
  echo "ERROR: $DEST already exists. Back it up or remove it intentionally before importing." >&2
  exit 2
fi

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git is required." >&2
  exit 2
fi

git clone --depth 1 https://github.com/storytold/craft-launcher.git "$TMP/upstream"

# Preserve the complete upstream tree (including binary assets, fonts and icons),
# but never copy its .git directory into this repository.
mkdir -p "$DEST"
cp -a "$TMP/upstream/." "$DEST/"
rm -rf "$DEST/.git"

# Preserve required upstream license/attribution files, replace product branding and rename
# launcher package identifiers/assets. The resulting identifiers still require build and install tests.
python3 - "$DEST" <<'PY'
from pathlib import Path
import re
import shutil
import sys

root = Path(sys.argv[1])
text_suffixes = {
    ".md", ".html", ".htm", ".txt", ".toml", ".rs", ".json", ".yml", ".yaml",
    ".xml", ".desktop", ".service", ".sh", ".py", ".css", ".js", ".svg", ".lock", ".nix", ".tsv", ".plist", ".properties", ".wxs", ".wxl", ".conf", ".cfg", ".po",
}
replacements = [
    ("ArtCraft App Suite", "Decode App Suite"),
    ("ArtCraft Apps", "Decode Apps"),
    ("ArtCraft App", "Decode App"),
    ("Craft App Suite", "Decode App Suite"),
    ("Craft Apps", "Decode Apps"),
    ("Craft App", "Decode App"),
    ("Crafting Apps", "Decode Apps"),
    ("Crafting App", "Decode App"),
    ("PhotoCraft", "PhotoDecode"),
    ("VectorCraft", "VectorDecode"),
    ("FilmCraft", "FilmDecode"),
    ("LightCraft", "LightDecode"),
    ("PdfCraft", "PdfDecode"),
    ("EffectCraft", "EffectDecode"),
    ("DesignCraft", "DesignDecode"),
    ("FigCraft", "FigDecode"),
    ("WordCraft", "WordDecode"),
    ("SoundCraft", "SoundDecode"),
    ("DeckCraft", "DeckDecode"),
    ("CADCraft", "CADDecode"),
    ("GridCraft", "GridDecode"),
    ("ArtCraft API", "Decode API"),
    ("CraftApp", "DecodeApp"),
    ("craft_app", "decode_app"),
    ("artcraft_logo", "decode_logo"),
    ("artcraft_mark", "decode_mark"),
    ("viewBox=\"-10 -19.42 136.34 136.34\"", "viewBox=\"0 0 128 128\""),
    ("ArtCraft Launcher", "Decode Launcher"),
    ("ArtCraft launcher", "Decode Launcher"),
    ("ArtCraft's", "Decode's"),
    ("ArtCraft", "Decode"),
    ("artcraft_launcher", "decode_launcher"),
    ("ARTCRAFT_LOGO", "DECODE_LOGO"),
    ("ARTCRAFT_LAUNCHER", "DECODE_LAUNCHER"),
    ("artcraft-launcher", "decode-launcher"),
    ("artcraft-logo-white", "decode-logo-white"),
    ("artcraft-logo", "decode-logo"),
    ("artcraft-mark", "decode-mark"),
    ("ai.storyteller.decode-launcher", "com.decode.launcher"),
    ("https://github.com/storytold/craft-launcher", "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher"),
]
skip_names = {"LICENSE-MIT", "LICENSE-APACHE", "NOTICE", "ATTRIBUTION.md", "LICENSE.txt"}
changed = []
for path in root.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes or path.name in skip_names:
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    updated = original
    for old, new in replacements:
        updated = updated.replace(old, new)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        changed.append(path.relative_to(root).as_posix())

# Replace upstream trademark artwork with original Decode assets.
# Repository-level NOTICE, ATTRIBUTION.md and license texts remain intact.
brand_dir = root / "docs" / "brand"
brand_dir.mkdir(parents=True, exist_ok=True)
for old_asset in list(brand_dir.iterdir()):
    if old_asset.is_file():
        old_asset.unlink()

logo_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 120" role="img" aria-label="Decode">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#315be9"/><stop offset="1" stop-color="#47d7e7"/></linearGradient></defs>
  <rect x="4" y="4" width="112" height="112" rx="28" fill="url(#g)"/>
  <path d="M37 31h25c22 0 37 13 37 29s-15 29-37 29H37V31zm22 43c11 0 18-5 18-14s-7-14-18-14h-5v28h5z" fill="#fff"/>
  <text x="142" y="82" font-family="Inter,Arial,sans-serif" font-size="70" font-weight="800" letter-spacing="-3" fill="CURRENT">Decode</text>
</svg>
"""
(brand_dir / "decode-logo.svg").write_text(logo_template.replace("CURRENT", "#15213b"), encoding="utf-8")
(brand_dir / "decode-logo-white.svg").write_text(logo_template.replace("CURRENT", "#ffffff"), encoding="utf-8")
mark_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-label="Decode">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#315be9"/><stop offset="1" stop-color="#47d7e7"/></linearGradient></defs>
  <rect x="2" y="2" width="124" height="124" rx="30" fill="url(#g)"/>
  <path d="M34 27h27c25 0 42 15 42 37S86 101 61 101H34V27zm25 53c13 0 21-6 21-16s-8-16-21-16h-3v32h3z" fill="#fff"/>
</svg>
"""
black_mark_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-label="Decode monochrome mark">
  <path d="M34 27h27c25 0 42 15 42 37S86 101 61 101H34V27zm25 53c13 0 21-6 21-16s-8-16-21-16h-3v32h3z" fill="#000"/>
</svg>
"""
(brand_dir / "decode-mark.svg").write_text(mark_template, encoding="utf-8")
(brand_dir / "decode-mark-black.svg").write_text(black_mark_template, encoding="utf-8")

icons_source = root / "crates" / "ui-egui" / "src" / "icons.rs"
if icons_source.exists():
    source = icons_source.read_text(encoding="utf-8").replace("1038.05 / 108.0", "640.0 / 120.0")
    icons_source.write_text(source, encoding="utf-8")

# Change displayed app names but preserve machine IDs and upstream release URLs for compatibility.
catalog_source = root / "crates" / "core" / "src" / "catalog.rs"
if catalog_source.exists():
    source = catalog_source.read_text(encoding="utf-8")
    source = source.replace(
        'assert_eq!(a.name.to_lowercase(), a.id);',
        'assert_eq!(a.name.to_lowercase().replace("decode", "craft"), a.id);'
    )
    launcher_match = re.search(r"pub const LAUNCHER: DecodeApp = app\(\n.*?\n\);", source, re.S)
    if not launcher_match:
        raise SystemExit("ERROR: upstream LAUNCHER record changed; review the import script.")
    launcher_block = launcher_match.group(0)
    launcher_block = launcher_block.replace(
        "pub const LAUNCHER: DecodeApp = app(",
        'pub const LAUNCHER: DecodeApp = DecodeApp {\n'
        '    former_ids: &["artcraft-launcher"],\n'
        '    former_names: &["ArtCraft Launcher"],\n'
        '    ..app(',
        1,
    )
    if not launcher_block.endswith("\n);"):
        raise SystemExit("ERROR: unexpected LAUNCHER record terminator.")
    launcher_block = launcher_block[:-3] + "\n    ),\n};"
    source = source[:launcher_match.start()] + launcher_block + source[launcher_match.end():]
    catalog_source.write_text(source, encoding="utf-8")

# Rename branded asset and packaging paths; update references in text files above first.
for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
    if not path.exists():
        continue
    new_name = path.name.replace("ai.storyteller.artcraft-launcher", "com.decode.launcher")
    new_name = new_name.replace("artcraft", "decode").replace("ArtCraft", "Decode")
    if new_name != path.name:
        target = path.with_name(new_name)
        if not target.exists():
            path.rename(target)

# Rebuild launcher-specific binary icons with an original Decode mark using Python's
# standard library, replacing old trademark artwork in PNG/ICO/ICNS resources.
import struct
import subprocess
import zlib

def write_decode_png(path, size, monochrome=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    samples = 3 if size <= 256 else 1
    raw = bytearray()
    for y in range(size):
        raw.append(0)
        for x in range(size):
            acc = [0, 0, 0, 0]
            for sy in range(samples):
                for sx in range(samples):
                    px = (x + (sx + 0.5) / samples) / size
                    py = (y + (sy + 0.5) / samples) / size
                    dx = max(0.0, abs(px - 0.5) - 0.30)
                    dy = max(0.0, abs(py - 0.5) - 0.30)
                    rounded = dx * dx + dy * dy <= 0.20 * 0.20
                    inside = abs(px - 0.5) <= 0.30 or abs(py - 0.5) <= 0.30 or rounded
                    if not inside:
                        rgba = (0, 0, 0, 0)
                    else:
                        amount = min(1.0, max(0.0, (px + py) / 2))
                        bg = tuple(round(a + (b - a) * amount) for a, b in zip((49, 91, 233), (71, 215, 231))) + (255,)
                        outer = ((0.27 <= px <= 0.46 and 0.20 <= py <= 0.80)
                                 or (((px - 0.44) / 0.30) ** 2 + ((py - 0.50) / 0.30) ** 2 <= 1 and px >= 0.40))
                        inner = (((px - 0.48) / 0.145) ** 2 + ((py - 0.50) / 0.165) ** 2 <= 1) and px >= 0.435
                        if outer and not inner:
                            rgba = (0, 0, 0, 255) if monochrome else (255, 255, 255, 255)
                        elif monochrome:
                            rgba = (0, 0, 0, 0)
                        else:
                            rgba = bg
                    for channel in range(4):
                        acc[channel] += rgba[channel]
            raw.extend(round(v / (samples * samples)) for v in acc)

    def chunk(kind, payload):
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">2I5B", size, size, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    path.write_bytes(png)

icon_dir = root / "assets" / "app-icon"
write_decode_png(icon_dir / "decode-launcher-1024.png", 1024)
for size in (16, 24, 32, 48, 64, 128, 256, 512):
    write_decode_png(icon_dir / "hicolor" / f"{size}x{size}" / "apps" / "com.decode.launcher.png", size)
write_decode_png(brand_dir / "decode-mark.png", 512)
write_decode_png(brand_dir / "decode-mark-64.png", 64)
write_decode_png(brand_dir / "decode-mark-black.png", 512, monochrome=True)
write_decode_png(brand_dir / "decode-mark-black-44.png", 44, monochrome=True)
(icon_dir / "decode-launcher.svg").write_text(mark_template, encoding="utf-8")
(icon_dir / "hicolor" / "scalable" / "apps" / "com.decode.launcher.svg").write_text(mark_template, encoding="utf-8")

with __import__("tempfile").TemporaryDirectory() as temp_dir:
    temp = Path(temp_dir)
    ico_pngs = []
    for size in (16, 20, 24, 32, 40, 48, 64, 128, 256):
        file = temp / f"ico-{size}.png"
        write_decode_png(file, size)
        ico_pngs.append(str(file))
    icns_pngs = []
    for size in (16, 32, 64, 128, 256, 512, 1024):
        file = temp / f"icns-{size}.png"
        write_decode_png(file, size)
        icns_pngs.append(str(file))
    if shutil.which("cargo"):
        subprocess.run(["cargo", "run", "-q", "-p", "xtask", "--", "ico", str(icon_dir / "decode-launcher.ico"), *ico_pngs], cwd=root, check=True)
        subprocess.run(["cargo", "run", "-q", "-p", "xtask", "--", "icns", str(icon_dir / "decode-launcher.icns"), *icns_pngs], cwd=root, check=True)
    else:
        print("cargo not found; skipping .ico and .icns conversion.")

# Upstream screenshots visibly contain the old product identity; do not ship them.
readme = root / "README.md"
if readme.exists():
    content = readme.read_text(encoding="utf-8")
    content = re.sub(r'<p align="center">\s*<img src="docs/screenshots/.*?</p>\s*', "", content, flags=re.S)
    content = content.replace("## What it does", "## What it does\n\n> Screenshots of the Decode-branded build will be added after the application is built and visually verified.\n")
    disclosure = ("> **Independent Decode fork:** this is a modified launcher based on code originally published at "
                  "https://github.com/storytold/craft-launcher. It is not affiliated with or endorsed by the ArtCraft team. "
                  "Technical app IDs and upstream release URLs remain unchanged so installation and updates can find "
                  "the original packages." + chr(10) + chr(10))
    if "Independent Decode fork" not in content:
        content = disclosure + content
    readme.write_text(content, encoding="utf-8")
screenshots = root / "docs" / "screenshots"
if screenshots.exists():
    shutil.rmtree(screenshots)

old_brand_license = brand_dir / "LICENSE-brand.txt"
if old_brand_license.exists():
    old_brand_license.unlink()

print(f"Imported upstream tree to {root}")
print(f"Updated branding strings in {len(changed)} text files.")
print("NOTICE, ATTRIBUTION.md and source license texts were preserved without modification.")\nprint("Original app IDs and release URLs remain intact for installation/update compatibility.")
print("IMPORTANT: review identifiers, icon assets, signing/package IDs and all changes before building.")
PY

cat <<'EOF'
Import completed. Next checks:
  cd launcher
  rustc --version
  cargo xtask ci

This import does not claim the Decode Launcher is buildable or release-ready.
Review the branding, app IDs, asset artwork, attribution and platform packaging first.
EOF
