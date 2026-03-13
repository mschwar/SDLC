---
tags:
  - reference
  - governance
type: concept
status: active
updated: 2026-03-10
---

# Human-in-the-Loop Gates

> [!abstract] Definition
> Explicit decision points where a human must approve, redirect, or reject agent action before the workflow continues.

## Common Gates

- spec approval
- architecture approval
- release approval
- production-change approval
- policy escalation approval

## Design Rule

Use gates at points where errors are expensive, hard to reverse, or risky to automate.

## Related Notes

- [[30-patterns/Higher-Autonomy Setup]]
- [[35-variants/Regulated Environment Variant]]
- [[20-reference/Separation of Duties]]
