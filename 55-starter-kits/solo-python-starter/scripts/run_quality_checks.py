from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.models import WorkRequest
from app.service import build_work_plan


def ensure_required_files() -> None:
    required = [
        ROOT / "AGENTS.md",
        ROOT / "ARCHITECTURE.md",
        ROOT / "SCHEMA.md",
        ROOT / "DECISIONS.md",
        ROOT / "requirements.txt",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("app", "scripts", "tests"):
        if not compileall.compile_dir(str(ROOT / relative), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_example_validates() -> None:
    raw = json.loads((ROOT / "examples" / "sample-input.json").read_text(encoding="utf-8"))
    request = WorkRequest.from_dict(raw)
    build_work_plan(request)


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def main() -> int:
    ensure_required_files()
    ensure_compiles()
    ensure_example_validates()
    run_tests()
    print("All quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
