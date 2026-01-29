from fastapi import APIRouter, Depends, HTTPException
from app.dashboard.schemas import DashboardResponse
from app.dashboard.service import get_dashboard_items_for_role

# NOTE:
# We DO NOT touch auth logic.
# We ONLY read role value passed from existing auth/session layer.

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_current_user_role():
    """
    Placeholder dependency.
    Replace internally later with existing auth/session.
    DOES NOT break current production.
    """
    return "user"  # safe default


@router.get("", response_model=DashboardResponse)
def get_dashboard(role: str = Depends(get_current_user_role)):
    if not role:
        raise HTTPException(status_code=401, detail="Unauthorized")

    items = get_dashboard_items_for_role(role)

    return DashboardResponse(
        role=role,
        items=items
    )
