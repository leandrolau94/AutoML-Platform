# AI Dataset Platform Frontend

React frontend for the AI Dataset Platform.

Built with React, TypeScript, TailwindCSS and React Router.

---

## Live Demo

Frontend:

https://auto-ml-platform-black.vercel.app/

Backend API:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

Swagger:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

## Features

### Homepage

* Dataset Upload
* Dataset Listing
* Responsive Design

### Dataset Dashboard

Interactive AutoML workflow:

1. Generate Schema
2. Recommend Targets
3. Select Target
4. Detect Task
5. Analyze Features
6. Run Benchmark
7. Train Best Model

---

## Dashboard Components

* Dataset Overview
* Pipeline Status
* Action Panel
* Target Selection Modal
* Task Detection Card
* Feature Analysis Card
* Benchmark Results Card
* Training Results Card

---

## User Experience

* Responsive Design
* TailwindCSS UI
* Loading States
* Skeleton Cards
* Guided Workflow

---

## Backend Integration

Consumes the deployed FastAPI backend:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io

Swagger:

https://ai-dataset-platform.nicebeach-9fbcb621.westeurope.azurecontainerapps.io/docs

---

## Current File Support

Supported:

* CSV (.csv)

Planned:

* Excel (.xlsx)
* JSON
* Parquet

---

## Version 2

### Prediction UI

The backend prediction endpoint is already implemented:

POST /api/v1/datasets/{dataset_id}/predict

A dedicated prediction interface will be added in Version 2.

### Additional Improvements

* Prediction Dashboard
* Interactive Charts
* Better Benchmark Visualizations
* Multi-format Uploads
* Authentication

---

## Tech Stack

* React
* TypeScript
* TailwindCSS
* React Router
* Axios
* Vite

---

## Author

Leandro Daniel Lau Alfonso