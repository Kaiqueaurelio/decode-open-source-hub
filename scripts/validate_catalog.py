#!/usr/bin/env python3
"""Validate the static software catalog using only the Python standard library."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "software.json"
REQUIRED = {
    "slug", "name", "icon", "category", "tagline", "description",
    "platforms", "license", "licenseUrl", "websiteUrl", "sourceUrl",
    "downloadUrl", "tags", "featured",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KNOWN_CATEGORIES = {
    "Criação visual",
    "Produtividade",
    "Internet e comunicação",
    "Segurança e privacidade",
    "Utilitários",
    "Infraestrutura e nuvem",
    "Vídeo e áudio",
    "CAD e engenharia",
    "Desenvolvimento",
    "Ciência e dados",
}


def is_https_url(value):
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
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERRO: não foi possível ler o JSON: {exc}")
        return 1
    if not isinstance(items, list):
        print("ERRO: a raiz de data/software.json deve ser uma lista.")
        return 1
    if len(items) < 20:
        errors.append(f"Catálogo muito pequeno: esperados pelo menos 20 registros; encontrados {len(items)}.")

    seen_slugs = set()
    seen_names = set()
    for index, item in enumerate(items):
        prefix = f"Registro #{index + 1}"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: deve ser um objeto JSON.")
            continue
        missing = sorted(REQUIRED - set(item))
        if missing:
            errors.append(f"{prefix}: campos obrigatórios ausentes: {', '.join(missing)}.")
            continue
        slug = item["slug"]
        name = item["name"]
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            errors.append(f"{prefix}: slug inválido: {slug!r}.")
        elif slug in seen_slugs:
            errors.append(f"{prefix}: slug duplicado: {slug}.")
        seen_slugs.add(slug)
        normalized_name = name.strip().casefold() if isinstance(name, str) else ""
        if not normalized_name:
            errors.append(f"{prefix}: nome vazio ou inválido.")
        elif normalized_name in seen_names:
            errors.append(f"{prefix}: nome duplicado: {name}.")
        seen_names.add(normalized_name)
        for field in ("name", "category", "tagline", "description", "license"):
            if not isinstance(item[field], str) or not item[field].strip():
                errors.append(f"{prefix}: {field} deve ser texto não vazio.")
        if item["category"] not in KNOWN_CATEGORIES:
            errors.append(f"{prefix}: categoria desconhecida: {item['category']!r}.")
        if not isinstance(item["platforms"], list) or not item["platforms"]:
            errors.append(f"{prefix}: platforms deve ser uma lista não vazia.")
        elif any(not isinstance(platform, str) or not platform.strip() for platform in item["platforms"]):
            errors.append(f"{prefix}: platforms contém valor inválido.")
        if not isinstance(item["tags"], list) or any(not isinstance(tag, str) for tag in item["tags"]):
            errors.append(f"{prefix}: tags deve ser uma lista de textos.")
        if not isinstance(item["featured"], bool):
            errors.append(f"{prefix}: featured deve ser true ou false.")
        for field in ("licenseUrl", "websiteUrl", "sourceUrl", "downloadUrl"):
            if not is_https_url(item[field]):
                errors.append(f"{prefix}: {field} precisa ser uma URL HTTPS válida.")

    if errors:
        print("Validação do catálogo: FALHOU")
        for error in errors:
            print(" - " + error)
        return 1
    category_count = len({item["category"] for item in items})
    print(f"Validação do catálogo: OK — {len(items)} registros, {category_count} categorias; campos obrigatórios, identificadores e URLs HTTPS passaram.")
    print("Observação: o teste não confirma disponibilidade online, titularidade dos domínios, validade jurídica das licenças ou segurança dos instaladores.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
