# Hospedagem do Decode Launcher para a Web

O arquivo `decode-launcher-web-<versão>.zip` (gerado a partir da release do GitHub ou por `packaging/web/package.sh`)
contém um site estático na pasta `decode-launcher-web-<versão>/`:

| Arquivo | Descrição |
|---|---|
| `index.html` | Página principal que carrega os recursos através de URLs relativas |
| `decode-launcher-web-<hash>.js` | Cola gerada pelo wasm-bindgen (módulo ES) |
| `decode-launcher-web-<hash>_bg.wasm` | A aplicação compilada (egui em WebAssembly com perfil `wasm-release`) |
| `_headers`, `.htaccess` | Regras de cabeçalho de exemplo para Netlify, Cloudflare Pages e Apache |

Não há código do lado do servidor (backend) ou dependências de Node.js. O conteúdo pode ser publicado diretamente em qualquer servidor web ou CDN de arquivos estáticos.

## Funcionamento da versão web

No navegador, o launcher opera em modo de catálogo e descoberta: exibe toda a Decode App Suite, a versão mais recente de cada aplicativo e os botões de download direto para a plataforma do visitante. Os dados de lançamento são obtidos diretamente via API do GitHub (`api.github.com`).

## Compatibilidade de caminhos e URLs

Todas as referências no `index.html` utilizam caminhos relativos (`public_url = "./"` em `apps/decode-launcher-web/Trunk.toml`). Portanto, o catálogo web funciona tanto na raiz de um domínio (`https://exemplo.com/`) quanto em subpastas (`https://exemplo.com/apps/launcher/`).

## Configurações recomendadas do servidor

- **MIME type:** sirva arquivos `.wasm` com o tipo `application/wasm` e `.js` com `text/javascript`.
- **Compressão:** habilite gzip ou Brotli para `.wasm`, `.js` e `.html`.
- **Cache:** utilize cabeçalhos imutáveis para arquivos com hash no nome (`Cache-Control: public, max-age=31536000, immutable`) e `no-cache` para o `index.html`.
- **Content Security Policy (CSP):** permita `connect-src https://api.github.com https://raw.githubusercontent.com` e `'wasm-unsafe-eval'` em `script-src`.

## Teste local

Para testar localmente, execute no diretório gerado:

```sh
python3 -m http.server 8765
```

Em seguida, acesse [http://localhost:8765/](http://localhost:8765/).
