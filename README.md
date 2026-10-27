# Decode Launcher & Open Source Hub

[![Decode Launcher CI](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml)
[![Catalog checks](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-stable-orange.svg?logo=rust)](https://www.rust-lang.org/)

**Catálogo web responsivo e código-fonte do Decode Launcher nativo em Rust, reunindo a suíte de aplicativos criativos open source sob a identidade Decode.**

Este repositório reúne o catálogo informativo e o código-fonte do **Decode Launcher**, com identidade própria e paridade funcional com a suíte de aplicativos. Consulte a [matriz de paridade funcional](docs/decode-launcher-parity.md) para detalhes técnicos de cada componente.

## O que você encontra

- **13 apps Decode:** DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD e DecodeGrid. Os nomes de referência continuam disponíveis para pesquisa.
- **Decode Launcher:** utilitário nativo em Rust, com links para o código-fonte e suas releases.
- Busca por nome, finalidade, recursos e palavras-chave.
- Filtros por categoria e sistema operacional, ordenação e cartões com links para download, site, código-fonte e licença.
- Interface web responsiva com modos de grade e tabela, busca sincronizada, filtros por estágio, categoria e plataforma, ícones e links oficiais.
- Código-fonte Rust do launcher em `launcher/`, com crates para catálogo/release, backend nativo, UI egui, shell desktop, WebAssembly e scripts de empacotamento.
- Matriz de paridade funcional que documenta os recursos do Decode Launcher e seu estado de implementação.
- **Integração upstream documentada:** [mapa de funcionalidades e plano de portabilidade](launcher-upstream/UPSTREAM-REFERENCE.md), com limites de marca/licença e pontos a validar.
- Dados estruturados em JSON, validador, testes automatizados e fluxo de validação no GitHub Actions.

## 📥 Downloads e Acesso aos Aplicativos da Suíte

Todos os 13 aplicativos da suíte Decode e o Decode Launcher estão integrados diretamente neste repositório.

### Links Diretos de Download:
- 🚀 **[Releases e Binários Compilados (GitHub Releases)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)**
- 📦 **[Baixar Código-Fonte Completo de Todos os Apps (.ZIP)](https://github.com/Kaiqueaurelio/decode-open-source-hub/archive/refs/heads/main.zip)**
- 🌐 **[Catálogo Web Interativo (Vercel)](https://decode-open-source-hub-catalog.vercel.app)**

### Aplicativos Disponíveis no Repositório:

| Aplicativo | Pasta no Repositório | Categoria | Pacote Release (v0.8.2) | Checksum | Como Compilar e Rodar (Rust) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Decode Launcher** | [`launcher/`](launcher/) | Gerenciador & Atualizador Desktop | [decode-launcher-linux-x86_64.tar.gz (16.6 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-launcher-linux-x86_64.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-launcher-linux-x86_64.tar.gz.sha256) | `cd launcher && cargo run --release -p decode-launcher` |
| **Decode Photo** | [`apps/decode-photo/`](apps/decode-photo/) | Edição e Retoque de Imagens | [decode-photo-release-package.tar.gz (22.7 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-photo-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-photo-release-package.tar.gz.sha256) | `cd apps/decode-photo && cargo run --release` |
| **Decode Vector** | [`apps/decode-vector/`](apps/decode-vector/) | Ilustração e Desenho Vetorial | [decode-vector-release-package.tar.gz (23.9 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-vector-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-vector-release-package.tar.gz.sha256) | `cd apps/decode-vector && cargo run --release` |
| **Decode Film** | [`apps/decode-film/`](apps/decode-film/) | Edição de Vídeo e Linha do Tempo | [decode-film-release-package.tar.gz (21.5 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-film-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-film-release-package.tar.gz.sha256) | `cd apps/decode-film && cargo run --release` |
| **Decode Light** | [`apps/decode-light/`](apps/decode-light/) | Catálogo Fotográfico e RAW | [decode-light-release-package.tar.gz (19.5 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-light-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-light-release-package.tar.gz.sha256) | `cd apps/decode-light && cargo run --release` |
| **Decode PDF** | [`apps/decode-pdf/`](apps/decode-pdf/) | Leitura, Proteção e Edição PDF | [decode-pdf-release-package.tar.gz (18.7 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-pdf-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-pdf-release-package.tar.gz.sha256) | `cd apps/decode-pdf && cargo run --release` |
| **Decode Effect** | [`apps/decode-effect/`](apps/decode-effect/) | Efeitos Visuais VFX e Motion | [decode-effect-release-package.tar.gz (13.7 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-effect-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-effect-release-package.tar.gz.sha256) | `cd apps/decode-effect && cargo run --release` |
| **Decode Design** | [`apps/decode-design/`](apps/decode-design/) | Diagramação e Publicação Editorial | [decode-design-release-package.tar.gz (10.6 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-design-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-design-release-package.tar.gz.sha256) | `cd apps/decode-design && cargo run --release` |
| **Decode Fig** | [`apps/decode-fig/`](apps/decode-fig/) | Design de Interfaces UI/UX | [decode-fig-release-package.tar.gz (11.2 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-fig-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-fig-release-package.tar.gz.sha256) | `cd apps/decode-fig && cargo run --release` |
| **Decode Word** | [`apps/decode-word/`](apps/decode-word/) | Processador de Textos e Documentos | [decode-word-release-package.tar.gz (12.3 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-word-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-word-release-package.tar.gz.sha256) | `cd apps/decode-word && cargo run --release` |
| **Decode Sound** | [`apps/decode-sound/`](apps/decode-sound/) | Estação de Áudio Digital (DAW) | [decode-sound-release-package.tar.gz (6.9 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-sound-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-sound-release-package.tar.gz.sha256) | `cd apps/decode-sound && cargo run --release` |
| **Decode Deck** | [`apps/decode-deck/`](apps/decode-deck/) | Apresentações e Slides | [decode-deck-release-package.tar.gz (5.8 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-deck-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-deck-release-package.tar.gz.sha256) | `cd apps/decode-deck && cargo run --release` |
| **Decode CAD** | [`apps/decode-cad/`](apps/decode-cad/) | Desenho Técnico 2D/3D (CAD) | [decode-cad-release-package.tar.gz (5.8 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-cad-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-cad-release-package.tar.gz.sha256) | `cd apps/decode-cad && cargo run --release` |
| **Decode Grid** | [`apps/decode-grid/`](apps/decode-grid/) | Planilhas e Modelagem de Dados | [decode-grid-release-package.tar.gz (6.4 MB)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-grid-release-package.tar.gz) | [SHA-256](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/download/v0.8.2/decode-grid-release-package.tar.gz.sha256) | `cd apps/decode-grid && cargo run --release` |

## Fontes e referências

- [Catálogo oficial Decode Open Source Hub](https://decode-open-source-hub-catalog.vercel.app/)
- [Suíte de Aplicativos (Monorepo)](https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps)
- [Código-fonte do Decode Launcher](https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher)
- [Releases e Downloads do Decode Launcher](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)
- [Upstream Storytold (ArtCraft Creative Suite)](https://github.com/storytold)
- [Design Reference (GetArtCraft Apps)](https://getartcraft.com/apps)

Cada registro aponta para páginas do projeto correspondente. Os softwares utilizam a arquitetura modular da suíte Craft da Storytold, mantidos e customizados sob a identidade visual Decode Analytics.

## Princípios de Engenharia da Suíte Decode

Inspirado na arquitetura e design system de excelência do [ArtCraft](https://getartcraft.com/apps) da [Storytold](https://github.com/storytold), a suíte segue 6 princípios fundamentais:

1. **Código Aberto:** Licenças permissivas (MIT ou Apache-2.0) com repositório transparente e monorepo auditável.
2. **Nativo em Rust, Sem Electron:** Compilação direta para código de máquina em macOS, Windows e Linux com aceleração por GPU via WGPU. Sem Chromium e sem WebViews pesadas.
3. **Familiar desde o 1º Dia:** Workflows, atalhos de teclado e painéis alinhados às ferramentas líderes de mercado.
4. **Seus Arquivos, Sua Máquina:** Arquitetura local-first, formatos padronizados, sem cloud compulsória e sem telemetria invasiva.
5. **Pronto para Agentes & IA:** Automação e controle via CLI, canal de eventos JSON e integração com servidores MCP (Model Context Protocol).
6. **Também no Navegador:** Compilação cruzada para WebAssembly (WASM), permitindo execução instantânea na web sem instalação.

## Decode Launcher nativo

O **Decode Launcher** é um projeto nativo em Rust que centraliza a descoberta, instalação, abertura e atualização dos aplicativos da Decode App Suite. O projeto oferece suporte para Linux (incluindo AppImage, DEB, RPM e Flatpak), Windows, macOS, FreeBSD e WebAssembly, além de verificação de downloads por SHA-256.

**Status do projeto:** early alpha. A disponibilidade de pacotes varia por versão, sistema e arquitetura. Veja sempre a página de [releases](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/latest) antes de baixar.

O código-fonte completo do launcher está integrado em `launcher/`, com identidade visual Decode, suíte de testes passando e integração contínua (CI) automatizada via GitHub Actions. A matriz de paridade em [docs/decode-launcher-parity.md](docs/decode-launcher-parity.md) lista as verificações e recursos de cada plataforma.

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
- `launcher/LICENSE-MIT`, `launcher/LICENSE-APACHE`, `launcher/NOTICE`, `launcher/ATTRIBUTION.md`: licenças e atribuições de dependências.

## Validar e testar

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

Esses testes verificam estrutura e regras codificadas, garantindo consistência e integridade das informações.

## Compilar e testar o launcher Rust

Requer Rust estável, Cargo e dependências nativas da plataforma. No Linux, instale os pacotes de cabeçalho do sistema gráfico antes de compilar.

```bash
cd launcher
cargo fmt --all -- --check
cargo test --workspace --locked
```

Os testes do workspace validam os componentes do launcher em Linux, Windows, macOS, FreeBSD e WebAssembly.

## Licenças e atribuição

- Código do Decode Open Source Hub: MIT, veja [LICENSE](LICENSE).
- Textos e dados editoriais originais: CC BY 4.0, veja [LICENSE-DATA.md](LICENSE-DATA.md).
- Código do Decode Launcher: MIT OR Apache-2.0, veja `launcher/LICENSE-MIT` e `launcher/LICENSE-APACHE`.
- Aplicativos catalogados: respeite a licença e os avisos em cada repositório correspondente.
- Marcas, nomes e ativos de terceiros mantêm seus termos próprios.

## Atualização do catálogo

Ao atualizar os aplicativos da suíte Decode, mantenha `data/software.json`, `data/schema.json`, o validador e os testes sincronizados. O launcher é mantido como utilitário integrado de gerenciamento.

---

**Decode Open Source Hub** — catálogo oficial de código aberto e Decode Launcher da comunidade Decode.
