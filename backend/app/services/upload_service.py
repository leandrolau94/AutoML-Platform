from fastapi import UploadFile
from datetime import datetime
from pathlib import Path
import pandas as pd
from app.schemas.dataset_metadata import (DatasetMetadata, )
from app.storage.local_storage import (LocalStorage, )

class UploadService:
    def __init__(self, storage: LocalStorage):
        self.storage = storage
    
    async def upload_csv(self, file: UploadFile) -> DatasetMetadata:
        file_path = await self.storage.save_file(file)
        df = pd.read_csv(file_path)
        file_size_mb = round(Path(file_path).stat().st_size / (1024 * 1024), 2)
        return DatasetMetadata(
            file_name=file.filename,
            file_path=file_path,
            rows=len(df),
            columns=len(df.columns),
            file_size_mb=file_size_mb,
            content_type=file.content_type,
            uploaded_at=datetime.utcnow()
        )