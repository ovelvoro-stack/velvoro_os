# app/roles/models.py

from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Role(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"


class RoleAssignment(BaseModel):
    user_id: str
    role: Role
    assigned_by: Optional[str] = None
