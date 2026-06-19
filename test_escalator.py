from src.escalator import (
    should_escalate,
    generate_handoff
)

query = "I want refund immediately for duplicate billing charges"

result = should_escalate(query)

print("Escalate:", result)

if result:

    handoff = generate_handoff(
        "Frustrated User",
        query,
        ["billing_policy.txt"]
    )

    print(handoff)