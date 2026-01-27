from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str
    status: str

class FollowUp(BaseModel):
    id: str
    note: str
    due_date: str
