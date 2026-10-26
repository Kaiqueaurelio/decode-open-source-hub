"""Tests for the ArtCraft-specific catalog."""
import json, subprocess, sys, unittest
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"software.json"
EXPECTED={"artcraft-studio","craft-launcher","photocraft","vectorcraft","filmcraft","lightcraft","pdfcraft","effectcraft","designcraft","figcraft","wordcraft","soundcraft","deckcraft","cadcraft","gridcraft"}
class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.items=json.loads(DATA.read_text(encoding="utf-8"))
    def test_catalog_contains_only_artcraft_projects(self):
        self.assertEqual({x["slug"] for x in self.items},EXPECTED)
        self.assertEqual(len(self.items),15)
    def test_thirteen_apps_plus_studio_and_launcher(self):
        self.assertEqual(sum(x["kind"]=="Crafting App" for x in self.items),13)
        self.assertEqual(sum(x["kind"]=="Estúdio de IA" for x in self.items),1)
        self.assertEqual(sum(x["kind"]=="Launcher" for x in self.items),1)
    def test_slugs_and_names_are_unique(self):
        self.assertEqual(len({x["slug"] for x in self.items}),len(self.items))
        self.assertEqual(len({x["name"].casefold() for x in self.items}),len(self.items))
    def test_links_use_https_and_official_sources(self):
        for x in self.items:
            for key in ("licenseUrl","websiteUrl","sourceUrl","downloadUrl"):
                p=urlparse(x[key]); self.assertEqual(p.scheme,"https",f'{x["name"]}: {key}'); self.assertTrue(p.netloc)
            self.assertEqual(urlparse(x["sourceUrl"]).netloc,"github.com")
            self.assertTrue(urlparse(x["sourceUrl"]).path.startswith("/storytold/"))
            self.assertEqual(urlparse(x["websiteUrl"]).netloc,"getartcraft.com")
    def test_published_dual_license_label(self):
        for x in self.items:
            self.assertEqual(x["license"],"MIT OR Apache-2.0")
            self.assertTrue(x["licenseUrl"].endswith("/LICENSE-MIT"))
    def test_stage_is_present(self):
        for x in self.items: self.assertTrue(x["stage"].strip())
    def test_validator_passes(self):
        r=subprocess.run([sys.executable,str(ROOT/"scripts"/"validate_catalog.py")],cwd=ROOT,capture_output=True,text=True,check=False)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
if __name__=="__main__": unittest.main()
