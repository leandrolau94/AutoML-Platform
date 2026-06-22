# AI Dataset Platform

A full-stack AutoML platform built with FastAPI, React, MongoDB Atlas and Azure Cloud.

The platform enables users to upload datasets, automatically analyze their structure, identify machine learning targets, benchmark multiple algorithms, train the best-performing model and generate predictions.

---

## Architecture

React Frontend
↓
FastAPI Backend
↓
MongoDB Atlas

FastAPI Backend
↓
Azure Blob Storage

FastAPI Backend
↓
Machine Learning Pipeline

* Random Forest
* XGBoost
* LightGBM
* CatBoost

---

## Features

### Dataset Management

* Upload CSV datasets
* Dataset metadata storage
* Azure Blob Storage integration

### AutoML Workflow

1. Generate Schema
2. Recommend Target Columns
3. Select Target
4. Detect Task Type
5. Analyze Features
6. Benchmark Models
7. Train Best Model
8. Generate Predictions

### Cloud Deployment

* Azure Container Apps
* Azure Blob Storage
* MongoDB Atlas

---

## Current File Support

Supported:

* CSV (.csv)

Planned for Version 2:

* Excel (.xlsx)
* JSON
* Parquet
* TXT
* PDF ingestion workflows

---

## Repository Structure

ai-dataset-platform/

├── backend/

└── frontend/

---

## Live Services

Backend API:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

Swagger Documentation:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

Frontend:

https://auto-ml-platform-black.vercel.app/

---

## Version 2 Roadmap

* Prediction UI
* Multi-format uploads
* Improved feature analysis
* Better benchmark tie-breaking
* Interactive visualizations
* Experiment tracking
* Authentication

---

## Author

Leandro Daniel Lau Alfonso

Mathematician | Data Scientist | Machine Learning Engineer