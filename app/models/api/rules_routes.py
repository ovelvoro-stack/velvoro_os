from fastapi import APIRouter

router = APIRouter()

RULES = {
    "employee": ["write"],
    "manager": ["read"]
}

@router.get("/api/rules/{role}")
def get_rules(role: str):
    return {"permissions": RULES.get(role, [])}
