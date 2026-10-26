# Decode Launcher & Open Source Hub

[![Decode Launcher CI](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml)
[![Catalog checks](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-stable-orange.svg?logo=rust)](https://www.rust-lang.org/)

**Catálogo web responsivo e código-fonte do Decode Launcher nativo em Rust, reunindo a suíte de aplicativos criativos open source sob a identidade Decode.**

Este repositório reúne o catálogo informativo e o código-fonte do **Decode Launcher**, com identidade própria e paridade funcional com a suíte de referência. Consulte a [matriz de paridade funcional](docs/decode-launcher-parity.md) para detalhes técnicos de cada componente.

## O que você encontra

- **13 apps Decode:** DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD e DecodeGrid. Os nomes originais continuam disponíveis para pesquisa.
- **Decode Launcher (projeto original: ArtCraft Launcher):** utilitário separado, com links para o repositório oficial e suas releases.
- Busca por nome, finalidade, recursos e palavras-chave.
- Filtros por categoria e sistema operacional, ordenação e cartões com links para download, site, código-fonte e licença.
- Interface web responsiva com modos de grade e tabela, busca sincronizada, filtros por estágio, categoria e plataforma, ícones e links oficiais.
- Código-fonte Rust do launcher em `launcher/`, com crates para catálogo/release, backend nativo, UI egui, shell desktop, WebAssembly e scripts de empacotamento.
- Matriz de paridade funcional que documenta os recursos exigidos para o Decode Launcher e seu estado real de implementação.
- Dados separados em JSON, validador, testes automatizados e fluxo de validação no GitHub Actions.

## Fontes oficiais

- [Catálogo oficial de aplicativos ArtCraft](https://getartcraft.com/apps)
- [Repositório do ArtCraft Launcher](https://github.com/storytold/craft-launcher)
- [Releases do ArtCraft Launcher](https://github.com/storytold/craft-launcher/releases/latest)
- [Organização storytold no GitHub](https://github.com/storytold)

Cada registro aponta para páginas do projeto correspondente. Os estágios e requisitos podem mudar: confirme os detalhes nas fontes oficiais antes de utilizar versões alfa em trabalho importante.

## Decode Launcher nativo

O [Decode Launcher (nome original: ArtCraft Launcher)](https://github.com/storytold/craft-launcher) é um projeto nativo em Rust que centraliza a descoberta, instalação, abertura e atualização dos aplicativos da Craft App Suite. O README upstream documenta downloads para Linux (incluindo AppImage, DEB e RPM), Windows, macOS, FreeBSD e WebAssembly, bem como verificação de downloads por SHA-256.

**Status indicado pelo projeto original:** early alpha. A disponibilidade de pacotes varia por versão, sistema e arquitetura. Veja sempre a página de [releases](https://github.com/storytold/craft-launcher/releases/latest) antes de baixar.

O código-fonte completo do launcher está integrado em `launcher/`, com rebranding para o Decode, suíte de testes passando e integração contínua (CI) automatizada via GitHub Actions. A matriz de paridade em [docs/decode-launcher-parity.md](docs/decode-launcher-parity.md) lista as verificações e recursos de cada plataforma.

## Executar localmente

Requer Python 3 apenas para servir os arquivos; não exige Node.js, npm ou compilação.

```bash
git clone https://github.com/Kaiqueaurelio/decode-open-source-hub.git
cd decode-open-source-hub
python3 -m http.server 8080
```

Abra [http://localhost:8080](http://localhost:8080). Use um servidor HTTP porque a interface carrega `data/software.json`; abrir `index.html` diretamente pode ser bloqueado pelo navegador.

## Estrutura do projeto

- `index.html`: página principal e metadados.
- `styles.css`: identidade visual e layout responsivo.
- `app.js`: busca, filtros, ordenação e cartões.
- `data/software.json`: registros do catálogo.
- `data/schema.json`: esquema dos registros.
- `scripts/validate_catalog.py`: validação de escopo e estrutura.
- `tests/test_catalog.py`: testes automatizados.
- `docs/catalog-guidelines.md`: regras de manutenção do catálogo.
- `docs/verification.md`: processo e limites de verificação.
- `docs/decode-launcher-parity.md`: matriz de paridade funcional e checklist de portabilidade do Decode Launcher.
- `launcher/Cargo.toml`: workspace Rust do launcher.
- `launcher/apps/`: shell desktop e aplicação web.
- `launcher/crates/core/`: catálogo, releases e parsing.
- `launcher/crates/native/`: detecção, downloads e instalação nativa.
- `launcher/crates/ui-egui/`: interface compartilhada e traduções.
- `launcher/packaging/`: scripts de empacotamento por plataforma.
- `launcher/LICENSE-MIT`, `launcher/LICENSE-APACHE`, `launcher/NOTICE`, `launcher/ATTRIBUTION.md`: avisos e atribuições upstream.

## Validar e testar

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

Esses testes verificam estrutura e regras codificadas, mas não garantem que cada URL esteja respondendo no momento e não substituem uma revisão manual das fontes.

## Compilar e testar o launcher Rust

Requer Rust estável, Cargo e dependências nativas da plataforma. No Linux, o workflow instala os headers de sistema usados pelo egui/winit.

```bash
cd launcher
cargo fmt --all -- --check
cargo test --workspace --locked
```

Os testes do workspace não substituem validações de instalação e atualização reais em Linux, Windows, macOS, FreeBSD e WebAssembly. Não distribua instaladores Decode antes de validar IDs de pacotes, feeds de atualização, assinatura, instalação, desinstalação e migração por plataforma.

## Licenças e atribuição

- Código do Decode Open Source Hub: MIT, veja [LICENSE](LICENSE).
- Textos e dados editoriais originais: CC BY 4.0, veja [LICENSE-DATA.md](LICENSE-DATA.md).
- Aplicativos upstream: respeite a licença e os avisos em cada repositório; o ArtCraft Launcher indica MIT OR Apache-2.0.
- Marcas, nomes, logotipos e ativos de terceiros mantêm os termos próprios. Este catálogo é independente e não implica endosso.

Para redistribuir código ou ativos de um projeto upstream, consulte a licença desse projeto e preserve os avisos exigidos. Não reutilize marcas ou logotipos ArtCraft como se fossem de propriedade do Decode.

## Atualização do catálogo

Confira periodicamente [getartcraft.com/apps](https://getartcraft.com/apps) e o [catálogo do launcher](https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs). Ao alterar os 13 aplicativos da suíte, mantenha `data/software.json`, `data/schema.json`, o validador e os testes sincronizados. O launcher deve continuar identificado como uma ferramenta separada, não como um 14º Crafting App.

---

**Decode Open Source Hub** — catálogo independente, com fontes rastreáveis e informações claras sobre o ecossistema ArtCraft.
