from __future__ import annotations

import unittest

from change_control.models import ChangeRequest
from change_control.service import build_control_packet


class ChangeControlServiceTests(unittest.TestCase):
    def test_low_risk_internal_change_uses_standard_controls(self) -> None:
        request = ChangeRequest.from_dict(
            {
                "system": "ledger",
                "objective": "Clarify internal config note",
                "branch": "docs/config-note",
                "owner": "platform-team",
                "target_environment": "dev",
                "change_type": "config",
                "data_class": "internal",
                "acceptance_criteria": ["Docs updated"],
            }
        )

        packet = build_control_packet(request)

        self.assertEqual(packet.approvers, ("reviewer",))
        self.assertEqual(packet.required_controls, ("ci", "traceability-check"))
        self.assertEqual(packet.sandbox_tier, "standard")
        self.assertEqual(packet.retention_class, "one-year")

    def test_restricted_prod_change_requires_compliance_controls(self) -> None:
        request = ChangeRequest.from_dict(
            {
                "system": "ledger",
                "objective": "Ship restricted production change",
                "branch": "feat/restricted-prod-change",
                "owner": "platform-team",
                "target_environment": "prod",
                "change_type": "schema",
                "data_class": "restricted",
                "acceptance_criteria": ["Migration is reversible", "Controls are documented"],
                "risk_level": "high",
                "touches_sensitive_data": True,
                "rollback_ready": True,
            }
        )

        packet = build_control_packet(request)

        self.assertEqual(packet.sandbox_tier, "restricted")
        self.assertEqual(packet.retention_class, "seven-years")
        self.assertIn("privacy-officer", packet.approvers)
        self.assertIn("compliance-officer", packet.approvers)
        self.assertIn("architecture-reviewer", packet.approvers)
        self.assertIn("release-board-approval", packet.required_controls)
        self.assertIn("data-handling-review", packet.required_controls)
        self.assertIn("rollback-plan", packet.required_evidence)

    def test_policy_change_requires_policy_approval(self) -> None:
        request = ChangeRequest.from_dict(
            {
                "system": "ledger",
                "objective": "Update retention policy",
                "branch": "feat/policy-update",
                "owner": "compliance-team",
                "target_environment": "staging",
                "change_type": "policy",
                "data_class": "confidential",
                "acceptance_criteria": ["Policy is updated"],
                "changes_policy": True,
            }
        )

        packet = build_control_packet(request)

        self.assertIn("policy-approver", packet.approvers)
        self.assertIn("policy-approval", packet.required_controls)
        self.assertEqual(packet.sandbox_tier, "hardened")

    def test_prod_request_must_declare_rollback_ready(self) -> None:
        with self.assertRaises(ValueError):
            ChangeRequest.from_dict(
                {
                    "system": "ledger",
                    "objective": "Broken prod request",
                    "branch": "fix/broken-prod-request",
                    "owner": "platform-team",
                    "target_environment": "prod",
                    "change_type": "config",
                    "data_class": "internal",
                    "acceptance_criteria": ["Should fail"],
                }
            )

    def test_invalid_branch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ChangeRequest.from_dict(
                {
                    "system": "ledger",
                    "objective": "Broken branch",
                    "branch": "bad branch",
                    "owner": "platform-team",
                    "target_environment": "dev",
                    "change_type": "config",
                    "data_class": "internal",
                    "acceptance_criteria": ["Should fail"],
                }
            )


if __name__ == "__main__":
    unittest.main()
