# app/roles/service.py

from typing import Dict, List
from .models import Role, RoleAssignment
from .permissions import has_permission


class RoleService:
    """
    In-memory role handling layer.
    Does NOT touch DB.
    Safe for production extension.
    """

    _user_roles: Dict[str, Role] = {}

    @classmethod
    def list_roles(cls) -> List[Role]:
        return list(Role)

    @classmethod
    def assign_role(cls, assignment: RoleAssignment) -> None:
        cls._user_roles[assignment.user_id] = assignment.role

    @classmethod
    def get_user_role(cls, user_id: str) -> Role:
        return cls._user_roles.get(user_id, Role.user)

    @classmethod
    def user_has_permission(cls, user_id: str, permission: str) -> bool:
        role = cls.get_user_role(user_id)
        return has_permission(role, permission)
