from pydantic import BaseModel

class PredictionRequest(BaseModel):
    values: dict

class PredictionResponse(BaseModel):
    prediction: float | int | str