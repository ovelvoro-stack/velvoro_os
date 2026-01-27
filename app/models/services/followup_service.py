import uuid
from app.database import read_sheet, write_sheet

def add_followup(note: str, due_date: str):
    df = read_sheet("followups")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date
    }
    write_sheet("followups", df)
    return {"status": "followup added"}
