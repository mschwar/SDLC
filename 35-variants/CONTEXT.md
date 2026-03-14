---
generated: '2026-03-14T00:30:44Z'
generator: ctx/0.1.0
model: claude-haiku-4-5-20251001
content_hash: sha256:d0abc3052f8a33100399668251853f9e7b7607bb67222d1e3ce5d56ff698ef8f
files: 5
dirs: 0
tokens_total: 854
---
# C:/Users/Matty/Documents/SDLC/35-variants

Specialized SDLC practice variants for different repository and team configurations.

## Files

- **Deployed Product Variant.md** — Deployed Product Variant describes when to use deployment-focused practices including rollout policies, rollback procedures, and production telemetry for merges affecting staging or production environments.
- **Monorepo Variant.md** — Monorepo Variant outlines practices for repositories containing multiple deployable services, emphasizing path-based CI triggers, package-scoped ownership, and stronger repository maps to manage cross-domain complexity.
- **Regulated Environment Variant.md** — Regulated Environment Variant specifies compliance-focused additions such as approval gates, audit logs, identity controls, and formal evidence requirements for environments with traceability and regulatory constraints.
- **Small Team Variant.md** — Small Team Variant provides coordination mechanisms for shared repository ownership including CODEOWNERS rules, tighter PR expectations, branch protection, and consistent policy conventions across team members.
- **Solo Repo Variant.md** — Solo Repo Variant simplifies practices for single-operator repositories by reducing overhead while maintaining non-negotiable safeguards like blocking local checks, CI parity, branch protection, and independent agent review.

## Subdirectories

- None

## Notes

- Each variant file documents context-specific adaptations to core SDLC practices.
- Variants address different scales (solo to team), architectures (monorepo), deployment targets (production), and regulatory requirements.