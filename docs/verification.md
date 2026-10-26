# Verificação e manutenção

## Verificações automáticas

`scripts/validate_catalog.py` confirma que o catálogo contém exatamente os 13 apps e na mesma ordem do catálogo-fonte oficial do ArtCraft Launcher (`crates/core/src/catalog.rs`). Também verifica categorias, tipo, plataformas, estágio, licenças, campos obrigatórios, slugs únicos e URLs oficiais.

A suíte `tests/test_catalog.py` verifica o conjunto e a ordem dos 13 apps, exclui explicitamente o ArtCraft Studio e o próprio Launcher como entradas, e confere os links, os rótulos de licença e a execução do validador.

## Conferência das fontes

- Lista oficial: https://getartcraft.com/apps
- Catálogo-fonte do Launcher: https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs
- Repositórios: https://github.com/storytold

A validação estática não substitui uma consulta ao vivo dos endereços, não executa instaladores e não é uma auditoria de segurança. Os estágios podem mudar e alguns aplicativos continuam em alpha inicial ou em desenvolvimento.

## Processo de revisão

1. Compare a lista e a ordem com o site oficial e com o catálogo-fonte do Launcher.
2. Confira se cada app tem seu próprio repositório na organização oficial.
3. Confira os arquivos de licença e eventuais avisos sobre componentes de terceiros.
4. Atualize estágio e plataformas conforme as páginas oficiais atuais.
5. Execute o validador e a suíte de testes antes de abrir um pull request.

Este catálogo é independente e não é um produto oficial do ArtCraft. Evite sugerir afiliação ou endosso dos mantenedores.
