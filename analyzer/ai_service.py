import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def explain_code(code, language):
    prompt = f"""
You are CodeMentor AI, a coding tutor for college students.

The student has submitted {language} code.

Explain the code in simple language so a beginner can understand it.

Include:
1. What the code does
2. How the code works
3. Important concepts used
4. A simple example if useful

Code:
{code}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text