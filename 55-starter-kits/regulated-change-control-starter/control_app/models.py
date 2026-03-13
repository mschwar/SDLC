from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

BRANCH_PATTERN = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._/-]+$")
ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}
ALLOWED_DATA_CLASSES = {"internal", "confidential", "restricted"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}


@dataclass(frozen=True)
class ChangeRequest:
    objective: str
    branch: str
    target_environment: str
    data_class: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"
    touches_sensitive_data: bool = False
    changes_policy: bool = False
    rollback_ready: bool = False

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ChangeRequest":
        objective = raw.get("objective")
        branch = raw.get("branch")
        target_environment = raw.get("target_environment")
        data_class = raw.get("data_class")
        criteria = raw.get("acceptance_criteria")
        risk_level = raw.get("risk_level", "low")
        touches_sensitive_data = raw.get("touches_sensitive_data", False)
        changes_policy = raw.get("changes_policy", False)
        rollback_ready = raw.get("rollback_ready", False)

        if not isinstance(objective, str) or not objective.strip():
            raise ValueError("objective must be a non-empty string.")
        if not isinstance(branch, str) or not BRANCH_PATTERN.match(branch) or " " in branch:
            raise ValueError("branch must be slash-delimited and contain no spaces.")
        if target_environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError("target_environment must be dev, staging, or prod.")
        if data_class not in ALLOWED_DATA_CLASSES:
            raise ValueError("data_class must be internal, confidential, or restricted.")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError("risk_level must be low, medium, or high.")
        if not isinstance(criteria, list) or not criteria:
            raise ValueError("acceptance_criteria must be a non-empty list.")
        if not all(isinstance(item, str) and item.strip() for item in criteria):
            raise ValueError("acceptance_criteria entries must be non-empty strings.")
        if not isinstance(touches_sensitive_data, bool) or not isinstance(changes_policy, bool):
            raise ValueError("Boolean fields must be boolean values.")
        if not isinstance(rollback_ready, bool):
            raise ValueError("rollback_ready must be a boolean.")
        if target_environment == "prod" and "rollback_ready" not in raw:
            raise ValueError("Production requests must declare rollback_ready.")

        return cls(
            objective=objective.strip(),
            branch=branch.strip(),
            target_environment=target_environment,
            data_class=data_class,
            acceptance_criteria=tuple(item.strip() for item in criteria),
            risk_level=risk_level,
            touches_sensitive_data=touches_sensitive_data,
            changes_policy=changes_policy,
            rollback_ready=rollback_ready,
        )


@dataclass(frozen=True)
class ControlPlan:
    approvers: tuple[str, ...]
    required_controls: tuple[str, ...]
    sandbox_tier: str
    blocking_issues: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "approvers": list(self.approvers),
            "required_controls": list(self.required_controls),
            "sandbox_tier": self.sandbox_tier,
            "blocking_issues": list(self.blocking_issues),
        }


@dataclass(frozen=True)
class AuditEvent:
    event_index: int
    recorded_at: str
    actor: str
    action: str
    payload_hash: str
    previous_hash: str
    chain_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_index": self.event_index,
            "recorded_at": self.recorded_at,
            "actor": self.actor,
            "action": self.action,
            "payload_hash": self.payload_hash,
            "previous_hash": self.previous_hash,
            "chain_hash": self.chain_hash,
        }
