---
tags:
  - examples
  - python
  - regulated
  - auditability
type: example
status: active
updated: 2026-03-10
---

# Regulated Change Control Example

> [!summary] Use
> This is a fully worked example repo for a regulated environment where traceability, data handling, approval boundaries, and durable audit evidence materially change the workflow.

## Example Repo

- [[50-examples/regulated-change-control/README]]

## What It Demonstrates

- Layer 1: repo constitution plus explicit compliance, approval, and sandbox artifacts
- Layer 3: a deterministic local loop with audit-log validation
- Layer 5 and 6: separation-of-duties enforcement through approver and evidence rules
- Layer 7: operational readiness through incident, retention, and control-objective documentation

## Recommended Reading Path

1. [[50-examples/regulated-change-control/README]]
2. [[50-examples/regulated-change-control/AGENTS]]
3. [[50-examples/regulated-change-control/APPROVAL_MATRIX]]
4. [[50-examples/regulated-change-control/SANDBOX_POLICY]]
5. [[50-examples/regulated-change-control/AUDIT_LOG_POLICY]]
6. [[50-examples/regulated-change-control/scripts/run_quality_checks.py]]

## Related Notes

- [[35-variants/Regulated Environment Variant]]
- [[20-reference/Compliance and Auditability]]
- [[20-reference/Separation of Duties]]
- [[20-reference/Permissions and Sandbox Policy]]
- [[20-reference/Data Governance and Privacy]]
