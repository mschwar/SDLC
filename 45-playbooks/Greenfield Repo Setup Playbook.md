---
tags:
  - playbook
  - setup
type: playbook
status: active
updated: 2026-03-10
---

# Greenfield Repo Setup Playbook

> [!summary] Goal
> Stand up the minimum viable agent-first workflow in a new repository without overbuilding.

## Steps

1. Create `AGENTS.md` from [[40-templates/AGENTS Template]].
2. Add architecture and decision notes as needed from [[40-templates/Architecture Template]] and [[40-templates/Decision Log Template]].
3. Add local checks from [[40-templates/Quality Checks Template]].
4. Add CI from [[40-templates/CI Workflow Template]].
5. Add PR structure from [[40-templates/PR Template]].
6. Enable branch protection.
7. Document the repo's definition of done.
8. Run one end-to-end trial task and inspect the weak points.

## Exit Criteria

- a task can go from prompt to merged PR without informal side-channel steps
- review is independent
- local and remote checks agree

## Related Notes

- [[agentic-sdlc-blueprint]]
- [[20-reference/Definition of Done]]
