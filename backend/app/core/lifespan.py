from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.logging import logger
from pymongo import AsyncMongoClient
from app.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Starting")
    
    mongo_client = AsyncMongoClient(
        settings.MONGODB_URI
    )
    
    mongodb = mongo_client[
        settings.DATABASE_NAME
    ]
    
    app.state.mongo_client = mongo_client
    app.state.mongodb = mongodb
    
    logger.info(f"Connected to MongoDB: {settings.DATABASE_NAME}")
    
    yield
    
    logger.info("Application Shutting Down")
    mongo_client.close()