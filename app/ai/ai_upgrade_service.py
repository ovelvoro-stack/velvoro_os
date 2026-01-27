from app.ai.llm_client import generate_llm_summary

def smart_summary(tasks, followups, fallback_text):
    prompt = f"Tasks: {tasks}, Followups: {followups}"
    result = generate_llm_summary(prompt)
    return result or fallback_text
