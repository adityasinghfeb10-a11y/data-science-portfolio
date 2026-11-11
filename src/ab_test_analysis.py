"""Two-proportion A/B test on simulated binary conversion outcomes."""
from pathlib import Path
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "ab_test_simulated.csv")

summary = df.groupby("group")["converted"].agg(["sum", "count"])
counts = summary["sum"].to_numpy()
nobs = summary["count"].to_numpy()
rates = counts / nobs
z_stat, p_value = proportions_ztest(counts, nobs)

print(summary)
print(f"Control conversion rate:   {rates[0]:.2%}")
print(f"Treatment conversion rate: {rates[1]:.2%}")
print(f"Absolute difference:       {rates[1]-rates[0]:.2%}")
print(f"Z statistic:               {z_stat:.3f}")
print(f"Two-sided p-value:         {p_value:.4f}")
print("Interpretation: this is a simulated exercise, not evidence about a real product.")
