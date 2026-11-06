import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify-artifacts.py"


class VerifyArtifactsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.dist = self.root / "dist"
        self.dist.mkdir()
        self.manifest = self.root / "apps.json"
        self.manifest.write_text(json.dumps({"apps": [{"id": "photocraft"}]}), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def write_asset(self, name, payload=b"verified artifact"):
        path = self.dist / name
        path.write_bytes(payload)
        digest = hashlib.sha256(payload).hexdigest()
        (self.dist / f"{name}.sha256").write_text(f"{digest}  {name}\n", encoding="ascii")
        return path

    def run_verifier(self, *extra):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.dist), "--manifest", str(self.manifest), *extra],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_full_matrix_for_manifest_app_passes(self):
        for suffix in ("linux-x86_64.tar.gz", "linux-x86_64.AppImage", "windows-x64-portable.zip"):
            self.write_asset(f"photocraft-0.9.5-{suffix}")
        image = self.write_asset("photocraft-0.9.5-linux-x86_64.AppImage")
        zsync = self.dist / "photocraft-0.9.5-linux-x86_64.AppImage.zsync"
        zsync.write_bytes(b"delta metadata")
        (image.with_name(image.name + ".sha256")).write_text(
            f"{hashlib.sha256(image.read_bytes()).hexdigest()}  {image.name}\n"
            f"{hashlib.sha256(zsync.read_bytes()).hexdigest()}  {zsync.name}\n",
            encoding="ascii",
        )
        self.assertEqual(self.run_verifier().returncode, 0)

    def test_missing_artifacts_fail_strict_validation(self):
        self.write_asset("photocraft-0.9.5-linux-x86_64.tar.gz")
        result = self.run_verifier()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing expected matrix outputs", result.stdout)

    def test_checksum_mismatch_fails(self):
        path = self.write_asset("photocraft-0.9.5-linux-x86_64.tar.gz")
        path.with_name(path.name + ".sha256").write_text(f"{'0' * 64}  {path.name}\n", encoding="ascii")
        result = self.run_verifier("--allow-missing")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("checksum mismatch", result.stdout)

    def test_missing_checksum_sidecar_fails(self):
        (self.dist / "photocraft-0.9.5-linux-x86_64.tar.gz").write_bytes(b"payload")
        result = self.run_verifier("--allow-missing")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing checksum", result.stdout)

    def test_partial_build_can_be_published_when_present_assets_are_valid(self):
        self.write_asset("photocraft-0.9.5-linux-x86_64.tar.gz")
        result = self.run_verifier("--allow-missing")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Missing expected matrix outputs", result.stdout)


if __name__ == "__main__":
    unittest.main()
