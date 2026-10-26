#!/usr/bin/env python3
"""
Applies complete Decode Analytics branding, visual identity, logos,
and corporate metadata across all 13 Decode apps in apps/ and the launcher.
Company: Decode Analytics (Presidente Prudente, SP, Brasil)
Social: https://www.instagram.com/decode.analytics/
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"
BRAND_DIR = ROOT / "assets" / "brand"

APPS_METADATA = [
    {
        "dir": "decode-photo",
        "slug": "photocraft",
        "name": "Decode Photo",
        "short_name": "DecodePhoto",
        "tagline": "Editor profissional de imagens, camadas, máscaras e documentos PSD em puro Rust.",
        "description": "O Decode Photo é uma ferramenta avançada de edição de imagens e pintura digital desenvolvida em Rust. Suporta camadas não destrutivas, máscaras, ajustes tonais, tipografia vetorial e leitura nativa de arquivos Photoshop (PSD), combinando performance extrema com arquitetura de código aberto.",
    },
    {
        "dir": "decode-vector",
        "slug": "vectorcraft",
        "name": "Decode Vector",
        "short_name": "DecodeVector",
        "tagline": "Ilustração vetorial precisa, curvas de Bézier e design gráfico em puro Rust.",
        "description": "O Decode Vector é um editor de gráficos vetoriais construído do zero em Rust, focado em ilustrações de alta precisão, tipografia, curvas paramétricas, formas geométricas e exportação em SVG e PDF com renderização acelerada por GPU.",
    },
    {
        "dir": "decode-film",
        "slug": "filmcraft",
        "name": "Decode Film",
        "short_name": "DecodeFilm",
        "tagline": "Editor de vídeo não linear, composição em tempo real e gradação de cor em Rust.",
        "description": "O Decode Film é uma plataforma de edição e montagem de vídeo não linear (NLE) em Rust. Projetado para timeline multicanal, cortes rápidos, pós-produção de áudio e correção de cor com precisão cinematográfica.",
    },
    {
        "dir": "decode-light",
        "slug": "lightcraft",
        "name": "Decode Light",
        "short_name": "DecodeLight",
        "tagline": "Revelação digital de arquivos RAW e catalogação fotográfica não destrutiva.",
        "description": "O Decode Light é um estúdio de revelação digital para fotógrafos. Processa arquivos RAW de múltiplos fabricantes de câmeras, oferecendo curva de tons, redução de ruído, calibração de lentes e catalogação inteligente.",
    },
    {
        "dir": "decode-pdf",
        "slug": "pdfcraft",
        "name": "Decode PDF",
        "short_name": "DecodePdf",
        "tagline": "Leitor, editor, organizador e assinador de documentos PDF com máxima segurança.",
        "description": "O Decode PDF oferece ferramentas completas para manipular documentos PDF em Rust: mesclar e dividir páginas, anotações, preenchimento de formulários, OCR e proteção com criptografia.",
    },
    {
        "dir": "decode-effect",
        "slug": "effectcraft",
        "name": "Decode Effect",
        "short_name": "DecodeEffect",
        "tagline": "Motion graphics, composição de efeitos visuais e animação procedural em Rust.",
        "description": "O Decode Effect é o aplicativo de motion design da suíte Decode. Trabalha com animação baseada em nós, keyframing, partículas, simulações procedurais e composição visual para cinema e transmissões.",
    },
    {
        "dir": "decode-design",
        "slug": "designcraft",
        "name": "Decode Design",
        "short_name": "DecodeDesign",
        "tagline": "Diagramação editorial, paginação de livros, revistas e impressos com tipografia avançada.",
        "description": "O Decode Design é um software de editoração eletrônica (DTP) para criação de layouts de páginas, livros, catálogos e folhetos, com suporte completo a grids modulares, estilos de parágrafo e fechamento de arquivos pré-impressão.",
    },
    {
        "dir": "decode-fig",
        "slug": "figcraft",
        "name": "Decode Fig",
        "short_name": "DecodeFig",
        "tagline": "Design de interfaces de usuário (UI/UX), design systems e prototipagem interativa.",
        "description": "O Decode Fig é a ferramenta da suíte Decode para designers de produto e interfaces. Permite prototipagem de telas, componentes reutilizáveis, layouts flexíveis e design responsivo.",
    },
    {
        "dir": "decode-word",
        "slug": "wordcraft",
        "name": "Decode Word",
        "short_name": "DecodeWord",
        "tagline": "Processador de texto com formatação rica, citações acadêmicas e tipografia limpa.",
        "description": "O Decode Word é um editor de texto moderno e rápido, criado em Rust para escrita focada, relatórios corporativos, artigos científicos e formatação padronizada de documentos com integração Zotero.",
    },
    {
        "dir": "decode-sound",
        "slug": "soundcraft",
        "name": "Decode Sound",
        "short_name": "DecodeSound",
        "tagline": "Estação de áudio digital (DAW), gravação multipista e mixagem de alta fidelidade.",
        "description": "O Decode Sound é a estação de trabalho de áudio digital da Decode. Projetada para gravação de podcasts, mixagem musical, edição de trilhas sonoras e processamento de efeitos com latência ultrabaixa.",
    },
    {
        "dir": "decode-deck",
        "slug": "deckcraft",
        "name": "Decode Deck",
        "short_name": "DecodeDeck",
        "tagline": "Criação de apresentações visuais elegantes, slides dinâmicos e pitch decks.",
        "description": "O Decode Deck transforma ideias em apresentações impactantes. Possui templates estruturados, transições suaves, gráficos incorporados e modo apresentador para reuniões e palestras.",
    },
    {
        "dir": "decode-cad",
        "slug": "cadcraft",
        "name": "Decode CAD",
        "short_name": "DecodeCAD",
        "tagline": "CAD 2D e 3D de código aberto para desenho técnico, documentação e projetos em Rust.",
        "description": "O Decode CAD é um software completo de CAD desenvolvido em Rust pela Decode Analytics. Oferece leitura e gravação nativa de DXF/DWG, hachuras, cotas arquitetônicas, comandos via CLI e automação por agentes MCP.",
    },
    {
        "dir": "decode-grid",
        "slug": "gridcraft",
        "name": "Decode Grid",
        "short_name": "DecodeGrid",
        "tagline": "Planilhas eletrônicas de alta performance, fórmulas analíticas e visualização de dados.",
        "description": "O Decode Grid é uma planilha de cálculo clean-room desenvolvida em Rust. Suporta milhares de linhas sem travamentos, cálculo matricial, gráficos interativos e compatibilidade com formatos de dados abertos.",
    },
]


def copy_brand_assets_to_app(app_dir: Path):
    target_brand = app_dir / "docs" / "brand"
    target_brand.mkdir(parents=True, exist_ok=True)

    # Copy official Decode brand assets
    for asset in BRAND_DIR.glob("*"):
        if asset.is_file():
            shutil.copy2(asset, target_brand / asset.name)

    # Overwrite legacy artcraft asset names with Decode assets so any remaining code/docs reference renders Decode
    legacy_mappings = [
        ("artcraft-logo.png", "decode-logo.png"),
        ("artcraft-logo.svg", "decode-logo.svg"),
        ("artcraft-logo-white.png", "decode-logo-white.png"),
        ("artcraft-logo-white.svg", "decode-logo-white.svg"),
        ("artcraft-mark.png", "decode-mark.png"),
        ("artcraft-mark.svg", "decode-mark.svg"),
        ("artcraft-mark-black.png", "decode-mark-black.png"),
        ("artcraft-mark-black.svg", "decode-mark-black.svg"),
    ]
    for legacy_name, decode_src in legacy_mappings:
        src_file = BRAND_DIR / decode_src
        if src_file.exists():
            shutil.copy2(src_file, target_brand / legacy_name)

    # Also place brand assets in assets/brand if directory exists
    assets_brand = app_dir / "assets" / "brand"
    assets_brand.mkdir(parents=True, exist_ok=True)
    for asset in BRAND_DIR.glob("*"):
        if asset.is_file():
            shutil.copy2(asset, assets_brand / asset.name)


def create_app_readme(app_dir: Path, meta: dict):
    readme_path = app_dir / "README.md"
    name = meta["name"]
    short_name = meta["short_name"]
    slug = meta["slug"]
    tagline = meta["tagline"]
    description = meta["description"]

    content = f"""> **{name} — desenvolvido e mantido pela [Decode Analytics](https://www.instagram.com/decode.analytics/).**
> Sede: Presidente Prudente - SP, Brasil | [Hub Oficial](https://kaiqueaurelio.github.io/decode-open-source-hub/)
> Esta edição faz parte da suíte Decode, construída em puro Rust a partir de código aberto.
> Avisos e licenças preservados em [LICENSE-MIT](LICENSE-MIT), [LICENSE-APACHE](LICENSE-APACHE), [NOTICE](NOTICE) e [ATTRIBUTION.md](ATTRIBUTION.md).

<p align="center">
  <a href="https://kaiqueaurelio.github.io/decode-open-source-hub/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/decode-logo-white.svg">
      <img alt="Decode Analytics" src="docs/brand/decode-logo.svg" width="240">
    </picture>
  </a>
</p>

<h1 align="center">{name}</h1>

<p align="center">
  <b>{tagline}</b>
</p>

<p align="center">
  <img alt="Linguagem: 100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="Licença: MIT OR Apache-2.0" src="https://img.shields.io/badge/licença-MIT%20%2F%20Apache--2.0-blue?style=flat-square">
  <a href="https://www.instagram.com/decode.analytics/"><img alt="Instagram: @decode.analytics" src="https://img.shields.io/badge/Instagram-@decode.analytics-E4405F?style=flat-square&logo=instagram&logoColor=white"></a>
  <a href="https://kaiqueaurelio.github.io/decode-open-source-hub/"><img alt="Decode Hub" src="https://img.shields.io/badge/Decode%20Hub-Presidente%20Prudente-0891b2?style=flat-square"></a>
</p>

---

## Sobre o Aplicativo

{description}

O **{short_name}** foi desenvolvido com foco em desempenho nativo, arquitetura limpa em Rust e segurança de memória. Integrado ao ecossistema [Decode Open Source Hub](https://github.com/Kaiqueaurelio/decode-open-source-hub), o programa pode ser instalado e atualizado de forma centralizada pelo [Decode Launcher](../../launcher/).

## Identidade Visual e Empresa

* **Empresa Mantenedora:** Decode Analytics
* **Localização / Sede:** Presidente Prudente — São Paulo, Brasil
* **Rede Social Oficial:** Instagram [@decode.analytics](https://www.instagram.com/decode.analytics/)
* **E-mail de Contato:** decoanalytics@outlook.com.br
* **Repositório Central:** [Kaiqueaurelio/decode-open-source-hub](https://github.com/Kaiqueaurelio/decode-open-source-hub)

---

## Compilação e Execução Local

Requer o compilador Rust estável instalado (`rustup`):

```bash
# Compilar e executar a aplicação em modo release
cargo run --release -p {slug}

# Executar a suíte de testes
cargo test --workspace
```

## Instalação pelo Decode Launcher

Para instalar o **{name}** e todos os aplicativos da suíte Decode com instalador gráfico e atualizações automáticas:
1. Abra o [Decode Launcher](../../launcher/).
2. Localize o **{short_name}** na grade de aplicativos.
3. Clique em **Instalar** para configurar o binário no seu sistema operacional (Linux, Windows ou macOS).

---

## Licença e Atribuição de Código Aberto

Este software é código aberto licenciado sob **MIT OR Apache-2.0**.
Os avisos legais, direitos autorais dos colaboradores e termos completos das licenças estão documentados em:
* [`LICENSE-MIT`](LICENSE-MIT)
* [`LICENSE-APACHE`](LICENSE-APACHE)
* [`NOTICE`](NOTICE)
* [`ATTRIBUTION.md`](ATTRIBUTION.md)

Marcas e logotipos **Decode** e **Decode Analytics** são propriedade da Decode Analytics.
"""
    readme_path.write_text(content, encoding="utf-8")


def rebrand_packaging_files(app_dir: Path, meta: dict):
    name = meta["name"]
    short_name = meta["short_name"]
    slug = meta["slug"]

    # Linux .desktop files
    packaging_linux = app_dir / "packaging" / "linux"
    if packaging_linux.exists():
        for desktop_file in packaging_linux.glob("*.desktop"):
            try:
                txt = desktop_file.read_text(encoding="utf-8", errors="replace")
                lines = []
                for line in txt.splitlines():
                    if line.startswith("Name="):
                        lines.append(f"Name={short_name}")
                    elif line.startswith("GenericName="):
                        lines.append(f"GenericName={name}")
                    elif line.startswith("Icon="):
                        lines.append(f"Icon=com.decode.{slug}")
                    elif line.startswith("StartupWMClass="):
                        lines.append(f"StartupWMClass={slug}")
                    else:
                        lines.append(line)
                desktop_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
            except Exception as e:
                print(f"Warn updating {desktop_file}: {e}")

        # Linux AppStream metadata
        for xml_file in packaging_linux.glob("*.metainfo.xml.in"):
            try:
                txt = xml_file.read_text(encoding="utf-8", errors="replace")
                txt = txt.replace("<developer id=\"ai.storyteller\">", "<developer id=\"com.decode\">")
                txt = txt.replace("<name>Learning Machines LLC</name>", "<name>Decode Analytics</name>")
                txt = txt.replace("<name>ArtCraft</name>", f"<name>{short_name}</name>")
                txt = txt.replace("https://getartcraft.com/apps", "https://kaiqueaurelio.github.io/decode-open-source-hub/")
                xml_file.write_text(txt, encoding="utf-8")
            except Exception as e:
                print(f"Warn updating {xml_file}: {e}")

    # macOS Info.plist.in
    macos_plist = app_dir / "packaging" / "macos" / "Info.plist.in"
    if macos_plist.exists():
        try:
            txt = macos_plist.read_text(encoding="utf-8", errors="replace")
            txt = txt.replace("<string>ArtCraft", f"<string>{short_name}")
            txt = txt.replace("ai.storyteller.", "com.decode.")
            txt = txt.replace("Learning Machines LLC", "Decode Analytics (Presidente Prudente, SP)")
            macos_plist.write_text(txt, encoding="utf-8")
        except Exception as e:
            print(f"Warn updating {macos_plist}: {e}")


def main():
    print("Iniciando rebranding completo dos 13 aplicativos da Decode App Suite...")
    for meta in APPS_METADATA:
        app_dir = APPS_DIR / meta["dir"]
        if not app_dir.exists():
            print(f"Diretório {app_dir} não encontrado, pulando...")
            continue

        print(f"==> Rebranding {meta['name']} em {app_dir.name}...")
        copy_brand_assets_to_app(app_dir)
        create_app_readme(app_dir, meta)
        rebrand_packaging_files(app_dir, meta)

    print("\nRebranding concluído com sucesso em todos os aplicativos!")


if __name__ == "__main__":
    main()
