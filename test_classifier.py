from src.classifier import classify_persona

messages = [
    "Our API is returning 401 Unauthorized errors.",
    "I have tried everything and nothing works!",
    "What is the business impact of this outage?"
]

for message in messages:

    persona = classify_persona(message)

    print("\n==============================")
    print("Message:")
    print(message)

    print("\nDetected Persona:")
    print(persona)
    print("==============================")