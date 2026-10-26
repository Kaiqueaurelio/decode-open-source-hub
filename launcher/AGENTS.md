# AGENTS.md: guia para agentes de IA e colaboradores

O Decode Launcher instala, atualiza e inicializa os aplicativos da **Decode App Suite** (DecodePhoto, DecodeLight,
DecodeFilm, DecodeDesign, DecodeVector, DecodePdf, DecodeEffect, DecodeWord, DecodeDeck, DecodeGrid,
DecodeCAD, DecodeSound e DecodeFig). O projeto é desenvolvido **exclusivamente em Rust** (sem JavaScript ou TypeScript): o aplicativo desktop
utiliza egui/eframe nativo, e a versão web é o mesmo código Rust compilado para WebAssembly (trunk +
wasm-bindgen). **Nunca use Tauri, Electron ou wrappers webview**.

O nome de produto em qualquer texto voltado ao usuário é sempre **Decode Launcher** (interface, títulos de janela, Sobre,
menu de bandeja, notificações, instaladores e documentação). A suíte é a **Decode App Suite**. Nomes de máquina permanecem em minúsculas: crates e binários (`decode-launcher`,
`decode-launcher-*`), nomes de arquivo e o identificador de aplicativo `com.decode.launcher`.

## 1. Mapa do Workspace

```text
crates/
  core      decode-launcher-core      puro e compatível com wasm: catálogo de apps, versões,
                                        análise de releases do GitHub e seleção de binários por plataforma
  native    decode-launcher-native    exclusivo desktop: HTTP, detecção de apps instalados, download,
                                        verificação SHA-256 e instalação
  ui-egui   decode-launcher-ui-egui   interface egui compartilhada (desktop e web)
apps/
  decode-launcher                     shell desktop (eframe): janela, ícone de bandeja, notificações
  decode-launcher-web                 mesma interface no navegador (trunk; apenas catálogo e downloads)
xtask/                                automações cargo xtask ci | wasm | version | ico
packaging/                            scripts de empacotamento para macOS, Windows, Linux, FreeBSD e web
assets/app-icon/                      ícone do próprio launcher (SVG mestre, renders, ícones de bandeja)
assets/app-icons/                     ícones dos aplicativos Decode
assets/fonts/                         fontes OFL (Archivo, Inter, Geist Mono)
```

Camadas: `core` não depende de nenhum outro crate do workspace e deve compilar para `wasm32-unknown-unknown`.
`native` pode depender de `core`. `ui-egui` pode depender de `core` (e de `native` apenas sob
`cfg(not(target_arch = "wasm32"))` ou via trait implementada pelo shell desktop).

## 2. Regras de ouro

### Nunca cause pânico ou travamento (prioridade máxima)

Uma resposta inválida da rede, release malformada, download interrompido, disco cheio ou arquivo de preferências corrompido deve resultar em um erro compreensível para o usuário, nunca em um pânico (`panic`).

- **Código de produção nunca entra em pânico.** Não use `unwrap()`, `expect()`, `panic!`, `unreachable!`, `todo!` ou `unimplemented!`. Retorne o tipo de erro do crate e propague com `?`.
- Todas as raízes de crates de produção (`lib.rs`, `main.rs` de binários e `xtask`) utilizam
  `#![deny(clippy::unwrap_used, clippy::expect_used, clippy::panic, clippy::unimplemented, clippy::todo, clippy::unreachable)]`.
- **Proibido código `unsafe`.** O workspace define `unsafe_code = "forbid"`.
- **Qualquer entrada de rede deve ser tratada como não confiável.** Use `get()` em vez de indexação direta, aritmética protegida para tamanhos e offsets, e limite o tamanho máximo de downloads e payloads JSON.

### Instalação segura de softwares

- Faça downloads exclusivamente a partir de URLs e releases oficiais autenticadas. A única exceção é o espelho de loopback de desenvolvedor (`DECODE_LAUNCHER_DOWNLOAD_BASE`, `cargo xtask local`), restrito a endereços locais e protegido pela flag cargo `local-mirror`.
- Verifique a integridade de cada download contra o `SHA256SUMS.txt` da release antes de executá-lo ou instalá-lo.
- Nunca execute um instalador com privilégios elevados de forma silenciosa; informe previamente o usuário sobre a ação.
- Nunca remova arquivos do usuário que não tenham sido instalados pelo próprio launcher.

### Identidade e interface

A interface segue design consistente: cantos retos e modernos, linhas finas de 1 px em vez de sombras pesadas, fontes Archivo para cabeçalhos e nomes de apps, Inter para texto corrido e Geist Mono para rótulos e botões. Construa novas telas reutilizando os componentes de `widgets.rs` e tokens de `theme::Tokens`.

Respeite as preferências de animação do sistema operacional: com animações desligadas no Windows, "Reduzir movimento" no macOS/Linux ou `prefers-reduced-motion` no navegador, os elementos não devem deslizar ou esvanecer bruscamente (`Host::reduce_motion`, `crates/ui-egui/src/motion.rs`).

### Idiomas e internacionalização

Todas as mensagens exibidas na interface passam pelo módulo `crates/ui-egui/src/i18n` (`tl!("…")` para literais, `fmt` para interpolações `{…}`, `tn` para contagens). O Português do Brasil é suportado nativamente.

## 3. Verificações antes de concluir qualquer tarefa

```sh
cargo xtask ci              # valida formatação, clippy sem avisos, testes e compilação wasm
```

Também é possível executar testes pontuais: `cargo test -p <crate>`, `cargo clippy -p <crate> --all-targets -- -D warnings`, `cargo xtask wasm`.

## 4. Pacotes de release

| Plataforma | Arquivos gerados |
|---|---|
| Windows | `decode-launcher-<ver>-windows-{x64,x86,arm64}.msi`, `…-windows-{x64,x86,arm64}-portable.zip` |
| macOS | `decode-launcher-<ver>-macos-universal.dmg` |
| Linux | `decode-launcher-<ver>-linux-{x86_64,aarch64}.{AppImage,AppImage.zsync,deb,rpm,tar.gz,flatpak}`, `decode-launcher-<ver>-linux-riscv64.{deb,rpm,tar.gz}` |
| FreeBSD | `decode-launcher-<ver>-freebsd-x86_64.tar.gz` |
| Web | `decode-launcher-web-<ver>.zip` |
