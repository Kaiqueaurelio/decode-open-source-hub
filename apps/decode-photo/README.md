> **Decode Photo — desenvolvido e mantido pela [Decode Analytics](https://www.instagram.com/decode.analytics/).**
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

<h1 align="center">Decode Photo</h1>

<p align="center">
  <b>Editor profissional de imagens, camadas, máscaras e documentos PSD em puro Rust.</b>
</p>

<p align="center">
  <img alt="Linguagem: 100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="Licença: MIT OR Apache-2.0" src="https://img.shields.io/badge/licença-MIT%20%2F%20Apache--2.0-blue?style=flat-square">
  <a href="https://www.instagram.com/decode.analytics/"><img alt="Instagram: @decode.analytics" src="https://img.shields.io/badge/Instagram-@decode.analytics-E4405F?style=flat-square&logo=instagram&logoColor=white"></a>
  <a href="https://kaiqueaurelio.github.io/decode-open-source-hub/"><img alt="Decode Hub" src="https://img.shields.io/badge/Decode%20Hub-Presidente%20Prudente-0891b2?style=flat-square"></a>
</p>

---

## Sobre o Aplicativo

O Decode Photo é uma ferramenta avançada de edição de imagens e pintura digital desenvolvida em Rust. Suporta camadas não destrutivas, máscaras, ajustes tonais, tipografia vetorial e leitura nativa de arquivos Photoshop (PSD), combinando performance extrema com arquitetura de código aberto.

O **DecodePhoto** foi desenvolvido com foco em desempenho nativo, arquitetura limpa em Rust e segurança de memória. Integrado ao ecossistema [Decode Open Source Hub](https://github.com/Kaiqueaurelio/decode-open-source-hub), o programa pode ser instalado e atualizado de forma centralizada pelo [Decode Launcher](../../launcher/).

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
cargo run --release -p photocraft

# Executar a suíte de testes
cargo test --workspace
```

## Instalação pelo Decode Launcher

Para instalar o **Decode Photo** e todos os aplicativos da suíte Decode com instalador gráfico e atualizações automáticas:
1. Abra o [Decode Launcher](../../launcher/).
2. Localize o **DecodePhoto** na grade de aplicativos.
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
