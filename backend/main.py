
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="DocuMind AI",
    description="AI-powered Document Intelligence Platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "application": "DocuMind AI",
        "message": "Welcome to the Document Intelligence Platform",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
