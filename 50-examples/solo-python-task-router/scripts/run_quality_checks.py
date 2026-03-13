from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from task_router.models import TaskSpec
from task_router.service import build_workflow_decision

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "SCHEMA.md",
    ROOT / "DECISIONS.md",
    ROOT / "requirements.txt",
]


def ensure_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("task_router", "scripts", "tests"):
        path = ROOT / relative
        if not compileall.compile_dir(str(path), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_examples_validate() -> None:
    examples_dir = ROOT / "examples"
    for path in sorted(examples_dir.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        spec = TaskSpec.from_dict(raw)
        build_workflow_decision(spec)


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_examples_validate()
    run_tests()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
