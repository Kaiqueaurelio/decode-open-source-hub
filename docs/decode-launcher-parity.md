# Decode Launcher — matriz de paridade funcional

## Objetivo do produto

O Decode Open Source Hub não deve ficar apenas como uma página de catálogo. O objetivo de produto é criar uma aplicação própria, com identidade visual Decode, que ofereça as funções do ArtCraft Launcher sem apresentar o resultado como produto oficial da ArtCraft.

Projeto de referência: https://github.com/storytold/craft-launcher

## Requisitos funcionais que precisam ser implementados

| Área | Comportamento esperado | Verificação de aceite |
|---|---|---|
| Catálogo | Exibir os 13 apps da Craft App Suite e os dados oficiais de cada release | Lista completa, estados vazios e erros de API testados |
| Detecção de sistema | Identificar sistema operacional e arquitetura para sugerir o pacote correto | Casos Linux x86_64/aarch64, Windows x64/ARM64/x86, macOS e plataformas suportadas |
| Releases | Consultar releases oficiais e interpretar versões, arquivos e notas | Fixtures reais e respostas malformadas cobertas por testes |
| Instalação | Baixar o pacote compatível, exibir progresso e pedir confirmação quando necessário | Não instalar em silêncio; falhas e cancelamentos recuperáveis |
| Integridade | Validar SHA-256 do arquivo antes de instalar ou executar | Arquivo alterado ou checksum ausente/inválido não pode ser instalado |
| Aplicativos existentes | Detectar aplicativos instalados manualmente e por outros gerenciadores quando suportado | App instalado fora do launcher aparece com estado correto |
| Inicialização | Abrir aplicativos instalados a partir da interface e do menu de bandeja quando suportado | Mensagens claras para apps ausentes ou que não iniciam |
| Atualizações | Verificar novas versões dos aplicativos instalados e apresentar notificações | Não substituir um aplicativo enquanto estiver em execução |
| Atualização do Decode Launcher | Verificar e aplicar a própria atualização com verificação de integridade | Recuperação segura em erro, cancelamento e reinício |
| Instalação por sistema | Usar formatos e caminhos nativos compatíveis com cada plataforma | Nunca remover arquivos do usuário que não pertençam ao launcher |
| Linux | Documentar e testar AppImage, DEB, RPM e Flatpak conforme a release; considerar integração com tray | Requisitos, permissões e limites de sandbox visíveis |
| Windows | Suportar MSI e pacote portátil quando publicados | Instalação, atalhos, desinstalação e dados portáteis testados |
| macOS | Suportar DMG/universal build conforme a release | Instalação documentada e validação dos pacotes oficiais |
| FreeBSD | Suportar formatos oficialmente publicados | Dependências e passos de instalação documentados |
| Versão web | Oferecer catálogo e downloads recomendados no navegador | A interface web não afirma que pode instalar programas localmente |
| Idiomas | Suportar Português do Brasil como padrão preferencial e arquitetura de internacionalização | Strings sem tradução têm fallback; idioma persiste entre sessões |
| Preferências | Configurações de idioma, atualização, aparência e comportamento suportadas pelo produto | Preferências persistem e valores inválidos são tratados |
| Logs e diagnóstico | Exibir mensagens acionáveis e gravar logs sem dados pessoais desnecessários | Logs rotacionados e caminhos documentados por sistema |
| Acessibilidade | Navegação por teclado, foco visível, contraste e respeito a reduzir movimento | Testes manuais por sistema e testes automatizados aplicáveis |
| Segurança | HTTPS, allowlist de origens, limites de download e parsing defensivo de dados remotos | Nenhum instalador executado antes da validação |
| CI e release | Formatação, lint, testes nativos, compilação WebAssembly e empacotamento | Pipeline verde antes de uma release pública |

## Identidade Decode

- Nome de produto proposto: **Decode Launcher**.
- Usar marca, ícone, paleta, tipografia e textos próprios do Decode.
- Remover o nome visual, logotipo, marca “A”, ícones e outros ativos protegidos da ArtCraft no aplicativo derivado.
- Não alterar o nome, identidade ou arquivos de licença dos 13 aplicativos upstream.
- Identificar com clareza que os downloads são fornecidos pelos projetos originais da Craft App Suite.
- Não insinuar patrocínio, afiliação ou aprovação da ArtCraft.

## Licenças e atribuição

O launcher de referência declara licença MIT OR Apache-2.0 para seu código, mas o NOTICE upstream exclui expressamente a marca e os logotipos ArtCraft dessas licenças e exige que versões modificadas removam ou substituam esses ativos. Os ativos de terceiros têm suas próprias atribuições.

Antes de importar código, preservar os avisos de licença e a lista de atribuições de cada ativo. Este documento não afirma que a aplicação completa já foi portada ou que todas as funções estão implementadas.

## Estado real de implementação

- [x] Catálogo web atual e busca/filtros existentes.
- [x] Ficha informativa do ArtCraft Launcher com links para o upstream.
- [x] Documentação e validação do catálogo.
- [ ] Importar e adaptar o código nativo Rust para o Decode Launcher.
- [ ] Substituir a identidade visual upstream por ativos Decode.
- [ ] Implementar e testar o fluxo nativo de download, checksum, instalação, detecção e atualização.
- [ ] Implementar menu de bandeja, notificações e atualização do próprio launcher.
- [ ] Portar e testar a versão WebAssembly/catalog-only.
- [ ] Completar testes por sistema operacional e pipeline de releases.

A aplicação só deve ser apresentada como launcher funcional depois que as caixas pendentes forem implementadas e verificadas por CI e testes de uso real.
