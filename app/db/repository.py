from app.db.excel_db import read_sheet, write_sheet

def add_record(sheet, record):
    df = read_sheet(sheet)
    df = df._append(record, ignore_index=True)
    write_sheet(sheet, df)

def list_records(sheet):
    return read_sheet(sheet).to_dict(orient="records")
