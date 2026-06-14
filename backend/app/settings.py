from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Dataset Platform"
    API_V1_PREFIX: str = "/api/v1"
    
    MONGODB_URI: str
    DATABASE_NAME: str
    UPLOAD_DIR: str
    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER: str = "datasets"
    
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore"
    )

settings = Settings()