# DATA_CLASSIFICATION.md

| Data Class | Allowed Storage | Allowed Models | Logging Rules | Approval Needed |
|------------|-----------------|----------------|---------------|-----------------|
| internal | repo or local machine | approved default models | normal logging | reviewer |
| confidential | approved internal storage | approved internal models | minimize logged content | service-owner |
| restricted | restricted environment only | no external model access | log only audit metadata | privacy-officer |
