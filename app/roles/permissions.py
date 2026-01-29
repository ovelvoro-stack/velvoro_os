# app/roles/permissions.py

from typing import Dict, Set
from .models import Role

ROLE_PERMISSIONS: Dict[Role, Set[str]] = {
    Role.admin: {
        "users:read",
        "users:write",
        "data:read",
        "data:write",
        "reports:read",
        "billing:manage",
        "roles:assign",
    },
    Role.manager: {
        "users:read",
        "data:read",
        "data:write",
        "reports:read",
    },
    Role.user: {
        "data:read",
        "data:write",
    },
}


def has_permission(role: Role, permission: str) -> bool:
    permissions = ROLE_PERMISSIONS.get(role, set())
    return permission in permissions
