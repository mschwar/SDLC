from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
BRANCH_PATTERN = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._/-]+$")


@dataclass(frozen=True)
class ReleaseRequest:
    objective: str
    branch: str
    environment: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"
    customer_visible: bool = False
    rollback_ready: bool = False

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ReleaseRequest":
        objective = raw.get("objective")
        branch = raw.get("branch")
        environment = raw.get("environment")
        criteria = raw.get("acceptance_criteria")
        risk_level = raw.get("risk_level", "low")
        customer_visible = raw.get("customer_visible", False)
        rollback_ready = raw.get("rollback_ready", False)

        if not isinstance(objective, str) or not objective.strip():
            raise ValueError("objective must be a non-empty string.")
        if not isinstance(branch, str) or not BRANCH_PATTERN.match(branch) or " " in branch:
            raise ValueError("branch must be slash-delimited and contain no spaces.")
        if environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError("environment must be dev, staging, or prod.")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError("risk_level must be low, medium, or high.")
        if not isinstance(criteria, list) or not criteria:
            raise ValueError("acceptance_criteria must be a non-empty list.")
        if not all(isinstance(item, str) and item.strip() for item in criteria):
            raise ValueError("acceptance_criteria entries must be non-empty strings.")
        if not isinstance(customer_visible, bool) or not isinstance(rollback_ready, bool):
            raise ValueError("customer_visible and rollback_ready must be boolean values.")
        if environment == "prod" and "rollback_ready" not in raw:
            raise ValueError("Production requests must declare rollback_ready.")

        return cls(
            objective=objective.strip(),
            branch=branch.strip(),
            environment=environment,
            acceptance_criteria=tuple(item.strip() for item in criteria),
            risk_level=risk_level,
            customer_visible=customer_visible,
            rollback_ready=rollback_ready,
        )


@dataclass(frozen=True)
class ReleasePlan:
    review_roles: tuple[str, ...]
    required_gates: tuple[str, ...]
    release_strategy: str
    blocking_issues: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "review_roles": list(self.review_roles),
            "required_gates": list(self.required_gates),
            "release_strategy": self.release_strategy,
            "blocking_issues": list(self.blocking_issues),
        }
