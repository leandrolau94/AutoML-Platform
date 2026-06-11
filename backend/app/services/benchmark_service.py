from sklearn.ensemble import RandomForestClassifier
from app.schemas.benchmark import (BenchmarkResponse, )
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

class BenchmarkService:
    def __init__(self, evaluation_service):
        self.evaluation_service = (evaluation_service)
    
    async def benchmark(self, dataset: dict):
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
        candidate_models = [("RandomForestClassifier", RandomForestClassifier(n_estimators=100, random_state=42))]
        results = []
        for model_name, model in candidate_models:
            pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
            pipeline.fit(X_train, y_train)
            predictions = (pipeline.predict(X_test))
            metrics = (self.evaluation_service.evaluate_classification(y_test, predictions))
            results.append({
                "model": model_name,
                "metrics": metrics
            })
        best_result = max(results, key=lambda x: x["metrics"]["accuracy"])
        return BenchmarkResponse(
            best_model=best_result["model"],
            best_metric=best_result["metrics"]["accuracy"],
            results=results
        )