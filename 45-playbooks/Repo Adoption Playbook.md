---
tags:
  - playbook
  - adoption
type: playbook
status: active
updated: 2026-03-10
---

# Repo Adoption Playbook

> [!summary] Goal
> Introduce the blueprint into an existing repo incrementally instead of attempting a full process rewrite in one pass.

## Steps

1. Add the smallest possible onboarding note.
2. Introduce local checks before advanced automation.
3. Add CI that mirrors the local checks.
4. Require evidence-bearing PRs.
5. Add contracts only where ambiguity is painful.
6. Improve retrieval and repo mapping once the repo size demands it.
7. Add deployment, governance, and autonomy controls only after the baseline is stable.

## Anti-Pattern

Do not add swarm orchestration, machine-readable specs, and self-healing operations all at once to a repo that still lacks basic checks and branch protection.

## Related Notes

- [[50-examples/Example Implementation Roadmap]]
- [[35-variants/Solo Repo Variant]]
- [[35-variants/Small Team Variant]]
