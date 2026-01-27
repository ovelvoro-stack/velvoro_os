File name: followup_routes.py
File path: app/models/api/followup_routes.py
Full code:
from fastapi import APIRouter
from app.models.services.followup_service import create_followup, list_followups

router = APIRouter()

@router.post("/")
def add_followup(data: dict):
    return create_followup(data)

@router.get("/")
def get_followups():
    return list_followups()
