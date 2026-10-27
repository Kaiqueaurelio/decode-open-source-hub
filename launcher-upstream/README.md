# Upstream launcher reference

This directory is reserved for a tracked integration of the upstream launcher from
[`storytold/craft-launcher`](https://github.com/storytold/craft-launcher).

## Integration status

The repository's adapted Decode launcher remains under `launcher/`. Do not overwrite
that directory with upstream files automatically: it has Decode-specific package names,
identifiers, assets, branding and suite configuration.

Upstream project metadata, feature inventory and licensing information must remain discoverable
here as the integration is completed. Upstream MIT/Apache-2.0 notices and all required third-party
attributions must be retained for any source or binary redistributed from that project.

## Upstream feature areas to port/adapt

- Catalog metadata, release lookup and version/status handling.
- Native install/update/remove flows, package selection by OS/architecture, checksum verification.
- Desktop UI, grid/table views, app detail pages, search, filters, tray/menu-bar integration.
- Browser/WASM catalog client.
- Localization and accessibility support.
- Platform-specific packaging and release CI.
- Tests for release parsing, package selection, install records, locale/UI, and platform behavior.

## Source

- Repository: https://github.com/storytold/craft-launcher
- Upstream main tree: https://github.com/storytold/craft-launcher/tree/main
- Imported/ported code must keep applicable source headers, licenses, notices and attribution files.
- ArtCraft trademarks and brand assets are not covered by MIT/Apache-2.0; use Decode brand assets instead.

This note is not a claim that the upstream application has been fully vendored or that the Decode
launcher is feature-complete. Use CI and platform builds to verify every integration step.
