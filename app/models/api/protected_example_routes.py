from fastapi import APIRouter, Depends

from app.models.auth.dependencies import get_current_user, require_role

router = APIRouter()


@router.get("/me")
def read_me(user=Depends(get_current_user)):
    return {
        "user": user.get("sub"),
        "role": user.get("role"),
    }


@router.get("/admin-only")
def admin_only(user=Depends(require_role("admin"))):
    return {
        "message": "Admin access granted",
        "user": user.get("sub"),
    }
