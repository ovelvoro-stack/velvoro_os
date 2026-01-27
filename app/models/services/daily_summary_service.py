from datetime import date
from app.database import read_sheet, write_sheet
import uuid

def add_task(title: str):
    df = read_sheet("tasks")from datetime import date, datetime
from app.database import read_sheet, write_sheet
import uuid

# -----------------------------
# TASK & FOLLOWUP OPERATIONS
# -----------------------------

def add_task(title: str):
    df = read_sheet("tasks")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending"
    }
    write_sheet("tasks", df)

def add_followup(note: str, due_date: str):
    df = read_sheet("followups")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date
    }
    write_sheet("followups", df)

# -----------------------------
# AI SUGGESTION ENGINE (STUB)
# -----------------------------

def generate_ai_suggestion(tasks, followups):
    suggestions = []

    pending_tasks = [t for t in tasks if t["status"] == "pending"]

    # Rule 1: Too many pending tasks
    if len(pending_tasks) > 5:
        suggestions.append(
            "You have too many pending tasks. Focus on completing 2–3 high-impact tasks today."
        )

    # Rule 2: No tasks at all
    if len(tasks) == 0:
        suggestions.append(
            "You have no tasks planned today. Define at least one meaningful task to stay productive."
        )

    # Rule 3: Overdue followups
    today = date.today()
    overdue = []

    for f in followups:
        try:
            due = datetime.strptime(f["due_date"], "%Y-%m-%d").date()
            if due < today:
                overdue.append(f)
        except Exception:
            continue

    if overdue:
        suggestions.append(
            f"You have {len(overdue)} overdue follow-ups. Close them before starting new work."
        )

    # Rule 4: Repeated task patterns (basic keyword check)
    titles = [t["title"].lower() for t in pending_tasks]
    if any(titles.count(t) > 2 for t in titles):
        suggestions.append(
            "You are repeating similar tasks. Consider batching or automating them."
        )

    # Default fallback
    if not suggestions:
        suggestions.append(
            "Good balance today. Complete one important task and review follow-ups."
        )

    return suggestions

# -----------------------------
# DAILY SUMMARY (FINAL OUTPUT)
# -----------------------------

def get_daily_summary():
    tasks_df = read_sheet("tasks")
    followups_df = read_sheet("followups")

    tasks = tasks_df.to_dict(orient="records")
    followups = followups_df.to_dict(orient="records")

    ai_suggestions = generate_ai_suggestion(tasks, followups)

    return {
        "date": str(date.today()),
        "tasks": tasks,
        "pending_followups": followups,
        "ai_suggestions": ai_suggestions,
        "ai_mode": "rule-based-stub (ML-ready)"
    }
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending"
    }
    write_sheet("tasks", df)

def add_followup(note: str, due_date: str):
    df = read_sheet("followups")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date
    }
    write_sheet("followups", df)

def get_daily_summary():
    tasks_df = read_sheet("tasks")
    followups_df = read_sheet("followups")

    return {
        "date": str(date.today()),
        "tasks": tasks_df.to_dict(orient="records"),
        "pending_followups": followups_df.to_dict(orient="records"),
        "ai_suggestion": "Complete pending tasks before adding new ones."
    }
