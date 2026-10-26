# Decode Open Source Hub — ArtCraft Edition

**O catálogo independente dos programas open source do ecossistema ArtCraft.**

Este repositório é intencionalmente focado nos projetos oficiais ArtCraft — não em um diretório genérico de softwares de código aberto.

## Escopo do catálogo

A página oficial do ArtCraft apresenta 13 Crafting Apps: PhotoCraft, VectorCraft, FilmCraft, LightCraft, PdfCraft, EffectCraft, DesignCraft, FigCraft, WordCraft, SoundCraft, DeckCraft, CADCraft e GridCraft. O catálogo inclui esses 13 aplicativos, o ArtCraft Studio e o ArtCraft Launcher.

- **13 Crafting Apps:** programas criativos e de produtividade listados em [getartcraft.com/apps](https://getartcraft.com/apps).
- **ArtCraft Studio:** o estúdio principal de criação de imagens e vídeos com IA e composição visual, em [getartcraft.com](https://getartcraft.com/).
- **ArtCraft Launcher:** instalador e atualizador oficial da suíte.

**Total nesta edição: 15 projetos do ecossistema ArtCraft.** Os 13 Crafting Apps são distinguidos dos dois projetos relacionados pelos campos de tipo e estágio.

> Este catálogo é independente, mantido neste repositório. Não é um site oficial do ArtCraft, não é afiliado à equipe ArtCraft e não representa endosso dos desenvolvedores.

## Recursos

- Pesquisa por nome, finalidade, categoria, tipo, licença, estágio ou palavra-chave.
- Filtros por categoria e sistema operacional.
- Ordenação por destaque, nome e categoria.
- Cartões com descrições, plataformas, tipo de projeto e estágio informado.
- Links para páginas oficiais de download, sites, código-fonte e licença.
- Interface responsiva em português, sem frameworks ou dependências externas.
- Dados em JSON, validador, testes automatizados e GitHub Actions.
- Publicação do site pelo Vercel.

## Fonte e licenciamento dos projetos listados

Cada entrada aponta para um repositório sob a organização [github.com/storytold](https://github.com/storytold) e uma página em [getartcraft.com](https://getartcraft.com/). Os projetos desta lista disponibilizam a licença **MIT OU Apache-2.0**, pelos arquivos de licença nos respectivos repositórios. Os ativos de marca e componentes de terceiros podem ter termos próprios e não são relicenciados por esta listagem.

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
- `data/software.json`: 15 entradas do ecossistema ArtCraft.
- `data/schema.json`: esquema dos registros.
- `scripts/validate_catalog.py`: validação de escopo e dados.
- `tests/test_catalog.py`: testes automatizados.
- `docs/catalog-guidelines.md`: regras para manter o catálogo restrito aos projetos ArtCraft.
- `docs/verification.md`: processo e limites de verificação.
- `LICENSE`: licença MIT para o código deste catálogo.
- `LICENSE-DATA.md`: CC BY 4.0 para os textos e dados editoriais originais.

## Testes

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

As verificações automatizadas confirmam estrutura, escopo e sintaxe dos links. Elas **não** garantem que cada URL esteja respondendo neste momento, não constituem auditoria de segurança e não substituem a revisão das versões nas fontes oficiais.

## Atualizar o catálogo

A lista dos 13 Crafting Apps é publicada em [getartcraft.com/apps](https://getartcraft.com/apps). Se a equipe ArtCraft adicionar um novo produto, confirme-o na página oficial e no repositório correspondente; depois atualize `data/software.json`, `data/schema.json`, `scripts/validate_catalog.py` e `tests/test_catalog.py` juntos. Não acrescente programas de outras equipes.

## Licenciamento deste catálogo

- Código da interface e scripts deste repositório: **MIT**, conforme `LICENSE`.
- Textos e dados editoriais originais: **CC BY 4.0**, conforme `LICENSE-DATA.md`.
- Programas listados: **MIT OU Apache-2.0**, nos termos dos repositórios oficiais; cada projeto mantém seus próprios avisos, direitos e condições para componentes de terceiros.
- Marcas e logotipos ArtCraft permanecem propriedade de seus titulares. Esta página usa emojis como marcadores visuais, sem copiar os ícones oficiais.

**Decode Open Source Hub — os projetos open source do ArtCraft, organizados em um catálogo claro e independente.**
