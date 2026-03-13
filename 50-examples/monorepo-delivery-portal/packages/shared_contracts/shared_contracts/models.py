from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ALLOWED_STATUSES = {"queued", "in-review", "blocked", "ready"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
ALLOWED_DEPLOYMENT_TARGETS = {"none", "staging", "prod"}


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
class WorkItem:
    id: str
    title: str
    owner: str
    area: str
    status: str
    risk_level: str
    has_runbook: bool = False
    needs_migration: bool = False
    deployment_target: str = "none"

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "WorkItem":
        required_keys = ("id", "title", "owner", "area", "status", "risk_level")
        missing = [key for key in required_keys if key not in raw]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        item_id = _require_non_empty_string(raw, "id")
        title = _require_non_empty_string(raw, "title")
        owner = _require_non_empty_string(raw, "owner")
        area = _require_non_empty_string(raw, "area")
        status = _require_non_empty_string(raw, "status")
        risk_level = _require_non_empty_string(raw, "risk_level")

        if status not in ALLOWED_STATUSES:
            raise ValueError(f"status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError(f"risk_level must be one of: {', '.join(sorted(ALLOWED_RISK_LEVELS))}")

        deployment_target = raw.get("deployment_target", "none")
        if deployment_target not in ALLOWED_DEPLOYMENT_TARGETS:
            raise ValueError(
                f"deployment_target must be one of: {', '.join(sorted(ALLOWED_DEPLOYMENT_TARGETS))}"
            )

        return cls(
            id=item_id,
            title=title,
            owner=owner,
            area=area,
            status=status,
            risk_level=risk_level,
            has_runbook=_require_bool(raw, "has_runbook"),
            needs_migration=_require_bool(raw, "needs_migration"),
            deployment_target=deployment_target,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner,
            "area": self.area,
            "status": self.status,
            "risk_level": self.risk_level,
            "has_runbook": self.has_runbook,
            "needs_migration": self.needs_migration,
            "deployment_target": self.deployment_target,
        }


@dataclass(frozen=True)
class Summary:
    total_items: int
    status_counts: dict[str, int]
    high_risk_count: int
    blocked_items: tuple[str, ...]
    runbook_gaps: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_items": self.total_items,
            "status_counts": dict(self.status_counts),
            "high_risk_count": self.high_risk_count,
            "blocked_items": list(self.blocked_items),
            "runbook_gaps": list(self.runbook_gaps),
        }
