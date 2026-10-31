# DocuMind AI

**AI-Powered Document Intelligence Platform**

DocuMind AI is an AI-powered document intelligence platform designed to help users extract knowledge from business documents, ask questions using natural language, and receive context-aware answers with references to original document sources.

The platform aims to make business knowledge more accessible through intelligent document processing, semantic search, and Retrieval-Augmented Generation (RAG).

## Vision

Make business knowledge accessible, searchable, and actionable through AI-powered document intelligence.

## Key Features

### Implemented
- Modular FastAPI backend architecture
- Centralized application configuration using Pydantic Settings
- Application health-check endpoint
- Application readiness endpoint
- Automated API testing using Pytest
- Interactive API documentation using Swagger UI

### Planned
- Document upload and management
- PDF and Microsoft Word document processing
- Intelligent document search
- AI-powered question answering
- Retrieval-Augmented Generation (RAG)
- Source and page-level citations
- Secure user authentication and authorization
- Document usage analytics

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Configuration | Pydantic Settings |
| Frontend | Next.js, TypeScript |
| Database | PostgreSQL |
| Vector Search | pgvector |
| AI Architecture | Retrieval-Augmented Generation |
| Testing | Pytest, HTTPX |
| API Documentation | Swagger / OpenAPI |
| Containerization | Docker |

*Some technologies are planned for future development and are not yet integrated.*

## Backend Architecture

```text
ai-document-intelligence/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       └── health.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── schemas/
│   │   └── services/
│   │
│   └── main.py
│
├── tests/
│   └── test_health.py
│
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

The backend follows a modular architecture that separates API routes, application configuration, data schemas, and business services.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |
| GET | `/api/v1/health` | Application health check |
| GET | `/api/v1/ready` | Application readiness check |

### Interactive API Documentation

Once the backend is running, access:

- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI Schema: http://127.0.0.1:8000/openapi.json

## Getting Started

### Prerequisites

- Python 3.12 or later
- Git
- PowerShell (Windows) or a compatible terminal

### 1. Clone the repository

```bash
git clone https://github.com/rj-tech-labs/ai-document-intelligence.git
cd ai-document-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install development dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 5. Start the application

```bash
python -m uvicorn backend.main:app --reload
```

The backend will be available at:

`http://127.0.0.1:8000`

## Running Tests

Execute the automated test suite:

```bash
python -m pytest -v
```

The current test suite validates:

- Root endpoint response
- Health-check endpoint response
- Readiness endpoint response

**Current test status:** 3 tests passing.

## Project Status

**Phase 1 – Foundation:** Completed

- Initial repository setup
- FastAPI application initialization
- Modular backend architecture
- Centralized configuration
- Health and readiness endpoints
- Automated API tests

**Phase 2 – Document Intelligence:** Planned

- Document upload and processing
- Text extraction
- Document storage
- Vector embeddings
- Semantic search
- RAG-based question answering

## Repository

[https://github.com/rj-tech-labs/ai-document-intelligence](https://github.com/rj-tech-labs/ai-document-intelligence)

## About

Built and maintained by **RJ Tech Labs**.

*Building practical AI-powered enterprise solutions.*