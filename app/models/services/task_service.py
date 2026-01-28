from app.db.excel_db import add_task, get_tasks

def create_task(user, task):
    add_task(user, task)

def list_tasks():
    return get_tasks()
