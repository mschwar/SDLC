from __future__ import annotations

import unittest

from release_gateway.models import ReleaseRequest
from release_gateway.service import build_release_plan


class ReleaseGatewayServiceTests(unittest.TestCase):
    def test_low_risk_docs_change_stays_direct(self) -> None:
        request = ReleaseRequest.from_dict(
            {
                "service": "release-gateway",
                "objective": "Clarify docs",
                "branch": "docs/clarify-release-note",
                "owner": "platform-team",
                "environment": "dev",
                "change_type": "docs",
                "acceptance_criteria": ["Docs are updated"],
            }
        )

        plan = build_release_plan(request)

        self.assertEqual(plan.review_roles, ("reviewer",))
        self.assertEqual(plan.required_gates, ("ci",))
        self.assertEqual(plan.allowed_environments, ("dev",))
        self.assertEqual(plan.rollout_strategy, "direct")

    def test_high_risk_prod_auth_change_requires_strong_controls(self) -> None:
        request = ReleaseRequest.from_dict(
            {
                "service": "release-gateway",
                "objective": "Change auth flow",
                "branch": "feat/auth-tightening",
                "owner": "platform-team",
                "environment": "prod",
                "change_type": "feature",
                "acceptance_criteria": ["Auth flow is updated", "Tests cover the new path"],
                "risk_level": "high",
                "customer_visible": True,
                "touches_auth": True,
                "rollback_ready": True,
            }
        )

        plan = build_release_plan(request)

        self.assertIn("service-owner", plan.review_roles)
        self.assertIn("release-manager", plan.review_roles)
        self.assertIn("security-reviewer", plan.review_roles)
        self.assertIn("release-approval", plan.required_gates)
        self.assertIn("human-approval", plan.required_gates)
        self.assertIn("security-review", plan.required_gates)
        self.assertEqual(plan.rollout_strategy, "canary")
        self.assertEqual(plan.blocking_issues, ())

    def test_schema_migration_requires_architecture_controls(self) -> None:
        request = ReleaseRequest.from_dict(
            {
                "service": "release-gateway",
                "objective": "Ship schema migration",
                "branch": "feat/schema-migration",
                "owner": "platform-team",
                "environment": "staging",
                "change_type": "schema",
                "acceptance_criteria": ["Schema is updated"],
                "risk_level": "medium",
                "touches_schema": True,
                "requires_migration": True,
            }
        )

        plan = build_release_plan(request)

        self.assertIn("architecture-reviewer", plan.review_roles)
        self.assertIn("architecture-review", plan.required_gates)
        self.assertIn("migration-plan", plan.required_evidence)
        self.assertEqual(plan.allowed_environments, ("dev", "staging"))

    def test_production_request_must_declare_rollback_ready(self) -> None:
        with self.assertRaises(ValueError):
            ReleaseRequest.from_dict(
                {
                    "service": "release-gateway",
                    "objective": "Broken prod request",
                    "branch": "fix/broken-request",
                    "owner": "platform-team",
                    "environment": "prod",
                    "change_type": "bugfix",
                    "acceptance_criteria": ["Should fail"],
                }
            )

    def test_invalid_branch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ReleaseRequest.from_dict(
                {
                    "service": "release-gateway",
                    "objective": "Broken branch",
                    "branch": "bad branch",
                    "owner": "platform-team",
                    "environment": "dev",
                    "change_type": "bugfix",
                    "acceptance_criteria": ["Should fail"],
                }
            )


if __name__ == "__main__":
    unittest.main()
