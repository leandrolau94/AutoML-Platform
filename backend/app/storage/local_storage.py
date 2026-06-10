from fastapi import UploadFile
from app.settings import settings
from pathlib import Path

class LocalStorage:
    def __init__(self):
        self.upload_dir = Path(settings.UPLOAD_DIR)
        self.upload_dir.mkdir(exist_ok=True)
    
    async def save_file(self, file: UploadFile) -> str:
        file_path = (self.upload_dir / file.filename)
        content = await file.read()
        with open(file_path, "wb") as buffer:
            buffer.write(content)
        return str(file_path)