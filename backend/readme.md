# AI Dataset Platform Backend

Production-ready AutoML backend built with FastAPI, MongoDB Atlas and Azure Cloud.

---

## Deployment

Backend API:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

Swagger Documentation:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

---

## Features

### Dataset Management

* CSV Upload
* Azure Blob Storage Integration
* MongoDB Atlas Metadata Storage
* Dataset CRUD

### Automated ML Workflow

* Schema Analysis
* Target Recommendation
* Target Selection
* Task Detection
* Feature Analysis
* Model Benchmarking
* Best Model Selection
* Model Training
* Model Registry
* Prediction API

### Benchmarked Models

Classification:

* RandomForestClassifier
* XGBClassifier
* LGBMClassifier
* CatBoostClassifier

Regression:

* RandomForestRegressor
* XGBRegressor
* LGBMRegressor
* CatBoostRegressor

---

## API Workflow

POST /api/v1/datasets/upload

↓

GET /api/v1/datasets/{dataset_id}/schema

↓

GET /api/v1/datasets/{dataset_id}/target-candidates

↓

POST /api/v1/datasets/{dataset_id}/target

↓

GET /api/v1/datasets/{dataset_id}/task-type

↓

GET /api/v1/datasets/{dataset_id}/feature-analysis

↓

GET /api/v1/datasets/{dataset_id}/benchmark

↓

GET /api/v1/datasets/{dataset_id}/train

↓

POST /api/v1/datasets/{dataset_id}/predict

---

## Current File Support

Supported:

* CSV (.csv)

Planned:

* Excel (.xlsx)
* JSON
* Parquet

---

## Tech Stack

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* CatBoost
* Pandas
* NumPy
* Joblib

### Cloud

* Azure Container Apps
* Azure Blob Storage
* Azure Container Registry
* MongoDB Atlas

### DevOps

* Docker
* Git
* GitHub

---

## Project Structure

backend/

├── app/

├── models/

├── uploads/

├── Dockerfile

├── requirements.txt

└── main.py

---

## Author

Leandro Daniel Lau Alfonso