---
tags:
  - pattern
  - risks
type: pattern
status: active
updated: 2026-03-10
---

# Workflow Anti-Patterns

> [!warning] Use
> These are common ways agent-first workflows fail while still looking productive.

## Anti-Patterns

- adding autonomy before adding guardrails
- replacing architecture with prompts
- letting one agent write, review, and approve the same change
- using longer prompts instead of better retrieval
- shipping without evidence
- keeping multiple “canonical” docs alive
- overfitting the process to one model or vendor

## Countermoves

- smaller tasks
- stronger contracts
- independent review
- clear ownership
- versioned prompts and policies
- routine documentation hygiene

## Related Notes

- [[30-patterns/Advanced Failure Modes]]
- [[20-reference/Documentation Governance]]
- [[20-reference/Prompt and Policy Management]]
