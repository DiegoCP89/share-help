from fastapi import FastAPI
from src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """Operational health check endpoint for monitoring uptime and deployment status."""
    return {"status": "healthy", "service": settings.PROJECT_NAME}