# AI Dataset Platform

End-to-end AutoML-inspired platform built with FastAPI, React, MongoDB Atlas and Azure Cloud.

The platform allows users to upload datasets, automatically analyze their structure, recommend target variables, detect machine learning tasks, benchmark multiple algorithms, train the best model and generate predictions through a web interface.

---

## Live Demo

### Frontend (Vercel)

https://auto-ml-platform-black.vercel.app

### Backend API (Azure Container Apps)

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

### Swagger Documentation

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

---

## Current Features

### Dataset Management

* Upload CSV datasets
* Dataset metadata stored in MongoDB Atlas
* Dataset files stored in Azure Blob Storage
* Dataset CRUD operations

### Schema Analysis

Automatically extracts:

* Column names
* Data types
* Missing value percentages
* Cardinality
* Numeric vs categorical features

### Target Recommendation

Automatically recommends candidate target variables based on:

* Cardinality
* Missing values
* Data type
* Classification suitability
* Identifier detection

### Task Detection

Automatically detects:

* Classification
* Regression

### Feature Analysis

Automatically selects relevant features and excludes:

* Identifier columns
* Target column
* High-cardinality text features
* Columns with excessive missing values

### Automatic Preprocessing

Numerical Features:

* Median Imputation

Categorical Features:

* Most Frequent Imputation
* One-Hot Encoding

### Model Benchmarking

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

### Model Training

Automatically trains the best-performing model.

### Model Persistence

* Joblib pipelines
* Azure Blob Storage persistence

### Prediction Service

Generate predictions using trained models directly from the frontend.

---

## Architecture

```text
React Frontend (Vercel)
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

## Supported File Types

Current version supports:

* CSV (.csv)

Planned for future versions:

* Excel (.xlsx)
* Text (.txt)
* PDF (.pdf)
* Additional structured data formats

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Axios

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Database

* MongoDB Atlas

### Cloud

* Azure Container Apps
* Azure Blob Storage
* Azure Container Registry

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* CatBoost
* Pandas
* NumPy
* Joblib

### DevOps

* Docker
* GitHub
* Vercel
* Azure

---

## Roadmap

### V1.0 (Completed)

* Dataset Upload
* Schema Analysis
* Target Recommendation
* Target Selection
* Task Detection
* Feature Analysis
* Benchmarking
* Model Training
* Azure Blob Storage Persistence
* Prediction Service
* Azure Deployment
* Vercel Deployment

### V2

* Improved Feature Analysis
* Better Benchmark Tie-Breaking
* Prediction UI Improvements
* Duplicate Dataset Handling
* Large Dataset Support
* DuckDB Integration
* Additional File Types

### V3

* AI Agent Assistant
* Guided AutoML Workflows
* Platform-Specific Help
* Autonomous Task Execution

---

## Author

**Leandro Daniel Lau Alfonso**

Mathematician | Data Scientist | Machine Learning Engineer | Full-Stack AI Developer