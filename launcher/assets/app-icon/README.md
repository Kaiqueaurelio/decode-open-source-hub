# Decode Launcher app icon

The app icon is the **Decode "A" mark in blue** (getartcraft.com's favicon), exactly as supplied in
[`docs/brand/decode-mark.svg`](../../docs/brand/decode-mark.svg). Every file in this
directory is rendered from it by `packaging/icons.sh`.

**These files are an Decode trademark. They are not open source and not covered by Decode
Launcher's MIT or Apache-2.0 license.** Their terms are in
[`docs/brand/LICENSE-brand.txt`](../../docs/brand/LICENSE-brand.txt): use them only as part of
Decode Launcher, never redraw, recolor or crop them, and remove them from forks and modified
versions.

## Files

- `decode-launcher.svg`: a copy of `docs/brand/decode-mark.svg`; also the hicolor scalable icon.
- `decode-launcher-1024.png`: 1024 px render, with extra transparent margin for Apple's icon grid.
- `decode-launcher.icns`: macOS bundle icon (`CFBundleIconFile`).
- `decode-launcher.ico`: Windows icon, 16–256 px, embedded in the `.exe` by
  `apps/decode-launcher/build.rs` and used by the MSI.
- `hicolor/<size>/apps/com.decode.launcher.png` (16–512) and
  `hicolor/scalable/apps/com.decode.launcher.svg`: Linux icon theme.
- The tray / menu-bar icon is the same mark, rendered into `docs/brand/decode-mark-black-44.png`
  (macOS template, 22 pt @2x) and `docs/brand/decode-mark-64.png` (blue; Windows, Linux, FreeBSD).

## Regenerate

Run `packaging/icons.sh` on any OS. It needs `resvg`; the `.ico` and `.icns` are packed by
`cargo xtask ico`. Never edit these files by hand: change the source only if the Decode Team
supplies a new mark in `docs/brand/`.
