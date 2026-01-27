import uuid
from app.db.repository import add_record, list_records

def create_followup(note, due_date, user):
    record = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date,
        "user": user
    }
    add_record("followups", record)
    return record

def list_followups(user):
    return [f for f in list_records("followups") if f["user"] == user]
