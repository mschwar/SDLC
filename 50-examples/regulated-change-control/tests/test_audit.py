from __future__ import annotations

from pathlib import Path
import sqlite3
import unittest
from uuid import uuid4

from change_control.audit import append_audit_event, verify_audit_chain
from change_control.models import ChangeRequest
from change_control.service import build_control_packet

ROOT = Path(__file__).resolve().parent.parent
AUDIT_ROOT = ROOT / "audit"
AUDIT_ROOT.mkdir(exist_ok=True)


def _request() -> ChangeRequest:
    return ChangeRequest.from_dict(
        {
            "system": "ledger",
            "objective": "Update schema",
            "branch": "feat/schema-update",
            "owner": "platform-team",
            "target_environment": "staging",
            "change_type": "schema",
            "data_class": "confidential",
            "acceptance_criteria": ["Migration documented"],
            "risk_level": "medium",
            "rollback_ready": True,
        }
    )


class ChangeControlAuditTests(unittest.TestCase):
    def _db_path(self) -> Path:
        return AUDIT_ROOT / f"test-{uuid4().hex}.db"

    def test_empty_chain_is_valid(self) -> None:
        db_path = self._db_path()
        try:
            valid, event_count = verify_audit_chain(db_path)
        finally:
            if db_path.exists():
                db_path.unlink()

        self.assertTrue(valid)
        self.assertEqual(event_count, 0)

    def test_appended_events_form_a_valid_chain(self) -> None:
        db_path = self._db_path()
        try:
            packet = build_control_packet(_request())
            append_audit_event(db_path, actor="worker", action="plan-generated", packet=packet)
            append_audit_event(db_path, actor="reviewer", action="review-requested", packet=packet)

            valid, event_count = verify_audit_chain(db_path)
        finally:
            if db_path.exists():
                db_path.unlink()

        self.assertTrue(valid)
        self.assertEqual(event_count, 2)

    def test_tampered_chain_is_detected(self) -> None:
        db_path = self._db_path()
        try:
            packet = build_control_packet(_request())
            append_audit_event(db_path, actor="worker", action="plan-generated", packet=packet)
            append_audit_event(db_path, actor="reviewer", action="review-requested", packet=packet)

            connection = sqlite3.connect(db_path)
            try:
                connection.execute(
                    "UPDATE audit_events SET chain_hash = ? WHERE event_index = 2",
                    ("tampered",),
                )
                connection.commit()
            finally:
                connection.close()

            valid, event_count = verify_audit_chain(db_path)
        finally:
            if db_path.exists():
                db_path.unlink()

        self.assertFalse(valid)
        self.assertEqual(event_count, 2)
