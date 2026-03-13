from __future__ import annotations

import json
import sys
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

AUDIT_ROOT = ROOT / "audit"
AUDIT_ROOT.mkdir(exist_ok=True)

from change_control.audit import append_audit_event, verify_audit_chain
from change_control.models import ChangeRequest
from change_control.service import build_control_packet


def _load_request(path: Path) -> ChangeRequest:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SystemExit(f"{path.name} must contain a JSON object.")
    return ChangeRequest.from_dict(raw)


def main() -> int:
    low_request = _load_request(ROOT / "examples" / "low-risk-change.json")
    high_request = _load_request(ROOT / "examples" / "high-risk-change.json")

    db_path = AUDIT_ROOT / f"smoke-{uuid4().hex}.db"
    try:
        append_audit_event(db_path, actor="worker", action="plan-generated", packet=build_control_packet(low_request))
        append_audit_event(
            db_path,
            actor="compliance-worker",
            action="plan-generated",
            packet=build_control_packet(high_request),
        )
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
