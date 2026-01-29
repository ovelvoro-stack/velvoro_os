from pydantic import BaseModel
from typing import List


class DashboardItem(BaseModel):
    title: str
    value: str


class DashboardResponse(BaseModel):
    role: str
    items: List[DashboardItem]
