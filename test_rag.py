from src.rag_pipeline import load_documents, chunk_documents

docs = load_documents()

print("Documents Loaded:", len(docs))
print(docs)

chunks = chunk_documents()

print("Total Chunks:", len(chunks))
print(docs)