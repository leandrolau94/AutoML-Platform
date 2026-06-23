from pydantic import BaseModel

class TrainingResponse(BaseModel):
    model_name: str
    task_type: str
    train_rows: int
    test_rows: int
    metrics: dict
    model_path: str
    model_blob_name: str
    model_blob_url: str