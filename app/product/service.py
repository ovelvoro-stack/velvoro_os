from app.product.audit import log_action

def primary_action(user):
    log_action(user["id"], user["role"], "PRIMARY_ACTION")
    return {"status": "success", "message": "Primary action completed"}

def get_empty_state(role: str):
    return f"No data available yet for {role}. Start by adding your first record."
