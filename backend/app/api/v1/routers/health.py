from fastapi import APIRouter
from datetime import datetime, UTC

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
async def health_check():
    return {
        "status": "healthy",
        "service": "AI Dataset Platform",
        "timestamp": datetime.now(UTC)
    }