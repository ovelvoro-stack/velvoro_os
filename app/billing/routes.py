from fastapi import APIRouter

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.get("/status")
def billing_status():
    return {
        "status": "disabled",
        "message": "Billing is not yet activated."
    }
