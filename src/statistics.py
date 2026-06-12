import numpy as np

def stats_analysis(df):
    mean = np.mean(df['revenue'])
    median = np.median(df['revenue'])
    std = np.std(df['revenue'])

    return mean, median, std


def percentile_analysis(df):
    return np.percentile(df['revenue'], 90)


def growth_rate(df):
    monthly = df.groupby('month')['revenue'].sum()
    return monthly.pct_change() * 100