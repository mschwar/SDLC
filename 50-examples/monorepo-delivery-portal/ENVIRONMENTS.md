# ENVIRONMENTS.md

## Environment Policy

### Local

- single-process server for fast feedback
- uses fixture data from `examples/work-items.json`

### Staging

- validates API plus static portal rendering path
- used for UI and contract sanity before production

### Prod

- serves the same contract surface as staging
- requires evidence for high-risk or migration-flagged items
