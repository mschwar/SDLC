from __future__ import annotations

from .models import ReleasePlan, ReleaseRequest


def _unique(items: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return tuple(ordered)


def _allowed_environments(environment: str) -> tuple[str, ...]:
    if environment == "dev":
        return ("dev",)
    if environment == "staging":
        return ("dev", "staging")
    return ("dev", "staging", "prod")


def build_release_plan(request: ReleaseRequest) -> ReleasePlan:
    review_roles = ["reviewer"]
    required_gates = ["ci"]
    required_evidence = ["tests"]
    blocking_issues: list[str] = []

    allowed_environments = _allowed_environments(request.environment)
    rollout_strategy = "direct"

    if request.environment in {"staging", "prod"}:
        review_roles.append("service-owner")
        required_evidence.append("staging-verification")
        rollout_strategy = "staged-rollout"

    if request.customer_visible or request.risk_level in {"medium", "high"}:
        review_roles.append("release-manager")
        required_gates.append("staging-validation")
        required_evidence.append("release-notes")
        rollout_strategy = "staged-rollout"

    if request.environment == "prod":
        required_gates.append("release-approval")
        required_evidence.append("rollback-plan")

    if request.risk_level == "high":
        required_gates.append("human-approval")
        rollout_strategy = "canary"

    if request.touches_auth:
        review_roles.append("security-reviewer")
        required_gates.append("security-review")
        required_evidence.append("security-test")
        rollout_strategy = "canary"

    if request.touches_schema or request.requires_migration or request.change_type == "schema":
        review_roles.append("architecture-reviewer")
        required_gates.append("architecture-review")
        required_evidence.append("schema-validation")
        rollout_strategy = "canary"

    if request.requires_migration:
        required_evidence.append("migration-plan")

    if request.needs_data_review:
        review_roles.append("data-reviewer")
        required_gates.append("data-review")
        required_evidence.append("data-impact-review")

    if request.change_type == "infrastructure":
        review_roles.append("sre-reviewer")
        required_gates.append("ops-review")
        required_evidence.append("ops-checklist")
        rollout_strategy = "canary"

    if request.environment == "prod" and not request.rollback_ready:
        blocking_issues.append("Production releases require rollback readiness.")

    summary = (
        f"{request.service} uses {rollout_strategy} with "
        f"{len(_unique(review_roles))} review role(s) and {len(_unique(required_gates))} gate(s)."
    )

    return ReleasePlan(
        service=request.service,
        review_roles=_unique(review_roles),
        required_gates=_unique(required_gates),
        allowed_environments=allowed_environments,
        rollout_strategy=rollout_strategy,
        required_evidence=_unique(required_evidence),
        blocking_issues=tuple(blocking_issues),
        summary=summary,
    )
