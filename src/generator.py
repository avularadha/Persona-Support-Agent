import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_adaptive_response(
    user_query,
    persona,
    context
):

    if persona == "Technical Expert":

        style = """
You are a senior technical support engineer.

Provide:
- Detailed explanation
- Root cause analysis
- Step-by-step troubleshooting
"""

    elif persona == "Frustrated User":

        style = """
You are an empathetic support specialist.

Provide:
- Reassurance
- Simple language
- Actionable steps
- Friendly tone
"""

    else:

        style = """
You are a business support manager.

Provide:
- Concise response
- Business impact
- Resolution guidance
- Minimal technical jargon
"""

    prompt = f"""
{style}

Context:
{context}

User Question:
{user_query}

Answer only using the context.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"