#!/usr/bin/env python3
"""Verify release package naming, expected coverage and SHA-256 files."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

NAME = re.compile(
    r"^(?P<app>[a-z0-9]+)-(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)-"
    r"(?:(?P<linux_platform>linux-x86_64)\.(?P<linux_suffix>tar\.gz|AppImage(?:\.zsync)?)|"
    r"(?P<windows_platform>windows-x64)-(?P<windows_suffix>portable\.zip))$"
)


def read_checksums(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+[* ]?(.+)", line.strip())
            if match:
                rows[match.group(2)] = match.group(1).lower()
    except OSError:
        return {}
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--manifest", type=Path, default=Path("scripts/apps-manifest.json"))
    parser.add_argument("--allow-missing", action="store_true", help="report missing matrix outputs but allow partial publish")
    parser.add_argument("--summary", type=Path, help="append an app/platform table to this Markdown file")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    apps = [item["id"] for item in manifest["apps"]]
    assets = [p for p in args.directory.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt"] if args.directory.exists() else []
    bad: list[str] = []
    present: set[tuple[str, str, str]] = set()
    sums: dict[str, str] = {}
    for path in assets:
        if path.name.endswith(".sha256"):
            if not read_checksums(path):
                bad.append(f"invalid or empty checksum sidecar: {path.name}")
            sums.update(read_checksums(path))
            continue
        match = NAME.fullmatch(path.name)
        if not match:
            # Previous release assets are preserved under a separate directory and aren't scanned.
            bad.append(f"unexpected artifact name: {path.name}")
            continue
        app = match["app"]
        platform = match["linux_platform"] or match["windows_platform"]
        suffix = match["linux_suffix"] or match["windows_suffix"]
        if app not in apps:
            bad.append(f"unknown app in artifact: {path.name}")
            continue
        present.add((app, platform, suffix))
        sibling = path.with_name(path.name + ".sha256")
        if sibling.is_file():
            sums.update(read_checksums(sibling))
        elif not path.name.endswith(".AppImage.zsync") and not (args.directory / "SHA256SUMS.txt").is_file():
            bad.append(f"missing checksum sidecar for {path.name}")
    missing: list[str] = []
    expected = [(app, "linux-x86_64", suffix) for app in apps for suffix in ("tar.gz", "AppImage", "AppImage.zsync")]
    expected += [(app, "windows-x64", "portable.zip") for app in apps]
    for key in expected:
        app, platform, suffix = key
        separator = "." if platform == "linux-x86_64" else "-"
        filename = f"{app}-<version>-{platform}{separator}{suffix}"
        if key not in present:
            missing.append(filename)
    # Every published payload must have a matching SHA-256 line, whether in its sidecar or the release manifest.
    release_sums = read_checksums(args.directory / "SHA256SUMS.txt")
    if (args.directory / "SHA256SUMS.txt").exists() and not release_sums:
        bad.append("SHA256SUMS.txt is empty or invalid")
    sums.update(release_sums)
    for path in assets:
        if path.name.endswith(".sha256"):
            continue
        match = NAME.fullmatch(path.name)
        if match and path.name not in sums:
            bad.append(f"missing checksum entry for {path.name}")
        elif match and hashlib.sha256(path.read_bytes()).hexdigest() != sums[path.name]:
            bad.append(f"checksum mismatch for {path.name}")
    lines = ["### Release artifact matrix", "", "| App | Linux tar.gz | Linux AppImage | Windows ZIP |", "|---|---:|---:|---:|"]
    for app in apps:
        vals = ["✅" if (app, "linux-x86_64", "tar.gz") in present else "—",
                "✅" if (app, "linux-x86_64", "AppImage") in present else "—",
                "✅" if (app, "windows-x64", "portable.zip") in present else "—"]
        lines.append(f"| {app} | {vals[0]} | {vals[1]} | {vals[2]} |")
    lines.extend(["", f"Published payloads verified: {len(present)}."])
    if missing:
        lines.extend(["", "Missing expected matrix outputs:", *[f"- `{item}`" for item in missing]])
    if bad:
        lines.extend(["", "Artifact validation errors:", *[f"- {item}" for item in bad]])
    if args.summary:
        with args.summary.open("a", encoding="utf-8") as output:
            output.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    if bad or (missing and not args.allow_missing):
        return 1
    if not present:
        print("No valid release artifacts were produced.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
