import pandas as pd

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analytics import *
from src.statistics import *
from src.insights import generate_insights


# Load data
orders, products, customers = load_data()

# Clean data
orders = clean_data(orders)
products = clean_data(products)
customers = clean_data(customers)

# Process
df = process_orders(orders, products, customers)

# KPIs
revenue, total_orders, avg = sales_kpis(df)

# Analytics
top_prod = top_products(df)
low_prod = lowest_products(df)
demand = product_demand(df)

region_sales = revenue_by_region(df)
category_sales = revenue_by_category(df)
monthly = monthly_revenue(df)

top_cust = top_customers(df)
repeat = repeat_customers(df)

# Statistics
mean, median, std = stats_analysis(df)
percentile = percentile_analysis(df)
growth = growth_rate(df)

# Insight
insight = generate_insights(revenue, avg, top_prod.idxmax())

# Output
print("Total Revenue:", revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg)

print("\nTop Products:\n", top_prod)
print("\nLowest Products:\n", low_prod)
print("\nProduct Demand:\n", demand)

print("\nTop Customers:\n", top_cust)
print("\nRepeat Customers:\n", repeat)

print("\nRegion-wise Sales:\n", region_sales)
print("\nCategory Sales:\n", category_sales)

print("\nMonthly Trends:\n", monthly)
print("\nGrowth Rate (%):\n", growth)

print("\nStatistics:")
print("Mean:", mean, "Median:", median, "Std:", std)
print("90th Percentile:", percentile)

print("\nAI Insight:", insight)