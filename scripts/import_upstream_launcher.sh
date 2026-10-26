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
  echo "Removing existing $DEST before fresh import..."
  rm -rf "$DEST"
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
# launcher package identifiers/assets.
python3 - "$ROOT" "$DEST" <<'PY'
from pathlib import Path
import re
import shutil
import sys

repo_root = Path(sys.argv[1])
root = Path(sys.argv[2])

text_suffixes = {
    ".md", ".html", ".htm", ".txt", ".toml", ".rs", ".json", ".yml", ".yaml",
    ".xml", ".desktop", ".service", ".sh", ".py", ".css", ".js", ".svg", ".lock",
    ".nix", ".tsv", ".plist", ".properties", ".wxs", ".wxl", ".conf", ".cfg", ".po",
}

replacements = [
    ("ArtCraft App Suite", "Decode App Suite"),
    ("ArtCraft Apps Suite", "Decode App Suite"),
    ("ArtCraft Apps", "Decode Apps"),
    ("ArtCraft App", "Decode App"),
    ("Craft App Suite", "Decode App Suite"),
    ("Craft Apps Suite", "Decode App Suite"),
    ("Craft Apps", "Decode Apps"),
    ("Craft App", "Decode App"),
    ("craft apps", "decode apps"),
    ("craft app", "decode app"),
    ("Crafting Apps", "Decode Apps"),
    ("Crafting App", "Decode App"),
    ("PhotoCraft", "DecodePhoto"),
    ("VectorCraft", "DecodeVector"),
    ("FilmCraft", "DecodeFilm"),
    ("LightCraft", "DecodeLight"),
    ("PdfCraft", "DecodePdf"),
    ("EffectCraft", "DecodeEffect"),
    ("DesignCraft", "DecodeDesign"),
    ("FigCraft", "DecodeFig"),
    ("WordCraft", "DecodeWord"),
    ("SoundCraft", "DecodeSound"),
    ("DeckCraft", "DecodeDeck"),
    ("CADCraft", "DecodeCAD"),
    ("CadCraft", "DecodeCad"),
    ("GridCraft", "DecodeGrid"),
    ("PrintCraft", "DecodePrint"),
    ("storytold/cadcraft", "Kaiqueaurelio/decodecad"),
    ("ArtCraft API", "Decode API"),
    ("CraftApp", "DecodeApp"),
    ("craft_app", "decode_app"),
    ("craft_apps", "decode_apps"),
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

    # Protect external upstream git dependencies and release URLs
    updated = updated.replace("storytold/decode-libs", "storytold/craft-libs")
    updated = updated.replace("decode-update", "craft-update")
    updated = updated.replace("decode-quit", "craft-quit")
    updated = updated.replace("decode/0.37", "craft/0.37")
    updated = updated.replace("decode/0.30", "craft/0.30")

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        changed.append(path.relative_to(root).as_posix())

# Replace upstream trademark artwork with original Decode assets
brand_dir = root / "docs" / "brand"
brand_dir.mkdir(parents=True, exist_ok=True)
for old_asset in list(brand_dir.iterdir()):
    if old_asset.is_file():
        old_asset.unlink()

repo_brand = repo_root / "assets" / "brand"
if repo_brand.exists():
    for f in repo_brand.iterdir():
        if f.is_file():
            shutil.copy2(f, brand_dir / f.name)

# Replace launcher icon assets with original Decode assets
icon_dir = root / "assets" / "app-icon"
icon_dir.mkdir(parents=True, exist_ok=True)
for old_icon in list(icon_dir.iterdir()):
    if old_icon.is_file() and old_icon.name not in {"LICENSE.txt", "README.md"}:
        old_icon.unlink()

repo_icons = repo_root / "assets" / "launcher-icon"
if repo_icons.exists():
    for f in repo_icons.iterdir():
        if f.is_file():
            shutil.copy2(f, icon_dir / f.name)
        elif f.is_dir() and f.name == "hicolor":
            shutil.copytree(f, icon_dir / "hicolor", dirs_exist_ok=True)

icons_source = root / "crates" / "ui-egui" / "src" / "icons.rs"
if icons_source.exists():
    source = icons_source.read_text(encoding="utf-8").replace("1038.05 / 108.0", "640.0 / 120.0")
    icons_source.write_text(source, encoding="utf-8")

# Update catalog.rs: former_names for all 13 Decode apps and test assertions
catalog_source = root / "crates" / "core" / "src" / "catalog.rs"
if catalog_source.exists():
    source = catalog_source.read_text(encoding="utf-8")
    source = source.replace(
        "assert_eq!(a.name.to_lowercase(), a.id);",
        'if a.id == "cadcraft" { assert_eq!(a.repo, "Kaiqueaurelio/decodecad"); } else { assert_eq!(a.repo, format!("storytold/{}", a.id)); }\n            assert_eq!(a.name.to_lowercase().replace("decode", "") + "craft", a.id);'
    )
    source = source.replace(
        'assert_eq!(pdf.names().collect::<Vec<_>>(), ["DecodePdf", "DecodePrint"]);',
        'assert_eq!(pdf.names().collect::<Vec<_>>(), ["DecodePdf", "PdfCraft", "PrintCraft"]);'
    )

    apps_pairs = [
        ("photocraft", "PhotoCraft"),
        ("vectorcraft", "VectorCraft"),
        ("filmcraft", "FilmCraft"),
        ("lightcraft", "LightCraft"),
        ("effectcraft", "EffectCraft"),
        ("designcraft", "DesignCraft"),
        ("figcraft", "FigCraft"),
        ("wordcraft", "WordCraft"),
        ("soundcraft", "SoundCraft"),
        ("deckcraft", "DeckCraft"),
        ("cadcraft", "CADCraft"),
        ("gridcraft", "GridCraft"),
    ]
    for app_id, former_name in apps_pairs:
        pat = re.compile(r"app\(\s*\"" + app_id + r"\"(.*?\"storytold/" + app_id + r"\".*?\))", re.S)
        m = pat.search(source)
        if m:
            repl = f"DecodeApp {{ former_names: &[\"{former_name}\"], ..app(\"{app_id}\"{m.group(1)} }}"
            source = source[:m.start()] + repl + source[m.end():]

    source = source.replace(
        'former_names: &["DecodePrint"],',
        'former_names: &["PdfCraft", "PrintCraft"],'
    )
    source = source.replace('"storytold/cadcraft"', '"Kaiqueaurelio/decodecad"')

    launcher_match = re.search(r"pub const LAUNCHER: DecodeApp = app\(\n.*?\n\);", source, re.S)
    if launcher_match:
        launcher_block = launcher_match.group(0)
        launcher_block = launcher_block.replace(
            "pub const LAUNCHER: DecodeApp = app(",
            'pub const LAUNCHER: DecodeApp = DecodeApp {\n'
            '    former_ids: &["artcraft-launcher"],\n'
            '    former_names: &["ArtCraft Launcher"],\n'
            '    ..app(',
            1,
        )
        if launcher_block.endswith("\n);"):
            launcher_block = launcher_block[:-3] + "\n    )\n};"
            source = source[:launcher_match.start()] + launcher_block + source[launcher_match.end():]

    catalog_source.write_text(source, encoding="utf-8")

# Update detect.rs test assertions for Decode names vs former PrintCraft / PdfCraft names
detect_source = root / "crates" / "native" / "src" / "detect.rs"
if detect_source.exists():
    ds = detect_source.read_text(encoding="utf-8")
    ds = ds.replace('assert_eq!(v("PdfDecode.AppImage"), Some(None));', 'assert_eq!(v("PdfCraft.AppImage"), Some(None));')
    ds = ds.replace('"PrintDecode"', '"PrintCraft"')
    ds = ds.replace('for dir in ["PdfDecode", "PrintCraft"] {', 'for dir in ["PdfDecode", "PdfCraft", "PrintCraft"] {')
    detect_source.write_text(ds, encoding="utf-8")

# Rename branded asset and packaging paths
for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
    if not path.exists():
        continue
    new_name = path.name.replace("ai.storyteller.artcraft-launcher", "com.decode.launcher")
    new_name = new_name.replace("artcraft", "decode").replace("ArtCraft", "Decode")
    if new_name != path.name:
        target = path.with_name(new_name)
        if not target.exists():
            path.rename(target)

# Clean up upstream screenshots and add Decode Launcher banner
readme = root / "README.md"
if readme.exists():
    content = readme.read_text(encoding="utf-8")
    content = re.sub(r'<p align="center">\s*<img src="docs/screenshots/.*?</p>\s*', "", content, flags=re.S)
    disclosure = ("> **Decode Launcher:** central oficial da suíte de aplicativos criativos Decode. "
                  "Uma solução moderna em Rust para instalar, gerenciar e atualizar ferramentas de "
                  "código aberto com alto desempenho, segurança e respeito à privacidade.\n\n")
    if "Decode Launcher:" not in content:
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
print("NOTICE, ATTRIBUTION.md and source license texts were preserved without modification.")
print("Original app IDs and release URLs remain intact for installation/update compatibility.")
PY

cat <<'EOF'
Import completed. Next checks:
  cd launcher
  rustc --version
  cargo xtask ci

This import does not claim the Decode Launcher is buildable or release-ready.
Review the branding, app IDs, asset artwork, attribution and platform packaging first.
EOF
