---
tags:
  - sdlc
  - layer
  - version-control
layer: 4
type: layer
status: active
updated: 2026-03-10
---

# Layer 4 - Version Control

> [!summary] Outcome
> Keep history legible, scoped, and safe for parallel autonomous work.

## What Happens Here

- create task-scoped branches from `origin/main`
- keep commits small and structured
- use worktrees for parallel work
- preserve a reviewable history

## Rules

- one branch per task
- conventional commit messages
- branch from `origin/main`
- use worktrees when parallel tasks would otherwise contaminate each other

## Failure Modes

- mixed-scope branches
- unreadable commit history
- accidental cross-task file pollution

## Related Notes

- [[20-reference/Conventional Commits]]
- [[20-reference/Agentic-First]]
