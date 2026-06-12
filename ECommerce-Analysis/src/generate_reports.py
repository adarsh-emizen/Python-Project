import pandas as pd
import os

# ----------------------------
# LOAD CLEAN DATA
# ----------------------------
orders = pd.read_csv("data/orders.csv")
products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")

# ----------------------------
# MERGE DATA
# ----------------------------
df = orders.merge(products, on="product_id", how="left")
df = df.merge(customers, on="customer_id", how="left")

df["revenue"] = df["quantity"] * df["price"]
df["order_date"] = pd.to_datetime(df["order_date"])

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# =========================================================
# 1. SALES REPORT
# =========================================================
sales_report = df.groupby("order_date").agg(
    total_revenue=("revenue", "sum"),
    total_orders=("order_id", "nunique"),
    total_quantity=("quantity", "sum")
).reset_index()

sales_report.to_csv("reports/sales_report.csv", index=False)
print("✅ sales_report.csv created")

# =========================================================
# 2. CUSTOMER REPORT
# =========================================================
customer_report = df.groupby("customer_id").agg(
    total_spent=("revenue", "sum"),
    total_orders=("order_id", "nunique"),
    avg_order_value=("revenue", "mean")
).reset_index()

# safer segmentation
def segment(value):
    if value > 5000:
        return "VIP"
    elif value > 2000:
        return "Regular"
    else:
        return "Low Value"

customer_report["segment"] = customer_report["total_spent"].apply(segment)

customer_report.to_csv("reports/customer_report.csv", index=False)
print("✅ customer_report.csv created")

# =========================================================
# 3. PRODUCT REPORT
# =========================================================
product_report = df.groupby("product_name").agg(
    total_revenue=("revenue", "sum"),
    total_units_sold=("quantity", "sum"),
    avg_price=("price", "mean")
).reset_index()

product_report = product_report.sort_values("total_revenue", ascending=False)

product_report.to_csv("reports/product_report.csv", index=False)
print("✅ product_report.csv created")

# =========================================================
# 4. BUSINESS SUMMARY REPORT
# =========================================================
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()

top_product = (
    product_report["product_name"].iloc[0]
    if not product_report.empty
    else "N/A"
)

business_report = f"""
================ BUSINESS REPORT ================

📊 TOTAL REVENUE: {total_revenue}
🧾 TOTAL ORDERS: {total_orders}
👥 TOTAL CUSTOMERS: {total_customers}

🔥 TOP PRODUCT: {top_product}

📈 INSIGHTS:
- Revenue depends heavily on top products.
- Customer base has clear segmentation.
- Repeat purchase behavior impacts growth.

⚡ RECOMMENDATIONS:
- Focus on VIP customers.
- Improve low-performing products.
- Increase retention using loyalty programs.

=================================================
"""

with open("reports/business_report.txt", "w", encoding="utf-8") as f:
    f.write(business_report)

print("✅ business_report.txt created")