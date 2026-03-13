from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

BRANCH_PATTERN = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._/-]+$")
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}


@dataclass(frozen=True)
class WorkRequest:
    objective: str
    branch: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "WorkRequest":
        objective = raw.get("objective")
        branch = raw.get("branch")
        criteria = raw.get("acceptance_criteria")
        risk_level = raw.get("risk_level", "low")

        if not isinstance(objective, str) or not objective.strip():
            raise ValueError("objective must be a non-empty string.")
        if not isinstance(branch, str) or not BRANCH_PATTERN.match(branch) or " " in branch:
            raise ValueError("branch must be slash-delimited and contain no spaces.")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError("risk_level must be low, medium, or high.")
        if not isinstance(criteria, list) or not criteria:
            raise ValueError("acceptance_criteria must be a non-empty list.")
        if not all(isinstance(item, str) and item.strip() for item in criteria):
            raise ValueError("acceptance_criteria entries must be non-empty strings.")

        return cls(
            objective=objective.strip(),
            branch=branch.strip(),
            acceptance_criteria=tuple(item.strip() for item in criteria),
            risk_level=risk_level,
        )


@dataclass(frozen=True)
class WorkPlan:
    review_roles: tuple[str, ...]
    required_gates: tuple[str, ...]
    summary: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "review_roles": list(self.review_roles),
            "required_gates": list(self.required_gates),
            "summary": self.summary,
        }
