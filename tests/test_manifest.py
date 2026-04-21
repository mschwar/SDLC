from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from sdlc.manifest import ManifestError, load_manifest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_MANIFEST = ROOT / "profiles" / "small-team-python-service.manifest.json"


class ManifestTests(unittest.TestCase):
    def test_load_example_manifest(self) -> None:
        manifest = load_manifest(EXAMPLE_MANIFEST)
        self.assertEqual(manifest.profile.id, "small-team-python-service")
        self.assertEqual(manifest.repository.slug, "acme-release-gateway")
        self.assertEqual(manifest.service.package_name, "service_app")
        self.assertEqual(manifest.service.module_name, "service_app")

    def test_rejects_module_name_mismatch(self) -> None:
        raw = json.loads(EXAMPLE_MANIFEST.read_text(encoding="utf-8"))
        raw["service"]["module_name"] = "different_module"
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = Path(tmp) / "bad.manifest.json"
            manifest_path.write_text(json.dumps(raw), encoding="utf-8")
            with self.assertRaises(ManifestError):
                load_manifest(manifest_path)


if __name__ == "__main__":
    unittest.main()
