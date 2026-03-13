from __future__ import annotations

import json
from pathlib import Path

from shared_contracts.models import Summary, WorkItem


def load_work_items(path: str | Path) -> tuple[WorkItem, ...]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("Work item file must contain a JSON array.")
    return tuple(WorkItem.from_dict(item) for item in raw)


def build_summary(items: tuple[WorkItem, ...]) -> Summary:
    status_counts = {status: 0 for status in ("queued", "in-review", "blocked", "ready")}
    blocked_items: list[str] = []
    runbook_gaps: list[str] = []
    high_risk_count = 0

    for item in items:
        status_counts[item.status] += 1
        if item.status == "blocked":
            blocked_items.append(item.id)
        if item.risk_level == "high":
            high_risk_count += 1
            if not item.has_runbook:
                runbook_gaps.append(item.id)

    return Summary(
        total_items=len(items),
        status_counts=status_counts,
        high_risk_count=high_risk_count,
        blocked_items=tuple(blocked_items),
        runbook_gaps=tuple(runbook_gaps),
    )
