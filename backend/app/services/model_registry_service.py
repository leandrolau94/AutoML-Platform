from app.schemas.model_registry import (ModelRegistryResponse, )

class ModelRegistryService:
    async def get_model(self, dataset: dict):
        training = dataset.get("training")
        if not training:
            return {"error": "No trained model found"}
        return ModelRegistryResponse(model_name=training["model_name"], task_type=training["task_type"], metrics=training["metrics"], model_path=training["model_path"])