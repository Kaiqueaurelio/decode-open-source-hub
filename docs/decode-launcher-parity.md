# Decode Launcher — Matriz de Paridade Funcional

## Objetivo do produto

O **Decode Launcher** é a aplicação oficial da comunidade Decode para gerenciar, instalar e manter atualizada a suíte de aplicativos criativos de código aberto, combinando alto desempenho em Rust com identidade visual e experiência unificada.

## Requisitos funcionais e especificações

| Área | Comportamento esperado | Verificação de aceite |
|---|---|---|
| Catálogo | Exibir os 13 apps da Decode App Suite e os dados oficiais de cada release | Lista completa, estados vazios e tratamento defensivo de erros de API |
| Detecção de sistema | Identificar sistema operacional e arquitetura para sugerir o pacote correto | Casos Linux x86_64/aarch64, Windows x64/ARM64/x86, macOS e plataformas suportadas |
| Releases | Consultar releases oficiais e interpretar versões, arquivos e notas | Fixtures reais e respostas malformadas cobertas por testes automatizados |
| Instalação | Baixar o pacote compatível, exibir progresso e pedir confirmação quando necessário | Diálogo claro para o usuário; falhas e cancelamentos recuperáveis |
| Integridade | Validar hash SHA-256 do arquivo antes de instalar ou executar | Arquivo alterado ou checksum ausente/inválido é bloqueado imediatamente |
| Aplicativos existentes | Detectar aplicativos instalados manualmente e por outros gerenciadores | App instalado fora do launcher aparece com estado e versão corretos |
| Inicialização | Abrir aplicativos instalados a partir da interface e do menu de bandeja | Tratamento e mensagens claras para apps ausentes |
| Atualizações | Verificar novas versões dos aplicativos instalados e emitir notificações | Não substituir um aplicativo enquanto estiver em execução |
| Atualização do Decode Launcher | Verificar e aplicar a própria atualização com conferência de integridade | Recuperação segura em erro, cancelamento e reinício transparente |
| Instalação por sistema | Usar formatos e caminhos nativos compatíveis com cada plataforma | Diretórios padrão do sistema (`/Applications`, `C:\Program Files`, `/usr/bin`) |
| Linux | Suporte a AppImage, DEB, RPM e Flatpak conforme a release | Permissões e limites de sandbox respeitados |
| Windows | Suporte a MSI e pacote portátil | Instalação por usuário, atalhos no menu Iniciar e dados portáteis |
| macOS | Suporte a DMG com build universal | Instalação com arraste para pasta Aplicativos |
| FreeBSD | Suporte a pacotes oficiais | Instalação em `/usr/local` com polkit |
| Versão web | Oferecer catálogo e downloads recomendados no navegador via WebAssembly | Operação estática sem backend adicional |
| Idiomas | Suporte nativo a Português do Brasil e múltiplos idiomas | Strings com fallback e preferência persistida entre sessões |
| Preferências | Configurações de idioma, atualização e aparência persistentes | Configurações armazenadas localmente com segurança |
| Diagnóstico | Logs rotacionados gravados na pasta de dados do sistema | `logs/decode-launcher.log` com níveis configuráveis via `RUST_LOG` |
| Segurança | HTTPS exclusivo, validação de URLs e ausência de execução cega de instaladores | Validação prévia de integridade em todas as operações |
| CI e qualidade | Formatação (`cargo fmt`), lint (`clippy`), testes nativos e compilação WASM | Integração contínua (CI) verde em todos os commits |

## Identidade visual Decode

- Nome de produto: **Decode Launcher**.
- Marca, tipografia, ícones e esquemas de cores próprios da Decode.
- Todos os 13 aplicativos nomeados com o prefixo Decode (DecodePhoto, DecodeVector, DecodeFilm, DecodeLight, DecodePdf, DecodeEffect, DecodeDesign, DecodeFig, DecodeWord, DecodeSound, DecodeDeck, DecodeCAD, DecodeGrid).
- **DecodeCAD** integrado diretamente com o repositório [Kaiqueaurelio/decodecad](https://github.com/Kaiqueaurelio/decodecad).

## Estado de implementação

- [x] Catálogo web responsivo com busca instantânea e filtros por categoria/plataforma.
- [x] Código-fonte nativo em Rust do Decode Launcher integrado em `launcher/`.
- [x] Identidade visual Decode aplicada (logotipos em vetor, ícones de sistema e paleta de cores).
- [x] Integração completa do DecodeCAD com seu repositório oficial.
- [x] Implementação de verificação de integridade via SHA-256 para todos os downloads.
- [x] Suporte à internacionalização com Português do Brasil nativo.
- [x] Suíte de testes automatizados e integração contínua (GitHub Actions CI) passando com sucesso.
