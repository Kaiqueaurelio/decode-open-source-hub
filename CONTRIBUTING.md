# Como contribuir

Obrigado por ajudar a manter este catálogo correto e útil.

## Escopo

Este catálogo contém somente os 13 Crafting Apps listados em https://getartcraft.com/apps e no catálogo-fonte oficial do ArtCraft Launcher: https://github.com/storytold/craft-launcher/blob/main/crates/core/src/catalog.rs. O Launcher é uma fonte de conferência, não uma entrada catalogada.

**Não adicione programas open source genéricos de outras equipes.** Isso quebraria o escopo deste projeto. O ArtCraft Studio e o Launcher também não devem ser adicionados como itens do catálogo.

## Sugerir uma correção ou novo produto oficial

1. Confirme que o app aparece no site oficial ArtCraft e no catálogo-fonte do Launcher.
2. Confirme que o código-fonte está na organização https://github.com/storytold.
3. Confira a licença nos arquivos oficiais LICENSE-MIT e LICENSE-APACHE.
4. Use a página oficial do produto para detalhes, plataformas e opções de download.
5. Descreva as fontes usadas no pull request.

## Testes locais

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

Se a equipe ArtCraft adicionar um app à suíte oficial, confirme a presença dele nas duas listas oficiais; só então atualize `data/software.json`, `data/schema.json`, `scripts/validate_catalog.py` e `tests/test_catalog.py` juntos.

## Padrões

- Não adivinhe licença, versão, plataformas ou estágio.
- Não copie logotipos, imagens ou capturas de tela sem confirmar os direitos.
- Não inclua tokens, senhas, dados pessoais ou instaladores.
- Não apresente testes locais como auditoria de segurança.
- Preserve os avisos de direito autoral e os créditos dos projetos originais.
