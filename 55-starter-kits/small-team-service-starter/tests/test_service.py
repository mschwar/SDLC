from __future__ import annotations

import unittest

from service_app.models import ReleaseRequest
from service_app.service import build_release_plan


class SmallTeamStarterTests(unittest.TestCase):
    def test_low_risk_dev_request_is_direct(self) -> None:
        request = ReleaseRequest.from_dict(
            {
                "objective": "Update docs",
                "branch": "docs/update-docs",
                "environment": "dev",
                "acceptance_criteria": ["Docs are updated"],
            }
        )

        plan = build_release_plan(request)

        self.assertEqual(plan.release_strategy, "direct")
        self.assertEqual(plan.required_gates, ("ci",))

    def test_high_risk_prod_request_adds_controls(self) -> None:
        request = ReleaseRequest.from_dict(
            {
                "objective": "Ship risky change",
                "branch": "feat/risky-change",
                "environment": "prod",
                "acceptance_criteria": ["Tests pass"],
                "risk_level": "high",
                "customer_visible": True,
                "rollback_ready": True,
            }
        )

        plan = build_release_plan(request)

        self.assertIn("service-owner", plan.review_roles)
        self.assertIn("human-approval", plan.required_gates)
        self.assertEqual(plan.release_strategy, "canary")


if __name__ == "__main__":
    unittest.main()
