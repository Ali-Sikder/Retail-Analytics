import pandas as pd
from pathlib import Path 

RAW = Path("raw")


sales_path = RAW / "sales data-set.xlsx"
features_path = RAW / "Features data set.xlsx"
stores_path = RAW / "stores data-set.xlsx"

sales = pd.read_excel (sales_path)
features = pd.read_excel (features_path)
stores = pd.read_excel (stores_path)

def quick_check(df: pd.DataFrame, name: str) -> None:
    print(f"\n==== {name} ====")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("\nDtypes:\n", df.dtypes)
    print("\nMissing values (top 12):\n", df.isna().sum().sort_values(ascending=False).head(12))
    print("\nFirst 3 rows:\n", df.head(3))

quick_check(sales, "SALES")
quick_check(features, "FEATURES")
quick_check(stores, "STORES")    