from __future__ import annotations

import json
import sys
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_app.audit import append_audit_event, verify_audit_chain
from control_app.models import ChangeRequest
from control_app.service import build_control_plan


def _load(name: str) -> ChangeRequest:
    raw = json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SystemExit("Example fixture must contain a JSON object.")
    return ChangeRequest.from_dict(raw)


def main() -> int:
    db_path = ROOT / "audit" / f"smoke-{uuid4().hex}.db"
    try:
        append_audit_event(db_path, "worker", "plan-generated", build_control_plan(_load("low-risk-change.json")))
        append_audit_event(db_path, "reviewer", "plan-generated", build_control_plan(_load("high-risk-change.json")))
        valid, event_count = verify_audit_chain(db_path)
        if not valid or event_count != 2:
            raise SystemExit("Audit smoke test failed.")
    finally:
        if db_path.exists():
            db_path.unlink()

    print("Audit smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
