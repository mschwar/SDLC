from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

ALLOWED_ENVIRONMENTS = {"dev", "staging", "prod"}
ALLOWED_CHANGE_TYPES = {"code", "schema", "config", "access", "policy"}
ALLOWED_DATA_CLASSES = {"internal", "confidential", "restricted"}
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
class ChangeRequest:
    system: str
    objective: str
    branch: str
    owner: str
    target_environment: str
    change_type: str
    data_class: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str = "low"
    touches_sensitive_data: bool = False
    changes_policy: bool = False
    vendor_impact: bool = False
    rollback_ready: bool = False
    evidence: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ChangeRequest":
        required_keys = (
            "system",
            "objective",
            "branch",
            "owner",
            "target_environment",
            "change_type",
            "data_class",
            "acceptance_criteria",
        )
        missing = [key for key in required_keys if key not in raw]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        system = _require_non_empty_string(raw, "system")
        objective = _require_non_empty_string(raw, "objective")
        branch = _require_non_empty_string(raw, "branch")
        owner = _require_non_empty_string(raw, "owner")
        target_environment = _require_non_empty_string(raw, "target_environment")
        change_type = _require_non_empty_string(raw, "change_type")
        data_class = _require_non_empty_string(raw, "data_class")

        if not BRANCH_PATTERN.match(branch) or " " in branch:
            raise ValueError("branch must be slash-delimited and contain no spaces.")
        if target_environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError(
                f"target_environment must be one of: {', '.join(sorted(ALLOWED_ENVIRONMENTS))}"
            )
        if change_type not in ALLOWED_CHANGE_TYPES:
            raise ValueError(f"change_type must be one of: {', '.join(sorted(ALLOWED_CHANGE_TYPES))}")
        if data_class not in ALLOWED_DATA_CLASSES:
            raise ValueError(f"data_class must be one of: {', '.join(sorted(ALLOWED_DATA_CLASSES))}")

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

        if target_environment == "prod" and "rollback_ready" not in raw:
            raise ValueError("Production requests must declare rollback_ready.")

        return cls(
            system=system,
            objective=objective,
            branch=branch,
            owner=owner,
            target_environment=target_environment,
            change_type=change_type,
            data_class=data_class,
            acceptance_criteria=tuple(item.strip() for item in criteria),
            risk_level=risk_level,
            touches_sensitive_data=_require_bool(raw, "touches_sensitive_data"),
            changes_policy=_require_bool(raw, "changes_policy"),
            vendor_impact=_require_bool(raw, "vendor_impact"),
            rollback_ready=_require_bool(raw, "rollback_ready"),
            evidence=tuple(item.strip() for item in evidence),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "system": self.system,
            "objective": self.objective,
            "branch": self.branch,
            "owner": self.owner,
            "target_environment": self.target_environment,
            "change_type": self.change_type,
            "data_class": self.data_class,
            "acceptance_criteria": list(self.acceptance_criteria),
            "risk_level": self.risk_level,
            "touches_sensitive_data": self.touches_sensitive_data,
            "changes_policy": self.changes_policy,
            "vendor_impact": self.vendor_impact,
            "rollback_ready": self.rollback_ready,
            "evidence": list(self.evidence),
        }


@dataclass(frozen=True)
class ControlPacket:
    system: str
    approvers: tuple[str, ...]
    required_controls: tuple[str, ...]
    sandbox_tier: str
    required_evidence: tuple[str, ...]
    retention_class: str
    blocking_issues: tuple[str, ...]
    summary: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "system": self.system,
            "approvers": list(self.approvers),
            "required_controls": list(self.required_controls),
            "sandbox_tier": self.sandbox_tier,
            "required_evidence": list(self.required_evidence),
            "retention_class": self.retention_class,
            "blocking_issues": list(self.blocking_issues),
            "summary": self.summary,
        }


@dataclass(frozen=True)
class AuditEvent:
    event_index: int
    recorded_at: str
    actor: str
    action: str
    system: str
    payload_hash: str
    previous_hash: str
    chain_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_index": self.event_index,
            "recorded_at": self.recorded_at,
            "actor": self.actor,
            "action": self.action,
            "system": self.system,
            "payload_hash": self.payload_hash,
            "previous_hash": self.previous_hash,
            "chain_hash": self.chain_hash,
        }
