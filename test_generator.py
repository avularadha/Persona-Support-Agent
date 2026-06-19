from src.generator import generate_adaptive_response

context = """
To reset password:

1. Click Forgot Password
2. Enter email
3. Check inbox
4. Create new password
"""

print(
    generate_adaptive_response(
        "How do I reset my password?",
        "Frustrated User",
        context
    )
)