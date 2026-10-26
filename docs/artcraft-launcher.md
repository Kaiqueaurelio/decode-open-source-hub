# Decode Launcher — Documentação de Referência

> Esta documentação reúne informações técnicas, arquitetura e referências do Decode Launcher.

- **Repositório do Launcher:** [Decode Launcher (launcher/)](https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher)
- **Releases e Downloads:** [releases/latest](https://github.com/Kaiqueaurelio/decode-open-source-hub/releases/latest)
- **Linguagem:** 100% Rust estável.
- **Propósito:** centralizar a descoberta, instalação, inicialização e atualização dos aplicativos da Decode App Suite.
- **Recursos implementados:** seleção automática de pacotes conforme sistema operacional e arquitetura de CPU; conferência de integridade por checksum SHA-256; notificações no sistema operacional; interface nativa com egui (sem Electron); compilação WebAssembly; internacionalização com suporte completo a Português do Brasil.
- **Plataformas suportadas:** Linux (AppImage, DEB, RPM, Flatpak, tar.gz), Windows (MSI e portátil x64, ARM64, x86), macOS (DMG universal assinado), FreeBSD e Web.
- **Estágio:** early alpha.

## Compilação e execução local

Para compilar no Linux com aceleração nativa:

```bash
cd launcher
cargo run --release -p decode-launcher
```

Para rodar a suíte completa de testes e checagens:

```bash
cd launcher
cargo xtask ci
```

## Licença e conformidade

O código-fonte do Decode Launcher é licenciado sob **MIT OR Apache-2.0**, com avisos e créditos detalhados em `launcher/NOTICE` e `launcher/ATTRIBUTION.md`. Os ativos da marca Decode são protegidos e seguem diretrizes próprias.
