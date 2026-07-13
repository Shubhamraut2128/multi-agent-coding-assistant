# 🤖 Multi-Agent Coding Assistant

Link - https://multi-agent-coding-assistant-kso8tzm53rth7zfkwzhuaf.streamlit.app/

An AI-powered Coding Interview Assistant built using **FastAPI**, **Streamlit**, **LangGraph**, **LangChain**, **Groq LLM**, and **ChromaDB**. The application intelligently routes user questions to specialized AI agents for Java, DSA, SQL, and HR interview preparation.

---

## 🚀 Features

- Multi-Agent Architecture
- Automatic Question Routing
- Java Interview Preparation
- Data Structures & Algorithms (DSA)
- SQL Interview Questions
- HR Interview Guidance
- Response Validation Agent
- Retrieval-Augmented Generation (RAG)
- FastAPI Backend
- Streamlit Frontend
- Groq LLM Integration
- ChromaDB Vector Store

---

## 🏗️ Tech Stack

- Python 3.11
- FastAPI
- Streamlit
- LangChain
- LangGraph
- Groq API
- ChromaDB
- Sentence Transformers
- Docker
- Docker Compose

---

## 📂 Project Structure

```
MULTI-AGENT-CODING-ASSISTANT
│
├── app
│   ├── agents
│   ├── graph
│   ├── prompts
│   ├── rag
│   ├── routes
│   ├── schemas
│   ├── utils
│   └── main.py
│
├── data
├── streamlit_app.py
├── requirements.txt
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yml
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-coding-assistant.git
```

Move into the project

```bash
cd multi-agent-coding-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

---

## ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

Open

```
http://localhost:8501
```

---

## 🐳 Docker Deployment

Build the containers

```bash
docker compose build
```

Run the application

```bash
docker compose up
```

---

## 🌐 API Endpoint

### Chat

**POST** `/chat`

Request

```json
{
    "question":"Explain Python decorators"
}
```

Response

```json
{
    "response":"Python decorators are..."
}
```

---

## 🤖 AI Agents

- Supervisor Agent
- Java Agent
- DSA Agent
- SQL Agent
- HR Agent
- Validator Agent

---

## 📚 RAG Pipeline

User Question

↓

Embedding Generation

↓

ChromaDB Retrieval

↓

Relevant Context

↓

Groq LLM

↓

Final Response

---

## 🎯 Future Enhancements

- PDF Upload
- Resume Analysis
- Coding Playground
- Conversation History
- Authentication
- Multi-language Support
- Cloud Deployment

---

## 👨‍💻 Author

**Shubham Raut**

Python Full Stack Developer
