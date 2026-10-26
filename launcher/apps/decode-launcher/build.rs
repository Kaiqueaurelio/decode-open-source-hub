//! Windows only: embed the app icon and version info (VERSIONINFO) into `decode-launcher.exe`.
//!
//! On every other target this does nothing. A missing resource compiler is a warning, so a
//! cross-compile from macOS or Linux still links, unless `DECODE_LAUNCHER_REQUIRE_WINRES=1` (set
//! by the release packaging) turns it into an error.

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-changed=../../assets/app-icon/decode-launcher.ico");
    println!("cargo:rerun-if-env-changed=DECODE_LAUNCHER_REQUIRE_WINRES");
    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() != Ok("windows") {
        return;
    }
    let mut res = winresource::WindowsResource::new();
    res.set_icon("../../assets/app-icon/decode-launcher.ico")
        .set("ProductName", "Decode Launcher")
        .set("FileDescription", "Decode Launcher")
        .set("CompanyName", "Learning Machines LLC")
        .set("LegalCopyright", "Copyright (c) the Decode Launcher authors. MIT OR Apache-2.0.")
        .set("OriginalFilename", "decode-launcher.exe")
        .set("InternalName", "decode-launcher");
    if let Err(e) = res.compile() {
        if std::env::var_os("DECODE_LAUNCHER_REQUIRE_WINRES").is_some() {
            println!("cargo:warning=embedding Windows resources failed: {e}");
            std::process::exit(1);
        }
        println!("cargo:warning=decode-launcher.exe built without icon/version resources: {e}");
    }
}
