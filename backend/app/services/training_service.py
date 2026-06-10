import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import ( RandomForestClassifier, RandomForestRegressor)
from sklearn.metrics import (accuracy_score, r2_score, mean_absolute_error)
from app.schemas.training import ( TrainingResponse)


class TrainingService:
    def __init__(self, evaluation_service):
        self.evaluation_service = evaluation_service
    async def train(self, dataset: dict):
        csv_path = dataset["file_path"]
        df = pd.read_csv(csv_path)
        target_column = (dataset["selected_target"]["column"])
        feature_columns = (dataset["feature_analysis"]["selected_features"])
        X = df[feature_columns]
        y = df[target_column]
        X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size=0.2, random_state=42))
        numeric_features = (X_train.select_dtypes(include=['int64', 'float64']).columns.to_list())
        categorical_features = (X_train.select_dtypes(include=['object']).columns.to_list())
        numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
        categorical_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("encoder", OneHotEncoder(handle_unknown="ignore"))])
        preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features), ("cat", categorical_transformer, categorical_features)])
        X_train_processed = (preprocessor.fit_transform(X_train))
        X_test_processed = (preprocessor.transform(X_test))
        task_type = (dataset["task_detection"]["task_type"])
        if task_type == "classification":
            model = (RandomForestClassifier(n_estimators=100, random_state=42))
        else:
            model = (RandomForestRegressor(n_estimators=100, random_state=42))
        full_pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
        full_pipeline.fit(X_train, y_train)
        predictions = (full_pipeline.predict(X_test))
        model_path = (f"models/{dataset['_id']}.joblib")
        joblib.dump(full_pipeline, model_path)
        metrics = (self.evaluation_service.evaluate_classification(y_test, predictions))
        training_info = TrainingResponse(
            model_name="RandomForestClassifier",
            task_type=task_type,
            train_rows=len(X_train),
            test_rows=len(X_test),
            metrics=metrics,
            model_path=model_path
        )
        return training_info