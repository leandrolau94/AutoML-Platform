from app.domain.dataset import Dataset
from typing import List
from bson import ObjectId
from datetime import datetime

class DatasetRepository:
    def __init__(self, collection):
        self.collection = collection
    
    async def create(self, dataset: Dataset) -> str:
        result = await self.collection.insert_one(dataset.model_dump(exclude={"id"}))
        return str(result.inserted_id)
    
    async def get_all(self) -> List[dict]:
        cursor = self.collection.find({})
        datasets = await cursor.to_list(length=None)
        for dataset in datasets:
            dataset["_id"] = str(dataset["_id"])
        return datasets
    
    async def get_by_id(self, dataset_id: str):
        dataset = await self.collection.find_one({"_id": ObjectId(dataset_id)})
        if dataset:
            dataset["_id"] = str(dataset["_id"])
        return dataset
    
    async def delete(self, dataset_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(dataset_id)})
        return result.deleted_count > 0
    
    async def update(self, dataset_id: str, update_data: dict) -> bool:
        update_data["updated_at"] = datetime.utcnow()
        result = await self.collection.update_one(
            {"_id": ObjectId(dataset_id)},
            {"$set": update_data}
        )
        return result.matched_count > 0
    
    async def create_metadata(self, metadata: dict) -> str:
        result = await self.collection.insert_one(metadata)
        return str(result.inserted_id)
    
    async def get_by_id(self, dataset_id: str):
        document = await self.collection.find_one({"_id": ObjectId(dataset_id)})
        return document
    
    async def save_schema(self, dataset_id: str, schema_data: dict):
        await self.collection.update_one({"_id": ObjectId(dataset_id)},{"$set": {"schema": schema_data}})
    
    async def save_target_candidates(self, dataset_id: str, candidates: dict):
        await (self.collection.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"target_candidates": candidates}}))
    
    async def save_selected_target(self, dataset_id: str, selected_target: dict):
        await self.collection.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"selected_target": selected_target}})
    
    async def save_task_detection(self, dataset_id: str, task_detection: dict):
        await self.collection.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"task_detection": task_detection}})
    
    async def save_feature_analysis(self, dataset_id: str, feature_analysis: dict):
        await self.collection.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"feature_analysis": feature_analysis}})
    
    async def save_training(self, dataset_id: str, training: dict):
        await self.collection.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"training": training}})