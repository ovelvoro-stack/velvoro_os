from fastapi import APIRouter, Depends
from app.models.schemas import FollowupCreate
from app.models.services.followup_service import add_followup
from app.auth.api_key_auth import verify_api_key

router = APIRouter()

@router.post("/")
def create_followup(payload: FollowupCreate, auth=Depends(verify_api_key)):
    return add_followup(payload.note, payload.due_date)
