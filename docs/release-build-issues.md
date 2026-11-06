# Release build notes

## Linux PdfCraft

The latest observed Linux build failure was `Build pdfcraft (Linux x86_64)` in workflow run
`42155623273` (job `127693749949`). Compilation reached the packaging step, where PdfCraft's
`cargo xtask models` fetch received HTTP 403 from the upstream OCR model URL
`https://ocrs-models.s3-accelerate.amazonaws.com/text-detection.rten`.

The model URLs and SHA-256 digests are recorded in `apps/decode-pdf/ATTRIBUTION.toml` and
verified by the project's asset tooling. This repository does not control the S3 bucket, and the
checksum alone does not identify an authorized mirror. The workflow therefore reports PdfCraft as
failed while allowing other successful app packages to be published. Restoring the full Linux
PdfCraft build requires the model owner to restore public access or provide an authorized stable
mirror containing byte-identical files.

Earlier Linux packaging failures for the Craft apps came from the absent `CRAFT_FONTS_DIR`
checkout. The workflow now checks out `storytold/craft-fonts` at commit
`b076417b5880bd4154bd22f00695b1d28c6bea83` and supplies that pinned path to the package scripts.

## Manual Launcher installation checklist

The automated native test covers installation and removal of a verified Linux tarball in a
custom folder. For a release smoke test, use a disposable Linux account or VM:

1. Open the Launcher and choose an app with a Linux tar.gz in the release.
2. Select a writable custom install folder and install. Confirm the app appears under
   `<chosen-folder>/<app-id>/` and launches from the Launcher.
3. Update the app and confirm user data in its `home/` directory remains intact.
4. Uninstall and confirm only Launcher-managed `bin/` and `share/` files are removed.
5. Repeat with a test release manifest that omits both AppImage and tar.gz; confirm the error names
   the app, version, Linux platform, and release page.
6. Repeat with a changed checksum and confirm installation stops before extraction.

Windows and macOS installations are not modified by the Linux tarball fallback.
