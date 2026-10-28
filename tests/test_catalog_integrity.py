import json
import os
import unittest

class TestCatalogIntegrity(unittest.TestCase):
    def setUp(self):
        catalog_path = os.path.join(os.path.dirname(__file__), "../data/software.json")
        with open(catalog_path, "r", encoding="utf-8") as f:
            self.catalog = json.load(f)

    def test_no_storytold_or_craftlauncher(self):
        """Verifica se nenhuma entrada aponta para repositórios legados ou storytold."""
        for item in self.catalog:
            content = json.dumps(item).lower()
            self.assertNotIn("storytold", content, f"Entrada {item['name']} contém 'storytold'")
            self.assertNotIn("craft-launcher", content, f"Entrada {item['name']} contém 'craft-launcher'")

    def test_all_source_urls_are_decode_official(self):
        """Garante que todos os links de código-fonte apontam exclusivamente para repositórios oficiais Decode."""
        allowed_prefixes = (
            "https://github.com/Kaiqueaurelio/decode-open-source-hub",
            "https://github.com/Kaiqueaurelio/decodecad"
        )
        for item in self.catalog:
            source_url = item.get("sourceUrl", "")
            self.assertTrue(
                source_url.startswith(allowed_prefixes),
                f"App {item['name']} possui sourceUrl não autorizada: {source_url}"
            )

    def test_all_download_urls_are_official(self):
        """Garante que os links de download apontam para releases oficiais da Decode."""
        for item in self.catalog:
            download_url = item.get("downloadUrl", "")
            self.assertTrue(
                "Kaiqueaurelio" in download_url,
                f"Download URL de {item['name']} não é oficial: {download_url}"
            )

if __name__ == "__main__":
    unittest.main()
