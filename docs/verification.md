# Verificação e Manutenção do Catálogo

## Verificações automáticas

O script `scripts/validate_catalog.py` valida que o catálogo contém rigorosamente os 13 aplicativos da Decode App Suite e o Decode Launcher, garantindo que as ordens, categorias, tipos, plataformas, estágios, licenças e URLs oficiais estejam perfeitamente formatados.

A suíte de testes em `tests/test_catalog.py` verifica:
1. Presença dos 13 aplicativos Decode com seus nomes padronizados (prefixo Decode);
2. Associação correta do DecodeCAD com o repositório `Kaiqueaurelio/decodecad`;
3. Registro dos nomes de referência nas tags de busca para paridade de busca;
4. Unicidade de slugs e nomes;
5. Estrutura e integridade de links e esquemas de URL;
6. Controles de interface no frontend web;
7. Documentação do código do launcher no README raiz e compilação do workspace.

## Processo de validação local

Para rodar as verificações locais:

```bash
# Validação estrutural do catálogo
python3 scripts/validate_catalog.py

# Testes automatizados com unittest
python3 -m unittest discover -s tests -v

# Testes de integração do launcher em Rust
cd launcher
cargo test --workspace --locked
```

## Diretrizes de revisão

1. Verifique sempre se as URLs HTTPS estão ativas e acessíveis.
2. Certifique-se de que nenhum instalador externo ou ativo não autorizado seja adicionado ao repositório.
3. Mantenha os 13 nomes com prefixo Decode padronizados em todos os arquivos de configuração e documentação.
