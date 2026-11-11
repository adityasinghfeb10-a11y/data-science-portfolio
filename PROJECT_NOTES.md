# Project notes and interview talking points

## Customer analysis
- Grain: one row per transaction.
- Revenue: quantity multiplied by unit price.
- Useful metrics: monthly revenue, distinct orders, distinct customers, average order value, and category revenue.
- Caveat: this dataset is simulated, so patterns are illustrative only.

## A/B test
- Outcome: binary conversion indicator (0/1).
- Comparison: treatment conversion proportion minus control conversion proportion.
- Test: two-sided two-proportion z-test.
- Discuss both effect size and uncertainty; do not use a p-value alone to make a product decision.
- Caveat: data is simulated and the experiment assumptions are for practice.
