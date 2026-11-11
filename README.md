# Data Science Portfolio — Aditya Singh

This repository contains two beginner-to-intermediate portfolio exercises demonstrating Python, SQL, descriptive analytics, and statistical testing.

## Projects

### 1. Customer transaction analysis
- Clean and inspect transaction-level data.
- Calculate monthly revenue, order counts, customer counts, and average order value.
- Compare revenue and units across product categories.
- Rank customers by total revenue.
- See `src/customer_analysis.py` and `sql/customer_analysis.sql`.

### 2. A/B test analysis
- Compare simulated conversion rates between control and treatment groups.
- Calculate absolute conversion-rate difference and a two-proportion z-test.
- Interpret the p-value cautiously; statistical significance is not the same as business importance.
- See `src/ab_test_analysis.py`.

## Run locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/customer_analysis.py
python src/ab_test_analysis.py
```


