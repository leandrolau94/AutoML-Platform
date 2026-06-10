from pydantic import BaseModel

class TaskDetectionResponse(BaseModel):
    task_type: str
    confidence: float
    reasons: list[str]