from __future__ import annotations

import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (ROOT / "packages" / "contracts", ROOT / "services" / "api_service")
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from api_service.service import build_summary, load_items


def ensure_required_files() -> None:
    required = [
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
        ROOT / "apps" / "web_portal" / "index.html",
        ROOT / "apps" / "web_portal" / "app.js",
        ROOT / "apps" / "web_portal" / "styles.css",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("packages", "services", "scripts", "tests"):
        if not compileall.compile_dir(str(ROOT / relative), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_example_validates() -> None:
    summary = build_summary(load_items(ROOT / "examples" / "items.json"))
    if summary.total_items < 1:
        raise SystemExit("Example fixture must contain at least one item.")


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def run_smoke() -> None:
    subprocess.run([sys.executable, "scripts/e2e_smoke.py"], cwd=ROOT, check=True)


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_example_validates()
    run_tests()
    run_smoke()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
