# ArtCraft Launcher — ficha de referência

> Esta documentação resume informações públicas do projeto upstream e não substitui seu README, seus avisos de licença ou suas releases.

- Projeto: [storytold/craft-launcher](https://github.com/storytold/craft-launcher)
- Downloads e notas da versão: [releases/latest](https://github.com/storytold/craft-launcher/releases/latest)
- Site do ecossistema: [getartcraft.com](https://getartcraft.com/)
- Linguagem informada: Rust.
- Propósito: centralizar descoberta, instalação, inicialização e atualização dos aplicativos Craft.
- Recursos descritos upstream: seleção de pacotes conforme sistema e arquitetura; verificação SHA-256; notificações de atualização; aplicativo nativo e versão WebAssembly; interface multilíngue.
- Plataformas e formatos documentados upstream: Linux, Windows, macOS, FreeBSD e WebAssembly. Os formatos disponíveis dependem de cada release.
- Status informado no README consultado: early alpha.

## Compilar no Linux

Consulte sempre o README upstream atualizado para requisitos e dependências. A documentação consultada descreve ferramentas Rust/Cargo e bibliotecas de desenvolvimento de sistema gráfico para Linux.

```bash
git clone https://github.com/storytold/craft-launcher.git
cd craft-launcher
cargo run --release -p artcraft-launcher
```

O comando é reproduzido como referência da documentação upstream, não como garantia de compilação no seu computador. Confira a versão Rust e instale as dependências do sistema descritas pelo projeto antes de compilar.

## Licença, avisos e marcas

O launcher declara licença de código **MIT OR Apache-2.0** e publica os arquivos `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` e `ATTRIBUTION.md`. O projeto declara que a marca e os logotipos ArtCraft não estão cobertos pelas licenças de código aberto. Por isso, esta ficha não copia os ativos de marca e direciona usuários ao repositório original.

Esta é uma síntese independente e não substitui a documentação original.
