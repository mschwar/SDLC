from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sdlc.generator import generate_repo
from sdlc.manifest import RepoManifest, load_manifest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_MANIFEST = ROOT / "profiles" / "small-team-python-service.manifest.json"


class GeneratorTests(unittest.TestCase):
    def test_generate_repo_writes_v1_baseline(self) -> None:
        base_manifest = load_manifest(EXAMPLE_MANIFEST)
        raw = base_manifest.to_dict()
        raw["repository"]["name"] = "Test Release Gateway"
        raw["repository"]["slug"] = "test-release-gateway"
        raw["product"]["name"] = "Test Release Gateway"
        raw["service"]["package_name"] = "release_gateway"
        raw["service"]["module_name"] = "release_gateway"
        raw["service"]["entrypoint"] = "python -m release_gateway"
        manifest = RepoManifest.from_dict(raw)

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "generated"
            result = generate_repo(manifest, output_dir)

            self.assertTrue((output_dir / "README.md").exists())
            self.assertTrue((output_dir / "repo.manifest.json").exists())
            self.assertTrue((output_dir / "FOUNDER-QUICKSTART.md").exists())
            self.assertTrue((output_dir / "RUNBOOKS.md").exists())
            self.assertTrue((output_dir / "runbooks" / "start-planning.md").exists())
            self.assertTrue((output_dir / "release_gateway" / "__init__.py").exists())
            self.assertFalse((output_dir / "service_app").exists())
            self.assertIn("release_gateway", (output_dir / "scripts" / "run_quality_checks.py").read_text(encoding="utf-8"))
            self.assertIn("repo.manifest.json", result.written_files)


if __name__ == "__main__":
    unittest.main()
