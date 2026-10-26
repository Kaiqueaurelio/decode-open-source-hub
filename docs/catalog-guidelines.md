# Diretrizes do catálogo ArtCraft

## Escopo permitido

O catálogo contém somente os 13 aplicativos da Craft App Suite oficial:
PhotoCraft, VectorCraft, FilmCraft, LightCraft, PdfCraft, EffectCraft, DesignCraft, FigCraft, WordCraft, SoundCraft, DeckCraft, CADCraft e GridCraft.

Fontes primárias:
- Lista dos produtos: https://getartcraft.com/apps
- Catálogo embutido no ArtCraft Launcher: https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs
- Código-fonte dos aplicativos: https://github.com/storytold

O ArtCraft Studio e o ArtCraft Launcher não são entradas deste catálogo. O Launcher é usado somente como fonte oficial de conferência da lista. Não acrescente ferramentas de outros mantenedores só por serem semelhantes.

## Registros

Cada entrada inclui slug exclusivo, nome, tipo, categoria, descrição objetiva, plataformas, licença, estágio atual e links HTTPS para site, repositório, licença e página oficial do produto. A lista e a ordem devem corresponder aos 13 apps do catálogo oficial.

## Licença

Os repositórios listados disponibilizam a opção MIT OU Apache-2.0 por meio dos arquivos oficiais LICENSE-MIT e LICENSE-APACHE. A licença indicada no catálogo é informativa. Ativos de marca, fontes, ícones e componentes de terceiros podem ter termos separados.

## Estágio de desenvolvimento

Mantenha os rótulos de acordo com a página oficial. Não transforme "Alpha inicial" ou "Em desenvolvimento" em "estável". Quando o status mudar, atualize o registro e cite a fonte no pull request.

## Downloads

Prefira a página oficial de cada app em https://getartcraft.com/apps/<app>, onde ficam as opções de instalação atuais. O campo de download deve apontar para a mesma página oficial do produto, evitando links de instaladores que possam ficar desatualizados.

A validação automatizada verifica o escopo, os valores esperados de estágio e plataforma, sintaxe de URLs e domínios. A disponibilidade dos links e a segurança dos instaladores ainda precisam de verificação externa.
