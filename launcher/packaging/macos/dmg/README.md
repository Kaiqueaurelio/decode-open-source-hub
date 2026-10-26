# Janela do instalador DMG para macOS

Apresentação visual exibida pelo Finder ao abrir o arquivo DMG: uma tela de fundo de 660 × 400 pt com o ícone do Decode Launcher e o atalho da pasta `Applications` lado a lado. O script `package.sh` inclui esses arquivos na imagem durante a compilação.

| Arquivo | Descrição |
|---|---|
| `background.svg` | Arte vetorial do plano de fundo com o símbolo Decode |
| `background.tiff` | Imagem renderizada em 1x e 2x (HiDPI) com paleta otimizada |
| `dmg-layout.DS_Store` | Configurações de layout do Finder: dimensões da janela, tamanho dos ícones e posições |
| `generate.py` | Script que gera `background.tiff` e `dmg-layout.DS_Store` a partir do SVG |

## Nome do volume

O volume montado é nomeado `Decode Launcher`. O layout aponta para a imagem de fundo através de um alias vinculado a esse nome exato. O nome do arquivo DMG (`decode-launcher-<versão>-macos-<arch>.dmg`) contém o número da versão.

## Como regenerar

Após editar `background.svg` ou as constantes de layout em `generate.py`, execute:

```sh
pip install 'pillow>=12' ds_store==1.3.3 mac_alias==2.2.3
python3 packaging/macos/dmg/generate.py
```
