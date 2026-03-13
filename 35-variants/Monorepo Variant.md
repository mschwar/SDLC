---
tags:
  - variant
  - monorepo
type: variant
status: active
updated: 2026-03-10
---

# Monorepo Variant

> [!summary] Fit
> Use this when a single repository contains multiple deployable services, packages, or domains.

## Additions

- path-based CI triggers
- package-scoped contracts and ownership
- scoped commit conventions
- stronger repository maps
- task routing that respects package boundaries

## Risks

- too much irrelevant context in each task
- large CI cost for small changes
- accidental cross-domain edits

## Related Notes

- [[20-reference/Repository Maps]]
- [[20-reference/Memory and Retrieval Strategy]]
