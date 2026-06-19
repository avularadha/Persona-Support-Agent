def classify_persona(message):

    text = message.lower()

    frustrated_words = [
        "nothing works",
        "frustrated",
        "angry",
        "urgent",
        "issue",
        "problem",
        "tried everything",
        "not working",
        "help"
    ]

    technical_words = [
        "api",
        "token",
        "401",
        "authentication",
        "endpoint",
        "database",
        "config",
        "server",
        "code"
    ]

    executive_words = [
        "business",
        "impact",
        "revenue",
        "timeline",
        "operations",
        "executive",
        "customer"
    ]

    if any(word in text for word in frustrated_words):
        return "Frustrated User"

    if any(word in text for word in technical_words):
        return "Technical Expert"

    if any(word in text for word in executive_words):
        return "Business Executive"

    return "Technical Expert"