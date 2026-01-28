from fastapi import APIRouter, Request
from app.billing.service import get_company_plan

router = APIRouter()

@router.get("/billing/status")
def billing_status(request: Request):
    company = request.state.user["company"]
    return {"company": company, "plan": get_company_plan(company)}
