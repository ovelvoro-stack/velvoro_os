from fastapi import APIRouter, HTTPException, Depends
from app.billing.billing_service import get_company, upgrade_plan, is_plan_active

router = APIRouter(prefix="/billing", tags=["billing"])

def company_guard(company: str):
    if not is_plan_active(company):
        raise HTTPException(status_code=403, detail="Plan expired")

@router.get("/status/{company}")
def status(company: str):
    return get_company(company)

@router.post("/upgrade/{company}/{plan}")
def upgrade(company: str, plan: str):
    return upgrade_plan(company, plan)
