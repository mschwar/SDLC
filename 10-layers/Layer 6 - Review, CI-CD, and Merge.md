---
tags:
  - sdlc
  - layer
  - review
  - ci
layer: 6
type: layer
status: active
updated: 2026-03-10
---

# Layer 6 - Review, CI-CD, and Merge

> [!summary] Outcome
> Verify changes in a clean environment, keep review independent from implementation, and merge only when the branch is provably ready.

## What Happens Here

- CI re-runs quality checks remotely
- a review agent or human reviews the diff
- fixes are pushed to the branch when necessary
- protected branches block unsafe merges

## Review Model

Baseline checklist:

1. does the diff match the stated objective
2. do checks pass
3. is there hidden scope creep
4. are there security or safety issues
5. does the change fit existing patterns

Advanced mode:

- use a different reviewer role or model family
- prompt it adversarially
- require artifacts in the PR
- score risk before merge

## CI Model

- run the same core checks locally and remotely
- treat local hooks as the first gate
- treat CI as the clean-environment confirmation gate
- optionally add a repair agent for routine CI failures

## Merge Controls

- branch protection
- review approval
- passing status checks
- merge queue only when concurrency demands it

## Failure Modes

- agents reviewing or approving their own work
- green local state but broken remote environment
- stale PRs merging into a changed base branch

## Related Notes

- [[20-reference/CI-CD]]
- [[20-reference/GitHub Actions]]
- [[20-reference/Code Review]]
- [[20-reference/Branch Protection Rules]]
- [[20-reference/Merge Queues]]
- [[20-reference/Adversarial Verification]]
- [[40-templates/CI Workflow Template]]
- [[40-templates/PR Template]]
