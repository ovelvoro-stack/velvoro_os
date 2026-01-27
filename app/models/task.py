from pydantic import BaseModel
from datetime import date

class Task(BaseModel):
    id: str
    title: str
    status: str = "pending"
    priority: str = "normal"
    created_date: date
    user: str
