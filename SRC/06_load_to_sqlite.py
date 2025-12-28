import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

# =========================
# Paths
# =========================
BASE = Path.cwd()                 # Retail Data
MODELLED = BASE / "Modelled"
DATABASE = BASE / "Database"
DATABASE.mkdir(exist_ok=True)

db_path = DATABASE / "retail_analytics.db"

# =========================
# Create SQLite engine
# =========================
engine = create_engine(f"sqlite:///{db_path}")

# =========================
# Load CSV files
# =========================
sales_fact = pd.read_csv(MODELLED / "sales_fact.csv", parse_dates=["Date"])
stores_info = pd.read_csv(MODELLED / "stores_info.csv")
calendar = pd.read_csv(MODELLED / "calendar.csv", parse_dates=["Date"])

# =========================
# Write tables to SQLite
# =========================
sales_fact.to_sql("sales_fact", engine, if_exists="replace", index=False)
stores_info.to_sql("stores_info", engine, if_exists="replace", index=False)
calendar.to_sql("calendar", engine, if_exists="replace", index=False)

# =========================
# Create indexes (performance)
# =========================
with engine.begin() as conn:
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_date ON sales_fact(Date);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_store ON sales_fact(Store_ID);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_calendar_date ON calendar(Date);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_store_id ON stores_info(Store_ID);"))

print("✅ SQLite database created at:", db_path)

# =========================
# Verify row counts
# =========================
with engine.connect() as conn:
    for table in ["sales_fact", "stores_info", "calendar"]:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table};")).scalar()
        print(f"{table}: {count:,} rows")

