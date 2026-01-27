import uuid
from app.database import read_sheet, write_sheet

def add_task(title: str):
    df = read_sheet("tasks")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending"
    }
    write_sheet("tasks", df)
    return {"status": "task added"}
