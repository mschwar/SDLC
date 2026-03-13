from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from release_gateway.models import ReleaseRequest
from release_gateway.service import build_release_plan

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "SCHEMA.md",
    ROOT / "DECISIONS.md",
    ROOT / "ROADMAP.md",
    ROOT / "RISK_REGISTER.md",
    ROOT / "ENVIRONMENTS.md",
    ROOT / "SLOS.md",
    ROOT / "THREAT_MODEL.md",
    ROOT / "CODEOWNERS",
    ROOT / "requirements.txt",
]


def ensure_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("release_gateway", "scripts", "tests"):
        path = ROOT / relative
        if not compileall.compile_dir(str(path), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_examples_validate() -> None:
    examples_dir = ROOT / "examples"
    for path in sorted(examples_dir.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise SystemExit(f"{path.name} must contain a JSON object.")
        request = ReleaseRequest.from_dict(raw)
        build_release_plan(request)


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def run_smoke_test() -> None:
    subprocess.run([sys.executable, "scripts/smoke_test.py"], cwd=ROOT, check=True)


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_examples_validate()
    run_tests()
    run_smoke_test()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
