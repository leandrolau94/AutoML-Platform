from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from app.api.v1.dependencies_dataset import (get_dataset_service, )
from app.schemas.dataset import DatasetCreate, DatasetUpdate
from app.services.dataset_service import (DatasetService, )
from app.schemas.target_selection import (TargetSelectionRequest, )

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_dataset(payload: DatasetCreate, service: DatasetService = Depends(get_dataset_service)):
    dataset_id = await service.create_dataset(payload)
    return {
        "id": dataset_id,
        "message": "Dataset created successfully"
    }

@router.get("/")
async def get_datasets(dataset_service=Depends(get_dataset_service)):
    return await dataset_service.get_all_datasets()

@router.get("/{dataset_id}")
async def get_dataset(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await dataset_service.get_dataset_by_id(dataset_id)

@router.delete("/{dataset_id}")
async def delete_dataset(dataset_id: str, dataset_service = Depends(get_dataset_service)):
    deleted = await dataset_service.delete_dataset(dataset_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return {"message": "Dataset deleted successfully"}

@router.put("/{dataset_id}")
async def update_dataset(dataset_id: str, dataset: DatasetUpdate, dataset_service = Depends(get_dataset_service)):
    updated = await dataset_service.update_dataset(dataset_id, dataset)
    if not updated:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return {"message": "Dataset updated successfully"}

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...), dataset_service = Depends(get_dataset_service)):
    return await dataset_service.upload_dataset(file)

@router.get("/{dataset_id}/profile")
async def profile_dataset(dataset_id: str, dataset_service = Depends(get_dataset_service)):
    return await dataset_service.profile_dataset(dataset_id)

@router.get("/{dataset_id}/insights")
async def dataset_insights(dataset_id: str, dataset_service = Depends(get_dataset_service)):
    return await (dataset_service.dataset_insights(dataset_id))

@router.get("/{dataset_id}/schema")
async def dataset_schema(dataset_id: str, dataset_service = Depends(get_dataset_service)):
    return await (dataset_service.get_schema(dataset_id))

@router.get("/{dataset_id}/target-candidates")
async def target_candidates(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.get_target_candidates(dataset_id))

@router.post("/{dataset_id}/target")
async def select_target(dataset_id: str, request: TargetSelectionRequest, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.select_target(dataset_id, request.target_column))

@router.get("/{dataset_id}/task-type")
async def task_type(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.get_task_type(dataset_id))

@router.get("/{dataset_id}/feature-analysis")
async def feature_analysis(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.get_feature_analysis(dataset_id))

@router.get("/{dataset_id}/train")
async def  train(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.train_model(dataset_id))

@router.get("/{dataset_id}/model")
async def model_registry(dataset_id: str, dataset_service=Depends(get_dataset_service)):
    return await (dataset_service.get_model_registry(dataset_id))