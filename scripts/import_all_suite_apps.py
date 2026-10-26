#!/usr/bin/env python3
"""
Imports all 13 Crafting Apps from upstream (storytold) into apps/ in decode-open-source-hub,
rebranding names and titles to the Decode identity while preserving open source licenses.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"

SUITE = [
    ("photocraft", "decode-photo", "DecodePhoto", "Image editing: layers, masks, type and real PSD files", "photocraft"),
    ("vectorcraft", "decode-vector", "DecodeVector", "Vector illustration", "vectorcraft"),
    ("filmcraft", "decode-film", "DecodeFilm", "Video editing, color and sound", "filmcraft"),
    ("lightcraft", "decode-light", "DecodeLight", "Photo library and raw development", "lightcraft"),
    ("pdfcraft", "decode-pdf", "DecodePdf", "Reading, organizing and protecting PDFs", "pdfcraft"),
    ("effectcraft", "decode-effect", "DecodeEffect", "Motion graphics and visual effects", "effectcraft"),
    ("designcraft", "decode-design", "DecodeDesign", "Page layout and desktop publishing", "designcraft"),
    ("figcraft", "decode-fig", "DecodeFig", "Interface design and prototyping", "figcraft"),
    ("wordcraft", "decode-word", "DecodeWord", "Word processing and documents", "wordcraft"),
    ("soundcraft", "decode-sound", "DecodeSound", "Audio recording and editing", "soundcraft"),
    ("deckcraft", "decode-deck", "DecodeDeck", "Presentations and slide shows", "deckcraft"),
    ("cadcraft", "decode-cad", "DecodeCAD", "Computer-aided design and drafting", "cadcraft"),
    ("gridcraft", "decode-grid", "DecodeGrid", "Spreadsheets and data", "gridcraft"),
]


def import_app(upstream_slug, dest_name, decode_name, description, original_name):
    target = APPS_DIR / dest_name
    print(f"==> Importing {upstream_slug} -> {target} ({decode_name})...")

    if target.exists():
        print(f"    Target directory {target} already exists. Cleaning up before fresh import...")
        shutil.rmtree(target)

    tmp_dir = Path("/tmp") / f"import-{upstream_slug}"
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)

    if upstream_slug == "cadcraft":
        upstream_url = "https://github.com/Kaiqueaurelio/decodecad.git"
    else:
        upstream_url = f"https://github.com/storytold/{upstream_slug}.git"
    print(f"    Cloning shallow from {upstream_url}...")
    clone_res = subprocess.run(
        ["git", "clone", "--depth", "1", upstream_url, str(tmp_dir)],
        check=False,
        capture_output=True,
        text=True,
    )
    if clone_res.returncode != 0:
        print(f"ERROR cloning {upstream_slug}: {clone_res.stderr}", file=sys.stderr)
        return False

    git_dir = tmp_dir / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)

    # Copy to target
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(tmp_dir, target)
    shutil.rmtree(tmp_dir)

    # Polish README.md
    readme_path = target / "README.md"
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8", errors="replace")
        header_note = (
            f"> **Decode Open Source Hub:** This is the `{decode_name}` application, "
            f"an open-source tool part of the Decode App Suite (originally `{upstream_slug}`). "
            f"Preserved under MIT / Apache-2.0 open source licenses.\n\n"
        )
        # Update title in README
        if not content.startswith("> **Decode Open Source Hub:"):
            content = header_note + content
        readme_path.write_text(content, encoding="utf-8")

    print(f"    Successfully imported {decode_name} into {target}")
    return True


def generate_apps_readme():
    readme_path = APPS_DIR / "README.md"
    rows = []
    for upstream, dest, name, desc, orig in SUITE:
        rows.append(f"| **[{name}]({dest}/)** | `{dest}` | {desc} | [Original]({upstream}) |")

    table = "\n".join(rows)
    content = f"""# Decode App Suite — Source Repositories

This directory contains the standalone source workspaces for all 13 applications in the **Decode App Suite**, recreated and maintained within the Decode Open Source Hub.

Each application is a clean, pure-Rust workspace designed with native GUI interfaces (`egui`), multiplatform packaging, and open-source standards.

| Application | Directory | Purpose | Origin |
|:---|:---|:---|:---|
{table}

## Architecture

* **Decoupled Workspaces**: Each application in `apps/<app>` has its own `Cargo.toml`, internal crates (`crates/*`), shell application (`apps/*`), and packaging recipes.
* **Launch & Updates**: The [Decode Launcher](../launcher/) discovers, opens, installs, and updates all applications in this suite.
* **Licensing**: All tools are open source under **MIT OR Apache-2.0** licenses.
"""
    readme_path.write_text(content, encoding="utf-8")
    print(f"Generated {readme_path}")


def main():
    print("Starting import of all 13 Decode suite applications...")
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    success_count = 0

    for upstream, dest, name, desc, orig in SUITE:
        if import_app(upstream, dest, name, desc, orig):
            success_count += 1

    generate_apps_readme()
    print(f"\nImport finished! {success_count}/{len(SUITE)} applications successfully recreated in {APPS_DIR}.")


if __name__ == "__main__":
    main()
