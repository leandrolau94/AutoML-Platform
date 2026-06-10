from fastapi import Depends
from app.api.v1.dependencies import get_db
from app.repositories.dataset_repository import (DatasetRepository, )
from app.services.dataset_service import (DatasetService, )
from app.storage.local_storage import (LocalStorage, )
from app.services.upload_service import (UploadService, )
from app.services.profiling_servicies import (ProfilingService, )
from app.services.insights_service import (InsightsService, )
from app.services.schema_service import (SchemaService, )
from app.services.target_recommendation_service import (TargetRecommendationService, )
from app.services.task_detection_service import (TaskDetectionService, )
from app.services.feature_analysis_service import (FeatureAnalysisService, )
from app.services.training_service import (TrainingService, )
from app.services.model_registry_service import (ModelRegistryService, )
from app.services.prediction_service import (PredictionService, )
from app.services.evaluation_service import (EvaluationService, )

def get_dataset_service(db = Depends(get_db)):
    repository = DatasetRepository(db["datasets"])
    storage = LocalStorage()
    upload_service = UploadService(storage)
    profiling_service = ProfilingService()
    insights_service = InsightsService()
    schema_service = SchemaService()
    target_service = TargetRecommendationService()
    task_detection_service = TaskDetectionService()
    feature_analysis_service = (FeatureAnalysisService())
    model_registry_service = (ModelRegistryService())
    prediction_service = (PredictionService())
    evaluation_service = (EvaluationService())
    training_service = (TrainingService(evaluation_service))
    return DatasetService(
        repository,
        upload_service,
        profiling_service,
        insights_service,
        schema_service,
        target_service,
        task_detection_service,
        feature_analysis_service,
        training_service,
        model_registry_service,
        prediction_service,
        evaluation_service
    )