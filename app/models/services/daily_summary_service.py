from datetime import date

def get_daily_summary():
    return {
        "date": str(date.today()),
        "tasks": [],
        "followups": [],
        "ai_suggestion": "Focus on one high-impact task today"
    }
