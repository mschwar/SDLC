from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (
    ROOT / "packages" / "shared_contracts",
    ROOT / "services" / "delivery_api",
)
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from delivery_api.service import build_summary, load_work_items

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "SCHEMA.md",
    ROOT / "DECISIONS.md",
    ROOT / "REPO_MAP.md",
    ROOT / "OWNERSHIP_MAP.md",
    ROOT / "ENVIRONMENTS.md",
    ROOT / "QA_STRATEGY.md",
    ROOT / "CODEOWNERS",
    ROOT / "requirements.txt",
    ROOT / "apps" / "ops_portal" / "index.html",
    ROOT / "apps" / "ops_portal" / "app.js",
    ROOT / "apps" / "ops_portal" / "styles.css",
]


def ensure_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("packages", "services", "scripts", "tests"):
        path = ROOT / relative
        if not compileall.compile_dir(str(path), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_examples_validate() -> None:
    items = load_work_items(ROOT / "examples" / "work-items.json")
    build_summary(items)


def ensure_static_assets_reference_expected_paths() -> None:
    html = (ROOT / "apps" / "ops_portal" / "index.html").read_text(encoding="utf-8")
    if "/static/app.js" not in html or "/static/styles.css" not in html:
        raise SystemExit("Portal HTML must reference the expected static asset paths.")

    script = (ROOT / "apps" / "ops_portal" / "app.js").read_text(encoding="utf-8")
    if "/api/summary" not in script or "/api/work-items" not in script:
        raise SystemExit("Portal JavaScript must fetch the expected API paths.")


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def run_smoke_test() -> None:
    subprocess.run([sys.executable, "scripts/e2e_smoke.py"], cwd=ROOT, check=True)


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_examples_validate()
    ensure_static_assets_reference_expected_paths()
    run_tests()
    run_smoke_test()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
