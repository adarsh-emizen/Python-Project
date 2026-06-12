import pandas as pd

def load_data():
    orders = pd.read_csv("data/orders.csv")
    products = pd.read_csv("data/products.csv")
    customers = pd.read_csv("data/customers.csv") 
    
    return orders, products, customers