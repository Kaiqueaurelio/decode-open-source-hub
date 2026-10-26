#!/usr/bin/env python3
"""Validate the 13 apps in ArtCraft's official Craft App Suite."""
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
EXPECTED_ORDER = ["photocraft","vectorcraft","filmcraft","lightcraft","pdfcraft","effectcraft","designcraft","figcraft","wordcraft","soundcraft","deckcraft","cadcraft","gridcraft"]
EXPECTED = set(EXPECTED_ORDER)
CATEGORIES = {"Imagem e fotografia", "Design e publicação", "Vídeo e motion", "Documentos e produtividade", "Áudio", "CAD e engenharia"}
STAGES = {
    "photocraft": "Alpha inicial",
    "vectorcraft": "Em desenvolvimento",
    "filmcraft": "Em desenvolvimento",
    "lightcraft": "Em desenvolvimento",
    "pdfcraft": "Alpha inicial",
    "effectcraft": "Em desenvolvimento",
    "designcraft": "Em desenvolvimento",
    "figcraft": "Alpha inicial",
    "wordcraft": "Em desenvolvimento",
    "soundcraft": "Em desenvolvimento",
    "deckcraft": "Em desenvolvimento",
    "cadcraft": "Em desenvolvimento",
    "gridcraft": "Em desenvolvimento",
}
PLATFORMS = {
    slug: (["macOS", "Windows", "Linux"] if slug == "filmcraft"
           else ["macOS", "Windows", "Linux", "Web"])
    for slug in EXPECTED_ORDER
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
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERRO: não foi possível ler o JSON: {exc}")
        return 1
    if not isinstance(items, list):
        print("ERRO: a raiz do catálogo deve ser uma lista.")
        return 1
    if len(items) != 13:
        errors.append(f"Esperados exatamente 13 Crafting Apps; encontrados {len(items)}.")

    slugs = []
    names = set()
    for index, item in enumerate(items):
        prefix = f"Registro #{index + 1}"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: deve ser um objeto JSON.")
            continue
        missing = sorted(REQUIRED - set(item))
        if missing:
            errors.append(f"{prefix}: campos ausentes: {', '.join(missing)}.")
            continue

        slug = item["slug"]
        name = item["name"]
        slugs.append(slug)
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            errors.append(f"{prefix}: slug inválido.")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{prefix}: nome vazio.")
        elif name.strip().casefold() in names:
            errors.append(f"{prefix}: nome duplicado {name}.")
        else:
            names.add(name.strip().casefold())

        if item["kind"] != "Crafting App":
            errors.append(f"{prefix}: somente entradas do tipo Crafting App são permitidas.")
        if item["category"] not in CATEGORIES:
            errors.append(f"{prefix}: categoria inesperada {item['category']!r}.")
        if item["license"] != "MIT OR Apache-2.0":
            errors.append(f"{prefix}: rótulo de licença inconsistente.")
        if item["stage"] != STAGES.get(slug):
            errors.append(f"{prefix}: estágio não corresponde à lista oficial para {slug}.")
        if item["platforms"] != PLATFORMS.get(slug):
            errors.append(f"{prefix}: plataformas não correspondem à lista oficial para {slug}.")
        if not isinstance(item["platforms"], list) or not item["platforms"]:
            errors.append(f"{prefix}: platforms deve ser uma lista não vazia.")
        elif len(item["platforms"]) != len(set(item["platforms"])):
            errors.append(f"{prefix}: platforms contém duplicatas.")
        if not isinstance(item["tags"], list) or any(not isinstance(tag, str) or not tag.strip() for tag in item["tags"]):
            errors.append(f"{prefix}: tags inválidas.")
        if not isinstance(item["featured"], bool):
            errors.append(f"{prefix}: featured deve ser booleano.")

        for key in ("licenseUrl", "websiteUrl", "sourceUrl", "downloadUrl"):
            if not is_https(item[key]):
                errors.append(f"{prefix}: {key} precisa ser uma URL HTTPS.")
        if is_https(item["licenseUrl"]):
            parsed = urlparse(item["licenseUrl"])
            if parsed.netloc != "github.com" or not parsed.path.startswith(f"/storytold/{slug}/"):
                errors.append(f"{prefix}: URL de licença fora do repositório oficial deste app.")
            if not parsed.path.endswith("/LICENSE-MIT"):
                errors.append(f"{prefix}: URL de licença deve apontar para LICENSE-MIT.")
        if is_https(item["sourceUrl"]):
            parsed = urlparse(item["sourceUrl"])
            if parsed.netloc != "github.com" or parsed.path != f"/storytold/{slug}":
                errors.append(f"{prefix}: repositório-fonte não corresponde ao app na organização oficial.")
        expected_page = f"https://getartcraft.com/apps/{slug}"
        if item["websiteUrl"] != expected_page or item["downloadUrl"] != expected_page:
            errors.append(f"{prefix}: site e página de download devem ser a página oficial do produto.")

    if slugs != EXPECTED_ORDER:
        errors.append("A lista precisa corresponder, na ordem oficial, aos 13 apps do ArtCraft Launcher.")
    if set(slugs) != EXPECTED:
        errors.append(
            "Escopo inválido. Entradas indevidas: "
            + ", ".join(sorted(set(slugs) - EXPECTED))
            + "; entradas ausentes: "
            + ", ".join(sorted(EXPECTED - set(slugs)))
            + "."
        )

    if errors:
        print("Validação do catálogo ArtCraft: FALHOU")
        for error in errors:
            print(" - " + error)
        return 1

    print("Validação do catálogo ArtCraft: OK — 13 apps oficiais, 6 categorias.")
    print("Escopo, ordem, plataformas, estágios, licenças e estrutura conferidos.")
    print("Observação: os links e os instaladores exigem verificação externa ao validador.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
