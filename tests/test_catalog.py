"""Tests for the Decode App Suite and separate launcher entry in Decode Monorepo."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "software.json"
EXPECTED_ORDER = [
    "photocraft", "vectorcraft", "filmcraft", "lightcraft", "pdfcraft",
    "effectcraft", "designcraft", "figcraft", "wordcraft", "soundcraft",
    "deckcraft", "cadcraft", "gridcraft",
]
EXPECTED_NAMES = {
    "photocraft":"DecodePhoto", "vectorcraft":"DecodeVector", "filmcraft":"DecodeFilm",
    "lightcraft":"DecodeLight", "pdfcraft":"DecodePdf", "effectcraft":"DecodeEffect",
    "designcraft":"DecodeDesign", "figcraft":"DecodeFig", "wordcraft":"DecodeWord",
    "soundcraft":"DecodeSound", "deckcraft":"DecodeDeck", "cadcraft":"DecodeCAD",
    "gridcraft":"DecodeGrid",
}
SLUG_TO_APP_DIR = {
    "photocraft": "decode-photo",
    "vectorcraft": "decode-vector",
    "filmcraft": "decode-film",
    "lightcraft": "decode-light",
    "pdfcraft": "decode-pdf",
    "effectcraft": "decode-effect",
    "designcraft": "decode-design",
    "figcraft": "decode-fig",
    "wordcraft": "decode-word",
    "soundcraft": "decode-sound",
    "deckcraft": "decode-deck",
    "cadcraft": "decode-cad",
    "gridcraft": "decode-grid",
}

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads(DATA.read_text(encoding="utf-8"))
        cls.by_slug = {item["slug"]: item for item in cls.items}

    def test_contains_13_decode_apps_and_one_separate_launcher(self):
        self.assertEqual(len(self.items), 14)
        self.assertEqual([item["slug"] for item in self.items], EXPECTED_ORDER + ["artcraft-launcher"])
        apps = [item for item in self.items if item["kind"] == "Aplicativo Decode"]
        self.assertEqual([item["slug"] for item in apps], EXPECTED_ORDER)
        self.assertEqual({item["slug"]: item["name"] for item in apps}, EXPECTED_NAMES)
        upstream_search_names = {
            "photocraft":"PhotoCraft", "vectorcraft":"VectorCraft", "filmcraft":"FilmCraft",
            "lightcraft":"LightCraft", "pdfcraft":"PdfCraft", "effectcraft":"EffectCraft",
            "designcraft":"DesignCraft", "figcraft":"FigCraft", "wordcraft":"WordCraft",
            "soundcraft":"SoundCraft", "deckcraft":"DeckCraft", "cadcraft":"CADCraft",
            "gridcraft":"GridCraft",
        }
        for item in apps:
            self.assertIn(upstream_search_names[item["slug"]], item["tags"])
        self.assertEqual(self.by_slug["artcraft-launcher"]["kind"], "Launcher")
        self.assertEqual(self.by_slug["artcraft-launcher"]["name"], "Decode Launcher")
        self.assertIn("ArtCraft Launcher", self.by_slug["artcraft-launcher"]["tags"])

    def test_slugs_and_names_are_unique(self):
        self.assertEqual(len({item["slug"] for item in self.items}), len(self.items))
        self.assertEqual(len({item["name"].casefold() for item in self.items}), len(self.items))

    def test_official_app_source_links(self):
        for slug in EXPECTED_ORDER:
            item = self.by_slug[slug]
            with self.subTest(app=item["name"]):
                app_dir = SLUG_TO_APP_DIR[slug]
                self.assertEqual(item["sourceUrl"], f"https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/apps/{app_dir}")
                self.assertEqual(item["licenseUrl"], f"https://github.com/Kaiqueaurelio/decode-open-source-hub/blob/main/apps/{app_dir}/LICENSE-MIT")
                self.assertEqual(item["websiteUrl"], "https://decode-open-source-hub-catalog.vercel.app")
                self.assertEqual(item["downloadUrl"], "https://github.com/Kaiqueaurelio/decode-open-source-hub/releases")
                self.assertEqual(item["license"], "MIT OR Apache-2.0")

    def test_launcher_links_and_disclosure(self):
        item = self.by_slug["artcraft-launcher"]
        self.assertEqual(item["sourceUrl"], "https://github.com/Kaiqueaurelio/decode-open-source-hub/tree/main/launcher")
        self.assertEqual(item["downloadUrl"], "https://github.com/Kaiqueaurelio/decode-open-source-hub/releases")
        self.assertEqual(item["licenseUrl"], "https://github.com/Kaiqueaurelio/decode-open-source-hub/blob/main/launcher/LICENSE-MIT")
        self.assertEqual(item["license"], "MIT OR Apache-2.0")
        self.assertIn("early alpha", item["description"])
        for key in ("licenseUrl","websiteUrl","sourceUrl","downloadUrl"):
            parsed = urlparse(item[key])
            self.assertEqual(parsed.scheme, "https")
            self.assertTrue(parsed.netloc)

    def test_stage_platforms_and_tags(self):
        for item in self.items:
            with self.subTest(app=item["name"]):
                self.assertTrue(item["stage"].strip())
                self.assertTrue(item["platforms"])
                self.assertEqual(len(item["platforms"]), len(set(item["platforms"])))
                self.assertTrue(all(isinstance(tag, str) and tag.strip() for tag in item["tags"]))

    def test_launcher_style_ui_controls_are_present(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "app.js").read_text(encoding="utf-8")
        stylesheet = (ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertIn('id="view-grid"', page)
        self.assertIn('id="view-table"', page)
        self.assertIn('id="status-tabs"', page)
        self.assertIn('id="reload-catalog"', page)
        self.assertIn('og:title" content="Decode Launcher — Open Source App Suite"', page)
        self.assertIn("function setView(", script)
        self.assertIn("function renderStatusTabs(", script)
        self.assertIn("assets/app-icons/", script)
        self.assertIn(".software-grid.table-view", stylesheet)
        self.assertIn(".status-tab", stylesheet)

    def test_root_readme_documents_imported_launcher_source(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("launcher/", readme)
        self.assertIn("cargo test --workspace --locked", readme)
        self.assertNotIn("o código do launcher nativo ainda não foi importado", readme.lower())

    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_catalog.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

if __name__ == "__main__":
    unittest.main()
