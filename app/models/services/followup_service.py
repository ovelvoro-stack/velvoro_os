from app.db.excel_db import add_followup, get_followups

def create_followup(user, note, due_date):
    add_followup(user, note, due_date)

def list_followups():
    return get_followups()
