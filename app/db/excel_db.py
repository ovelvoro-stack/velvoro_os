import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def load_excel(file):
    return pd.read_excel(DATA_DIR / file)

def save_excel(file, df):
    df.to_excel(DATA_DIR / file, index=False)
