# Decode Launcher & Open Source Hub

[![Decode Launcher CI](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/launcher-ci.yml)
[![Catalog checks](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/Kaiqueaurelio/decode-open-source-hub/actions/workflows/catalog-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-stable-orange.svg?logo=rust)](https://www.rust-lang.org/)

**Catálogo web responsivo e código-fonte do Decode Launcher nativo em Rust, reunindo a suíte de aplicativos criativos open source sob a identidade Decode.**

Este repositório reúne o catálogo informativo e o código-fonte do **Decode Launcher**, com identidade própria e paridade funcional com a suíte de aplicativos. Consulte a [matriz de paridade funcional](docs/decode-launcher-parity.md) para detalhes técnicos de cada componente.

## O que você encontra

- **Aplicativos próprios listados:** DecodeCraft, DecodeCraftX e DecodeClip. O Decode Launcher é listado separadamente como utilitário. O catálogo não inclui aplicativos upstream ou de terceiros.
- **Decode Launcher:** utilitário nativo em Rust, com links para o código-fonte e suas releases.
- Busca por nome, finalidade, recursos e palavras-chave.
- Filtros por categoria e sistema operacional, ordenação e cartões com links para download, site, código-fonte e licença.
- Interface web responsiva com modos de grade e tabela, busca sincronizada, filtros por estágio, categoria e plataforma, ícones e links oficiais.
- Código-fonte Rust do launcher em `launcher/`, com crates para catálogo/release, backend nativo, UI egui, shell desktop, WebAssembly e scripts de empacotamento.
- Matriz de paridade funcional que documenta os recursos do Decode Launcher e seu estado de implementação.
- **Integração upstream documentada:** [mapa de funcionalidades e plano de portabilidade](launcher-upstream/UPSTREAM-REFERENCE.md), com limites de marca/licença e pontos a validar.
- Dados estruturados em JSON, validador, testes automatizados e fluxo de validação no GitHub Actions.

## 📥 Downloads e Acesso aos Aplicativos da Suíte

O catálogo lista apenas os aplicativos próprios mantidos neste repositório (DecodeCraft, DecodeCraftX e DecodeClip) e o Decode Launcher. Projetos de terceiros ou upstream não devem aparecer como aplicativos próprios.

### Links Diretos de Download:
- 🚀 **[Releases e Binários Compilados (GitHub Releases)](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)**
- 📦 **[Baixar Código-Fonte Completo de Todos os Apps (.ZIP)](https://github.com/Kaiqueaurelio/decode-open-source-hub/archive/refs/heads/main.zip)**
- 🌐 **[Catálogo Web Interativo (Vercel)](https://decode-open-source-hub-catalog.vercel.app)**

### Aplicativos próprios listados

| Aplicativo | Código-fonte |
| :--- | :--- |
| **DecodeCraft** | [apps/decode-craft](apps/decode-craft/) |
| **DecodeCraftX** | [apps/decode-craftx](apps/decode-craftx/) |
| **DecodeClip** | [apps/decode-clip](apps/decode-clip/) |
| **Decode Launcher** | [launcher](launcher/) |

O catálogo não deve listar aplicativos upstream/de terceiros como produtos próprios. Consulte as releases para confirmar quais binários estão publicados antes de divulgar um download.

## Fontes e referências

- [Catálogo oficial Decode Open Source Hub](https://decode-open-source-hub-catalog.vercel.app/)
- [Suíte de Aplicativos (Monorepo)](https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps)
- [Código-fonte do Decode Launcher](https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher)
- [Releases e Downloads do Decode Launcher](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)
## Princípios de Engenharia da Suíte Decode

A suíte segue 6 princípios fundamentais:

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
