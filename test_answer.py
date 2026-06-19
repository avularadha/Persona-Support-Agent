from src.rag_pipeline import generate_answer

answer = generate_answer(
    "How do I reset my password?"
)

print(answer)