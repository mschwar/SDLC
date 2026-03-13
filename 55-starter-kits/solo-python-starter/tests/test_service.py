from __future__ import annotations

import unittest

from app.models import WorkRequest
from app.service import build_work_plan


class SoloStarterTests(unittest.TestCase):
    def test_low_risk_request_needs_one_reviewer(self) -> None:
        request = WorkRequest.from_dict(
            {
                "objective": "Update docs",
                "branch": "docs/update-readme",
                "acceptance_criteria": ["Docs are updated"],
            }
        )

        plan = build_work_plan(request)

        self.assertEqual(plan.review_roles, ("reviewer",))
        self.assertEqual(plan.required_gates, ())

    def test_high_risk_request_adds_controls(self) -> None:
        request = WorkRequest.from_dict(
            {
                "objective": "Harden auth path",
                "branch": "feat/auth-hardening",
                "acceptance_criteria": ["Behavior is covered by tests"],
                "risk_level": "high",
            }
        )

        plan = build_work_plan(request)

        self.assertIn("security-reviewer", plan.review_roles)
        self.assertIn("human-approval", plan.required_gates)


if __name__ == "__main__":
    unittest.main()
