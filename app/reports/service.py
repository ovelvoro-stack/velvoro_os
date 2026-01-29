from typing import Dict, List


def get_reports_data(role: str) -> Dict[str, List[dict]]:
    """
    Read-only aggregations.
    Production-safe.
    No DB mutation.
    """

    if role == "admin":
        return {
            "summary": [
                {"label": "Total Users", "value": "--"},
                {"label": "Total Entries", "value": "--"},
                {"label": "System Health", "value": "OK"},
            ],
            "details": []
        }

    if role == "manager":
        return {
            "summary": [
                {"label": "Team Entries Today", "value": "--"},
                {"label": "Pending Reviews", "value": "--"},
            ],
            "details": []
        }

    # default: user
    return {
        "summary": [
            {"label": "My Entries", "value": "--"},
            {"label": "Last Submission", "value": "--"},
        ],
        "details": []
    }
