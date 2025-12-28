import pandas as pd
from pathlib import Path

# Paths
CLEANED = Path("Cleaned")

# Load cleaned data
sales = pd.read_csv(CLEANED / "sales_clean.csv", parse_dates=["Date"])
features = pd.read_csv(CLEANED / "features_clean.csv", parse_dates=["Date"])
stores = pd.read_csv(CLEANED / "stores_clean.csv")

# =========================
# 1. Merge sales + features
# =========================
df = sales.merge(
    features,
    on=["Store_ID", "Date"],
    how="left"
)

# =========================
# 2. Merge with stores
# =========================
df = df.merge(
    stores,
    on="Store_ID",
    how="left"
)
# =========================
# 3. Safety checks
# =========================
print("Rows before merge:", len(sales))
print("Rows after merge :", len(df))

if len(df) != len(sales):
    raise ValueError("❌ Row count mismatch after merge!")

print("Missing Store_Type:", df["Store_Type"].isna().sum())
print("Missing Temperature:", df["Temperature"].isna().sum())

# Optional business flag: returns/refunds
df["Is_Return_Week"] = (df["Weekly_Sales"] < 0).astype(int)

# =========================
# 4. Save final dataset
# =========================
output_path = CLEANED / "retail_analytics.csv"
df.to_csv(output_path, index=False)

print("✅ Step 4 complete")
print("Final dataset saved as:", output_path)
print("Total columns:", len(df.columns))
print("\nPreview:")
print(df.head(3))