from app.domain.dataset import Dataset
from app.repositories.dataset_repository import (DatasetRepository, )
from app.schemas.dataset import DatasetCreate, DatasetUpdate
from app.services.upload_service import UploadService
from app.services.profiling_servicies import (ProfilingService, )
from app.services.insights_service import (InsightsService, )
from app.services.schema_service import (SchemaService, )
from app.services.target_recommendation_service import(TargetRecommendationService, )
from app.schemas.target_selection import (TargetSelectionResponse, )
from app.services.task_detection_service import (TaskDetectionService, )
from app.services.feature_analysis_service import (FeatureAnalysisService, )
from app.services.training_service import (TrainingService, )
from app.services.model_registry_service import (ModelRegistryService, )
from app.services.prediction_service import (PredictionService, )
from app.services.evaluation_service import (EvaluationService, )
from app.services.benchmark_service import (BenchmarkService, )

class DatasetService:
    
    def __init__(self, repository: DatasetRepository, upload_service: UploadService, profiling_service: ProfilingService, insights_service: InsightsService, schema_service: SchemaService, target_service: TargetRecommendationService, task_detection_service: TaskDetectionService, feature_analysis_service: FeatureAnalysisService, training_service: TrainingService, model_registry_service: ModelRegistryService, prediction_service: PredictionService, evaluation_service: EvaluationService, benchmark_service: BenchmarkService):
        self.repository = repository
        self.upload_service = upload_service
        self.profiling_service = profiling_service
        self.insights_service = (insights_service)
        self.schema_service = (schema_service)
        self.target_service = (target_service)
        self.task_detection_service = (task_detection_service)
        self.feature_analysis_service = (feature_analysis_service)
        self.training_service = (training_service)
        self.model_registry_service = (model_registry_service)
        self.prediction_service = (prediction_service)
        self.evaluation_service = (evaluation_service)
        self.benchmark_service = (benchmark_service)
    
    async def create_dataset(self, payload: DatasetCreate) -> str:
        dataset = Dataset(name=payload.name, description=payload.description)
        return await self.repository.create(dataset)
    
    async def get_all_datasets(self):
        return await self.repository.get_all()
    
    async def get_dataset_by_id(self, dataset_id: str):
        return await self.repository.get_by_id(dataset_id)
    
    async def delete_dataset(self, dataset_id: str):
        return await self.repository.delete(dataset_id)
    
    async def update_dataset(self, dataset_id: str, dataset: DatasetUpdate):
        update_data = dataset.model_dump(exclude_unset=True)
        return await self.repository.update(dataset_id, update_data)
    
    async def upload_dataset(self, file):
        metadata = await self.upload_service.upload_csv(file)
        dataset_id = await self.repository.create_metadata(metadata.model_dump())
        return {"id": dataset_id, **metadata.model_dump()}
    
    async def profile_dataset(self, dataset_id: str):
        dataset = await self.repository.get_by_id(dataset_id)
        if not dataset:
            return {"error": "Dataset not found"}
        return await self.profiling_service.profile_dataset(dataset["file_path"])
    
    async def dataset_insights(self, dataset_id: str):
        dataset = await self.repository.get_by_id(dataset_id)
        if not dataset:
            return {"error": "Dataset not found"}
        profile = (await self.profiling_service.profile_dataset(dataset["file_path"]))
        return await (self.insights_service.generate_insights(profile))
    
    async def get_schema(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        schema = await (self.schema_service.analyze(dataset["file_path"]))
        await (self.repository.save_schema(dataset_id, schema.model_dump()))
        return schema
    
    async def get_target_candidates(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        schema = (dataset.get("schema"))
        if not schema:
            return {"error": "Schema not generated"}
        candidates = await (self.target_service.recommend(schema))
        await (self.repository.save_target_candidates(dataset_id, candidates))
        return candidates
    
    async def select_target(self, dataset_id: str, target_column: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        schema = dataset.get("schema")
        if not schema:
            return {"error": "Schema not generated"}
        # analyzing when the user select target column, otherwise the platform itself
        schema_columns = [column["name"] for column in schema["columns"]]#getting all possible candidates
        if target_column not in schema_columns:
            return {"error": f"Column {target_column} not found"}
        #set up the top 5 column targets
        recommended_columns = [candidate["column"] for candidate in dataset.get("target_candidates", {}).get("candidates", [])[:5]]
        selection_type = ("recommended" if target_column in recommended_columns else "manual")#deciding if user or platform stated the target column, recommended correspond to platform and manual to user selection
        selected_target = {"column": target_column, "selection_type": selection_type}
        await (self.repository.save_selected_target(dataset_id, selected_target))
        return TargetSelectionResponse(target_column=target_column, selection_type=selection_type)
    
    async def get_task_type(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "dataset not found"}
        selected_target = dataset.get("selected_target")
        if not self.select_target:
            return {"error": "target not selected"}
        target_name = selected_target["column"]
        schema = dataset["schema"]
        target_column = next((column for column in schema["columns"] if column["name"] == target_name), None)
        if not target_column:
            return {"error": "Target column not found"}
        task_detection = await (self.task_detection_service.detect(target_column))
        await (self.repository.save_task_detection(dataset_id, task_detection.model_dump()))
        return task_detection
    
    async def get_feature_analysis(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        selected_target = dataset.get("selected_target")
        if not self.select_target:
            return {"error": "Target not selected"}
        target_name = (selected_target["column"])
        schema = dataset["schema"]
        feature_analysis = await (self.feature_analysis_service.analyze(schema, target_name))
        await (self.repository.save_feature_analysis(dataset_id, feature_analysis.model_dump()))
        return feature_analysis
    
    async def train_model(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        training_result = await (self.training_service.train(dataset))
        await (self.repository.save_training(dataset_id, training_result.model_dump()))
        return training_result
    
    async def get_model_registry(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found."}
        return await (self.model_registry_service.get_model(dataset))
    
    async def predict(self, dataset_id: str, values: dict):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        training = dataset.get("training")
        if not training:
            return {"error": "Not training model found"}
        model_path = training["model_path"]
        return await (self.prediction_service.predict(model_path, values))
    
    async def benchmark(self, dataset_id: str):
        dataset = await (self.repository.get_by_id(dataset_id))
        if not dataset:
            return {"error": "Dataset not found"}
        benchmark_result = await self.benchmark_service.benchmark(dataset)
        await self.repository.save_benchmark(dataset_id, benchmark_result.model_dump())
        return benchmark_result