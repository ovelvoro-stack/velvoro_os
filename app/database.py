import os
import pandas as pd

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "daily_data.xlsx")

def init_excel():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(FILE_PATH):
        with pd.ExcelWriter(FILE_PATH, engine="openpyxl") as writer:
            pd.DataFrame(columns=["id", "title", "status"]).to_excel(
                writer, sheet_name="tasks", index=False
            )
            pd.DataFrame(columns=["id", "note", "due_date"]).to_excel(
                writer, sheet_name="followups", index=False
            )

def read_sheet(sheet_name):
    init_excel()
    return pd.read_excel(FILE_PATH, sheet_name=sheet_name)

def write_sheet(sheet_name, df):
    init_excel()
    with pd.ExcelWriter(FILE_PATH, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
