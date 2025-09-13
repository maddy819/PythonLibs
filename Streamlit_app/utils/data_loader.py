import pandas as pd
import numpy as np

def generate_data(n=100):
    np.random.seed(42)
    df = pd.DataFrame({
        "ID": range(1, n+1),
        "Value": np.random.randint(0, 100, n),
        "Category": np.random.choice(["A", "B", "C"], n)
    })
    return df
