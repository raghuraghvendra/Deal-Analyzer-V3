# 📄 Deal Analyzer V3

An enterprise-style AI Contract Intelligence Platform that analyzes legal contracts using Retrieval-Augmented Generation (RAG), Multi-Agent AI, and Large Language Models.

The project is designed with production software engineering principles, making it modular, scalable, and ready for future enterprise integrations such as MCP, Docker deployment, authentication, monitoring, and cloud hosting.

---

## ✨ Features

* 📄 PDF Contract Parsing
* ✂️ Intelligent Text Chunking
* 🔍 Semantic Search with Qdrant Vector Database
* 🧠 BGE Embeddings
* 📚 Retrieval-Augmented Generation (RAG)
* 🤖 Multi-Agent AI Architecture
* ⚖️ Legal Risk Analysis
* 💰 Financial Risk Analysis
* 🛡️ Compliance Analysis
* 👨‍⚖️ Judge Agent for Final Contract Intelligence
* 📊 Interactive Streamlit Dashboard
* 🏗️ Modular Enterprise Architecture

---

## 🏛️ System Architecture

```text
                 Streamlit UI
                       │
                 pipeline.py
                       │
         ContractAnalysisService
                       │
        ┌──────────────┴──────────────┐
        │                             │
 Document Processing          Agent Orchestrator
(Parse → Chunk → Embed)               │
                                      ▼
          ┌─────────────┬─────────────┬─────────────┐
          ▼             ▼             ▼
     Legal Agent   Financial Agent   Compliance Agent
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  Judge Agent
                        ▼
              Final Contract Report
                        ▼
                 Streamlit Dashboard
```

---

## 🧠 AI Pipeline

1. Upload PDF Contract
2. Extract Contract Text
3. Chunk Document
4. Generate Embeddings
5. Store in Qdrant
6. Retrieve Relevant Context
7. Legal Agent Analysis
8. Financial Agent Analysis
9. Compliance Agent Analysis
10. Judge Agent Synthesizes Final Report
11. Display Results in Streamlit Dashboard

---

## 🛠️ Tech Stack

### AI & Machine Learning

* Google Gemini 2.5 Flash
* Sentence Transformers (BGE Small)
* Cross Encoder Reranker

### Vector Database

* Qdrant

### Backend

* Python
* FastAPI (planned)
* Streamlit

### Libraries

* PyMuPDF
* Qdrant Client
* Sentence Transformers
* Rank BM25
* Python Dotenv

---

## 📂 Project Structure

```
Deal_Analyzer_V3/

backend/
│
├── agents/
├── ingestion/
├── llm/
├── prompts/
├── retrieval/
├── services/
├── utils/
└── vectorstore/

assets/
docs/
tests/

app.py
pipeline.py
ui.py
config.py

requirements.txt
README.md
.gitignore
```

---

## 🚀 Future Roadmap

### Phase 1 ✅

* RAG Pipeline
* Vector Search
* Streamlit Dashboard
* Multi-Agent Architecture

### Phase 2

* Model Context Protocol (MCP)
* Tool Calling
* Agent Memory

### Phase 3

* JWT Authentication
* Prompt Injection Protection
* Input Validation
* Logging & Monitoring

### Phase 4

* Docker
* Docker Compose
* CI/CD
* Cloud Deployment

---

## 📌 Project Status

🚧 Actively under development.

Current focus:

* Enterprise Multi-Agent AI
* Production Software Architecture
* MCP Integration
* Security
* Docker Deployment

---

## 👨‍💻 Author

**Raghvendra Singh**

AI / Machine Learning Engineer

Focused on building production-ready AI systems using RAG, Agentic AI, and modern software architecture.
