#!/usr/bin/env python3
"""Generate the README support matrix from the latest GitHub release assets."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPO = "Kaiqueaurelio/decode-open-source-hub"
START = "<!-- RELEASE_SUPPORT_START -->"
END = "<!-- RELEASE_SUPPORT_END -->"
ASSET = re.compile(r"^(?P<app>[a-z0-9]+)-(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)-(?:(?P<platform>linux-x86_64)\.(?P<linux_format>tar\.gz|AppImage)|(?P<windows_platform>windows-x64)-(?P<windows_format>portable\.zip))$")


def version_key(version: str) -> tuple[tuple[int, ...], tuple[int, ...], str]:
    release, _, prerelease = version.partition("-")
    return tuple(map(int, release.split("."))), (1,) if not prerelease else (0,), prerelease


def latest_release() -> dict:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/releases/latest",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "decode-readme-release-check"},
    )
    token = os.environ.get("GH_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def matrix(manifest: dict, release: dict) -> str:
    known = {entry["id"]: entry["name"] for entry in manifest["apps"]}
    assets: dict[tuple[str, str, str], dict] = {}
    for asset in release.get("assets", []):
        match = ASSET.fullmatch(asset.get("name", ""))
        if not match or match["app"] not in known:
            continue
        platform = match["platform"] or match["windows_platform"]
        file_format = match["linux_format"] or match["windows_format"]
        key = (match["app"], platform, file_format)
        current = assets.get(key)
        # Release assets may contain several versioned copies; compare semantic version strings.
        if current is None or version_key(match["version"]) > version_key(ASSET.fullmatch(current["name"])["version"]):
            assets[key] = asset
    planned = {k: set(v) for k, v in manifest.get("planned_formats", {}).items()}
    rows = [
        f"Release consultada: [{release.get('tag_name', 'desconhecida')}]({release.get('html_url', f'https://github.com/{REPO}/releases/latest')}).",
        "",
        "| Aplicativo | Linux x86_64 · tar.gz | Linux x86_64 · AppImage | Windows x64 · ZIP portátil | macOS |",
        "|---|---|---|---|---|",
    ]
    for app, name in known.items():
        cells = []
        for platform, fmt in [("linux-x86_64", "tar.gz"), ("linux-x86_64", "AppImage"), ("windows-x64", "portable.zip")]:
            asset = assets.get((app, platform, fmt))
            if asset:
                filename = asset["name"]
                url = f"https://github.com/{REPO}/releases/latest/download/{filename}"
                cells.append(f"[Disponível]({url}) · `{filename}`")
            elif fmt in planned.get(platform, set()):
                cells.append("Planejado")
            else:
                cells.append("Não publicado")
        cells.append("Não publicado")
        rows.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path("scripts/apps-manifest.json"))
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--release-json", type=Path, help="use a saved release API response instead of requesting latest")
    parser.add_argument("--check", action="store_true", help="fail if generated content differs from README")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    release = json.loads(args.release_json.read_text(encoding="utf-8")) if args.release_json else latest_release()
    section = f"{START}\n{matrix(manifest, release)}\n{END}"
    readme = args.readme.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1:
        print("README must contain exactly one generated support matrix block", file=sys.stderr)
        return 2
    before, rest = readme.split(START, 1)
    _, after = rest.split(END, 1)
    output = before + section + after
    if args.check:
        if output != readme:
            print("README release support matrix is stale; run scripts/generate-readme-downloads.py", file=sys.stderr)
            return 1
        if "v0.9.0" in readme or "release-package.tar.gz" in readme:
            print("README contains a stale release or artifact link", file=sys.stderr)
            return 1
        print(f"README support matrix matches {release.get('tag_name', 'latest')}.")
        return 0
    args.readme.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
