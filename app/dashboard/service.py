from typing import List
from app.dashboard.schemas import DashboardItem


def get_dashboard_items_for_role(role: str) -> List[DashboardItem]:
    """
    Role-based dashboard data.
    Read-only, production-safe.
    """

    if role == "admin":
        return [
            DashboardItem(title="Total Users", value="--"),
            DashboardItem(title="System Status", value="Healthy"),
            DashboardItem(title="Pending Reports", value="--"),
        ]

    if role == "manager":
        return [
            DashboardItem(title="Team Members", value="--"),
            DashboardItem(title="Today Entries", value="--"),
        ]

    # default: user
    return [
        DashboardItem(title="My Entries", value="--"),
        DashboardItem(title="Last Login", value="--"),
    ]
