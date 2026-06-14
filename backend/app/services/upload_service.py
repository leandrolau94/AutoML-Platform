from fastapi import UploadFile
from datetime import datetime
from io import BytesIO
import pandas as pd
from app.schemas.dataset_metadata import DatasetMetadata
from app.storage.blob_storage import BlobStorage

class UploadService:
    def __init__(self, storage: BlobStorage):
        self.storage = storage

    async def upload_csv(self, file: UploadFile) -> DatasetMetadata:
        blob_info = await self.storage.upload_file(file)
        df = pd.read_csv(
            BytesIO(blob_info["content"])
        )
        file_size_mb = round(
            len(blob_info["content"]) / (1024 * 1024),
            2
        )
        return DatasetMetadata(
            file_name=file.filename,
            blob_name=blob_info["blob_name"],
            blob_url=blob_info["blob_url"],
            rows=len(df),
            columns=len(df.columns),
            file_size_mb=file_size_mb,
            content_type=file.content_type,
            uploaded_at=datetime.utcnow()
        )