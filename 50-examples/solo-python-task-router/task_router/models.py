from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


VALID_RISK_LEVELS = {"low", "medium", "high"}


def _require_non_empty_text(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _require_bool(name: str, value: Any) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be a boolean")
    return value


@dataclass(frozen=True)
class TaskSpec:
    objective: str
    branch: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"
    touches_schema: bool = False
    touches_auth: bool = False
    needs_production_access: bool = False
    requires_ui_validation: bool = False
    tags: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "TaskSpec":
        if not isinstance(raw, dict):
            raise ValueError("task spec must be a JSON object")

        objective = _require_non_empty_text("objective", raw.get("objective"))
        branch = _require_non_empty_text("branch", raw.get("branch"))
        if " " in branch:
            raise ValueError("branch must not contain spaces")

        acceptance_criteria_raw = raw.get("acceptance_criteria")
        if not isinstance(acceptance_criteria_raw, list) or not acceptance_criteria_raw:
            raise ValueError("acceptance_criteria must contain at least one entry")

        acceptance_criteria = tuple(
            _require_non_empty_text("acceptance_criteria entry", entry)
            for entry in acceptance_criteria_raw
        )

        risk_level = raw.get("risk_level", "low")
        if risk_level not in VALID_RISK_LEVELS:
            raise ValueError("risk_level must be one of: low, medium, high")

        tags_raw = raw.get("tags", [])
        if not isinstance(tags_raw, list):
            raise ValueError("tags must be a list of strings")
        tags = tuple(_require_non_empty_text("tag", tag) for tag in tags_raw)

        return cls(
            objective=objective,
            branch=branch,
            acceptance_criteria=acceptance_criteria,
            risk_level=risk_level,
            touches_schema=_require_bool("touches_schema", raw.get("touches_schema", False)),
            touches_auth=_require_bool("touches_auth", raw.get("touches_auth", False)),
            needs_production_access=_require_bool(
                "needs_production_access", raw.get("needs_production_access", False)
            ),
            requires_ui_validation=_require_bool(
                "requires_ui_validation", raw.get("requires_ui_validation", False)
            ),
            tags=tags,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "objective": self.objective,
            "branch": self.branch,
            "acceptance_criteria": list(self.acceptance_criteria),
            "risk_level": self.risk_level,
            "touches_schema": self.touches_schema,
            "touches_auth": self.touches_auth,
            "needs_production_access": self.needs_production_access,
            "requires_ui_validation": self.requires_ui_validation,
            "tags": list(self.tags),
        }


@dataclass(frozen=True)
class WorkflowDecision:
    review_roles: tuple[str, ...]
    required_gates: tuple[str, ...]
    local_checks: tuple[str, ...]
    release_strategy: str
    notes: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "review_roles": list(self.review_roles),
            "required_gates": list(self.required_gates),
            "local_checks": list(self.local_checks),
            "release_strategy": self.release_strategy,
            "notes": list(self.notes),
        }
