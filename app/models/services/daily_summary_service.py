from datetime import date
from app.database import read_sheet

def get_daily_summary():
    tasks = read_sheet("tasks")
    followups = read_sheet("followups")

    pending_tasks = tasks[tasks["status"] == "pending"] if not tasks.empty else []
    ai_suggestion = generate_ai_suggestion(pending_tasks)

    return {
        "date": str(date.today()),
        "tasks": tasks.to_dict(orient="records"),
        "followups": followups.to_dict(orient="records"),
        "ai_suggestion": ai_suggestion
    }

def generate_ai_suggestion(pending_tasks):
    if len(pending_tasks) == 0:
        return "You're clear today. Maintain momentum."
    if len(pending_tasks) > 5:
        return "You have many open tasks. Prioritize top 1."
    return "Focus on completing one high-impact task today."

# 🔮 Future LLM hook
def llm_stub(context: dict):
    return "LLM response placeholder"
