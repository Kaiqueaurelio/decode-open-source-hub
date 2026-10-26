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

# Keep upstream license/attribution documents intact. Brand replacement is limited
# to user-facing text and HTML; machine identifiers and package IDs are intentionally
# not mass-renamed because doing so blindly can break install/update compatibility.
python3 - "$DEST" <<'PY'
from pathlib import Path
import sys

root = Path(sys.argv[1])
text_suffixes = {
    ".md", ".html", ".htm", ".txt", ".toml", ".rs", ".json", ".yml", ".yaml",
    ".xml", ".desktop", ".service", ".sh", ".py", ".css", ".js", ".svg",
}
replacements = [
    ("ArtCraft Launcher", "Decode Launcher"),
    ("ArtCraft launcher", "Decode Launcher"),
    ("ArtCraft's", "Decode's"),
    ("ArtCraft", "Decode"),
    ("artcraft_launcher", "decode_launcher"),
    ("ARTCRAFT_LOGO", "DECODE_LOGO"),
    ("ARTCRAFT_LAUNCHER", "DECODE_LAUNCHER"),
    ("artcraft-launcher", "decode-launcher"),
    ("ai.storyteller.decode-launcher", "com.decode.launcher"),
    ("https://github.com/storytold/craft-launcher", "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher"),
]
skip_names = {"LICENSE-MIT", "LICENSE-APACHE", "NOTICE", "ATTRIBUTION.md"}
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

print(f"Imported upstream tree to {root}")
print(f"Updated branding strings in {len(changed)} text files.")
print("NOTICE, ATTRIBUTION.md and license texts were preserved without modification.")
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
