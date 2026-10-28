//! The Decode App Suite: the thirteen apps the launcher knows about.
//!
//! The list is data so a later version can fetch it from an API; [`SUITE`] is the built-in copy.
//!
//! Text here is English, the source the UI translates from: each `tagline` has a catalog row
//! keyed by the app id (`tr_ctx(app.id, app.tagline)` in `ui-egui`).

/// One app in the suite.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct DecodeApp {
    /// Machine name: repo, binary, package and asset stem (`photocraft`).
    pub id: &'static str,
    /// Display name (`DecodePhoto`).
    pub name: &'static str,
    /// What it's for, in a few words (English; the UI translates it by app id).
    pub tagline: &'static str,
    /// Brand colour (sRGB), for surfaces: decode-open-source-hub.vercel.app's `--app`.
    pub color: [u8; 3],
    /// The brand colour for text on a light background (the site's light `--app-ink`).
    pub ink_light: [u8; 3],
    /// The brand colour for text on a dark background (the site's dark `--app-ink`).
    pub ink_dark: [u8; 3],
    /// GitHub `owner/repo`.
    pub repo: &'static str,
    /// Older names its release assets may carry (DecodePdf shipped as DecodePrint until 0.2.1).
    pub former_ids: &'static [&'static str],
    /// Older display names its installers registered (DecodePdf's MSI said DecodePrint until 0.2.1).
    pub former_names: &'static [&'static str],
}

impl DecodeApp {
    /// `com.decode.<id>`: macOS bundle id, Flatpak id and Linux desktop-file id.
    pub fn bundle_id(&self) -> String {
        format!("com.decode.{}", self.id)
    }

    pub fn releases_url(&self) -> String {
        format!("https://github.com/{}/releases", self.repo)
    }

    pub fn repo_url(&self) -> String {
        format!("https://github.com/{}", self.repo)
    }

    /// The app's page on decode-open-source-hub.vercel.app.
    pub fn website(&self) -> String {
        format!("https://decode-open-source-hub.vercel.app/#{}", self.id)
    }

    /// Asset stems this app's releases may use, current first.
    pub fn stems(&self) -> impl Iterator<Item = &'static str> + '_ {
        std::iter::once(self.id).chain(self.former_ids.iter().copied())
    }

    /// Display names this app's installers may have registered, current first.
    pub fn names(&self) -> impl Iterator<Item = &'static str> + '_ {
        std::iter::once(self.name).chain(self.former_names.iter().copied())
    }

    pub fn by_id(id: &str) -> Option<&'static DecodeApp> {
        SUITE.iter().find(|a| a.id == id)
    }
}

const fn app(
    id: &'static str,
    name: &'static str,
    tagline: &'static str,
    [color, ink_light, ink_dark]: [[u8; 3]; 3],
    repo: &'static str,
) -> DecodeApp {
    DecodeApp { id, name, tagline, color, ink_light, ink_dark, repo, former_ids: &[], former_names: &[] }
}

