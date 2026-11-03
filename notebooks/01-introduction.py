import pandas as pd
import numpy as np


def load_sample_data() -> pd.DataFrame:
    """Load a sample DataFrame for demonstration."""
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 30, 35, 28],
        "city": ["New York", "London", "Tokyo", "Sydney"],
        "score": [85.5, 90.0, 78.5, 92.0],
    }
    return pd.DataFrame(data)


def basic_operations(df: pd.DataFrame) -> pd.DataFrame:
    """Demonstrate basic pandas operations."""
    df = df.copy()
    df["score_plus_5"] = df["score"] + 5
    adults = df[df["age"] >= 30]
    return adults


if __name__ == "__main__":
    df = load_sample_data()
    print(df)
    print("\n--- Adults (age >= 30) ---")
    print(basic_operations(df))