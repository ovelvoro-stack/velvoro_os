import uuid
from datetime import date
from app.db.repository import add_record, list_records

def create_task(title, priority, user):
    record = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending",
        "priority": priority,
        "created_date": date.today(),
        "user": user
    }
    add_record("tasks", record)
    return record

def list_tasks(user):
    return [t for t in list_records("tasks") if t["user"] == user]
