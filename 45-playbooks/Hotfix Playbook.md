---
tags:
  - playbook
  - incidents
type: playbook
status: active
updated: 2026-03-10
---

# Hotfix Playbook

> [!summary] Goal
> Resolve a production or high-severity defect quickly without abandoning evidence, review, or rollback discipline.

## Steps

1. Confirm severity and impact.
2. Contain or rollback if necessary.
3. Open a hotfix branch with a clear objective.
4. Reproduce the failure in the safest environment available.
5. Implement the smallest viable fix.
6. Run targeted local and CI validation.
7. Obtain the required approval gate.
8. Deploy using the chosen release strategy.
9. Record follow-up actions and postmortem work.

## Related Notes

- [[20-reference/Incident Response]]
- [[20-reference/Release Management]]
- [[20-reference/Postmortems]]
- [[40-templates/Incident Response Template]]
