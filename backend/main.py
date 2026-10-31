from fastapi import FastAPI
from backend.app.api.routes.documents import router as documents_router
from backend.app.api.routes.health import router as health_router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Document Intelligence Platform",
)


@app.get("/", tags=["General"])
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    documents_router,
    prefix=settings.API_V1_PREFIX,
)