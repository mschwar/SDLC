---
tags:
  - variant
  - solo
type: variant
status: active
updated: 2026-03-10
---

# Solo Repo Variant

> [!summary] Fit
> Use this when one human operator runs the repo and agent review is the main independence mechanism.

## Simplifications

- roadmap can remain the backlog
- one orchestrator plus one worker plus one reviewer is enough
- merge queues are usually unnecessary
- metrics can stay lightweight and git-derived

## Non-Negotiables

- blocking local checks
- CI parity with local checks
- branch protection
- independent review before merge

## Related Notes

- [[agentic-sdlc-blueprint]]
- [[10-layers/Layer 6 - Review, CI-CD, and Merge]]
