---
tags:
  - pattern
  - documentation
type: pattern
status: active
updated: 2026-03-10
---

# Documentation Drift and Process Erosion

> [!warning] Use
> This pattern describes what happens when the repo keeps the appearance of a process but the docs, prompts, and actual behavior stop matching.

## Warning Signs

- instructions only exist in chat history
- archived notes still look active
- templates diverge from live practice
- humans override the process informally
- prompts encode rules that are absent from the repo

## Recovery

- restore canonical note ownership
- archive superseded docs aggressively
- update definition of done to require doc maintenance
- review prompts and policies as first-class artifacts

## Related Notes

- [[20-reference/Documentation Governance]]
- [[20-reference/Prompt and Policy Management]]
- [[45-playbooks/Architecture and Process Change Playbook]]
