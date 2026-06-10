import pandas as pd

class ProfilingService:
    async def profile_dataset(self, file_path: str):
        df = pd.read_csv(file_path)
        numeric_columns = (df.select_dtypes(include=["number"]).columns.to_list())
        categorical_columns = (df.select_dtypes(exclude=["number"]).columns.to_list())
        missing_values = (df.isnull().sum().to_dict())
        numeric_summary = (df.describe().to_dict() if len(numeric_columns) > 0 else {})
        return {
            "rows": len(df),
            "columns": len(df.columns),
            "numeric_columns": numeric_columns,
            "categorical_columns": categorical_columns,
            "missing_values": missing_values,
            "numeric_summary": numeric_summary,
        }