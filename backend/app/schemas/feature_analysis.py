from pydantic import BaseModel
class FeatureAnalysisResponse(BaseModel):
    selected_features: list[str]
    excluded_features: list[dict]