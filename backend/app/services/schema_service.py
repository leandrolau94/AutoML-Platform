import pandas as pd
from app.schemas.schema_analysis import (ColumnAnalysis, DatasetSchema, )

class SchemaService:
    async def analyze(self, file_path: str) -> DatasetSchema:
        df = pd.read_csv(file_path)
        total_rows = len(df)
        columns = []
        for colum in df.columns:
            series = df[colum]
            n_unique = (series.nunique(dropna=True))
            cardinality = round(n_unique / total_rows, 4)
            missing_pct = round((series.isna().sum() / total_rows) * 100, 2)
            is_numeric = (pd.api.types.is_numeric_dtype(series))
            columns.append(ColumnAnalysis(
                name=colum,
                dtype=str(series.dtype),
                n_unique=int(n_unique),
                cardinality=cardinality,
                missing_pct=missing_pct,
                is_numeric=is_numeric
            ))
        return DatasetSchema(columns=columns)