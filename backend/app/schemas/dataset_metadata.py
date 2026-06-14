from datetime import datetime
from pydantic import BaseModel

class DatasetMetadata(BaseModel):
    file_name: str
    blob_name: str
    blob_url: str
    rows: int
    columns: int
    file_size_mb: float
    content_type: str
    uploaded_at: datetime