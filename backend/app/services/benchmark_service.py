from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from app.schemas.benchmark import (BenchmarkResponse, )
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor
from catboost import CatBoostClassifier, CatBoostRegressor

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
        task_type = (dataset["task_detection"]["task_type"])
        if task_type == "classification":
            candidate_models = [
                ("RandomForestClassifier", RandomForestClassifier(n_estimators=100, random_state=42)),
                ("XGBClassifier", XGBClassifier(random_state=42, eval_metric="logloss")),
                ("LGBMClassifier", LGBMClassifier(random_state=42, verbose=-1)),
                ("CatBoostClassifier", CatBoostClassifier(random_state=42, verbose=0))
            ]
        else:
            candidate_models = [
                ("RandomForestRegressor", RandomForestRegressor(n_estimators=100, random_state=42)),
                ("XGBRegressor", XGBRegressor(random_state=42)),
                ("LGBMRegressor", LGBMRegressor(random_state=42, verbose=-1)),
                ("CatBoostRegressor", CatBoostRegressor(random_state=42, verbose=0))
            ]
        results = []
        for model_name, model in candidate_models:
            try:
                pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
                pipeline.fit(X_train, y_train)
                predictions = (pipeline.predict(X_test))
                if task_type == "classification":
                    metrics = (self.evaluation_service.evaluate_classification(y_test, predictions))
                else:
                    metrics = (self.evaluation_service.evaluate_regression(y_test, predictions))
                results.append({
                    "model": model_name,
                    "metrics": metrics
                })
            except Exception as e:
                results.append({
                    "model": model_name,
                    "error": str(e)
                })
        if task_type == "classification":
            best_result = max(results, key=lambda x: x["metrics"]["accuracy"])
            best_metric=best_result["metrics"]["accuracy"]
        else:
            best_result = max(results, key=lambda x: x["metrics"]["r2_score"])
            best_metric=best_result["metrics"]["r2_score"]
        benchmark_result = {
            "best_model": best_result["model"],
            "best_metric": best_metric,
            "results": results,
            "created_at": datetime.utcnow().isoformat()
        }
        return BenchmarkResponse(**benchmark_result)