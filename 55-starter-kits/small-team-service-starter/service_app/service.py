from __future__ import annotations

from .models import ReleasePlan, ReleaseRequest


def build_release_plan(request: ReleaseRequest) -> ReleasePlan:
    review_roles = ["reviewer"]
    required_gates = ["ci"]
    release_strategy = "direct"
    blocking_issues: list[str] = []

    if request.environment in {"staging", "prod"}:
        review_roles.append("service-owner")
        required_gates.append("staging-validation")
        release_strategy = "staged-rollout"

    if request.customer_visible or request.risk_level in {"medium", "high"}:
        review_roles.append("release-manager")
        required_gates.append("release-approval")

    if request.risk_level == "high":
        release_strategy = "canary"
        required_gates.append("human-approval")

    if request.environment == "prod" and not request.rollback_ready:
        blocking_issues.append("Production releases require rollback readiness.")

    return ReleasePlan(
        review_roles=tuple(dict.fromkeys(review_roles)),
        required_gates=tuple(dict.fromkeys(required_gates)),
        release_strategy=release_strategy,
        blocking_issues=tuple(blocking_issues),
    )
