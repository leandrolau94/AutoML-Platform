from pydantic import BaseModel

class BenchmarkResponse(BaseModel):
    best_model: str
    best_metric: float
    results: list