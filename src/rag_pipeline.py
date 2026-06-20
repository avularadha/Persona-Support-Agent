import os
import chromadb

from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -------------------------
# Load Documents
# -------------------------

def load_documents():

    documents = []

    data_folder = "data"

    for file in os.listdir(data_folder):

        path = os.path.join(data_folder, file)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        documents.append({
            "source": file,
            "content": content
        })

    return documents


# -------------------------
# Chunk Documents
# -------------------------

def chunk_documents():

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = []

    docs = load_documents()

    for doc in docs:

        split_texts = splitter.split_text(doc["content"])

        for text in split_texts:

            chunks.append({
                "source": doc["source"],
                "text": text
            })

    return chunks


# -------------------------
# Generate Embeddings
# -------------------------

def get_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


# -------------------------
# Store Embeddings in ChromaDB
# -------------------------

def store_embeddings():

    chunks = chunk_documents()

    chroma_client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = chroma_client.get_or_create_collection(
        name="support_docs"
    )

    for index, chunk in enumerate(chunks):

        embedding = get_embedding(
            chunk["text"]
        )

        collection.add(
            ids=[str(index)],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[
                {
                    "source": chunk["source"]
                }
            ]
        )

    print(f"{len(chunks)} chunks stored successfully!")

def search_documents(query):

    chroma_client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = chroma_client.get_collection(
        name="support_docs"
    )

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results

def generate_answer(query):

    results = search_documents(query)

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
You are a customer support assistant.

Context:
{context}

Question:
{query}

Answer only using the context.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text