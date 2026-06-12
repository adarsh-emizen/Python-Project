def generate_insights(df):
    print("\n🧠 BUSINESS INSIGHTS\n")

    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_id"].nunique()

    avg_order_value = total_revenue / total_orders if total_orders else 0

    # Top product dependency check
    top_product = df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)

    print(f"💰 Total Revenue: {total_revenue}")
    print(f"🛒 Total Orders: {total_orders}")
    print(f"👥 Total Customers: {total_customers}")
    print(f"📦 Avg Order Value: {avg_order_value}")

    print("\n🔥 TOP PRODUCT:")
    print(top_product.head(1))

    print("\n📊 INSIGHTS:")

    if avg_order_value < 100:
        print("⚠️ Low average order value — consider upselling or bundles.")

    if not top_product.empty and top_product.iloc[0] > total_revenue * 0.3:
        print("⚠️ High dependency on single product — risk detected.")

    if total_customers < total_orders * 0.5:
        print("⚠️ Low repeat customers — retention issue.")

    print("\n✅ Insights Generated")