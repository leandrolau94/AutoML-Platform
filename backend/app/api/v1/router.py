from fastapi import APIRouter
from app.api.v1.routers import (health, db_health, datasets, )

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(db_health.router)
api_router.include_router(datasets.router)