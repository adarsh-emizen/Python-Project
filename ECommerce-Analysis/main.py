from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.analytics import *

from src.insights import generate_insights
from src.statistics import generate_statistics

# =========================
# LOAD DATA
# =========================
orders, products, customers = load_data()

if orders is None:
    print("❌ Data loading failed")
    exit()

# =========================
# CLEAN DATA
# =========================
orders = clean_data(orders)
products = clean_data(products)
customers = clean_data(customers)

# =========================
# MERGE DATA
# =========================
df = merge_data(orders, products, customers)

# =========================
# FEATURE ENGINEERING
# =========================
df = calculate_revenue(df)

# =========================
# KPI SECTION
# =========================
print("\n" + "="*60)
print("📊 SALES KPI REPORT")
print("="*60)

print("💰 Total Revenue:", get_total_revenue(df))
print("🛒 Total Orders:", get_total_orders(df))
print("👥 Total Customers:", df["customer_id"].nunique())
print("📦 Avg Order Value:", get_average_order_value(df))

# =========================
# ANALYTICS SECTION
# =========================
print("\n" + "="*60)
print("📊 BUSINESS ANALYTICS")
print("="*60)

print("\n🔥 Top Products")
print(top_products(df).head(5))

print("\n🌍 Revenue by Region")
print(revenue_by_region(df))

print("\n📂 Revenue by Category")
print(revenue_by_category(df))

print("\n👥 Top Customers")
print(top_customers(df).head(5))

# =========================
# INSIGHTS MODULE
# =========================
print("\n" + "="*60)
print("🧠 AI-STYLE BUSINESS INSIGHTS")
print("="*60)

generate_insights(df)

# =========================
# STATISTICS MODULE
# =========================
print("\n" + "="*60)
print("📊 STATISTICAL ANALYSIS")
print("="*60)

generate_statistics(df)

# =========================
# END
# =========================
print("\n" + "="*60)
print("✅ PIPELINE EXECUTION COMPLETE")
print("="*60)
