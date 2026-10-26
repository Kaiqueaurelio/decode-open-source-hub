# Como contribuir

Obrigado por ajudar a melhorar o Decode Open Source Hub! Queremos um catálogo útil, acessível, transparente e com informações fáceis de verificar.

## Sugerir um programa

Antes de enviar uma sugestão:

1. Confirme que existe uma licença open source verificável. Ser gratuito não é suficiente.
2. Procure a página oficial do projeto e o repositório de código-fonte, quando disponível.
3. Confira o nome, a descrição, as plataformas e a licença nas fontes originais.
4. Verifique se o programa já existe em data/software.json.
5. Abra uma issue com o modelo de sugestão ou envie um pull request.

Não cadastre sites de download de terceiros como fonte primária quando houver uma página oficial.

## Alterar o catálogo

Os registros ficam em data/software.json. Cada registro deve conter:

- slug: identificador único e estável, em letras minúsculas e hífens.
- name: nome oficial do programa.
- icon: emoji simples usado como marcador visual, não um logotipo de terceiro.
- category: categoria existente ou uma nova categoria justificada.
- tagline: frase curta sobre a finalidade.
- description: resumo objetivo escrito pela equipe do catálogo.
- platforms: lista de plataformas confirmadas.
- license: licença declarada pelo projeto.
- licenseUrl: fonte para conferir a licença.
- websiteUrl, sourceUrl e downloadUrl: links HTTPS oficiais relevantes.
- tags: palavras-chave úteis para a pesquisa.
- featured: valor booleano para definir destaque editorial.

## Testes locais

Execute a validação de dados:

    python3 scripts/validate_catalog.py

Execute a suíte de testes:

    python3 -m unittest discover -s tests -v

Antes de abrir um pull request, verifique também a interface em computador e celular, os links recém-adicionados e a acessibilidade básica.

## Padrões para pull requests

- Faça mudanças pequenas e com um objetivo claro.
- Explique o que mudou e por quê.
- Inclua fontes oficiais para novos registros ou correções de licenças.
- Não adicione chaves, senhas, tokens, dados pessoais ou arquivos de instalação ao repositório.
- Não copie logotipos, capturas de tela ou materiais de terceiros sem verificar os direitos.
- Não apresente verificações manuais como testes automatizados.
- Informe explicitamente se uma licença ou informação não pôde ser confirmada.

Ao contribuir, você confirma que tem autorização para enviar o conteúdo proposto e que ele não viola direitos de terceiros.
