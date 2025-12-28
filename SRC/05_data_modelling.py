import pandas as pd
from pathlib import Path

# =========================
# Paths (SAFE & SIMPLE)
# =========================
BASE = Path.cwd()              # Retail Data
CLEANED = BASE / "Cleaned"
MODELLED = BASE / "Modelled"
MODELLED.mkdir(exist_ok=True)

print("Base path:", BASE)
print("Cleaned exists:", CLEANED.exists())

# =========================
# Load merged dataset
# =========================
df = pd.read_csv(CLEANED / "retail_analytics.csv", parse_dates=["Date"])
print("Rows loaded:", len(df))

# =========================
# 1️⃣ Create CALENDAR table
# =========================
calendar = (
    df[["Date"]]
    .drop_duplicates()
    .assign(
        Year=lambda x: x["Date"].dt.year,
        Month=lambda x: x["Date"].dt.month,
        Month_Name=lambda x: x["Date"].dt.month_name(),
        Week=lambda x: x["Date"].dt.isocalendar().week,
        Quarter=lambda x: x["Date"].dt.quarter,
        YearMonth=lambda x: x["Date"].dt.strftime("%Y-%m")
    )
    .sort_values("Date")
)

calendar.to_csv(MODELLED / "calendar.csv", index=False)
print("Calendar table created:", len(calendar))

# =========================
# 2️⃣ Create STORES INFO table
# =========================
stores_info = (
    df[["Store_ID", "Store_Type", "Store_Size"]]
    .drop_duplicates()
    .sort_values("Store_ID")
)

stores_info.to_csv(MODELLED / "stores_info.csv", index=False)
print("Stores info table created:", len(stores_info))

# =========================
# 3️⃣ Create SALES FACT table
# =========================

# Use holiday flag from sales data
df = df.rename(columns={"IsHoliday_x": "IsHoliday"})

# Optional: drop the duplicate holiday column from features
if "IsHoliday_y" in df.columns:
    df = df.drop(columns=["IsHoliday_y"])

sales_fact = df[
    [
        "Store_ID",
        "Dept_ID",
        "Date",
        "Weekly_Sales",
        "IsHoliday",
        "Is_Return_Week",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        "Promo_Discount_1",
        "Promo_Discount_2",
        "Promo_Discount_3",
        "Promo_Discount_4",
        "Promo_Discount_5"
    ]
]

sales_fact.to_csv(MODELLED / "sales_fact.csv", index=False)
print("Sales fact table created:", len(sales_fact))

