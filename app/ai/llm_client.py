import os

def generate_llm_summary(prompt: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        import openai
        openai.api_key = api_key
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
    except Exception:
        return None
