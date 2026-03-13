from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ALLOWED_STATUSES = {"queued", "in-review", "blocked", "ready"}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}


@dataclass(frozen=True)
class Item:
    id: str
    title: str
    owner: str
    status: str
    risk_level: str = "low"

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Item":
        item_id = raw.get("id")
        title = raw.get("title")
        owner = raw.get("owner")
        status = raw.get("status")
        risk_level = raw.get("risk_level", "low")

        if not all(isinstance(value, str) and value.strip() for value in (item_id, title, owner, status)):
            raise ValueError("id, title, owner, and status must be non-empty strings.")
        if status not in ALLOWED_STATUSES:
            raise ValueError("status must be queued, in-review, blocked, or ready.")
        if risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError("risk_level must be low, medium, or high.")

        return cls(item_id.strip(), title.strip(), owner.strip(), status, risk_level)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner,
            "status": self.status,
            "risk_level": self.risk_level,
        }


@dataclass(frozen=True)
class Summary:
    total_items: int
    status_counts: dict[str, int]
    high_risk_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_items": self.total_items,
            "status_counts": dict(self.status_counts),
            "high_risk_count": self.high_risk_count,
        }
