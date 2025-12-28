import pandas as pd
from pathlib import Path

CLEANED = Path("Cleaned")

sales = pd.read_csv(CLEANED / "sales_clean.csv", parse_dates=["Date"])
features = pd.read_csv(CLEANED / "features_clean.csv", parse_dates=["Date"])
stores = pd.read_csv(CLEANED / "stores_clean.csv")

def dup_report(df: pd.DataFrame, keys: list[str], name: str) -> None:
    dups = df.duplicated(subset=keys).sum()
    print(f"\n--- {name} ---")
    print("Rows:", len(df))
    print("Expected unique keys:", keys)
    print("Duplicate rows on keys:", dups)

# 1) Grain / duplicate checks
dup_report(sales, ["Store_ID", "Dept_ID", "Date"], "SALES (Store-Dept-Week)")
dup_report(features, ["Store_ID", "Date"], "FEATURES (Store-Week)")
dup_report(stores, ["Store_ID"], "STORES (Store)")

# 2) Key coverage checks (join safety)
# How many sales rows match a features row?
sales_keys = sales[["Store_ID", "Date"]].drop_duplicates()
features_keys = features[["Store_ID", "Date"]].drop_duplicates()

matched = sales_keys.merge(features_keys, on=["Store_ID", "Date"], how="inner")
print("\n--- JOIN COVERAGE: sales ↔ features ---")
print("Unique sales (Store_ID, Date):", len(sales_keys))
print("Unique features (Store_ID, Date):", len(features_keys))
print("Matched keys:", len(matched))
print("Unmatched sales keys:", len(sales_keys) - len(matched))

# Stores coverage: are all stores in sales present in stores table?
sales_store_ids = set(sales["Store_ID"].unique())
stores_store_ids = set(stores["Store_ID"].unique())
missing_in_stores = sorted(sales_store_ids - stores_store_ids)

print("\n--- STORE COVERAGE: sales → stores ---")
print("Unique stores in sales:", len(sales_store_ids))
print("Unique stores in stores table:", len(stores_store_ids))
print("Stores in sales missing from stores table:", len(missing_in_stores))
if missing_in_stores[:10]:
    print("Example missing Store_IDs (up to 10):", missing_in_stores[:10])

# 3) Quick sanity ranges
print("\n--- SANITY CHECKS ---")
print("Sales date range:", sales["Date"].min(), "→", sales["Date"].max())
print("Features date range:", features["Date"].min(), "→", features["Date"].max())
print("Weekly_Sales min/max:", sales["Weekly_Sales"].min(), "/", sales["Weekly_Sales"].max())
