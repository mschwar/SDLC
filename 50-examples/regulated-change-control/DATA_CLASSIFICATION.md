# DATA_CLASSIFICATION.md

| Data Class | Allowed Storage | Allowed Models | Logging Rules | Approval Needed |
|------------|-----------------|----------------|---------------|-----------------|
| internal | repo or local machine | standard approved models | normal debug logging allowed | reviewer |
| confidential | approved internal storage only | approved internal models only | minimize fields and redact identifiers | service-owner |
| restricted | approved restricted environment only | no external model access | log only audit metadata, never raw content | privacy-officer and compliance-officer |
