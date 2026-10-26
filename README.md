# Decode Open Source Hub

**Descubra. Compare. Explore. Use software livre.**

**Site publicado:** [decode-open-source-hub-catalog.vercel.app](https://decode-open-source-hub-catalog.vercel.app)

O **Decode Open Source Hub** é um catálogo visual de softwares de código aberto, organizado por categoria, plataforma e licença. O objetivo é ajudar estudantes, profissionais, desenvolvedores e qualquer pessoa interessada em tecnologia a encontrar ferramentas úteis e acessar suas fontes oficiais sem precisar vasculhar dezenas de páginas.

> **Estado atual:** MVP estático funcional, com pesquisa, filtros, fichas de software e links para sites, códigos-fonte e downloads oficiais. O catálogo inicial é curado manualmente; ele não rastreia automaticamente todos os programas existentes.

## O que já está implementado

- Interface responsiva em português, sem frameworks ou dependências de terceiros.
- Catálogo inicial com 47 ferramentas de código aberto em várias categorias.
- Pesquisa por nome, finalidade e palavras-chave.
- Filtros por categoria e plataforma, além de ordenação.
- Cartões com resumo, licença clicável e botões para download, site oficial e código-fonte.
- Fonte de dados separada do código da interface.
- Script de validação do catálogo e testes automatizados.
- GitHub Actions para validar alterações.
- Deploy do site integrado ao repositório por meio do Vercel.

## Categorias iniciais

- Criação visual
- Produtividade
- Internet e comunicação
- Segurança e privacidade
- Utilitários
- Infraestrutura e nuvem
- Vídeo e áudio
- CAD e engenharia
- Desenvolvimento
- Ciência e dados

As categorias podem ser ampliadas conforme o catálogo crescer.

## Executar localmente

É um site estático e não exige Node.js, npm, compilação ou instalação de dependências.

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Inicie um servidor HTTP local com Python 3.
4. Abra o endereço local exibido pelo servidor no navegador.

Comandos:

    git clone https://github.com/Kaiqueaurelio/decode-open-source-hub.git
    cd decode-open-source-hub
    python3 -m http.server 8080

Acesse http://localhost:8080.

Não abra o arquivo index.html diretamente via file://, pois os navegadores podem bloquear a leitura do arquivo JSON local. Use o servidor HTTP local ou hospede o conteúdo em um serviço estático.

## Estrutura do projeto

- index.html — estrutura semântica da página.
- styles.css — identidade visual e layout responsivo.
- app.js — pesquisa, filtros, ordenação e renderização.
- data/software.json — registros do catálogo.
- data/schema.json — esquema esperado para cada registro.
- scripts/validate_catalog.py — validação de campos e links.
- tests/test_catalog.py — testes automatizados.
- docs/catalog-guidelines.md — regras para incluir programas.
- docs/verification.md — procedimento de checagem e atualização.
- LICENSE — licença do código da plataforma.
- LICENSE-DATA.md — política de licença para textos e dados editoriais originais.

## Adicionar um software

1. Edite data/software.json.
2. Inclua um identificador único, nome, categoria, descrição, plataformas, licença e links HTTPS oficiais.
3. Confirme as informações nas páginas oficiais do projeto.
4. Execute o validador:

    python3 scripts/validate_catalog.py

5. Execute os testes:

    python3 -m unittest discover -s tests -v

Leia docs/catalog-guidelines.md antes de cadastrar novos programas. Não classifique um programa como open source apenas por ser gratuito.

## Licenciamento

- Código-fonte deste catálogo: MIT, conforme LICENSE.
- Textos e metadados editoriais originais produzidos para o catálogo: CC BY 4.0, conforme LICENSE-DATA.md.
- Softwares catalogados: cada projeto conserva sua própria licença.
- Marcas, logotipos, ícones e imagens de terceiros não são relicenciados por este repositório. O catálogo usa ícones emoji como identificadores visuais iniciais, evitando copiar ativos de terceiros sem necessidade.

A licença declarada em cada ficha é informativa e deve ser conferida na fonte oficial antes de redistribuir ou modificar o software correspondente.

## Publicação

O site está publicado em **https://decode-open-source-hub-catalog.vercel.app**. O projeto Vercel **decode-open-source-hub-catalog** está conectado ao repositório e à branch main; alterações na branch de produção disparam novas implantações pelo GitHub.

O primeiro deployment do catálogo foi concluído com estado READY. A disponibilidade pública pode mudar por configurações do provedor, então consulte o painel do projeto caso o endereço deixe de responder. O workflow de CI do GitHub valida os registros antes das alterações, mas não substitui a verificação da implantação depois de cada publicação.

## Limitações conhecidas

- A lista não representa todos os programas open source existentes.
- Os registros são mantidos manualmente; links, plataformas e licenças podem mudar.
- O catálogo não hospeda os instaladores nem garante a segurança de arquivos de terceiros.
- A aplicação não executa instaladores, não faz varredura de malware e não verifica automaticamente a última versão lançada.
- Os filtros operam sobre os dados incluídos localmente no repositório.

## Contribuir

Sugestões para novos programas, correções e melhorias são bem-vindas. Leia CONTRIBUTING.md e envie uma issue ou pull request com fontes oficiais sempre que possível.

**Decode Open Source Hub — mais clareza para encontrar software aberto.**
