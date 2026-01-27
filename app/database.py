import pandas as pd
from app.config import DATA_DIR

def _file_path(name: str):
    return DATA_DIR / f"{name}.csv"

def read_sheet(name: str) -> pd.DataFrame:
    path = _file_path(name)
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)

def write_sheet(name: str, df: pd.DataFrame):
    path = _file_path(name)
    df.to_csv(path, index=False)
