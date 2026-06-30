# 🚀 Enterprise AI Contract Intelligence Platform

An enterprise-grade AI-powered contract analysis platform that combines **Retrieval-Augmented Generation (RAG)**, **Multi-Agent AI**, and a **custom MCP-inspired tool architecture** to deliver intelligent legal, financial, and compliance insights from business contracts.

---

## ✨ Features

* 📄 Upload and analyze PDF contracts
* 🔍 Semantic chunking using Recursive Character Text Splitter
* 🧠 Embedding generation with Sentence Transformers
* 🗂️ Qdrant Vector Database for semantic retrieval
* ⚡ Hybrid Retrieval Pipeline (Embeddings + BM25)
* 🤖 Multi-Agent AI Architecture

  * Legal Agent
  * Financial Agent
  * Compliance Agent
  * Judge Agent
* 🛠️ Custom MCP-inspired Tool Architecture
* 📚 Company Policy Retrieval Tool
* 🎯 Intelligent Risk Assessment
* 📊 Interactive Streamlit Dashboard
* 🐳 Dockerized Deployment

---

# 🏗️ System Architecture

```text
                     ┌────────────────────────┐
                     │     Upload PDF         │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │      PDF Parser        │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │    Smart Chunking      │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │  Embedding Generation  │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │ Qdrant Vector Database │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │  Knowledge Service     │
                     └──────────┬─────────────┘
                                │
                                ▼
                    ┌──────────────────────────┐
                    │   Agent Orchestrator     │
                    └──────────┬───────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
 ┌────────────────┐   ┌────────────────┐   ┌─────────────────┐
 │  Legal Agent   │   │ Financial Agent│   │ Compliance Agent│
 └────────┬───────┘   └────────┬───────┘   └────────┬────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                     ┌────────────────────────┐
                     │      Judge Agent       │
                     └──────────┬─────────────┘
                                ▼
                     ┌────────────────────────┐
                     │   Streamlit Dashboard  │
                     └────────────────────────┘
```

---

# 🧠 Multi-Agent Workflow

### ⚖️ Legal Agent

* Liability Analysis
* Termination Clauses
* Governing Law
* Confidentiality
* Legal Risk Assessment

### 💰 Financial Agent

* Payment Terms
* Financial Obligations
* Pricing Risks
* Late Payment Clauses
* Financial Risk Analysis

### 🛡️ Compliance Agent

* Data Privacy
* Regulatory Compliance
* Intellectual Property
* Security Requirements
* Compliance Risk Analysis

### 👨‍⚖️ Judge Agent

Combines all specialist reports into a final executive contract assessment including:

* Overall Risk Score
* Financial Risk
* Payment Summary
* Termination Summary
* Missing Clauses
* Red Flags
* Recommendations

---

# 🛠️ MCP-inspired Tool Architecture

The project includes a lightweight MCP-inspired tool architecture that enables agents to access external tools before generating their final analysis.

Current Tool:

* Company Policy Search Tool

Architecture:

```text
Legal Agent
      │
      ▼
Tool Decision Engine
      │
      ▼
MCP Client
      │
      ▼
MCP Server
      │
      ▼
Company Policy Tool
      │
      ▼
Policy Result
      │
      ▼
LLM Analysis
```

---

# 💻 Tech Stack

### Languages

* Python

### AI & LLM

* Google Gemini
* Sentence Transformers

### Retrieval

* Qdrant
* BM25
* Vector Embeddings

### Backend

* FastAPI
* Streamlit

### PDF Processing

* PyMuPDF

### Deployment

* Docker
* Docker Compose

---

# 📂 Project Structure

```text
Deal_Analyzer_V3/

├── backend/
│   ├── agents/
│   ├── ingestion/
│   ├── llm/
│   ├── mcp/
│   ├── prompts/
│   ├── retrieval/
│   ├── services/
│   ├── utils/
│   └── vectorstore/
│
├── assets/
├── docs/
├── tests/
│
├── app.py
├── pipeline.py
├── ui.py
├── config.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Deal-Analyzer-V3.git

cd Deal-Analyzer-V3
```

---

## Local Setup

```bash
pip install -r requirements.txt

streamlit run app.py
```

---

## Docker

```bash
docker compose up --build
```

---

# 📈 Future Improvements

* JWT Authentication
* Prompt Injection Protection
* Role-Based Access Control
* Official MCP SDK Integration
* Additional AI Tools
* Cloud Deployment
* Monitoring & Logging
* Advanced Agent Tool Selection

---

# 👨‍💻 Author

**Raghvendra Singh**

AI / ML Engineer | Generative AI | RAG | Multi-Agent Systems

---

# ⭐ If you found this project interesting, consider giving it a star!
