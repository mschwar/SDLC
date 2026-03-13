from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}
ALLOWED_CHANGE_TYPES = {"docs", "feature", "bugfix", "schema", "infrastructure"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
BRANCH_PATTERN = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._/-]+$")


def _require_non_empty_string(raw: dict[str, Any], key: str) -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string.")
    return value.strip()


def _require_bool(raw: dict[str, Any], key: str, *, default: bool = False) -> bool:
    value = raw.get(key, default)
    if not isinstance(value, bool):
        raise ValueError(f"{key} must be a boolean.")
    return value


@dataclass(frozen=True)
class ReleaseRequest:
    service: str
    objective: str
    branch: str
    owner: str
    environment: str
    change_type: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"
    customer_visible: bool = False
    touches_auth: bool = False
    touches_schema: bool = False
    requires_migration: bool = False
    rollback_ready: bool = False
    needs_data_review: bool = False
    evidence: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ReleaseRequest":
        required_keys = (
            "service",
            "objective",
            "branch",
            "owner",
            "environment",
            "change_type",
            "acceptance_criteria",
        )
        missing = [key for key in required_keys if key not in raw]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        service = _require_non_empty_string(raw, "service")
        objective = _require_non_empty_string(raw, "objective")
        branch = _require_non_empty_string(raw, "branch")
        owner = _require_non_empty_string(raw, "owner")
        environment = _require_non_empty_string(raw, "environment")
        change_type = _require_non_empty_string(raw, "change_type")

        if not BRANCH_PATTERN.match(branch) or " " in branch:
            raise ValueError("branch must be slash-delimited and contain no spaces.")
        if environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError(f"environment must be one of: {', '.join(sorted(ALLOWED_ENVIRONMENTS))}")
        if change_type not in ALLOWED_CHANGE_TYPES:
            raise ValueError(f"change_type must be one of: {', '.join(sorted(ALLOWED_CHANGE_TYPES))}")

        risk_level = raw.get("risk_level", "low")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError(f"risk_level must be one of: {', '.join(sorted(ALLOWED_RISK_LEVELS))}")

        criteria = raw["acceptance_criteria"]
        if not isinstance(criteria, list) or not criteria:
            raise ValueError("acceptance_criteria must be a non-empty list.")
        if not all(isinstance(item, str) and item.strip() for item in criteria):
            raise ValueError("acceptance_criteria entries must be non-empty strings.")

        evidence = raw.get("evidence", [])
        if not isinstance(evidence, list):
            raise ValueError("evidence must be a list.")
        if not all(isinstance(item, str) and item.strip() for item in evidence):
            raise ValueError("evidence entries must be non-empty strings.")

        if environment == "prod" and "rollback_ready" not in raw:
            raise ValueError("Production requests must declare rollback_ready.")

        return cls(
            service=service,
            objective=objective,
            branch=branch,
            owner=owner,
            environment=environment,
            change_type=change_type,
            acceptance_criteria=tuple(item.strip() for item in criteria),
            risk_level=risk_level,
            customer_visible=_require_bool(raw, "customer_visible"),
            touches_auth=_require_bool(raw, "touches_auth"),
            touches_schema=_require_bool(raw, "touches_schema"),
            requires_migration=_require_bool(raw, "requires_migration"),
            rollback_ready=_require_bool(raw, "rollback_ready"),
            needs_data_review=_require_bool(raw, "needs_data_review"),
            evidence=tuple(item.strip() for item in evidence),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "service": self.service,
            "objective": self.objective,
            "branch": self.branch,
            "owner": self.owner,
            "environment": self.environment,
            "change_type": self.change_type,
            "acceptance_criteria": list(self.acceptance_criteria),
            "risk_level": self.risk_level,
            "customer_visible": self.customer_visible,
            "touches_auth": self.touches_auth,
            "touches_schema": self.touches_schema,
            "requires_migration": self.requires_migration,
            "rollback_ready": self.rollback_ready,
            "needs_data_review": self.needs_data_review,
            "evidence": list(self.evidence),
        }


@dataclass(frozen=True)
class ReleasePlan:
    service: str
    review_roles: tuple[str, ...]
    required_gates: tuple[str, ...]
    allowed_environments: tuple[str, ...]
    rollout_strategy: str
    required_evidence: tuple[str, ...]
    blocking_issues: tuple[str, ...]
    summary: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "service": self.service,
            "review_roles": list(self.review_roles),
            "required_gates": list(self.required_gates),
            "allowed_environments": list(self.allowed_environments),
            "rollout_strategy": self.rollout_strategy,
            "required_evidence": list(self.required_evidence),
            "blocking_issues": list(self.blocking_issues),
            "summary": self.summary,
        }
