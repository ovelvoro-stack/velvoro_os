from fastapi import APIRouter, Depends
from app.models.schemas import TaskCreate
from app.models.services.task_service import add_task
from app.auth.api_key_auth import verify_api_key

router = APIRouter()

@router.post("/")
def create_task(payload: TaskCreate, auth=Depends(verify_api_key)):
    return add_task(payload.title)
