# Suíte de Aplicativos Decode — Repositórios de Código-Fonte

Este diretório contém os códigos-fonte independentes de todos os 13 aplicativos da **Decode App Suite**, organizados e mantidos no âmbito do Decode Open Source Hub da **Decode Analytics** (Presidente Prudente - SP).

Cada aplicativo é um workspace modular em Rust com interface nativa acelerada por GPU (WGPU/egui), empacotamento multiplataforma e padrões modernos de código aberto.

### Links Diretos de Download:
- 🚀 **[Releases e Pacotes Oficiais Compilados](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)**
- 📦 **[Baixar Código-Fonte Completo da Suíte (.ZIP)](https://github.com/Kaiqueaurelio/decode-open-source-hub/archive/refs/heads/main.zip)**
- 🌐 **[Catálogo Web Interativo](https://decode-open-source-hub-catalog.vercel.app)**

---

### Aplicativos Disponíveis no Monorepo:

| Aplicativo | Diretório | Finalidade | Como Compilar e Rodar |
| :--- | :--- | :--- | :--- |
| **[DecodePhoto](decode-photo/)** | [`apps/decode-photo`](decode-photo/) | Edição de imagens: camadas, máscaras, texto e suporte a PSD | `cd decode-photo && cargo run --release` |
| **[DecodeVector](decode-vector/)** | [`apps/decode-vector`](decode-vector/) | Ilustração e desenho vetorial profissional | `cd decode-vector && cargo run --release` |
| **[DecodeFilm](decode-film/)** | [`apps/decode-film`](decode-film/) | Edição de vídeo não linear, cor e áudio | `cd decode-film && cargo run --release` |
| **[DecodeLight](decode-light/)** | [`apps/decode-light`](decode-light/) | Revelação RAW fotográfica e catálogo | `cd decode-light && cargo run --release` |
| **[DecodePdf](decode-pdf/)** | [`apps/decode-pdf`](decode-pdf/) | Leitura, anotação, organização e segurança em PDFs | `cd decode-pdf && cargo run --release` |
| **[DecodeEffect](decode-effect/)** | [`apps/decode-effect`](decode-effect/) | Motion graphics, composição e efeitos visuais (VFX) | `cd decode-effect && cargo run --release` |
| **[DecodeDesign](decode-design/)** | [`apps/decode-design`](decode-design/) | Diagramação, editoração de páginas e publicação | `cd decode-design && cargo run --release` |
| **[DecodeFig](decode-fig/)** | [`apps/decode-fig`](decode-fig/) | Design de interfaces de usuário (UI/UX) e prototipagem | `cd decode-fig && cargo run --release` |
| **[DecodeWord](decode-word/)** | [`apps/decode-word`](decode-word/) | Processamento de texto e formatação de documentos | `cd decode-word && cargo run --release` |
| **[DecodeSound](decode-sound/)** | [`apps/decode-sound`](decode-sound/) | Estação de áudio digital (DAW) multipista | `cd decode-sound && cargo run --release` |
| **[DecodeDeck](decode-deck/)** | [`apps/decode-deck`](decode-deck/) | Apresentações visuais e slides dinâmicos | `cd decode-deck && cargo run --release` |
| **[DecodeCAD](decode-cad/)** | [`apps/decode-cad`](decode-cad/) | Projeto e desenho técnico 2D/3D assistido por computador | `cd decode-cad && cargo run --release` |
| **[DecodeGrid](decode-grid/)** | [`apps/decode-grid`](decode-grid/) | Planilhas eletrônicas e análise de dados | `cd decode-grid && cargo run --release` |

---

## Arquitetura

* **Workspaces independentes:** Cada aplicação em `apps/<app>` conta com seu próprio `Cargo.toml`, crates internos (`crates/*`), shell de desktop (`apps/*`) e receitas de empacotamento.
* **Gerenciamento centralizado:** O [Decode Launcher](../launcher/) descobre, abre, instala e atualiza todos os aplicativos desta suíte.
* **Licenciamento:** Todas as ferramentas são de código aberto sob licenças **MIT OR Apache-2.0**.
