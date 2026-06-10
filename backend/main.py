from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.lifespan import lifespan
from app.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)