/// The Decode App Suite, in display order matching decode-open-source-hub.vercel.app:
pub const SUITE: [DecodeApp; 13] = [
    DecodeApp {
        former_names: &["PhotoCraft"],
        ..app("photocraft", "DecodePhoto", "Image editing", [[0x2f, 0x7b, 0xf5], [0x1a, 0x5b, 0xc4], [0x7f, 0xb0, 0xff]], "Kaiqueaurelio/decode-open-source-hub")
    },
    DecodeApp {
        former_names: &["VectorCraft"],
        ..app(
            "vectorcraft",
            "DecodeVector",
            "Vector illustration",
            [[0xe8, 0x57, 0x3f], [0xb8, 0x3a, 0x24], [0xff, 0x8a, 0x70]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["FilmCraft"],
        ..app(
            "filmcraft",
            "DecodeFilm",
            "Video editing, color and sound",
            [[0x8b, 0x5c, 0xf6], [0x6a, 0x3f, 0xd6], [0xb6, 0x9c, 0xff]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["LightCraft"],
        ..app(
            "lightcraft",
            "DecodeLight",
            "Photo library and raw development",
            [[0xf2, 0xa5, 0x16], [0x8a, 0x58, 0x00], [0xff, 0xc1, 0x4d]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_ids: &["printcraft"],
        former_names: &["PdfCraft", "PrintCraft"],
        ..app(
            "pdfcraft",
            "DecodePdf",
            "Reading, organizing and protecting PDFs",
            [[0x12, 0xa5, 0x8a], [0x0a, 0x75, 0x63], [0x3f, 0xd6, 0xb8]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["EffectCraft"],
        ..app(
            "effectcraft",
            "DecodeEffect",
            "Motion graphics and visual effects",
            [[0xe0, 0x36, 0x8f], [0xb0, 0x20, 0x6c], [0xff, 0x7a, 0xb8]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["DesignCraft"],
        ..app(
            "designcraft",
            "DecodeDesign",
            "Page layout and publishing",
            [[0x7b, 0xb5, 0x1c], [0x45, 0x70, 0x08], [0xa6, 0xe0, 0x4a]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["FigCraft"],
        ..app(
            "figcraft",
            "DecodeFig",
            "Interface design and prototyping",
            [[0x02, 0xda, 0x96], [0x04, 0x7a, 0x56], [0x4f, 0xe8, 0xb6]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["WordCraft"],
        ..app(
            "wordcraft",
            "DecodeWord",
            "Writing and document design",
            [[0x3f, 0x5f, 0xe0], [0x2a, 0x44, 0xb8], [0x8e, 0xa2, 0xff]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["SoundCraft"],
        ..app(
            "soundcraft",
            "DecodeSound",
            "Recording, editing and mixing audio",
            [[0x1f, 0xa5, 0xc9], [0x0e, 0x72, 0x90], [0x5f, 0xd0, 0xee]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["DeckCraft"],
        ..app(
            "deckcraft",
            "DecodeDeck",
            "Presentations and slide shows",
            [[0xf0, 0x7a, 0x1e], [0xa8, 0x4f, 0x0a], [0xff, 0xa0, 0x60]],
            "Kaiqueaurelio/decode-open-source-hub",
        )
    },
    DecodeApp {
        former_names: &["CADCraft"],
        ..app(
            "cadcraft",
            "DecodeCAD",
            "Computer-aided design and drafting",
            [[0x3e, 0xa6, 0xe8], [0x1a, 0x6f, 0xa8], [0x7c, 0xc8, 0xff]],
            "Kaiqueaurelio/decodecad",
        )
    },
    DecodeApp {
        former_names: &["GridCraft"],
        ..app("gridcraft", "DecodeGrid", "Spreadsheets and data", [[0x1f, 0x9d, 0x55], [0x12, 0x70, 0x3a], [0x4f, 0xd6, 0x8a]], "Kaiqueaurelio/decode-open-source-hub")
    },
];

/// Decode's website.
pub const WEBSITE_URL: &str = "https://kaiqueaurelio.github.io/decode-open-source-hub/";
/// The GitHub account every Decode App's repository lives under: the only one the launcher
/// installs from, whatever the release feed says.
pub const GITHUB_OWNER: &str = "Kaiqueaurelio";
/// Decode on GitHub: every Decode App's source.
pub const GITHUB_URL: &str = "https://github.com/Kaiqueaurelio/decode-open-source-hub";
/// Decode's social accounts: (service, URL). Shown as small icons, less prominent than Discord.
pub const SOCIAL: [(&str, &str); 5] = [
    ("X", "https://x.com/decoanalytics"),
    ("Instagram", "https://www.instagram.com/decode.analytics/"),
    ("LinkedIn", "https://www.linkedin.com/company/decodeanalytics"),
    ("YouTube", "https://www.youtube.com/@OfficialArtcraftStudios"),
    ("TikTok", "https://www.tiktok.com/@decode.analytics"),
];

/// The Decode community on Discord.
pub const DISCORD_URL: &str = "https://github.com/Kaiqueaurelio/decode-open-source-hub/discussions";
/// Deep link into the Discord application for the Decode server invite.
pub const DISCORD_APP_URL: &str = "discord://-/invite/artcraft";

/// Decode Launcher itself, described like a Decode App so it can update itself with the same
/// machinery (asset names `decode-launcher-<ver>-…`, bundle id `com.decode.launcher`,
/// `Decode Launcher.app`). Not part of [`SUITE`].
pub const LAUNCHER: DecodeApp = DecodeApp {
    former_ids: &["artcraft-launcher"],
    former_names: &["ArtCraft Launcher"],
    ..app(
        "decode-launcher",
        "Decode Launcher",
        "Installs and updates the Decode App Suite",
        [[0x0b, 0x0b, 0x0c], [0x0b, 0x0b, 0x0c], [0xf2, 0xf1, 0xee]],
        "Kaiqueaurelio/craft-launcher",
    )
};

/// The launcher's own repo, checked so it can say when a newer launcher is out.
pub const LAUNCHER_REPO: &str = "Kaiqueaurelio/craft-launcher";
/// The launcher's own asset stem.
pub const LAUNCHER_ID: &str = "decode-launcher";

/// A Decode App's 128 px icon (PNG), as copied from its repo into `assets/app-icons`: the UI
/// draws it, and the Linux install puts it in the desktop menu.
pub fn app_icon_png(id: &str) -> Option<&'static [u8]> {
    Some(match id {
        "photocraft" => include_bytes!("../../../assets/app-icons/photocraft.png"),
        "vectorcraft" => include_bytes!("../../../assets/app-icons/vectorcraft.png"),
        "filmcraft" => include_bytes!("../../../assets/app-icons/filmcraft.png"),
        "lightcraft" => include_bytes!("../../../assets/app-icons/lightcraft.png"),
        "pdfcraft" => include_bytes!("../../../assets/app-icons/pdfcraft.png"),
        "effectcraft" => include_bytes!("../../../assets/app-icons/effectcraft.png"),
        "designcraft" => include_bytes!("../../../assets/app-icons/designcraft.png"),
        "wordcraft" => include_bytes!("../../../assets/app-icons/wordcraft.png"),
        "deckcraft" => include_bytes!("../../../assets/app-icons/deckcraft.png"),
        "gridcraft" => include_bytes!("../../../assets/app-icons/gridcraft.png"),
        "cadcraft" => include_bytes!("../../../assets/app-icons/cadcraft.png"),
        "soundcraft" => include_bytes!("../../../assets/app-icons/soundcraft.png"),
        "figcraft" => include_bytes!("../../../assets/app-icons/figcraft.png"),
        _ => return None,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn every_app_has_its_icon() {
        for app in &SUITE {
            let png = app_icon_png(app.id).unwrap_or_else(|| panic!("no icon for {}", app.id));
            assert!(png.starts_with(b"\x89PNG\r\n\x1a\n"), "{} icon isn't a PNG", app.id);
        }
        assert!(app_icon_png("notacraft").is_none());
    }

    #[test]
    fn suite_has_thirteen_apps_with_unique_ids() {
        assert_eq!(SUITE.len(), 13);
        let mut ids: Vec<_> = SUITE.iter().map(|a| a.id).collect();
        ids.sort_unstable();
        ids.dedup();
        assert_eq!(ids.len(), SUITE.len());
        for a in &SUITE {
            if a.id == "cadcraft" {
                assert_eq!(a.repo, "Kaiqueaurelio/decodecad");
            } else {
                assert_eq!(a.repo, format!("Kaiqueaurelio/{}", a.id));
            }
            assert_eq!(a.name.to_lowercase().replace("decode", "") + "craft", a.id);
        }
    }

    #[test]
    fn pdfcraft_also_answers_to_printcraft() {
        let pdf = DecodeApp::by_id("pdfcraft").unwrap();
        assert_eq!(pdf.stems().collect::<Vec<_>>(), ["pdfcraft", "printcraft"]);
        assert_eq!(pdf.names().collect::<Vec<_>>(), ["DecodePdf", "PdfCraft", "PrintCraft"]);
        assert_eq!(pdf.website(), "https://decode-open-source-hub.vercel.app/#pdfcraft");
        assert_eq!(DecodeApp::by_id("wordcraft").unwrap().website(), "https://decode-open-source-hub.vercel.app/#wordcraft");
    }
}
