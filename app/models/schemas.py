from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class FollowupCreate(BaseModel):
    note: str
    due_date: str
