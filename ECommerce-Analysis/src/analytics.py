import pandas as pd

# ----------------------------
# MERGE DATA
# ----------------------------
def merge_data(orders, products, customers):

    df = orders.merge(products, on="product_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")

    return df

# ----------------------------
# REVENUE
# ----------------------------
def calculate_revenue(df):
    df["revenue"] = df["quantity"] * df["price"]
    return df

# ----------------------------
# KPIs
# ----------------------------
def get_total_revenue(df):
    return df["revenue"].sum()

def get_total_orders(df):
    return df["order_id"].nunique()

def get_average_order_value(df):
    return df["revenue"].sum() / df["order_id"].nunique()

# ----------------------------
# ANALYTICS
# ----------------------------
def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum()

def revenue_by_region(df):
    return df.groupby("region")["revenue"].sum()

def top_products(df):
    return df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)

def top_customers(df):
    return df.groupby("customer_name")["revenue"].sum().sort_values(ascending=False)


