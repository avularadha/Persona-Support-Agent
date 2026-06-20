🤖 Persona Support Agent

An AI-powered customer support chatbot built using Retrieval-Augmented Generation (RAG), Google Gemini, ChromaDB, and Streamlit.

The system automatically detects customer personas, retrieves relevant information from a knowledge base, generates persona-adaptive responses, and escalates sensitive issues to a human support agent when necessary.

---

📌 Project Overview

Persona Support Agent is an intelligent support assistant designed to improve customer interactions by combining:

- Persona Detection
- Retrieval-Augmented Generation (RAG)
- Adaptive Response Generation
- Human Escalation Workflow

Instead of relying solely on an LLM, the system first retrieves relevant information from a support knowledge base and then generates grounded responses using Gemini.

---

🎯 Objectives

The application can:

- Detect customer personas automatically
- Retrieve relevant support documents
- Generate context-aware responses
- Adapt tone based on user persona
- Escalate sensitive issues
- Generate structured handoff summaries
- Provide an interactive Streamlit interface

---

👤 Supported Personas

Technical Expert

Characteristics:

- Uses technical terminology
- Requests APIs, logs, configurations
- Wants detailed explanations

Response Style:

- Detailed
- Technical
- Step-by-step troubleshooting
- Root cause analysis

Example:

Why am I receiving a 401 Unauthorized error while using your API?

---

Frustrated User

Characteristics:

- Uses emotional language
- Expresses urgency
- Repeated complaints

Response Style:

- Empathetic
- Friendly
- Action-oriented
- Simple language

Example:

I've tried everything and nothing works!

---

Business Executive

Characteristics:

- Outcome focused
- Interested in business impact
- Prefers concise communication

Response Style:

- Professional
- Brief
- Impact-focused
- Resolution-oriented

Example:

How will this issue impact operations and when will it be resolved?

---

🚀 Features

- Persona Detection
- Document Loading
- Text Chunking
- Gemini Embeddings
- ChromaDB Vector Storage
- Semantic Search
- Adaptive Response Generation
- Escalation Logic
- Human Handoff Summary
- Streamlit User Interface
- Chat History

---

🛠️ Tech Stack

Backend

- Python 3.11+

LLM

- Google Gemini 2.5 Flash

Embeddings

- Gemini Embedding Model

Vector Database

- ChromaDB

Frameworks & Libraries

- Streamlit
- LangChain Text Splitter
- Python Dotenv
- Google GenAI SDK

---

📂 Project Structure

persona-support-agent/
│
├── data/
│   ├── api_troubleshooting.md
│   ├── billing_policy.txt
│   ├── account_lockout.txt
│   ├── payment_failure.txt
│   ├── login_issues.txt
│   ├── password_reset_guide.txt
│   └── password_reset_guide.pdf
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── classifier.py
│   ├── rag_pipeline.py
│   ├── generator.py
│   └── escalator.py
│
├── chroma_db/
│
├── app.py
├── requirements.txt
├── .env
└── README.md

---

🔄 System Architecture

User Query
      ↓
Persona Classification
      ↓
Knowledge Base Retrieval
      ↓
Vector Similarity Search
      ↓
Relevant Context Retrieval
      ↓
Adaptive Prompt Generation
      ↓
Response Generation
      ↓
Escalation Check
      ↓
Human Handoff (if needed)

---

🧠 Persona Detection Strategy

The system uses Google Gemini to analyze incoming messages and classify users into one of three personas:

- Technical Expert
- Frustrated User
- Business Executive

The detected persona determines the response tone, structure, and level of technical detail.

---

📚 RAG Pipeline Design

Step 1: Document Ingestion

Support documents are loaded from the data directory.

Supported formats:

- TXT
- Markdown
- PDF

---

Step 2: Document Chunking

Documents are split using:

RecursiveCharacterTextSplitter

Configuration:

Chunk Size: 300
Chunk Overlap: 50

---

Step 3: Embedding Generation

Each chunk is converted into vector embeddings using:

Gemini Embedding Model

---

Step 4: Vector Storage

Embeddings are stored in:

ChromaDB

with metadata including:

- Source Document
- Chunk Information

---

Step 5: Retrieval

User queries are embedded and matched against stored document embeddings using semantic similarity search.

Top matching chunks are retrieved and passed to Gemini.

---

🚨 Escalation Logic

The system escalates conversations when:

- Billing issues are detected
- Refund requests are detected
- Legal concerns are detected
- Account-sensitive requests are detected

Keywords include:

billing
refund
payment
legal
account

---

📄 Human Handoff Summary

When escalation occurs, the system generates:

{
  "persona": "Frustrated User",
  "issue": "Unable to reset password",
  "documents_used": [
    "password_reset_guide.pdf"
  ],
  "attempted_steps": [
    "Knowledge Base Search",
    "AI Generated Response"
  ],
  "recommendation": "Human support agent review required"
}

---

▶️ Installation

Clone Repository

git clone <repository-url>
cd persona-support-agent

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

---

🔑 Environment Variables

Create a ".env" file:

GEMINI_API_KEY=your_api_key_here

---

▶️ Run Application

python -m streamlit run app.py

---

💬 Example Queries

Technical Expert

What are the header requirements for bearer token authentication?

Frustrated User

I've tried everything and nothing works!

Business Executive

How does this issue impact operations?

Password Reset

How do I reset my password?

Billing Escalation

I want an immediate refund for duplicate charges.

---

📊 Future Improvements

- Multi-turn memory
- LangGraph workflow
- Confidence-based escalation
- Analytics dashboard
- Human approval workflow
- Feedback collection

---

⚠️ Known Limitations

- Limited by available support documents
- Requires valid Gemini API access
- Basic conversation memory
- Escalation rules are keyword-based

---

🎓 Learning Outcomes

Through this project I learned:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- ChromaDB
- Embeddings
- Semantic Search
- Prompt Engineering
- Gemini API Integration
- Streamlit Deployment
- Human-in-the-Loop AI Systems

---

👩‍💻 Author

Radha

MERN Stack Developer | Python Developer | AI Enthusiast