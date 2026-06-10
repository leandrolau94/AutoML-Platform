from datetime import datetime
from pydantic import BaseModel

class DatasetMetadata(BaseModel):
    file_name: str
    file_path: str
    rows: int
    columns: int
    file_size_mb: float
    content_type: str
    uploaded_at: datetime