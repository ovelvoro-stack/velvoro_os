from pydantic import BaseModel
from datetime import date

class FollowUp(BaseModel):
    id: str
    note: str
    due_date: date
    user: str
