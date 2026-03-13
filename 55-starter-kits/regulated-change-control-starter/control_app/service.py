from __future__ import annotations

from .models import ChangeRequest, ControlPlan


def build_control_plan(request: ChangeRequest) -> ControlPlan:
    approvers = ["reviewer"]
    required_controls = ["ci", "traceability-check"]
    sandbox_tier = "standard"
    blocking_issues: list[str] = []

    if request.target_environment in {"staging", "prod"}:
        approvers.append("service-owner")
        required_controls.append("environment-approval")

    if request.risk_level in {"medium", "high"}:
        approvers.append("release-manager")
        required_controls.append("two-person-review")

    if request.data_class == "restricted" or request.touches_sensitive_data:
        approvers.append("privacy-officer")
        required_controls.append("data-handling-review")
        sandbox_tier = "restricted"
    elif request.data_class == "confidential":
        sandbox_tier = "hardened"

    if request.changes_policy:
        approvers.append("policy-approver")
        required_controls.append("policy-approval")

    if request.target_environment == "prod" and request.risk_level == "high":
        approvers.append("compliance-officer")
        required_controls.append("release-board-approval")

    if request.target_environment == "prod" and not request.rollback_ready:
        blocking_issues.append("Production changes require rollback readiness.")

    return ControlPlan(
        approvers=tuple(dict.fromkeys(approvers)),
        required_controls=tuple(dict.fromkeys(required_controls)),
        sandbox_tier=sandbox_tier,
        blocking_issues=tuple(blocking_issues),
    )
