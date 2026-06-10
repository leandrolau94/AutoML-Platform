# AI Dataset Platform

An end-to-end AutoML-inspired platform built with FastAPI, MongoDB Atlas, Pandas, and Scikit-Learn.

The platform allows users to upload datasets, automatically analyze their structure, recommend target variables, detect machine learning tasks, perform feature selection, train machine learning models, persist trained pipelines, and manage model metadata.

---

## Features

### Dataset Management

* Upload CSV datasets
* Store metadata in MongoDB Atlas
* Full CRUD operations
* Dataset profiling and statistics

### Schema Analysis

Automatically analyzes uploaded datasets and extracts:

* Column names
* Data types
* Missing values
* Cardinality
* Unique value counts
* Numeric vs categorical features

### Target Recommendation Engine

The platform recommends potential target columns using a rule-based scoring system based on:

* Cardinality
* Missing values
* Data type
* Classification suitability
* Identifier detection

Example:

```json
{
  "column": "Survived",
  "score": 95
}
```

### Target Selection

Users can:

* Select one of the recommended target columns
* Manually choose any dataset column

This design keeps the platform flexible while still providing intelligent recommendations.

### Task Detection

Automatically detects the machine learning task based on the selected target.

Currently supported:

* Classification
* Regression

Example:

```json
{
  "task_type": "classification",
  "confidence": 0.98
}
```

### Feature Analysis

Automatically selects relevant input features and excludes:

* Identifier columns
* Target column
* High-cardinality text columns
* Columns with excessive missing values

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

### Training Pipeline

The platform automatically builds and trains a machine learning pipeline.

Current implementation:

* RandomForestClassifier
* RandomForestRegressor

Training workflow:

```text
Dataset
    ↓
Feature Selection
    ↓
Train/Test Split
    ↓
Missing Value Imputation
    ↓
Categorical Encoding
    ↓
Model Training
    ↓
Evaluation
```

### Automatic Preprocessing

Numerical features:

* Median imputation

Categorical features:

* Most frequent imputation
* One-Hot Encoding

Implemented using:

* ColumnTransformer
* Pipeline
* SimpleImputer
* OneHotEncoder

### Model Persistence

Trained models are stored as serialized Joblib pipelines.

Example:

```text
models/
└── 6a21ed3132e358596fee7b15.joblib
```

The entire preprocessing and training pipeline is persisted, allowing future inference without rebuilding transformations.

### Model Registry

Model metadata is stored in MongoDB.

Example:

```json
{
  "training": {
    "model_name": "RandomForestClassifier",
    "task_type": "classification",
    "train_rows": 712,
    "test_rows": 179,
    "metrics": {
      "accuracy": 0.8045
    },
    "model_path": "models/6a21ed3132e358596fee7b15.joblib"
  }
}
```

---

## Architecture

```text
Upload Dataset
       ↓
Schema Analysis
       ↓
Target Recommendation
       ↓
Target Selection
       ↓
Task Detection
       ↓
Feature Analysis
       ↓
Training
       ↓
Model Persistence
       ↓
Model Registry
```

---

## Tech Stack

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Database

* MongoDB Atlas

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Random Forest
* ColumnTransformer
* Pipeline
* Joblib

### Development

* Python 3.12+
* VS Code

---

## Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── storage/
│
├── uploads/
├── models/
│
├── .env
├── requirements.txt
└── main.py
```

---

## Current API Flow

### 1. Upload Dataset

```http
POST /datasets/upload
```

### 2. Generate Schema

```http
GET /datasets/{dataset_id}/schema
```

### 3. Recommend Target Columns

```http
GET /datasets/{dataset_id}/target-candidates
```

### 4. Select Target

```http
POST /datasets/{dataset_id}/target
```

### 5. Detect Task Type

```http
GET /datasets/{dataset_id}/task-type
```

### 6. Analyze Features

```http
GET /datasets/{dataset_id}/feature-analysis
```

### 7. Train Model

```http
GET /datasets/{dataset_id}/train
```

### 8. Model Registry

```http
GET /datasets/{dataset_id}/model
```

---

## Example Result

Using the Titanic dataset:

```json
{
  "model_name": "RandomForestClassifier",
  "task_type": "classification",
  "metrics": {
    "accuracy": 0.8045
  }
}
```

---

## Roadmap

### Completed

* Dataset Upload
* Dataset CRUD
* MongoDB Atlas Integration
* Schema Analysis
* Target Recommendation
* Target Selection
* Task Detection
* Feature Analysis
* Training Service
* Model Persistence
* Model Registry

### In Progress

* Prediction API

### Planned

* Docker Support
* Azure Deployment
* XGBoost Integration
* LightGBM Integration
* CatBoost Integration
* Automatic Model Benchmarking
* Model Selection Engine
* Experiment Tracking
* Monitoring and Observability

---

## Author

Leandro Daniel Lau Alfonso

Mathematician | Data Scientist | Machine Learning Engineer | Full-Stack AI Developer
