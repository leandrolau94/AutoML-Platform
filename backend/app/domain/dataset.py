from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Dataset(BaseModel):
    id: Optional[str] = None
    
    name: str
    description: str | None = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)