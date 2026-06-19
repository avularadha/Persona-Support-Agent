from src.rag_pipeline import get_embedding

embedding = get_embedding(
    "How can I reset my password?"
)

print("Vector Length:", len(embedding))
print(embedding[:5])