from __future__ import annotations

import compileall
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from change_control.models import ChangeRequest
from change_control.service import build_control_packet

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "SCHEMA.md",
    ROOT / "DECISIONS.md",
    ROOT / "CONTROL_OBJECTIVES.md",
    ROOT / "APPROVAL_MATRIX.md",
    ROOT / "DATA_CLASSIFICATION.md",
    ROOT / "SANDBOX_POLICY.md",
    ROOT / "AUDIT_LOG_POLICY.md",
    ROOT / "INCIDENT_RESPONSE.md",
    ROOT / "CODEOWNERS",
    ROOT / "requirements.txt",
]


def ensure_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def ensure_compiles() -> None:
    for relative in ("change_control", "scripts", "tests"):
        path = ROOT / relative
        if not compileall.compile_dir(str(path), quiet=1, force=True):
            raise SystemExit(f"Compilation failed for {relative}")


def ensure_examples_validate() -> None:
    for path in sorted((ROOT / "examples").glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise SystemExit(f"{path.name} must contain a JSON object.")
        request = ChangeRequest.from_dict(raw)
        build_control_packet(request)


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        check=True,
    )


def run_smoke_test() -> None:
    subprocess.run([sys.executable, "scripts/audit_smoke.py"], cwd=ROOT, check=True)


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
