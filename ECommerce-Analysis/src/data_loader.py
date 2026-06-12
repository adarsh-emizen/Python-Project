import pandas as pd
import os

def load_data():
    try:
        orders = pd.read_csv("data/orders.csv")
        products = pd.read_csv("data/products.csv")
        customers = pd.read_csv("data/customers.csv")

        print("✅ Data loaded successfully")

        return orders, products, customers

    except Exception as e:
        print("❌ Error:", e)
        return None, None, None