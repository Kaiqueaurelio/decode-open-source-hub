"""Tests for the exact 13-app ArtCraft Craft App Suite catalog."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "software.json"
EXPECTED_ORDER = ["photocraft","vectorcraft","filmcraft","lightcraft","pdfcraft","effectcraft","designcraft","figcraft","wordcraft","soundcraft","deckcraft","cadcraft","gridcraft"]
EXPECTED = set(EXPECTED_ORDER)
EXPECTED_NAMES = {"photocraft":"PhotoDecode","vectorcraft":"VectorDecode","filmcraft":"FilmDecode","lightcraft":"LightDecode","pdfcraft":"PdfDecode","effectcraft":"EffectDecode","designcraft":"DesignDecode","figcraft":"FigDecode","wordcraft":"WordDecode","soundcraft":"SoundDecode","deckcraft":"DeckDecode","cadcraft":"CADDecode","gridcraft":"GridDecode"}


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads(DATA.read_text(encoding="utf-8"))

    def test_contains_exactly_the_apps_in_the_official_launcher_catalog(self):
        self.assertEqual(len(self.items), 13)
        self.assertEqual([item["slug"] for item in self.items], EXPECTED_ORDER)
        self.assertEqual({item["slug"] for item in self.items}, EXPECTED)
        self.assertTrue(all(item["kind"] == "Crafting App" for item in self.items))
        self.assertEqual({item["slug"]: item["name"] for item in self.items}, EXPECTED_NAMES)
        original_names = {"photocraft":"PhotoCraft","vectorcraft":"VectorCraft","filmcraft":"FilmCraft","lightcraft":"LightCraft","pdfcraft":"PdfCraft","effectcraft":"EffectCraft","designcraft":"DesignCraft","figcraft":"FigCraft","wordcraft":"WordCraft","soundcraft":"SoundCraft","deckcraft":"DeckCraft","cadcraft":"CADCraft","gridcraft":"GridCraft"}
        for item in self.items:
            self.assertIn(original_names[item["slug"]], item["tags"])
        self.assertNotIn("artcraft-studio", {item["slug"] for item in self.items})
        self.assertNotIn("craft-launcher", {item["slug"] for item in self.items})

    def test_slugs_and_names_are_unique(self):
        self.assertEqual(len({item["slug"] for item in self.items}), len(self.items))
        self.assertEqual(len({item["name"].casefold() for item in self.items}), len(self.items))

    def test_every_entry_links_to_its_official_project(self):
        for item in self.items:
            with self.subTest(app=item["name"]):
                slug = item["slug"]
                self.assertEqual(item["kind"], "Crafting App")
                self.assertEqual(item["sourceUrl"], f"https://github.com/storytold/{slug}")
                self.assertEqual(item["websiteUrl"], f"https://getartcraft.com/apps/{slug}")
                self.assertEqual(item["downloadUrl"], item["websiteUrl"])
                self.assertEqual(item["licenseUrl"], f"https://github.com/storytold/{slug}/blob/main/LICENSE-MIT")
                for key in ("licenseUrl", "websiteUrl", "sourceUrl", "downloadUrl"):
                    parsed = urlparse(item[key])
                    self.assertEqual(parsed.scheme, "https")
                    self.assertTrue(parsed.netloc)

    def test_official_license_label_is_consistent(self):
        for item in self.items:
            with self.subTest(app=item["name"]):
                self.assertEqual(item["license"], "MIT OR Apache-2.0")

    def test_stage_and_platforms_are_present(self):
        for item in self.items:
            with self.subTest(app=item["name"]):
                self.assertTrue(item["stage"].strip())
                self.assertTrue(item["platforms"])
                self.assertEqual(len(item["platforms"]), len(set(item["platforms"])))

    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_catalog.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
