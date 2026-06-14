from azure.storage.blob import BlobServiceClient
from app.settings import settings

class BlobStorageService:
    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )

        self.container = self.client.get_container_client(
            settings.AZURE_STORAGE_CONTAINER
        )
    
    async def upload_file(self, file):
        blob_name = file.filename
        blob_client = self.container.get_blob_client(blob_name)
        content = await file.read()
        blob_client.upload_blob(
            content,
            overwrite=True
        )
        return {
            "blob_name": blob_name,
            "blob_url": blob_client.url
        }