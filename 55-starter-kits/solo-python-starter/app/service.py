from __future__ import annotations

from .models import WorkPlan, WorkRequest


def build_work_plan(request: WorkRequest) -> WorkPlan:
    review_roles = ["reviewer"]
    required_gates: list[str] = []

    if request.risk_level in {"medium", "high"}:
        review_roles.append("owner")
        required_gates.append("ci")

    if request.risk_level == "high":
        review_roles.append("security-reviewer")
        required_gates.append("human-approval")

    summary = f"{request.objective} requires {len(review_roles)} review role(s)."
    return WorkPlan(
        review_roles=tuple(review_roles),
        required_gates=tuple(required_gates),
        summary=summary,
    )
