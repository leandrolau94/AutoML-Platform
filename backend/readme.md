# AI Dataset Platform

An end-to-end AutoML-inspired platform built with FastAPI, MongoDB Atlas and Azure Cloud.

The platform allows users to upload datasets, automatically analyze their structure, recommend target variables, detect machine learning tasks, benchmark multiple algorithms, train the best model and generate predictions through a REST API.

---

# Project Status

## Backend

✅ Fully implemented

✅ Deployed on Azure Container Apps

✅ Connected to MongoDB Atlas

✅ Connected to Azure Blob Storage

✅ Dockerized

✅ Production-ready MVP

## Frontend

🚧 React + TypeScript frontend currently under development

---

# Live Deployment

### Public API

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

### Swagger Documentation

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

---

# Features

## Dataset Management

- Upload CSV datasets
- Store dataset metadata in MongoDB Atlas
- Store datasets in Azure Blob Storage
- Dataset CRUD operations
- Dataset profiling and statistics

---

## Schema Analysis

Automatically analyzes uploaded datasets and extracts:

- Column names
- Data types
- Missing value percentages
- Cardinality
- Unique values
- Numeric vs categorical features

Example:

```json
{
  "name": "Age",
  "dtype": "float64",
  "missing_pct": 19.87,
  "is_numeric": true
}
```

---

## Target Recommendation Engine

Automatically recommends candidate target columns using a rule-based scoring system based on:

- Cardinality
- Missing values
- Data type
- Classification suitability
- Identifier detection

Example:

```json
{
  "column": "Survived",
  "score": 95
}
```

---

## Target Selection

Users can:

- Select a recommended target
- Manually choose any dataset column

This allows both automation and user control.

---

## Task Detection

Automatically detects:

- Classification
- Regression

Example:

```json
{
  "task_type": "classification",
  "problem_type": "binary",
  "confidence": 0.99
}
```

---

## Feature Analysis

Automatically selects relevant input features and excludes:

- Identifier columns
- Target column
- High-cardinality text features
- Columns with excessive missing values

Example:

```json
{
  "selected_features": [
    "Pclass",
    "Sex",
    "Age",
    "Fare"
  ]
}
```

---

## Automatic Preprocessing

Numerical features:

- Median Imputation

Categorical features:

- Most Frequent Imputation
- One-Hot Encoding

Implemented using:

- ColumnTransformer
- Pipeline
- SimpleImputer
- OneHotEncoder

---

## Model Benchmarking

Automatically benchmarks multiple machine learning algorithms.

### Classification Models

- RandomForestClassifier
- XGBClassifier
- LGBMClassifier
- CatBoostClassifier

### Regression Models

- RandomForestRegressor
- XGBRegressor
- LGBMRegressor
- CatBoostRegressor

Example:

```json
{
  "best_model": "CatBoostClassifier",
  "best_metric": 0.8268
}
```

---

## Model Training

The platform automatically:

```text
Dataset
    ↓
Schema Analysis
    ↓
Target Selection
    ↓
Task Detection
    ↓
Feature Analysis
    ↓
Train/Test Split
    ↓
Preprocessing
    ↓
Model Training
    ↓
Evaluation
```

---

## Model Persistence

Trained models are stored as Joblib pipelines.

Example:

```text
models/
└── 6a21ed3132e358596fee7b15.joblib
```

The entire preprocessing and training pipeline is persisted.

---

## Model Registry

Model metadata is stored in MongoDB Atlas.

Example:

```json
{
  "training": {
    "model_name": "CatBoostClassifier",
    "task_type": "classification",
    "metrics": {
      "accuracy": 0.8268
    }
  }
}
```

---

## Prediction Service

Generate predictions using trained models.

Example request:

```json
{
  "values": {
    "City": "Madrid",
    "Gender": "F"
  }
}
```

Example response:

```json
{
  "prediction": 1
}
```

---

# Architecture

```text
React Frontend (In Progress)
            ↓
      FastAPI Backend
            ↓
 ┌──────────┴──────────┐
 ↓                     ↓

MongoDB Atlas    Azure Blob Storage

            ↓
      ML Pipeline

   Random Forest
      XGBoost
      LightGBM
      CatBoost
```

---

# Tech Stack

## Backend

- FastAPI
- Pydantic
- Uvicorn

## Database

- MongoDB Atlas

## Cloud

- Azure Container Apps
- Azure Blob Storage
- Azure Container Registry (ACR)

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost
- Pandas
- NumPy
- Joblib

## DevOps

- Docker
- Git
- GitHub

---

# API Workflow

## 1. Upload Dataset

```http
POST /api/v1/datasets/upload
```

## 2. Generate Schema

```http
GET /api/v1/datasets/{dataset_id}/schema
```

## 3. Recommend Targets

```http
GET /api/v1/datasets/{dataset_id}/target-candidates
```

## 4. Select Target

```http
POST /api/v1/datasets/{dataset_id}/target
```

## 5. Detect Task

```http
GET /api/v1/datasets/{dataset_id}/task-type
```

## 6. Feature Analysis

```http
GET /api/v1/datasets/{dataset_id}/feature-analysis
```

## 7. Benchmark Models

```http
GET /api/v1/datasets/{dataset_id}/benchmark
```

## 8. Train Best Model

```http
GET /api/v1/datasets/{dataset_id}/train-best-model
```

## 9. Model Registry

```http
GET /api/v1/datasets/{dataset_id}/model
```

## 10. Predict

```http
POST /api/v1/datasets/{dataset_id}/predict
```

---

# Example Results

### Titanic Dataset

```json
{
  "model_name": "CatBoostClassifier",
  "accuracy": 0.8268,
  "precision": 0.8525,
  "recall": 0.7027,
  "f1_score": 0.7704
}
```

---

# Roadmap

## Completed

- Dataset Upload
- Dataset CRUD
- MongoDB Atlas Integration
- Azure Blob Storage Integration
- Schema Analysis
- Target Recommendation
- Target Selection
- Task Detection
- Feature Analysis
- Automatic Preprocessing
- Model Benchmarking
- Best Model Selection
- Model Training
- Model Registry
- Prediction API
- Docker Containerization
- Azure Deployment

## In Progress

- React Frontend
- Interactive Dashboard
- Dataset Visualization

## Planned

- User Authentication
- Experiment Tracking
- Model Monitoring
- Explainable AI (SHAP)
- Automated Feature Engineering
- Hyperparameter Optimization

---

# Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── storage/
│   └── settings.py
│
├── models/
├── uploads/
│
├── requirements.txt
├── Dockerfile
└── main.py
```

---

# Author

**Leandro Daniel Lau Alfonso**

Mathematician | Data Scientist | Machine Learning Engineer | Full-Stack AI Developer