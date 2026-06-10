from fastapi import FastAPI
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

def get_database(app: FastAPI) -> AsyncDatabase:
    return app.state.mongodb

def get_client(app: FastAPI) -> AsyncMongoClient:
    app.state.mongo_client