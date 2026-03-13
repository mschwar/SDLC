# ENVIRONMENTS.md

## Environment Policy

### Dev

- used for fast feedback
- low-risk changes may stop here if they are internal-only

### Staging

- required for medium- and high-risk changes
- required for customer-visible changes before production

### Prod

- requires rollback readiness
- requires release approval for high-risk changes
- requires stronger evidence for schema, auth, and infrastructure changes
