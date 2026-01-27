def generate_ai_suggestion(tasks, followups):
    if not tasks and not followups:
        return "Focus on one high-impact task today"
    if tasks:
        return f"Complete pending task: {tasks[0]['title']}"
    return "Review follow-ups due today"
