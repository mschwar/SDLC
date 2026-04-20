---
title: "Agentic Principles Playbook"
principle: "Index"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Agentic Principles Playbook

A curated, agent-optimized reference of 15 engineering principles for designing, building, and operating production-grade multi-agent LLM systems. Each sheet is self-contained, machine-readable, and structured so that autonomous agents can retrieve, apply, and self-evaluate against a single principle without loading the full playbook. Use this index as the canonical entry point when an agent needs to reason about architecture, prompt design, orchestration, evaluation, or safety.

## Table of Contents

1. [DRY – Don't Repeat Yourself](./01-dry.md)
2. [TDD – Test-Driven Development](./02-tdd.md)
3. [SOLID – Five Object-Oriented Design Principles](./03-solid.md)
4. [KISS – Keep It Simple, Stupid](./04-kiss.md)
5. [YAGNI – You Aren't Gonna Need It](./05-yagni.md)
6. [Tell, Don't Ask (TDA)](./06-tell-dont-ask.md)
7. [Law of Demeter (LoD) / Principle of Least Knowledge](./07-law-of-demeter.md)
8. [Composition over Inheritance](./08-composition-over-inheritance.md)
9. [Narrow Scope / Single Responsibility per Agent](./09-narrow-scope.md)
10. [Reflection (Self-Evaluation / Plan-Act-Reflect)](./10-reflection.md)
11. [Observability-First Design](./11-observability-first.md)
12. [Human-in-the-Loop (HITL) + Guardrails](./12-hitl-guardrails.md)
13. [Structured Output + Idempotency](./13-structured-output-idempotency.md)
14. [Evaluation-Driven Development (EDD)](./14-evaluation-driven-development.md)
15. [Multi-Agent Orchestration Patterns (ReAct, Supervisor, etc.)](./15-multi-agent-orchestration.md)

## How to Use This Playbook

- **Retrieve one sheet at a time.** Each principle is a standalone document. Load only the sheet relevant to the current architectural or prompt-design decision to minimize context bloat.
- **Treat Core Rules as hard constraints.** When an agent is planning an action, the `Core Rules` and `Quick Checklist` sections double as guardrails — validate proposed outputs against them before execution.
- **Drive evaluations from the Quick Checklist.** Each sheet's checklist can be lifted directly into an LLM-as-a-judge rubric or a deterministic CI check for Evaluation-Driven Development (see Sheet 14).
- **Compose principles, don't stack them.** When multiple sheets apply (e.g., Narrow Scope + Observability + HITL), compose the rules rather than duplicating logic — consistent with DRY and Composition over Inheritance.
