from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Dataset Platform"
    API_V1_PREFIX: str = "/api/v1"
    
    MONGODB_URI: str
    DATABASE_NAME: str
    UPLOAD_DIR: str
    
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore"
    )

settings = Settings()