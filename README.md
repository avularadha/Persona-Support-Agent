# 🤖 Persona Support Agent

An AI-powered customer support chatbot built using RAG (Retrieval Augmented Generation), Gemini API, ChromaDB, and Streamlit.

## 📌 Project Overview

Persona Support Agent helps users get answers from support documents.

Instead of relying only on an LLM, the chatbot first searches relevant documents from a knowledge base and then generates accurate answers using Gemini.

---

## 🚀 Features

- Load support documents
- Split documents into chunks
- Generate embeddings using Gemini
- Store embeddings in ChromaDB
- Semantic search using vector similarity
- AI-generated answers using Gemini
- Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Gemini API
- ChromaDB
- LangChain Text Splitter
- Streamlit

---

## 📂 Project Structure

```text
persona-support-agent/
│
├── data/
│   ├── api_troubleshooting.md
│   ├── billing_policy.txt
│   └── password_reset_guide.txt
│
├── src/
│   ├── rag_pipeline.py
│   ├── classifier.py
│   ├── escalator.py
│   └── generator.py
│
├── chroma_db/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🔄 RAG Workflow

```text
Support Documents
        ↓
Document Chunking
        ↓
Gemini Embeddings
        ↓
ChromaDB Storage
        ↓
User Question
        ↓
Similarity Search
        ↓
Relevant Context Retrieval
        ↓
Gemini Response Generation
        ↓
Final Answer
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd persona-support-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## 💬 Example Questions

- How do I reset my password?
- Why am I getting 401 Unauthorized?
- What is the billing policy?

---

## 🎯 Learning Outcomes

Through this project I learned:

- Retrieval Augmented Generation (RAG)
- Vector Databases
- Embeddings
- Semantic Search
- ChromaDB
- Gemini API Integration
- Streamlit Application Development

---

## 👩‍💻 Author

Radha

MERN Stack Developer | Python Developer | AI Enthusiast