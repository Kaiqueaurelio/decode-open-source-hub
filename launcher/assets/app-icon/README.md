# Ícone do aplicativo Decode Launcher

O ícone do aplicativo é o símbolo oficial **Decode em azul e ciano**, fornecido em
[`docs/brand/decode-mark.svg`](../../docs/brand/decode-mark.svg). Todos os arquivos nesta
pasta são gerados a partir dele através de `packaging/icons.sh`.

## Arquivos

- `decode-launcher.svg`: cópia de `docs/brand/decode-mark.svg`; ícone vetorial escalável para temas hicolor.
- `decode-launcher-1024.png`: renderização de 1024 px com margem transparente para as diretrizes de ícones do macOS.
- `decode-launcher.icns`: pacote de ícones para o bundle do macOS (`CFBundleIconFile`).
- `decode-launcher.ico`: ícone do Windows (16 a 256 px), embutido no `.exe` por
  `apps/decode-launcher/build.rs` e utilizado pelo instalador MSI.
- `hicolor/<tamanho>/apps/com.decode.launcher.png` (16–512) e
  `hicolor/scalable/apps/com.decode.launcher.svg`: tema de ícones padrão para distribuições Linux.
- O ícone da bandeja / barra de tarefas utiliza o mesmo símbolo renderizado em `docs/brand/decode-mark-black-44.png`
  (máscara para macOS) e `docs/brand/decode-mark-64.png` (colorido para Windows, Linux e FreeBSD).

## Como regenerar

Execute `packaging/icons.sh` em qualquer sistema operacional compatível (requer `resvg` e `cargo xtask ico`).
