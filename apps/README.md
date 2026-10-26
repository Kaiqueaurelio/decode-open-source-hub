# Suíte de Aplicativos Decode — Repositórios de Código-Fonte

Este diretório contém os códigos-fonte independentes de todos os 13 aplicativos da **Decode App Suite**, organizados e mantidos no âmbito do Decode Open Source Hub.

Cada aplicativo é um workspace modular em Rust com interface nativa em egui, empacotamento multiplataforma e padrões modernos de código aberto.

| Aplicativo | Diretório | Finalidade | Código-fonte |
|:---|:---|:---|:---|
| **[DecodePhoto](decode-photo/)** | `decode-photo` | Edição de imagens: camadas, máscaras, texto e suporte real a PSD | [GitHub](https://github.com/storytold/photocraft) |
| **[DecodeVector](decode-vector/)** | `decode-vector` | Ilustração vetorial | [GitHub](https://github.com/storytold/vectorcraft) |
| **[DecodeFilm](decode-film/)** | `decode-film` | Edição de vídeo, pós-produção, cor e áudio | [GitHub](https://github.com/storytold/filmcraft) |
| **[DecodeLight](decode-light/)** | `decode-light` | Revelação RAW e catálogo de fotografias | [GitHub](https://github.com/storytold/lightcraft) |
| **[DecodePdf](decode-pdf/)** | `decode-pdf` | Leitura, anotação, organização e segurança em PDFs | [GitHub](https://github.com/storytold/pdfcraft) |
| **[DecodeEffect](decode-effect/)** | `decode-effect` | Motion graphics e efeitos visuais | [GitHub](https://github.com/storytold/effectcraft) |
| **[DecodeDesign](decode-design/)** | `decode-design` | Diagramação, editoração de páginas e publicação | [GitHub](https://github.com/storytold/designcraft) |
| **[DecodeFig](decode-fig/)** | `decode-fig` | Design de interfaces de usuário e prototipagem interativa | [GitHub](https://github.com/storytold/figcraft) |
| **[DecodeWord](decode-word/)** | `decode-word` | Processamento de texto e formatação de documentos | [GitHub](https://github.com/storytold/wordcraft) |
| **[DecodeSound](decode-sound/)** | `decode-sound` | Gravação, mixagem e edição de áudio multipista | [GitHub](https://github.com/storytold/soundcraft) |
| **[DecodeDeck](decode-deck/)** | `decode-deck` | Apresentações e slides visuais | [GitHub](https://github.com/storytold/deckcraft) |
| **[DecodeCAD](decode-cad/)** | `decode-cad` | Projeto e desenho técnico assistido por computador (CAD) | [GitHub](https://github.com/Kaiqueaurelio/decodecad) |
| **[DecodeGrid](decode-grid/)** | `decode-grid` | Planilhas eletrônicas e processamento de dados | [GitHub](https://github.com/storytold/gridcraft) |

## Arquitetura

* **Workspaces independentes:** Cada aplicação em `apps/<app>` conta com seu próprio `Cargo.toml`, crates internos (`crates/*`), shell de desktop (`apps/*`) e receitas de empacotamento.
* **Gerenciamento centralizado:** O [Decode Launcher](../launcher/) descobre, abre, instala e atualiza todos os aplicativos desta suíte.
* **Licenciamento:** Todas as ferramentas são de código aberto sob licenças **MIT OR Apache-2.0**.
