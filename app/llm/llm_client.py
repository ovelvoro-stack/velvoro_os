import os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def generate_ai_text(prompt: str) -> str:
    if not OPENAI_KEY:
        return "LLM not configured. Using rule-based suggestion."
    try:
        # stub – replace with real OpenAI call later
        return f"LLM suggestion for: {prompt}"
    except Exception:
        return "LLM failed. Fallback active."
