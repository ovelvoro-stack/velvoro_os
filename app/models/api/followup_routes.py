from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security import get_current_user
from app.services.followup_service import create_followup, list_followups

router = APIRouter()

class FollowReq(BaseModel):
    note: str
    due_date: str

@router.post("/")
def add_followup(data: FollowReq, user=Depends(get_current_user)):
    return create_followup(data.note, data.due_date, user)

@router.get("/")
def get_followups(user=Depends(get_current_user)):
    return list_followups(user)
