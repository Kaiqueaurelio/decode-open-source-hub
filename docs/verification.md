# Verificação e manutenção dos registros

## O que o validador automático faz

O script scripts/validate_catalog.py verifica o formato geral do JSON, os campos obrigatórios, os slugs e nomes duplicados, as categorias, as listas de plataformas e a presença de URLs HTTPS. O workflow executa esses controles em alterações enviadas ao GitHub.

## O que ele não faz

A validação automática atual não acessa a internet para confirmar que:
- o domínio ainda pertence ao projeto;
- um link está respondendo;
- a licença declarada continua sendo a versão atual;
- a última versão foi identificada corretamente;
- o instalador é seguro ou livre de malware;
- o produto continua recebendo manutenção.

Uma URL sintaticamente válida não equivale a uma fonte verificada.

## Procedimento recomendado para revisão

1. Abra o site oficial do programa.
2. Confira a licença no site oficial ou nos arquivos de licença do repositório de origem.
3. Confirme as plataformas e a página oficial de download.
4. Revise a descrição para evitar promessas não comprovadas.
5. Execute os testes automáticos.
6. Registre as páginas utilizadas na descrição do pull request.

## Estado de verificação

O catálogo inicial foi montado como uma primeira curadoria editorial. Os links e licenças devem ser revisados individualmente antes de considerar os registros auditados. O repositório não deve exibir um selo geral de "verificado" até existir um processo de verificação rastreável e aplicado aos itens.
