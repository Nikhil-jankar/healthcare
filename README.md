# Healthcare AI Assistant

## Overview

Healthcare AI Assistant is a Retrieval-Augmented Generation (RAG) application designed to answer healthcare policy and operational questions using a private knowledge base.

The system combines semantic search with a Large Language Model (LLM) to generate accurate, context-aware responses while providing source attribution for transparency.

This project demonstrates modern AI engineering practices including:

* Retrieval-Augmented Generation (RAG)
* Vector Search with ChromaDB
* HuggingFace Embeddings
* Ollama-based Local LLM Inference
* FastAPI REST APIs
* Tool-Based Query Routing
* Docker Containerization

---

## Architecture

```text
                 User
                   │
                   ▼
              FastAPI API
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
      Tool Router          RAG
         │                 │
         ▼                 ▼
 Appointment Tool     ChromaDB
                           │
                           ▼
                  HuggingFace Embeddings
                           │
                           ▼
                     Gemma3 (Ollama)
                           │
                           ▼
                        Response
```

---

## Project Structure

```text
healthcare-ai-assistant/

├── app/
│   ├── main.py
│   ├── llm.py
│   ├── retriever.py
│   ├── ingest.py
│   ├── config.py
│   ├── router.py
│   ├── tools.py
│   └── exceptions.py
│
├── data/
│   ├── appointment_policy.txt
│   ├── discharge_policy.txt
│   ├── hipaa_guidelines.txt
│   ├── telehealth_policy.txt
│
├── vector_store/
├── logs/
├── tests/
│   ├── test_ingest.py
│   ├── test_retriever.py
│   └── test_answer.py
│
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## Features

### Retrieval-Augmented Generation (RAG)

* Retrieves relevant healthcare documents
* Uses semantic similarity search
* Generates grounded responses

### Source Attribution

Every answer includes source documents used during retrieval.

### Tool-Based Query Routing

Appointment-related questions are routed to structured tools instead of the RAG pipeline.

### Docker Support

Application can be deployed as a containerized service.

---

## Technology Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Backend API      | FastAPI           |
| Vector Database  | ChromaDB          |
| Embeddings       | all-MiniLM-L6-v2  |
| LLM              | Gemma3 via Ollama |
| Framework        | LangChain         |
| Containerization | Docker            |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd healthcare-ai-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a .env file:

```env
MODEL_NAME=gemma3:4b
VECTOR_DB_PATH=vector_store
```

---

## Ingest Documents

```bash
python test_ingest.py
```

---

## Run API

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Docker Deployment

Build Image:

```bash
docker build -t healthcare-ai .
```

Run Container:

```bash
docker run -p 8000:8000 healthcare-ai
```

---

## Sample API Requests

### Healthcare Policy Question

```json
{
  "question": "Can patients request medication refill through telehealth?"
}
```

### PHI Access Question

```json
{
  "question": "How are patient records secured and who is authorized to access PHI?"
}
```

### Tool-Based Query

```json
{
  "question": "What appointment slots are available in Neurology?"
}
```

---

## Safety Considerations

* Uses synthetic healthcare data only
* No PHI or real patient data
* Provides source attribution
* Reduces hallucinations through retrieval grounding

---

## Future Enhancements

* Hybrid Search (BM25 + Vector Search)
* Multi-document Retrieval
* Re-ranking Pipeline
* Role-Based Access Control
* Production Monitoring
* Cloud Deployment

## Dataset / Source Details

The application uses synthetic healthcare policy documents created specifically for demonstration and evaluation purposes.

No real patient records, Protected Health Information (PHI), confidential healthcare data, or client data were used.

Included documents:

* telehealth_policy.txt
* appointment_policy.txt
* hipaa_guidelines.txt
* discharge_policy.txt

These documents simulate common healthcare operational and compliance policies.

---

## LLM Used

### Gemma3:4b (Ollama)

The application uses the Gemma3:4b large language model running locally through Ollama.

Reasons for selection:

* Runs locally without external API costs
* Good balance between performance and resource consumption
* Suitable for Retrieval-Augmented Generation workflows
* Easy integration with LangChain

---

## Embedding Model Used

### all-MiniLM-L6-v2

Used for generating vector embeddings of healthcare documents.

Reasons for selection:

* Lightweight and fast
* Good semantic search performance
* Low memory requirements
* Widely adopted in RAG applications

---

## Vector Database Used

### ChromaDB

ChromaDB stores document embeddings and enables semantic similarity search.

Reasons for selection:

* Open source
* Lightweight deployment
* Easy LangChain integration
* Suitable for local development and prototyping

---

## Prompting Strategy

The system follows a retrieval-grounded prompting approach.

Workflow:

1. Retrieve relevant document chunks from ChromaDB.
2. Inject retrieved context into the prompt.
3. Instruct the LLM to answer only using retrieved information.
4. Return a fallback response when relevant information cannot be found.

This reduces hallucinations and improves answer reliability.

---

## Agent / Tool Workflow

The application uses a lightweight routing layer.

### RAG Flow

User Question
→ Retriever
→ ChromaDB
→ Retrieved Context
→ Gemma3
→ Response

### Tool Flow

Appointment-related questions
→ Query Router
→ Appointment Tool
→ Structured Response

This demonstrates both retrieval-based and tool-based reasoning.

---

## Limitations

* Small synthetic dataset
* Limited domain coverage
* Basic query routing logic
* No user authentication
* No conversation memory
* Local deployment only

---

## Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Document Re-ranking
* Multi-turn Memory
* Role-Based Access Control
* Cloud Deployment
* Monitoring and Observability
* Additional Healthcare Tools
* Larger Healthcare Knowledge Base



# Quick Start Guide

## Prerequisites

Before running the application, ensure the following are installed:

* Python 3.11 or higher
* Git
* Docker (optional)
* Ollama

---

## Step 1: Clone Repository

```bash
git clone <repository-url>
cd healthcare-ai-assistant
```

---

## Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Install Ollama

Download and install Ollama:

https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## Step 5: Pull LLM Model

```bash
ollama pull gemma3:4b
```

Verify model:

```bash
ollama list
```

Expected output:

```text
gemma3:4b
```

---

## Step 6: Create Environment File

Create a `.env` file in the project root:

```env
MODEL_NAME=gemma3:4b
VECTOR_DB_PATH=vector_store
```

---

## Step 7: Index Documents

Run document ingestion:

```bash
python test_ingest.py
```

Expected output:

```text
Documents indexed successfully!
```

---

## Step 8: Start FastAPI Application

```bash
uvicorn app.main:app --reload
```

Expected output:

```text
Application startup complete.
```

---

## Step 9: Open Swagger UI

Open:

http://localhost:8000/docs

---

## Step 10: Test the Assistant

Example request:

```json
{
  "question": "Can patients request medication refill through telehealth?"
}
```

Expected response:

```json
{
  "answer": "...",
  "sources": [
    "telehealth_policy.txt"
  ],
  "confidence": "high"
}
```

# Running with Docker

## Build Docker Image

```bash
docker build -t healthcare-ai .
```

## Run Container

```bash
docker run -p 8000:8000 healthcare-ai
```

## Open Swagger

http://localhost:8000/docs

--- 

### Note

Ollama must be running on the host machine.

Verify:

```bash
ollama list
```

If using Docker, the application connects to Ollama using:

```text
http://host.docker.internal:11434
```



---

## Author

Nikhil Jankar

AI Engineer Assignment Submission
