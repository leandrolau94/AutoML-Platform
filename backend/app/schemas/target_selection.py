from pydantic import BaseModel

class TargetSelectionRequest(BaseModel):
    target_column: str

class TargetSelectionResponse(BaseModel):
    target_column: str
    selection_type: str