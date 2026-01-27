from datetime import date
from typing import Dict, Any, List


class DailySummaryService:
    """
    Service layer for Daily Summary Engine.
    All business logic lives here.
    API routes should ONLY call these methods.
    """

    @staticmethod
    def get_today_summary() -> Dict[str, Any]:
        """
        Build and return today's summary data.
        """

        tasks = DailySummaryService._get_tasks()
        pending_followups = DailySummaryService._get_pending_followups()
        ai_suggestion = DailySummaryService._get_ai_suggestion(tasks)

        return {
            "date": str(date.today()),
            "tasks": tasks,
            "pending_followups": pending_followups,
            "ai_suggestion": ai_suggestion
        }

    @staticmethod
    def _get_tasks() -> List[Dict[str, Any]]:
        """
        Fetch tasks (DB integration later)
        """

        return [
            {
                "id": 1,
                "title": "Review pending tasks",
                "status": "pending",
                "priority": "high"
            },
            {
                "id": 2,
                "title": "Send follow-up emails",
                "status": "completed",
                "priority": "medium"
            }
        ]

    @staticmethod
    def _get_pending_followups() -> List[Dict[str, Any]]:
        """
        Fetch follow-ups (DB integration later)
        """

        return [
            {
                "id": 101,
                "note": "Call client regarding proposal",
                "due_time": "16:00"
            }
        ]

    @staticmethod
    def _get_ai_suggestion(tasks: List[Dict[str, Any]]) -> str:
        """
        AI suggestion logic (stub for now)
        """

        high_priority_pending = [
            t for t in tasks
            if t["priority"] == "high" and t["status"] == "pending"
        ]

        if high_priority_pending:
            return "Focus on completing your highest priority task first."

        return "You are doing well. Maintain steady progress today."
