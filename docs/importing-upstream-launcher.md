# Importação e sincronização do Launcher

O código-fonte do launcher está localizado no diretório `launcher/`. Para atualizar ou ressincronizar com os padrões de referência upstream:

```bash
bash scripts/import_upstream_launcher.sh
```

O script clona a estrutura de referência, preserva os ativos binários, remove metadados git aninhados e aplica as substituições de identidade e marca Decode, mantendo intactos os arquivos de licença e conformidade (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` e `ATTRIBUTION.md`).

## Diretrizes importantes

- O código-fonte do launcher é em Rust nativo, possuindo suporte a compilação web em WebAssembly (WASM), instaladores para múltiplos sistemas operacionais (Windows, macOS, Linux, FreeBSD) e workflows de empacotamento.
- Todas as substituições de marca devem preservar títulos de janela, rótulos de bandeja, notificações, ícones SVG/PNG, identificadores de pacotes e suíte de testes.
- Mantenha sempre os avisos legais e de licença de terceiros exigidos.
- Os testes contínuos (`cargo xtask ci` e GitHub Actions) devem permanecer verdes antes de qualquer publicação de release.

## Referências técnicas

- Código integrado: diretório `launcher/`
- Checklist e matriz de paridade: [Matriz de Paridade do Decode Launcher](decode-launcher-parity.md)
