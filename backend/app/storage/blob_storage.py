from azure.storage.blob import BlobServiceClient
from app.settings import settings
from pathlib import Path

class BlobStorage:
    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )
        self.container = self.client.get_container_client(
            settings.AZURE_STORAGE_CONTAINER
        )

    async def upload_file(self, file):
        content = await file.read()
        blob_client = self.container.get_blob_client(file.filename)
        blob_client.upload_blob(
            content,
            overwrite=True
        )
        return {
            "blob_name": file.filename,
            "blob_url": blob_client.url,
            "content": content
        }
    
    async def download_file(self, blob_name: str) -> str:
        temp_dir = Path("/tmp")
        temp_dir.mkdir(exist_ok=True)
        local_file = temp_dir / blob_name
        blob_client = self.container.get_blob_client(blob_name)
        with open(local_file, "wb") as file:
            file.write(
                blob_client.download_blob().readall()
            )
        return str(local_file)