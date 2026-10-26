#!/usr/bin/env python3
"""Validate the 13 official Craft apps plus the separate launcher utility in Decode Monorepo."""
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
EXPECTED_ORDER = [
    "photocraft", "vectorcraft", "filmcraft", "lightcraft", "pdfcraft",
    "effectcraft", "designcraft", "figcraft", "wordcraft", "soundcraft",
    "deckcraft", "cadcraft", "gridcraft",
]
EXPECTED_NAMES = {
    "photocraft":"DecodePhoto", "vectorcraft":"DecodeVector", "filmcraft":"DecodeFilm",
    "lightcraft":"DecodeLight", "pdfcraft":"DecodePdf", "effectcraft":"DecodeEffect",
    "designcraft":"DecodeDesign", "figcraft":"DecodeFig", "wordcraft":"DecodeWord",
    "soundcraft":"DecodeSound", "deckcraft":"DecodeDeck", "cadcraft":"DecodeCAD",
    "gridcraft":"DecodeGrid",
}
SLUG_TO_APP_DIR = {
    "photocraft": "decode-photo",
    "vectorcraft": "decode-vector",
    "filmcraft": "decode-film",
    "lightcraft": "decode-light",
    "pdfcraft": "decode-pdf",
    "effectcraft": "decode-effect",
    "designcraft": "decode-design",
    "figcraft": "decode-fig",
    "wordcraft": "decode-word",
    "soundcraft": "decode-sound",
    "deckcraft": "decode-deck",
    "cadcraft": "decode-cad",
    "gridcraft": "decode-grid",
}
CATEGORIES = {
    "Imagem e fotografia", "Design e publicação", "Vídeo e motion",
    "Documentos e produtividade", "Áudio", "CAD e engenharia",
}
STAGES = {
    "photocraft":"Alpha inicial", "vectorcraft":"Em desenvolvimento",
    "filmcraft":"Em desenvolvimento", "lightcraft":"Em desenvolvimento",
    "pdfcraft":"Alpha inicial", "effectcraft":"Em desenvolvimento",
    "designcraft":"Em desenvolvimento", "figcraft":"Alpha inicial",
    "wordcraft":"Em desenvolvimento", "soundcraft":"Em desenvolvimento",
    "deckcraft":"Em desenvolvimento", "cadcraft":"Em desenvolvimento",
    "gridcraft":"Em desenvolvimento",
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
    if len(items) != 14:
        errors.append(f"Esperados 13 Crafting Apps e 1 launcher; encontrados {len(items)} registros.")

    slugs = []
    names = set()
    for index, item in enumerate(items):
        prefix = f"Registro #{index + 1}"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: deve ser um objeto JSON.")
            continue
        missing = sorted(REQUIRED - set(item))
        extra = sorted(set(item) - REQUIRED)
        if missing:
            errors.append(f"{prefix}: campos ausentes: {', '.join(missing)}.")
            continue
        if extra:
            errors.append(f"{prefix}: campos inesperados: {', '.join(extra)}.")
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

        if slug == "artcraft-launcher":
            if name != "Decode Launcher" or item["kind"] != "Launcher":
                errors.append(f"{prefix}: launcher deve ser identificado separadamente.")
            if item["category"] != "Launchers e utilitários":
                errors.append(f"{prefix}: categoria incorreta do launcher.")
            if "ArtCraft Launcher" not in item["tags"]:
                errors.append(f"{prefix}: nome upstream do launcher deve permanecer como termo de busca.")
            if item["sourceUrl"] != "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher":
                errors.append(f"{prefix}: repositório do launcher incorreto.")
            if item["downloadUrl"] != "https://github.com/Kaiqueaurelio/decode-open-source-hub/releases":
                errors.append(f"{prefix}: download deve apontar para releases do repositório.")
            if item["license"] != "MIT OR Apache-2.0":
                errors.append(f"{prefix}: rótulo de licença inconsistente no launcher.")
            if not isinstance(item["platforms"], list) or not item["platforms"]:
                errors.append(f"{prefix}: platforms deve ser uma lista não vazia.")
        else:
            if slug not in EXPECTED_NAMES:
                errors.append(f"{prefix}: slug fora do escopo permitido: {slug!r}.")
                continue
            if name != EXPECTED_NAMES.get(slug):
                errors.append(f"{prefix}: nome de apresentação Decode incorreto para {slug}.")
            if item["kind"] != "Crafting App":
                errors.append(f"{prefix}: tipo deve ser Crafting App.")
            if item["category"] not in CATEGORIES:
                errors.append(f"{prefix}: categoria inesperada {item['category']!r}.")
            if item["license"] != "MIT OR Apache-2.0":
                errors.append(f"{prefix}: rótulo de licença inconsistente.")
            if item["stage"] != STAGES.get(slug):
                errors.append(f"{prefix}: estágio não corresponde à lista oficial para {slug}.")
            if item["platforms"] != PLATFORMS.get(slug):
                errors.append(f"{prefix}: plataformas não correspondem à lista oficial para {slug}.")
            
            app_dir = SLUG_TO_APP_DIR.get(slug)
            expected_license = f"https://github.com/Kaiqueaurelio/decode-open-source-hub/blob/main/apps/{app_dir}/LICENSE-MIT"
            if item["licenseUrl"] != expected_license:
                errors.append(f"{prefix}: URL de licença deve apontar para {expected_license}.")
            
            expected_source = f"https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps/{app_dir}"
            if item["sourceUrl"] != expected_source:
                errors.append(f"{prefix}: repositório-fonte não corresponde ao app no monorepo Decode.")
            
            expected_page = "https://decode-open-source-hub-catalog.vercel.app"
            if item["websiteUrl"] != expected_page:
                errors.append(f"{prefix}: site deve apontar para o catálogo Decode.")
            if item["downloadUrl"] != "https://github.com/Kaiqueaurelio/decode-open-source-hub/releases":
                errors.append(f"{prefix}: página de download deve apontar para releases do repositório Decode.")

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

    expected_all = EXPECTED_ORDER + ["artcraft-launcher"]
    if slugs != expected_all:
        errors.append("A lista deve conter, em ordem, os 13 apps oficiais seguidos do launcher separado.")
    if len(set(slugs)) != len(slugs):
        errors.append("Há slugs duplicados no catálogo.")

    if errors:
        print("Validação do catálogo Decode: FALHOU")
        for error in errors:
            print(" - " + error)
        return 1

    print("Validação do catálogo Decode: OK — 13 Apps Decode e 1 launcher no repositório.")
    print("Estrutura, escopo, links HTTPS Decode e campos de catálogo conferidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
