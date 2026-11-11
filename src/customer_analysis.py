"""Descriptive customer analysis using explicitly simulated transactions."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "customer_transactions_simulated.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["transaction_date"])
df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

monthly = (df.groupby("month", as_index=False)
             .agg(orders=("transaction_id", "nunique"),
                  customers=("customer_id", "nunique"),
                  revenue=("revenue", "sum")))
monthly["average_order_value"] = monthly["revenue"] / monthly["orders"]

segments = (df.groupby("category", as_index=False)
              .agg(orders=("transaction_id", "nunique"),
                   revenue=("revenue", "sum"),
                   units=("quantity", "sum"))
              .sort_values("revenue", ascending=False))

customer = (df.groupby("customer_id", as_index=False)
              .agg(orders=("transaction_id", "nunique"),
                   revenue=("revenue", "sum"))
              .sort_values("revenue", ascending=False))

monthly.to_csv(OUT / "monthly_summary.csv", index=False)
segments.to_csv(OUT / "category_summary.csv", index=False)
customer.to_csv(OUT / "customer_summary.csv", index=False)
print("Analysis complete. Results saved in outputs/.")
print("\\nMonthly summary:\\n", monthly.to_string(index=False))
print("\\nCategory summary:\\n", segments.to_string(index=False))
