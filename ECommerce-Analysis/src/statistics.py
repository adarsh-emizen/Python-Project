import numpy as np

def generate_statistics(df):
    print("\n📊 STATISTICAL ANALYSIS\n")

    if df.empty:
        print("❌ No data available")
        return

    revenue = df["revenue"]

    # ----------------------------
    # BASIC STATISTICS
    # ----------------------------
    mean = np.mean(revenue)
    median = np.median(revenue)
    std = np.std(revenue)

    print("Mean Revenue:", mean)
    print("Median Revenue:", median)
    print("Standard Deviation:", std)

    # ----------------------------
    # PERCENTILES
    # ----------------------------
    print("\n📈 Percentiles:")
    print("25%:", np.percentile(revenue, 25))
    print("50%:", np.percentile(revenue, 50))
    print("75%:", np.percentile(revenue, 75))

    # ----------------------------
    # TREND ANALYSIS
    # ----------------------------
    if "order_date" not in df.columns:
        print("\n⚠️ No date column — skipping trend analysis")
        return

    df["order_date"] = df["order_date"].astype(str)

    daily = df.groupby("order_date")["revenue"].sum()

    if len(daily) > 1:
        x = np.arange(len(daily))
        y = daily.values

        slope = np.polyfit(x, y, 1)[0]

        print("\n📉 TREND ANALYSIS:")

        if slope > 0:
            print("📈 Upward trend")
        elif slope < 0:
            print("📉 Downward trend")
        else:
            print("➡️ Stable trend")

        print("Slope:", slope)

    print("\n✅ Statistics Generated")