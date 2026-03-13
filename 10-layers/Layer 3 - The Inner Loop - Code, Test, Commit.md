---
tags:
  - sdlc
  - layer
  - inner-loop
layer: 3
type: layer
status: active
updated: 2026-03-10
---

# Layer 3 - The Inner Loop - Code, Test, Commit

> [!summary] Outcome
> Make the local execution loop fast, repeatable, and hard to bypass.
> This layer is where agent speed becomes real engineering speed.

## What Happens Here

- write code
- run local quality checks
- repair failures
- commit only after the checks pass

## Core Controls

- git hooks for blocking validation
- an explicit test-first loop where useful
- direct feedback from compiler, runtime, and test failures
- short repair cycles before code leaves the machine

## Agent-Native TDD

Use Red -> Green -> Blue when the task has meaningful behavioral logic:

1. write or generate the test and watch it fail
2. make the smallest change that passes
3. refactor, simplify, lint, and re-run

## Structured Editing

If the stack supports it, prefer AST- or LSP-aware edits over blind text editing. This reduces symbol mistakes, broken syntax, and formatting drift.

## Failure Modes

- hooks are advisory rather than structural
- the agent writes code without validating behavior
- failures are read by humans instead of being routed back into the local repair loop

## Related Notes

- [[20-reference/Git Hooks]]
- [[20-reference/Shift-Left Testing]]
- [[20-reference/Property-Based Testing]]
- [[20-reference/Mutation Testing]]
- [[20-reference/Inner Loop vs Outer Loop]]
- [[40-templates/Quality Checks Template]]
