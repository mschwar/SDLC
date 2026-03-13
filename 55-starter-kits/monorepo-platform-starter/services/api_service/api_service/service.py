from __future__ import annotations

import json
from pathlib import Path

from contracts.models import Item, Summary


def load_items(path: str | Path) -> tuple[Item, ...]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("Item file must contain a JSON array.")
    return tuple(Item.from_dict(item) for item in raw)


def build_summary(items: tuple[Item, ...]) -> Summary:
    status_counts = {status: 0 for status in ("queued", "in-review", "blocked", "ready")}
    high_risk_count = 0
    for item in items:
        status_counts[item.status] += 1
        if item.risk_level == "high":
            high_risk_count += 1
    return Summary(total_items=len(items), status_counts=status_counts, high_risk_count=high_risk_count)
