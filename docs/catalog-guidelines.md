# Diretrizes do Catálogo Decode

## Escopo permitido

O catálogo contém os 13 aplicativos da **Decode App Suite**:
DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD e DecodeGrid.

O **Decode Launcher** atua como utilitário nativo de instalação e gerenciamento da suíte. Não acrescente softwares genéricos não relacionados ao ecossistema Decode para manter a integridade e coesão da suíte.

## Registros e metadados

Cada registro de software contém:
- `slug`: identificador único técnico;
- `name`: nome de apresentação com prefixo Decode (ex.: `DecodePhoto`, `DecodeCAD`);
- `icon`: caractere visual ou emoji de identificação;
- `category`: categoria de atuação (ex.: "Imagem e fotografia", "Design e publicação");
- `kind`: identificação do tipo de produto;
- `tagline`: frase curta de destaque em português;
- `description`: descrição técnica e clara dos recursos;
- `platforms`: plataformas suportadas (macOS, Windows, Linux, Web);
- `license`: termo de licenciamento de código aberto (ex.: "MIT OR Apache-2.0");
- `licenseUrl`, `websiteUrl`, `sourceUrl`, `downloadUrl`: URLs válidas em HTTPS;
- `tags`: termos de pesquisa, incluindo os nomes de referência (ex.: `PhotoCraft`, `CADCraft`);
- `stage`: estágio atual de desenvolvimento ("Alpha inicial", "Em desenvolvimento").

## DecodeCAD

O DecodeCAD é mantido no repositório [Kaiqueaurelio/decodecad](https://github.com/Kaiqueaurelio/decodecad), e todos os links de código-fonte e licença apontam diretamente para este projeto.

## Nomes e apresentação

Na interface e na documentação, utilize sempre os nomes oficiais Decode: DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD e DecodeGrid. Os nomes de referência continuam cadastrados no campo `tags` para permitir busca imediata por qualquer termo anterior.
