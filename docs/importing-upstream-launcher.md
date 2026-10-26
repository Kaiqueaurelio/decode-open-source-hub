# Importing the upstream launcher

The launcher source lives in `launcher/` after running:

```bash
bash scripts/import_upstream_launcher.sh
```

The script clones the public `storytold/craft-launcher` repository into a new `launcher/` directory, includes binary assets, removes the nested Git metadata, and performs a first-pass replacement of visible branding. It intentionally preserves `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`, and `ATTRIBUTION.md`.

## Important limitations

- This is a reproducible import script; it does **not** mean the source has already been imported or tested.
- The upstream project has native Rust, a WASM web build, OS-specific installers, icons/fonts, and packaging workflows. All of these need to be audited after import.
- Brand substitutions are only a first pass. Check all window titles, tray labels, notifications, screenshots, SVG/PNG icons, package identifiers, application IDs, URLs, release feeds, installer metadata and tests.
- Keep upstream copyright/license/third-party notices. Replace ArtCraft trademarks and artwork in the product itself; do not remove legally required notices.
- Do not publish installers until CI passes and install/update/uninstall flows are tested on each supported OS.
- The upstream app is early alpha; importing its code does not remove its limitations or guarantee that every supported target builds in this repository.

## Upstream

- Source: https://github.com/storytold/craft-launcher
- License files and notices are kept with the imported source.
- Feature parity checklist: [Decode Launcher parity](decode-launcher-parity.md)
