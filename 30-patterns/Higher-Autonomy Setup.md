---
tags:
  - pattern
  - autonomy
type: pattern
status: active
updated: 2026-03-10
---

# Higher-Autonomy Setup

> [!summary] Use
> Add more autonomy only after the basic repo guardrails are already trustworthy.

## Required Before You Scale

- strong local quality gates
- CI parity with local checks
- independent review
- branch protection
- stable telemetry

## Additions

- spec approval gate
- architecture review gate
- deployment authorization gate
- sandboxed run-fail-fix loops
- read-only production by default
- explicit escalation rules

## Related Notes

- [[10-layers/Layer 7 - Deployment and Feedback]]
- [[20-reference/Observability]]
- [[30-patterns/Advanced Failure Modes]]
