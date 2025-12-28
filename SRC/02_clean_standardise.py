import pandas as pd
from pathlib import Path

RAW = Path("raw")
CLEANED = Path("Cleaned")
CLEANED.mkdir(exist_ok=True)

sales = pd.read_excel(RAW / "sales data-set.xlsx")
features = pd.read_excel(RAW / "Features data set.xlsx")
stores = pd.read_excel(RAW / "stores data-set.xlsx")

sales = sales.rename(columns={
    "Store": "Store_ID",
    "Dept": "Dept_ID"
})

features = features.rename(columns={
    "Store": "Store_ID",
    "Starting week": "Date",
    "MarkDown1": "Promo_Discount_1",
    "MarkDown2": "Promo_Discount_2",
    "MarkDown3": "Promo_Discount_3",
    "MarkDown4": "Promo_Discount_4",
    "MarkDown5": "Promo_Discount_5"
})

stores = stores.rename(columns={
    "Store": "Store_ID",
    "Type": "Store_Type",
    "Size": "Store_Size"
})

sales["Date"] = pd.to_datetime(sales["Date"])
features["Date"] = pd.to_datetime(features["Date"])

features[
    [
        "Promo_Discount_1",
        "Promo_Discount_2",
        "Promo_Discount_3",
        "Promo_Discount_4",
        "Promo_Discount_5"
    ]
] = features[
    [
        "Promo_Discount_1",
        "Promo_Discount_2",
        "Promo_Discount_3",
        "Promo_Discount_4",
        "Promo_Discount_5"
    ]
].fillna(0)

sales.to_csv(CLEANED / "sales_clean.csv", index=False)
features.to_csv(CLEANED / "features_clean.csv", index=False)
stores.to_csv(CLEANED / "stores_clean.csv", index=False)

print("✅ Cleaned data saved in 'Cleaned/' folder")
