def filter_by_threshold(df, threshold):
    return df[df["Value"] >= threshold]

def summarize_by_category(df):
    return df.groupby("Category")["Value"].mean().reset_index()
