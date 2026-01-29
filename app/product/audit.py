from datetime import datetime

AUDIT_LOG = []

def log_action(user_id: str, role: str, action: str):
    AUDIT_LOG.append({
        "user_id": user_id,
        "role": role,
        "action": action,
        "time": datetime.utcnow().isoformat()
    })

def get_audit_log():
    return AUDIT_LOG
