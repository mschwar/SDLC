---
tags:
  - examples
  - python
  - solo-repo
type: example
status: active
updated: 2026-03-10
---

# Solo Python Task Router Example

> [!summary] Use
> This is a fully worked example repo that applies the vault to a small, self-contained Python project.
> It demonstrates the minimum viable agent-first workflow with real docs, source code, tests, hooks, CI, and PR structure.

## Example Repo

- [[50-examples/solo-python-task-router/README]]

## What It Demonstrates

- Layer 1: repo constitution with `AGENTS.md`, `ARCHITECTURE.md`, `SCHEMA.md`, and `DECISIONS.md`
- Layer 3: local quality enforcement through `scripts/run_quality_checks.py`
- Layer 5 and 6: evidence-bearing PR structure and CI parity
- Layer 7: a lightweight release path appropriate for a solo, non-deployed repo

## Recommended Reading Path

1. [[50-examples/solo-python-task-router/README]]
2. [[50-examples/solo-python-task-router/AGENTS]]
3. [[50-examples/solo-python-task-router/scripts/run_quality_checks.py]]
4. [[50-examples/solo-python-task-router/.github/workflows/ci.yml]]
5. [[50-examples/solo-python-task-router/tests/test_service.py]]

## Related Notes

- [[35-variants/Solo Repo Variant]]
- [[45-playbooks/Greenfield Repo Setup Playbook]]
- [[40-templates/AGENTS Template]]
