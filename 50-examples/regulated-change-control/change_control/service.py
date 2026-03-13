from __future__ import annotations

from .models import ChangeRequest, ControlPacket


def _unique(items: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return tuple(ordered)


def _retention_class(data_class: str) -> str:
    if data_class == "restricted":
        return "seven-years"
    if data_class == "confidential":
        return "three-years"
    return "one-year"


def build_control_packet(request: ChangeRequest) -> ControlPacket:
    approvers = ["reviewer"]
    required_controls = ["ci", "traceability-check"]
    required_evidence = ["tests"]
    sandbox_tier = "standard"
    blocking_issues: list[str] = []

    if request.target_environment in {"staging", "prod"}:
        approvers.append("service-owner")
        required_controls.append("environment-approval")
        required_evidence.append("deployment-plan")

    if request.risk_level in {"medium", "high"}:
        approvers.append("release-manager")
        required_controls.append("two-person-review")
        required_evidence.append("risk-assessment")

    if request.data_class == "confidential":
        sandbox_tier = "hardened"
        required_evidence.append("data-handling-checklist")

    if request.data_class == "restricted" or request.touches_sensitive_data:
        sandbox_tier = "restricted"
        approvers.append("privacy-officer")
        required_controls.append("data-handling-review")
        required_evidence.append("redaction-check")

    if request.change_type == "schema":
        approvers.append("architecture-reviewer")
        required_controls.append("architecture-review")
        required_evidence.append("migration-plan")

    if request.change_type == "access":
        approvers.append("security-reviewer")
        required_controls.append("access-review")
        required_evidence.append("access-diff")

    if request.change_type == "policy" or request.changes_policy:
        approvers.append("policy-approver")
        required_controls.append("policy-approval")
        required_evidence.append("policy-diff")

    if request.vendor_impact:
        approvers.append("vendor-risk-reviewer")
        required_controls.append("vendor-review")
        required_evidence.append("vendor-assessment")

    if request.target_environment == "prod":
        required_controls.append("release-approval")
        required_evidence.append("rollback-plan")

    if request.target_environment == "prod" and request.risk_level == "high":
        approvers.append("compliance-officer")
        required_controls.append("release-board-approval")

    if request.target_environment == "prod" and not request.rollback_ready:
        blocking_issues.append("Production changes require rollback readiness.")

    summary = (
        f"{request.system} requires {len(_unique(approvers))} approver(s), "
        f"{len(_unique(required_controls))} control(s), and {sandbox_tier} sandboxing."
    )

    return ControlPacket(
        system=request.system,
        approvers=_unique(approvers),
        required_controls=_unique(required_controls),
        sandbox_tier=sandbox_tier,
        required_evidence=_unique(required_evidence),
        retention_class=_retention_class(request.data_class),
        blocking_issues=tuple(blocking_issues),
        summary=summary,
    )
