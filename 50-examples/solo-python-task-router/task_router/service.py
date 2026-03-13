from __future__ import annotations

from .models import TaskSpec, WorkflowDecision


def _dedupe(values: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return tuple(ordered)


def build_workflow_decision(spec: TaskSpec) -> WorkflowDecision:
    review_roles = ["reviewer"]
    required_gates: list[str] = []
    local_checks = ["python scripts/run_quality_checks.py"]
    notes: list[str] = []
    release_strategy = "merge-to-main"

    if spec.risk_level in {"medium", "high"}:
        review_roles.append("senior-reviewer")
        notes.append("Use a narrower review scope and attach explicit evidence.")
        if spec.risk_level == "medium":
            release_strategy = "staged-rollout"

    if spec.touches_schema:
        review_roles.append("architecture-reviewer")
        required_gates.append("architecture-review")
        notes.append("Document schema impact before merge.")

    if spec.touches_auth:
        review_roles.append("security-reviewer")
        required_gates.append("security-review")
        notes.append("Review authentication and authorization paths explicitly.")

    if spec.requires_ui_validation:
        local_checks.append("capture-ui-evidence")
        notes.append("Attach screenshots or traces for UI-affecting changes.")

    if spec.needs_production_access:
        required_gates.append("release-approval")
        release_strategy = "staged-rollout"
        notes.append("Production access should remain read-only until approval is granted.")

    if spec.risk_level == "high":
        required_gates.append("human-approval")
        release_strategy = "canary"
        notes.append("Treat the change as high-risk and prefer progressive exposure.")

    return WorkflowDecision(
        review_roles=_dedupe(review_roles),
        required_gates=_dedupe(required_gates),
        local_checks=_dedupe(local_checks),
        release_strategy=release_strategy,
        notes=_dedupe(notes),
    )
