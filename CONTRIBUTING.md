# Como contribuir

Agradecemos pelo interesse em contribuir com o **Decode Open Source Hub** e o **Decode Launcher**. Sua ajuda é fundamental para manter este ecossistema atualizado, acessível e de alta qualidade.

## Escopo

O catálogo contempla os 13 aplicativos da Decode App Suite (DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD e DecodeGrid) e o Decode Launcher como ferramenta nativa de gerenciamento.

**Não inclua programas arbitrários de terceiros que não façam parte da suíte Decode.** Isso garante consistência, foco na experiência do usuário e aderência aos padrões técnicos do projeto.

## Sugerir correções ou atualizações

1. Confirme as informações nas fontes oficiais do projeto (releases, tags e documentação).
2. Para o DecodeCAD, utilize o repositório oficial [Kaiqueaurelio/decodecad](https://github.com/Kaiqueaurelio/decodecad).
3. Verifique as licenças nos arquivos oficiais (MIT, Apache-2.0, etc.).
4. Indique links oficiais para documentação, plataformas suportadas e notas de lançamento.
5. Descreva detalhadamente as mudanças e motivações no seu Pull Request.

## Testes locais

Antes de submeter sua contribuição, execute os testes automatizados do catálogo e do launcher:

```bash
# Validação e testes do catálogo web
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v

# Validação do launcher Rust
cd launcher
cargo fmt --all -- --check
cargo test --workspace --locked
```

Ao alterar qualquer dado estruturado dos 13 aplicativos da suíte, certifique-se de sincronizar `data/software.json`, `data/schema.json`, `scripts/validate_catalog.py` e `tests/test_catalog.py` em conjunto.

## Padrões e boas práticas

- Não assuma ou altere licenças, versões ou plataformas sem conferência das fontes.
- Não copie ativos protegidos sem os devidos direitos ou conformidade de marca.
- Não submeta credenciais, tokens, dados sensíveis ou instaladores binários não verificados.
- Preserve todos os avisos de direito autoral, atribuições e termos de licença exigidos por lei.
