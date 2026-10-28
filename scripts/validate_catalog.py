#!/usr/bin/env python3
"""Validate all Decode suite apps and launcher utility."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "software.json"
REQUIRED = {
    "slug", "name", "icon", "category", "kind", "tagline", "description",
    "platforms", "license", "licenseUrl", "websiteUrl", "sourceUrl",
    "downloadUrl", "tags", "stage", "featured",
}
OPTIONAL = {
    "downloadWindows", "downloadWindowsExe", "downloadLinux", "downloadMacOS",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def is_https(value):
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme == "https" and bool(parsed.netloc)

def main():
    errors = []
    if not CATALOG.exists():
        print("ERRO: data/software.json não foi encontrado.")
        return 1
    try:
        items = json.loads(CATALOG.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERRO: {exc}")
        return 1
    if not isinstance(items, list):
        print("ERRO: raiz deve ser lista.")
        return 1

    seen_slugs = set()
    for idx, item in enumerate(items, 1):
        prefix = f"Registro #{idx}"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: deve ser um objeto.")
            continue
        missing = REQUIRED - set(item.keys())
        if missing:
            errors.append(f"{prefix}: campos obrigatórios ausentes: {sorted(missing)}.")
            continue
        slug = item.get("slug", "")
        if not SLUG_RE.match(slug):
            errors.append(f"{prefix}: slug inválido: {slug!r}.")
        if slug in seen_slugs:
            errors.append(f"{prefix}: slug duplicado: {slug!r}.")
        seen_slugs.add(slug)

        for url_field in ("licenseUrl", "websiteUrl", "sourceUrl", "downloadUrl"):
            val = item.get(url_field)
            if not is_https(val):
                errors.append(f"{prefix}: {url_field} deve ser uma URL HTTPS válida.")
            elif "storytold" in val.lower() or "artcraft" in val.lower():
                errors.append(f"{prefix}: {url_field} contém referência não permitida: {val}.")

    if errors:
        print("Validação do catálogo Decode: FALHOU")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"Validação do catálogo Decode: OK — {len(items)} aplicativos verificados no monorepo Decode.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
