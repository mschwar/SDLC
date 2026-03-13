---
tags:
  - sdlc
  - layer
  - pull-requests
layer: 5
type: layer
status: active
updated: 2026-03-10
---

# Layer 5 - Pull Requests

> [!summary] Outcome
> Make every branch visible, reviewable, and evidence-bearing as early as possible.

## What Happens Here

- push the branch automatically after commit
- open a draft PR automatically when possible
- keep the PR visible while work is still in progress
- promote to ready only after review criteria are met

## PR Expectations

- clear scope matched to the branch objective
- evidence, not just claims
- UI changes include screenshots or traces
- service changes include contract or integration-test evidence

## Failure Modes

- finished work sits on invisible branches
- PRs become status theater without test proof
- ready-state is used as a substitute for review quality

## Related Notes

- [[20-reference/Draft PRs and Ready PRs]]
- [[20-reference/Code Review]]
- [[40-templates/PR Template]]
