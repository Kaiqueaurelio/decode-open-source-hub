# Verificação e manutenção

## Verificações automáticas

`scripts/validate_catalog.py` verifica que o catálogo contém exatamente os 15 projetos do escopo atual, incluindo os 13 Crafting Apps, ArtCraft Studio e ArtCraft Launcher. Confere também campos obrigatórios, slugs únicos, tipos, categorias, licenças, HTTPS e domínios oficiais.

A suíte `tests/test_catalog.py` verifica escopo, unicidade, links sintaticamente válidos e execução do validador.

## Limites

Os testes não auditam o código dos aplicativos, não executam instaladores e não confirmam em tempo real a disponibilidade de todas as URLs. O catálogo não garante a estabilidade dos produtos: vários Crafting Apps continuam em alpha inicial ou em desenvolvimento.

## Processo de revisão

1. Compare a lista com https://getartcraft.com/apps.
2. Confira o site e o repositório oficial em github.com/storytold.
3. Confira os arquivos de licença e eventuais avisos sobre componentes de terceiros.
4. Atualize estágio e plataformas conforme as páginas atuais.
5. Execute o validador e a suíte de testes antes de abrir um pull request.

Este catálogo é independente e não é um produto oficial do ArtCraft. Evite sugerir afiliação ou endosso dos mantenedores.
