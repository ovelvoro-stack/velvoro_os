# app/roles/routes.py

from fastapi import APIRouter, HTTPException
from typing import List

from .models import Role, RoleAssignment
from .service import RoleService

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.get("/", response_model=List[Role])
def list_roles():
    return RoleService.list_roles()


@router.post("/assign")
def assign_role(payload: RoleAssignment):
    try:
        RoleService.assign_role(payload)
        return {
            "status": "success",
            "user_id": payload.user_id,
            "role": payload.role,
        }
    except Exception:
        raise HTTPException(status_code=400, detail="Unable to assign role")
