# Decode Open Source Hub — Decode Edition

**Coleção independente de 13 ferramentas com nomes de apresentação Decode, baseadas em projetos open source do ArtCraft.**

Este repositório é intencionalmente focado na suíte oficial de aplicativos do ArtCraft — não em um diretório genérico de softwares de código aberto.

## Escopo do catálogo

O catálogo contém somente os 13 aplicativos que compõem a Craft App Suite e aparecem na lista oficial do ArtCraft Launcher: PhotoCraft, VectorCraft, FilmCraft, LightCraft, PdfCraft, EffectCraft, DesignCraft, FigCraft, WordCraft, SoundCraft, DeckCraft, CADCraft e GridCraft.

- **Fonte oficial dos produtos:** [getartcraft.com/apps](https://getartcraft.com/apps).
- **Lista no código do Launcher:** [crates/core/src/catalog.rs](https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs).
- **Código-fonte:** os repositórios individuais em [github.com/storytold](https://github.com/storytold).

**Total nesta edição: 13 aplicativos.** O ArtCraft Studio e o ArtCraft Launcher não são listados como itens do catálogo: o objetivo é reproduzir apenas os apps da suíte que o Launcher instala e gerencia.

> Este catálogo é independente, mantido neste repositório. Não é um site oficial do ArtCraft, não é afiliado à equipe ArtCraft e não representa endosso dos desenvolvedores.

## Mapeamento de nomes

| Nome exibido no Decode | Nome oficial do projeto |
|---|---|
| PhotoDecode | PhotoCraft |
| VectorDecode | VectorCraft |
| FilmDecode | FilmCraft |
| LightDecode | LightCraft |
| PdfDecode | PdfCraft |
| EffectDecode | EffectCraft |
| DesignDecode | DesignCraft |
| FigDecode | FigCraft |
| WordDecode | WordCraft |
| SoundDecode | SoundCraft |
| DeckDecode | DeckCraft |
| CADDecode | CADCraft |
| GridDecode | GridCraft |

## Recursos

- Pesquisa por nome, finalidade, categoria, licença, estágio ou palavra-chave.
- Filtros por categoria e sistema operacional.
- Ordenação por destaque, nome e categoria.
- Cartões com descrições, plataformas e estágio de desenvolvimento.
- Links para páginas oficiais de download, código-fonte e licença.
- Interface responsiva em português, sem frameworks ou dependências externas.
- Dados em JSON, validador, testes automatizados e GitHub Actions.
- Publicação do site pelo Vercel.

## Fonte e licenciamento dos projetos listados

Cada entrada aponta para o repositório do próprio app sob [github.com/storytold](https://github.com/storytold) e para a página correspondente em [getartcraft.com/apps](https://getartcraft.com/apps). Os repositórios indicam a opção de licença **MIT OU Apache-2.0** por meio dos arquivos oficiais de licença. Marcas, ícones e componentes de terceiros podem ter termos próprios e não são relicenciados por esta listagem.

O estágio de cada aplicativo — por exemplo, **Alpha inicial** ou **Em desenvolvimento** — é informativo e pode mudar. Verifique a página individual antes de usar uma versão inicial em trabalho importante.

## Executar localmente

Requer Python 3 apenas para servir os arquivos locais; não exige Node.js, npm nem compilação.

```bash
git clone https://github.com/Kaiqueaurelio/decode-open-source-hub.git
cd decode-open-source-hub
python3 -m http.server 8080
```

Abra http://localhost:8080. É necessário usar um servidor HTTP porque a interface carrega `data/software.json`; abrir `index.html` diretamente pode ser bloqueado pelo navegador.

## Estrutura

- `index.html`: página principal.
- `styles.css`: layout responsivo e identidade visual.
- `app.js`: pesquisa, filtros, ordenação e cartões.
- `data/software.json`: os 13 apps oficiais da suíte.
- `data/schema.json`: esquema dos registros.
- `scripts/validate_catalog.py`: validação de escopo, ordem, plataformas e estágios.
- `tests/test_catalog.py`: testes automatizados.
- `docs/catalog-guidelines.md`: regras para manter o catálogo restrito aos 13 apps.
- `docs/verification.md`: processo e limites de verificação.
- `LICENSE`: licença MIT para o código deste catálogo.
- `LICENSE-DATA.md`: CC BY 4.0 para os textos e dados editoriais originais.

## Testes

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

As verificações automatizadas confirmam a lista esperada, sua ordem, a estrutura dos dados e a sintaxe dos links. Elas não garantem que cada URL esteja respondendo neste momento, não constituem auditoria de segurança e não substituem a revisão das versões nas fontes oficiais.

## Atualizar o catálogo

A lista dos 13 Crafting Apps é publicada em [getartcraft.com/apps](https://getartcraft.com/apps) e no catálogo-fonte do [ArtCraft Launcher](https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs). Só adicione um produto depois de confirmar que ele está nas duas listas oficiais e que possui um repositório próprio em `github.com/storytold`. Ao mudar o escopo, atualize `data/software.json`, `data/schema.json`, `scripts/validate_catalog.py` e `tests/test_catalog.py` juntos. Não acrescente programas de outras equipes.

## Licenciamento deste catálogo

- Código da interface e scripts deste repositório: **MIT**, conforme `LICENSE`.
- Textos e dados editoriais originais: **CC BY 4.0**, conforme `LICENSE-DATA.md`.
- Programas listados: **MIT OU Apache-2.0**, nos termos de cada repositório oficial; cada projeto mantém seus próprios avisos, direitos e condições para componentes de terceiros.
- Marcas e logotipos ArtCraft permanecem propriedade de seus titulares. Esta página usa emojis como marcadores visuais, sem copiar os ícones oficiais.

**Decode Open Source Hub — os 13 Crafting Apps do ArtCraft, organizados em um catálogo claro e independente.**
