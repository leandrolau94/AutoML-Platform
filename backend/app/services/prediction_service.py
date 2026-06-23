import joblib
import pandas as pd
from app.schemas.prediction import (PredictionResponse, )

class PredictionService:
    def __init__(self, storage):
        self.storage = storage
    
    async def predict(self, model_blob_name: str, values: dict):
        local_model_path = await (self.storage.download_model(model_blob_name))
        pipeline = joblib.load(local_model_path)
        input_df = pd.DataFrame([values])
        prediction = (pipeline.predict(input_df)[0])
        return PredictionResponse(prediction=prediction.item() if hasattr(prediction, "item") else prediction)