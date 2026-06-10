from fastapi import APIRouter, Depends
from pymongo.asynchronous.database import AsyncDatabase
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/health/db", tags=["database"])

@router.get("/")
async def database_health(db: AsyncDatabase = Depends(get_db)):
    await db.command("ping")
    
    return {
        "database": "connected"
    }