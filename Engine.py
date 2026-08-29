import os, json
from google import genai
from google.genai import types

def diagnose(case, prompt_text):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set.")
    client = genai.Client(api_key=api_key)
    payload = f"""{prompt_text}

CASE:
{json.dumps(case, indent=2)}

Return the diagnosis JSON now."""
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=payload,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )
    return json.loads(response.text)
