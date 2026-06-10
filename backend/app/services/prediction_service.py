import joblib
import pandas as pd
from app.schemas.prediction import (PredictionResponse, )

class PredictionService:
    async def predict(self, model_path: str, values: dict):
        pipeline = joblib.load(model_path)
        input_df = pd.DataFrame([values])
        prediction = (pipeline.predict(input_df)[0])
        return PredictionResponse(prediction=prediction.item() if hasattr (prediction, "item") else prediction)