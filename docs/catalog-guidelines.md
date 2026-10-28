# Diretrizes do Catálogo Decode

## Escopo permitido

O catálogo exibe somente os aplicativos próprios mantidos neste repositório: **DecodeCraft**, **DecodeCraftX** e **DecodeClip**, além do **Decode Launcher** como utilitário de instalação e gerenciamento. Não incluir aplicativos de terceiros, upstream ou reempacotados sob nomes Decode. Só cadastrar um aplicativo quando seu código-fonte e manutenção estiverem comprovadamente presentes no monorepo.

## Registros e metadados

Cada registro deve conter `slug`, `name`, `icon`, `category`, `kind`, `tagline`, `description`, `platforms`, `license`, `licenseUrl`, `websiteUrl`, `sourceUrl`, `downloadUrl`, `tags` e `stage`. Os links de fonte e licença devem apontar para o código real do respectivo aplicativo neste repositório.

## Regras de origem

- Não adicionar projetos externos só porque existem diretórios, forks ou nomes de referência.
- Não substituir nomes e ícones de projetos de terceiros para apresentá-los como aplicativos próprios.
- Manter downloads vinculados às releases verificadas do projeto correspondente.
- Atualizar `data/software.json`, o validador e os testes juntos.
