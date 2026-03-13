from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from service_app.models import ReleaseRequest
from service_app.service import build_release_plan


def ensure_required_files() -> None:
    required = [
        ROOT / "AGENTS.md",
        ROOT / "ARCHITECTURE.md",
        ROOT / "SCHEMA.md",
        ROOT / "DECISIONS.md",
        ROOT / "ROADMAP.md",
        ROOT / "RISK_REGISTER.md",
        ROOT / "ENVIRONMENTS.md",
        ROOT / "SLOS.md",
        ROOT / "CODEOWNERS",
        ROOT / "requirements.txt",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("service_app", "scripts", "tests"):
        if not compileall.compile_dir(str(ROOT / relative), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_examples_validate() -> None:
    for name in ("low-risk-request.json", "high-risk-request.json"):
        raw = json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))
        request = ReleaseRequest.from_dict(raw)
        build_release_plan(request)


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def run_smoke() -> None:
    subprocess.run([sys.executable, "scripts/smoke_test.py"], cwd=ROOT, check=True)


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_examples_validate()
    run_tests()
    run_smoke()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
