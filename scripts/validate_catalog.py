#!/usr/bin/env python3
"""Validate the ArtCraft-specific catalog using only the Python standard library."""
import json, re, sys
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"data"/"software.json"
REQUIRED={"slug","name","icon","category","kind","tagline","description","platforms","license","licenseUrl","websiteUrl","sourceUrl","downloadUrl","tags","stage","featured"}
EXPECTED={"artcraft-studio","craft-launcher","photocraft","vectorcraft","filmcraft","lightcraft","pdfcraft","effectcraft","designcraft","figcraft","wordcraft","soundcraft","deckcraft","cadcraft","gridcraft"}
CATEGORIES={"IA e criação","Instalação e atualização","Imagem e fotografia","Design e publicação","Vídeo e motion","Documentos e produtividade","Áudio","CAD e engenharia"}
SLUG_RE=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def https(value):
    if not isinstance(value,str) or not value.strip(): return False
    p=urlparse(value.strip())
    return p.scheme=="https" and bool(p.netloc)

def main():
    errors=[]
    if not CATALOG.exists():
        print("ERRO: data/software.json não foi encontrado."); return 1
    try: items=json.loads(CATALOG.read_text(encoding="utf-8"))
    except (json.JSONDecodeError,OSError) as exc:
        print(f"ERRO: não foi possível ler o JSON: {exc}"); return 1
    if not isinstance(items,list):
        print("ERRO: raiz do catálogo deve ser uma lista."); return 1
    if len(items)!=15: errors.append(f"Esperadas 15 entradas oficiais do ecossistema ArtCraft; encontradas {len(items)}.")
    slugs=set(); names=set()
    for i,item in enumerate(items):
        pre=f"Registro #{i+1}"
        if not isinstance(item,dict): errors.append(f"{pre}: deve ser objeto JSON."); continue
        missing=sorted(REQUIRED-set(item))
        if missing: errors.append(f"{pre}: campos ausentes: {', '.join(missing)}."); continue
        slug=item["slug"]; name=item["name"]
        if not isinstance(slug,str) or not SLUG_RE.fullmatch(slug): errors.append(f"{pre}: slug inválido.")
        if slug in slugs: errors.append(f"{pre}: slug duplicado {slug}.")
        slugs.add(slug)
        norm=name.strip().casefold() if isinstance(name,str) else ""
        if not norm: errors.append(f"{pre}: nome vazio.")
        if norm in names: errors.append(f"{pre}: nome duplicado {name}.")
        names.add(norm)
        for key in ("name","category","kind","tagline","description","license","stage"):
            if not isinstance(item[key],str) or not item[key].strip(): errors.append(f"{pre}: {key} deve ser texto não vazio.")
        if item["category"] not in CATEGORIES: errors.append(f"{pre}: categoria inesperada {item['category']!r}.")
        if item["kind"] not in {"Crafting App","Estúdio de IA","Launcher"}: errors.append(f"{pre}: tipo inválido.")
        if item["license"]!="MIT OR Apache-2.0": errors.append(f"{pre}: licença declarada inconsistente.")
        if not isinstance(item["platforms"],list) or not item["platforms"] or any(not isinstance(v,str) or not v.strip() for v in item["platforms"]):
            errors.append(f"{pre}: platforms deve conter nomes válidos.")
        if not isinstance(item["tags"],list) or any(not isinstance(v,str) or not v.strip() for v in item["tags"]): errors.append(f"{pre}: tags inválidas.")
        if not isinstance(item["featured"],bool): errors.append(f"{pre}: featured deve ser booleano.")
        for key in ("licenseUrl","websiteUrl","sourceUrl","downloadUrl"):
            if not https(item[key]): errors.append(f"{pre}: {key} precisa ser URL HTTPS.")
        if https(item["licenseUrl"]) and urlparse(item["licenseUrl"]).netloc!="github.com": errors.append(f"{pre}: licença fora do GitHub.")
        if https(item["sourceUrl"]):
            parsed=urlparse(item["sourceUrl"])
            if parsed.netloc!="github.com" or not parsed.path.startswith("/storytold/"): errors.append(f"{pre}: repositório não é da organização oficial storytold.")
        if https(item["websiteUrl"]) and urlparse(item["websiteUrl"]).netloc!="getartcraft.com": errors.append(f"{pre}: site não é do domínio oficial getartcraft.com.")
    if slugs-EXPECTED: errors.append("Entradas fora do escopo ArtCraft: "+", ".join(sorted(slugs-EXPECTED))+".")
    if EXPECTED-slugs: errors.append("Entradas oficiais ausentes: "+", ".join(sorted(EXPECTED-slugs))+".")
    if errors:
        print("Validação do catálogo ArtCraft: FALHOU")
        for e in errors: print(" - "+e)
        return 1
    cats=len({x["category"] for x in items})
    apps=sum(x["kind"]=="Crafting App" for x in items)
    print(f"Validação do catálogo ArtCraft: OK — {len(items)} projetos ({apps} Crafting Apps), {cats} categorias.")
    print("Observação: estrutura e escopo passaram; os links não foram consultados ao vivo e os binários não foram auditados.")
    return 0
if __name__=="__main__": sys.exit(main())
