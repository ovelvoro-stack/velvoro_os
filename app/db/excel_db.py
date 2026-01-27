import pandas as pd
import os
from app.core.config import DATA_DIR

def _path(name):
    os.makedirs(DATA_DIR, exist_ok=True)
    return f"{DATA_DIR}/{name}.xlsx"

def read_sheet(name):
    path = _path(name)
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_excel(path)

def write_sheet(name, df):
    df.to_excel(_path(name), index=False)
