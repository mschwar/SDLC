---
tags:
  - pattern
  - risks
type: pattern
status: active
updated: 2026-03-10
---

# Advanced Failure Modes

> [!warning] Watch List
> As autonomy rises, the dominant failures become structural:
> context degradation, cascading hallucination, and oversized permission blast radius.

## Failure Modes

- context degradation from oversized prompts or poor retrieval
- one flawed assumption propagating across architect, coder, tester, and deployer stages
- agents receiving broad cloud, data, or production permissions

## Countermeasures

- smaller tasks
- better repository maps
- stronger contracts
- stricter permissions
- independent review and approval gates

## Related Notes

- [[20-reference/Repository Maps]]
- [[20-reference/Contract-Driven Development]]
- [[20-reference/Observability]]
- [[30-patterns/Higher-Autonomy Setup]]
