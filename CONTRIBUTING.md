# Como contribuir

Obrigado por ajudar a manter este catálogo correto e útil.

## Escopo

Este catálogo é intencionalmente restrito ao ecossistema ArtCraft: os 13 Crafting Apps da página oficial https://getartcraft.com/apps, o ArtCraft Studio e o ArtCraft Launcher.

**Não adicione programas open source genéricos de outras equipes.** Isso quebraria o escopo deste projeto.

## Sugerir uma correção ou novo produto oficial

1. Confirme a entrada no site oficial ArtCraft.
2. Confirme que o código-fonte está na organização https://github.com/storytold.
3. Confira a licença nos arquivos oficiais LICENSE-MIT e LICENSE-APACHE.
4. Use a página oficial do produto para detalhes, plataformas e opções de download.
5. Descreva as fontes usadas no pull request.

## Testes locais

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

Se o ArtCraft publicar novos apps, atualize `data/software.json`, `data/schema.json`, `scripts/validate_catalog.py` e `tests/test_catalog.py` juntos. Não inclua produtos que não sejam confirmados pelo site oficial.

## Padrões

- Não adivinhe licença, versão, plataformas ou estágio.
- Não copie logotipos, imagens ou capturas de tela sem confirmar os direitos.
- Não inclua tokens, senhas, dados pessoais ou instaladores.
- Não apresente testes locais como auditoria de segurança.
- Preserve os avisos de direito autoral e os créditos dos projetos originais.
