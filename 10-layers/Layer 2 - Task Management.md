---
tags:
  - sdlc
  - layer
  - orchestration
layer: 2
type: layer
status: active
updated: 2026-03-10
---

# Layer 2 - Task Management

> [!summary] Outcome
> Turn intent into bounded, executable work.
> The orchestrator controls scope, routing, and sequencing so workers do not improvise the backlog.

## What Happens Here

- Read the roadmap, repo state, and risk register
- choose the next task
- assign a branch and a short objective
- route only the relevant context to the worker

## Default Pattern

The roadmap is the backlog.

Worker prompt:

```text
Read AGENTS.md. [Objective in 1-3 sentences]. Branch: [name].
```

## Guardrails

- one branch per task
- explicit objective plus branch name
- no duplicate handoff docs when the answer already exists in the repo
- use repository maps before using longer prompts

## Scaling Pattern

When the repo becomes too large or work becomes ambiguous:

- add symbol maps, `ctags`, or language-server-driven retrieval
- add a clarifier or PM role to turn raw intent into acceptance criteria
- decompose work into smaller independent tasks before assigning workers

## Failure Modes

- silent scope creep
- low-quality retrieval from large repos
- ticket bloat that duplicates canonical docs

## Related Notes

- [[20-reference/Repository Maps]]
- [[20-reference/Agentic-First]]
- [[30-patterns/Swarm Orchestration]]
- [[40-templates/Spec Template]]
