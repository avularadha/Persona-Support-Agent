import json

from src.config import SENSITIVE_KEYWORDS


def should_escalate(query, confidence=1.0):

    query = query.lower()

    if confidence < 0.45:
        return True

    for word in SENSITIVE_KEYWORDS:
        if word in query:
            return True

    return False

def generate_handoff(
    persona,
    issue,
    sources
):

    handoff = {
        "persona": persona,
        "issue": issue,
        "documents_used": sources,
        "attempted_steps": [
            "Knowledge Base Search",
            "AI Generated Response"
        ],
        "recommendation":
        "Human support agent review required"
    }

    return json.dumps(
        handoff,
        indent=4
    )