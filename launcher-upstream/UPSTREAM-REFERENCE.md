# Upstream launcher capability reference

Source repository: https://github.com/Kaiqueaurelio/decode-open-source-hub
Source branch: main
Source revision inspected: 7aafad661a11594a70ae949471d481f30d8fe64a

This is a capability/reference document for porting and validating functionality in the Decode Launcher,
not a copy of the upstream source tree.

## Capabilities observed in the upstream repository

### Catalog and release metadata
- Built-in catalog of thirteen creative apps.
- Per-app source and release URLs, product identifiers, colors and names.
- Release metadata parsing, semver handling, platform/architecture matching, status/version reporting.
- Detailed information, screenshots and release-feed support.

### Native installation and updates
- Install, update, remove, and open apps through the desktop launcher.
- Select platform-native installer formats and portable packages.
- SHA-256 verification before installing packages.
- Records of installed apps, versions, package kind, install paths and files.
- Detection of apps already installed outside the launcher.
- Self-update support for the launcher itself.
- Queueing, process handling, proxy support, HTTP handling, single-instance guard, login/startup behavior.
- OS-aware paths, desktop entries, tray/menu-bar behavior and notifications.

### Desktop UI and accessibility
- Native Rust/egui desktop UI.
- Grid and sortable table views.
- App details, status and download actions.
- Settings, themes, motion preferences and platform integration.
- Accessibility support and UI regression tests.

### Browser client and localization
- Separate WASM/web entrypoint using the same core catalog and UI.
- Localized interface in English, Brazilian Portuguese, Czech, French, German, Hungarian, Japanese,
  Polish, Russian, Simplified Chinese and Spanish.
- Locale detection, translation tests and fallback behavior.

### Build, release and distribution
- Rust workspace with core, native backend, UI crates, desktop/web binaries and xtask utilities.
- CI, release, packaging-lint, FreeBSD, Nix and Windows ARM64 workflows.
- Linux package/app bundle scripts, Flatpak/NFPM configurations, macOS packaging, Windows installer
  packaging, web packaging and image/icon generation tools.

## Decode integration rules

1. Keep all products branded with Decode names, IDs, icons, colors, links and identifiers.
2. Point release lookups to authorized Decode repositories/releases; never silently fetch upstream
   executables when a Decode build is expected.
3. Retain code attribution, copyright notices, MIT/Apache-2.0 license texts and third-party attribution
   for every imported component.
4. ArtCraft's trademark/brand files are expressly separate from its open-source code license and must
   not be reused as Decode branding.
5. Do not represent a feature as implemented until corresponding code and tests exist and CI/builds pass.

## Source snapshot status

The upstream source snapshot is stored under `launcher-upstream/source/` as a **non-buildable reference subtree**. It contains the upstream Cargo workspace, source for the core/native/UI crates, desktop and web entry points, tests, localization tables, release/packaging scripts, CI workflows, and the upstream README/NOTICE/license files. Branding-specific ArtCraft assets and app icon PNGs are intentionally omitted. A source attribution is present in `launcher-upstream/source/ATTRIBUTION.md`.

The source subtree is not wired into the live Decode launcher and its code has not been compiled here. It uses upstream package names and upstream release repositories. Treat it as an audit/porting baseline, not a claim of feature parity in `launcher/`. Integrate or cherry-pick behavior into the Decode names, release feeds, package IDs, branding and license obligations, then run the relevant CI and platform builds before claiming completion.
