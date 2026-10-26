"""Basic integrity tests for the software catalog."""

import json
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "software.json"


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads(DATA.read_text(encoding="utf-8"))

    def test_catalog_contains_a_useful_starter_set(self):
        self.assertGreaterEqual(len(self.items), 20)

    def test_slugs_are_unique(self):
        slugs = [item["slug"] for item in self.items]
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_every_record_has_https_links(self):
        for item in self.items:
            for field in ("licenseUrl", "websiteUrl", "sourceUrl", "downloadUrl"):
                parsed = urlparse(item[field])
                self.assertEqual(parsed.scheme, "https", f"{item['name']}: {field}")
                self.assertTrue(parsed.netloc, f"{item['name']}: {field}")

    def test_every_record_has_a_category_and_license(self):
        for item in self.items:
            self.assertTrue(item["category"].strip())
            self.assertTrue(item["license"].strip())

    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_catalog.py")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
