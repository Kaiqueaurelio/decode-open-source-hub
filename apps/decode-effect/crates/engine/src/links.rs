//! Community and project links (shown in Help ▸, the About dialog, the start screen and the
//! header's Discord button).

pub const APP_NAME: &str = "EffectCraft";
pub const APP_SLUG: &str = "effectcraft";
pub const DISCORD: &str = "https://discord.gg/artcraft";
pub const WEBSITE: &str = "https://decode-open-source-hub.vercel.app";
pub const APP_PAGE: &str = "https://decode-open-source-hub.vercel.app/#effectcraft";
pub const GITHUB: &str = "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps/effectcraft";
pub const ISSUES: &str = "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps/effectcraft/issues";

/// Sibling apps of the ArtCraft family: (name, what it is, GitHub repo, app page).
pub const SIBLINGS: &[(&str, &str)] = &[
    ("PhotoCraft", "photocraft"),
    ("VectorCraft", "vectorcraft"),
    ("FilmCraft", "filmcraft"),
    ("LightCraft", "lightcraft"),
    ("PdfCraft", "pdfcraft"),
    ("DesignCraft", "designcraft"),
];

pub fn github_of(slug: &str) -> String {
    format!("https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps/{slug}")
}
pub fn page_of(slug: &str) -> String {
    format!("https://decode-open-source-hub.vercel.app/#{slug}")
}
