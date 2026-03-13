from __future__ import annotations

import unittest

from task_router.models import TaskSpec
from task_router.service import build_workflow_decision


class TaskRouterTests(unittest.TestCase):
    def test_low_risk_task_requires_only_basic_review(self) -> None:
        spec = TaskSpec.from_dict(
            {
                "objective": "Add a docs-only note",
                "branch": "docs/add-note",
                "acceptance_criteria": ["New note is linked from the index"],
            }
        )

        decision = build_workflow_decision(spec)

        self.assertEqual(decision.review_roles, ("reviewer",))
        self.assertEqual(decision.required_gates, ())
        self.assertEqual(decision.release_strategy, "merge-to-main")

    def test_high_risk_auth_change_adds_gates(self) -> None:
        spec = TaskSpec.from_dict(
            {
                "objective": "Change auth flow",
                "branch": "feat/auth-hardening",
                "acceptance_criteria": ["Auth path is updated", "Tests cover the new path"],
                "risk_level": "high",
                "touches_auth": True,
                "needs_production_access": True,
            }
        )

        decision = build_workflow_decision(spec)

        self.assertIn("security-reviewer", decision.review_roles)
        self.assertIn("security-review", decision.required_gates)
        self.assertIn("release-approval", decision.required_gates)
        self.assertIn("human-approval", decision.required_gates)
        self.assertEqual(decision.release_strategy, "canary")

    def test_schema_change_requires_architecture_review(self) -> None:
        spec = TaskSpec.from_dict(
            {
                "objective": "Add a new schema field",
                "branch": "feat/schema-field",
                "acceptance_criteria": ["Schema docs are updated"],
                "risk_level": "medium",
                "touches_schema": True,
            }
        )

        decision = build_workflow_decision(spec)

        self.assertIn("architecture-review", decision.required_gates)
        self.assertIn("architecture-reviewer", decision.review_roles)
        self.assertEqual(decision.release_strategy, "staged-rollout")

    def test_invalid_branch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            TaskSpec.from_dict(
                {
                    "objective": "Broken branch",
                    "branch": "bad branch",
                    "acceptance_criteria": ["Should fail validation"],
                }
            )


if __name__ == "__main__":
    unittest.main()
