from __future__ import annotations

from pathlib import Path
import sqlite3
import unittest
from uuid import uuid4

from control_app.audit import append_audit_event, verify_audit_chain
from control_app.models import ChangeRequest
from control_app.service import build_control_plan

ROOT = Path(__file__).resolve().parent.parent


def _request() -> ChangeRequest:
    return ChangeRequest.from_dict(
        {
            "objective": "Update policy",
            "branch": "feat/policy-update",
            "target_environment": "staging",
            "data_class": "confidential",
            "acceptance_criteria": ["Policy updated"],
            "risk_level": "medium",
            "changes_policy": True,
            "rollback_ready": True,
        }
    )


class RegulatedStarterAuditTests(unittest.TestCase):
    def _db_path(self) -> Path:
        return ROOT / "audit" / f"test-{uuid4().hex}.db"

    def test_valid_chain(self) -> None:
        db_path = self._db_path()
        try:
            plan = build_control_plan(_request())
            append_audit_event(db_path, "worker", "plan-generated", plan)
            append_audit_event(db_path, "reviewer", "review-requested", plan)
            valid, event_count = verify_audit_chain(db_path)
        finally:
            if db_path.exists():
                db_path.unlink()

        self.assertTrue(valid)
        self.assertEqual(event_count, 2)

    def test_tampering_is_detected(self) -> None:
        db_path = self._db_path()
        try:
            plan = build_control_plan(_request())
            append_audit_event(db_path, "worker", "plan-generated", plan)
            connection = sqlite3.connect(db_path)
            try:
                connection.execute("UPDATE audit_events SET chain_hash = ? WHERE event_index = 1", ("tampered",))
                connection.commit()
            finally:
                connection.close()
            valid, _ = verify_audit_chain(db_path)
        finally:
            if db_path.exists():
                db_path.unlink()

        self.assertFalse(valid)
