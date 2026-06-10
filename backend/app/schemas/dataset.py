from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class DatasetCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = None

class DatasetResponse(BaseModel):
    id: str
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime

class DatasetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None