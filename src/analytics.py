import pandas as pd

def process_orders(orders, products, customers):
    # Merge datasets
    df = orders.merge(products, on="product_id")
    df = df.merge(customers, on="customer_id")

    # Revenue calculation
    df['revenue'] = df['price'] * df['quantity']

    # Convert date
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')

    return df


# KPIs
def sales_kpis(df):
    revenue = df['revenue'].sum()
    total_orders = df['order_id'].nunique()
    avg = revenue / total_orders

    return revenue, total_orders, avg


# Product Analytics
def top_products(df):
    return df.groupby('product_name')['revenue'].sum().sort_values(ascending=False)

def lowest_products(df):
    return df.groupby('product_name')['revenue'].sum().sort_values().head()

def product_demand(df):
    return df.groupby('product_name')['quantity'].sum()


# Category / Region
def revenue_by_category(df):
    return df.groupby('category')['revenue'].sum()

def revenue_by_region(df):
    return df.groupby('region')['revenue'].sum()


# Monthly Trends
def monthly_revenue(df):
    return df.groupby('month')['revenue'].sum()


# Customer Analytics
def top_customers(df):
    return df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False)

def repeat_customers(df):
    return df['customer_name'].value_counts()

def customer_lifetime_value(df):
    return df.groupby('customer_name')['revenue'].sum()

def purchase_frequency(df):
    return df['customer_name'].value_counts()