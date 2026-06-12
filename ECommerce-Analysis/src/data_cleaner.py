import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()

    # fill missing values safely
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    text_cols = df.select_dtypes(include=["object"]).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    # IMPORTANT FIX: consistent naming
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df