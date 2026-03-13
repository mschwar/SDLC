from __future__ import annotations

import unittest

from control_app.models import ChangeRequest
from control_app.service import build_control_plan


class RegulatedStarterTests(unittest.TestCase):
    def test_low_risk_internal_change_is_standard(self) -> None:
        request = ChangeRequest.from_dict(
            {
                "objective": "Clarify note",
                "branch": "docs/clarify-note",
                "target_environment": "dev",
                "data_class": "internal",
                "acceptance_criteria": ["Docs updated"],
            }
        )

        plan = build_control_plan(request)

        self.assertEqual(plan.sandbox_tier, "standard")
        self.assertEqual(plan.approvers, ("reviewer",))

    def test_high_risk_restricted_prod_change_adds_controls(self) -> None:
        request = ChangeRequest.from_dict(
            {
                "objective": "Ship risky change",
                "branch": "feat/risky-change",
                "target_environment": "prod",
                "data_class": "restricted",
                "acceptance_criteria": ["Tests pass"],
                "risk_level": "high",
                "touches_sensitive_data": True,
                "changes_policy": True,
                "rollback_ready": True,
            }
        )

        plan = build_control_plan(request)

        self.assertIn("privacy-officer", plan.approvers)
        self.assertIn("compliance-officer", plan.approvers)
        self.assertIn("policy-approval", plan.required_controls)
        self.assertEqual(plan.sandbox_tier, "restricted")


if __name__ == "__main__":
    unittest.main()
