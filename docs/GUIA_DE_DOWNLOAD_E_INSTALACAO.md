# Guia Oficial de Download, Instalação e Atualização
## Decode Open Source Hub — Decode Analytics

Bem-vindo ao guia oficial de instalação e distribuição dos aplicativos da suíte **Decode Open Source Hub**, desenvolvida e mantida pela **Decode Analytics** (Presidente Prudente – SP, Brasil).

---

## 🚀 Método Recomendado: Decode Launcher (Desktop)

O **Decode Launcher** é o aplicativo desktop oficial que centraliza a descoberta, instalação, execução e **atualização automática contínua** de todos os programas da suíte Decode.

### Recursos do Launcher:
* **Atualização Automática**: Sempre que uma nova versão ou correção for publicada no repositório GitHub, o Launcher identifica e atualiza os aplicativos em segundo plano sem necessidade de reinstalação manual.
* **Sem dependência de nuvem**: Funciona 100% offline, localmente na sua máquina.
* **Nativo em Rust**: Interface acelerada por GPU (WGPU/egui), extremamente leve, sem Electron e sem consumo excessivo de memória RAM.

### Baixar o Decode Launcher:
| Sistema Operacional | Formato do Pacote | Link Direto |
| :--- | :--- | :--- |
| **Windows** (10 / 11 64-bit) | Instalador `.msi` / `.exe` | [Download Windows](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/latest) |
| **Linux** (Ubuntu, Debian, Fedora, Arch) | `.deb` / `.tar.gz` / AppImage | [Download Linux](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/latest) |
| **macOS** (Apple Silicon M1/M2/M3 & Intel) | `.dmg` Universal | [Download macOS](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/latest) |

---

## 📦 Lista de Aplicativos da Suíte Decode

Você também pode baixar e executar cada ferramenta de forma independente ou compilá-la a partir do código-fonte:

| Aplicativo | Categoria | Finalidade | Link no Monorepo |
| :--- | :--- | :--- | :--- |
| **DecodePhoto** | Imagem & Foto | Editor profissional com camadas, máscaras e suporte a arquivos PSD/PSB | [`apps/decode-photo`](../apps/decode-photo/) |
| **DecodeVector** | Ilustração | Desenho vetorial, curvas de Bézier e design gráfico paramétrico | [`apps/decode-vector`](../apps/decode-vector/) |
| **DecodeFilm** | Vídeo & Montagem | Edição de vídeo não-linear (NLE), timeline multicanal e gradação de cor | [`apps/decode-film`](../apps/decode-film/) |
| **DecodeLight** | Fotografia RAW | Revelação digital não-destrutiva de fotos RAW e catalogação inteligente | [`apps/decode-light`](../apps/decode-light/) |
| **DecodePdf** | Documentos | Leitura, edição, mesclagem, anotações e proteção criptográfica de PDFs | [`apps/decode-pdf`](../apps/decode-pdf/) |
| **DecodeEffect** | VFX & Motion | Motion graphics, composição visual nodal e animação procedural | [`apps/decode-effect`](../apps/decode-effect/) |
| **DecodeDesign** | Editoração | Diagramação de livros, revistas, brochuras e paginação com tipografia avançada | [`apps/decode-design`](../apps/decode-design/) |
| **DecodeFig** | UI / UX Design | Design de interfaces de usuário, design systems e prototipagem interativa | [`apps/decode-fig`](../apps/decode-fig/) |
| **DecodeWord** | Processador de Texto | Redação e edição rápida de documentos acadêmicos e profissionais | [`apps/decode-word`](../apps/decode-word/) |
| **DecodeSound** | Áudio & Música | Estação de áudio digital (DAW), gravação multipista e mixagem de som | [`apps/decode-sound`](../apps/decode-sound/) |
| **DecodeDeck** | Apresentações | Criador de slides dinâmicos com transições e animações | [`apps/decode-deck`](../apps/decode-deck/) |
| **DecodeCAD** | Engenharia & Arquitetura | Desenho técnico assistido por computador 2D/3D com linha de comando e snaps | [`apps/decode-cad`](../apps/decode-cad/) |
| **DecodeGrid** | Dados & Planilhas | Planilhas eletrônicas com suporte completo a `.xlsx`, fórmulas e tabelas dinâmicas | [`apps/decode-grid`](../apps/decode-grid/) |
| **DecodeCraft** | IA Criativa & 3D | IDE completa para criação generativa com IA, composição 2D e cenários 3D | [`apps/decode-craft`](../apps/decode-craft/) |
| **DecodeCraftX** | Runtime & Extensões | Módulos de aceleração nativa, shaders e extensões para o DecodeCraft | [`apps/decode-craftx`](../apps/decode-craftx/) |

---

## 🛠️ Como Compilar Localmente a partir do Código-Fonte

Todos os aplicativos da suíte Decode são 100% de código aberto sob licenças **MIT OR Apache-2.0**.

### Pré-requisitos:
* Compilador Rust estável instalado via [rustup.rs](https://rustup.rs/):
  ```bash
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

### Passos de compilação:
1. Clone o repositório oficial:
   ```bash
   git clone https://github.com/Kaiqueaurelio/decode-open-source-hub.git
   cd decode-open-source-hub
   ```

2. Compile e execute o **Decode Launcher**:
   ```bash
   cd launcher
   cargo run --release
   ```

3. Ou compile qualquer aplicativo individualmente:
   ```bash
   # Exemplo para o DecodePhoto:
   cd apps/decode-photo
   cargo run --release

   # Exemplo para o DecodeCAD:
   cd apps/decode-cad
   cargo run --release
   ```

---

## 🌐 Portais Oficiais e Acesso Web

* **Catálogo e Hub Web Oficial:** [https://decode-open-source-hub.vercel.app/](https://decode-open-source-hub.vercel.app/)
* **Repositório Monorepo:** [https://github.com/Kaiqueaurelio/decode-open-source-hub](https://github.com/Kaiqueaurelio/decode-open-source-hub)
* **Releases e Binários Compilados:** [https://github.com/Kaiqueaurelio/decode-open-source-hub/releases](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases)

---

## 🏢 Sobre a Mantenedora

* **Empresa:** Decode Analytics
* **Sede:** Presidente Prudente — São Paulo, Brasil
* **Instagram Oficial:** [@decode.analytics](https://www.instagram.com/decode.analytics/)
* **E-mail de Contato:** decoanalytics@outlook.com.br
