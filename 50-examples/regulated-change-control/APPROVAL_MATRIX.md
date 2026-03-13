# APPROVAL_MATRIX.md

| Trigger | Required Approvers | Required Controls |
|---------|--------------------|-------------------|
| any change | reviewer | ci, traceability-check |
| staging or prod | service-owner | environment-approval |
| medium or high risk | release-manager | two-person-review |
| restricted data or sensitive data | privacy-officer | data-handling-review |
| policy change | policy-approver | policy-approval |
| schema change | architecture-reviewer | architecture-review |
| vendor impact | vendor-risk-reviewer | vendor-review |
| prod high risk | compliance-officer | release-board-approval |
