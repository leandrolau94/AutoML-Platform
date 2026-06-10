from pydantic import BaseModel

class ModelRegistryResponse(BaseModel):
    model_name: str
    task_type: str
    metrics: dict
    model_path: str