# SLOS.md

## Service Targets

- availability: 99.9 percent monthly for the `/plan` endpoint
- latency: 95th percentile under 250 ms for local-sized requests
- correctness: release plans for representative fixtures remain stable unless deliberately changed

## Alerting Triggers

- endpoint unavailable
- repeated 500 responses
- smoke test failures after deployment
- unexpected increase in rejected low-risk requests
