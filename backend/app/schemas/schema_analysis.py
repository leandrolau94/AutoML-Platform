from pydantic import BaseModel

class ColumnAnalysis(BaseModel):
    name: str
    dtype: str
    n_unique: int
    cardinality: float
    missing_pct: float
    is_numeric: bool

class DatasetSchema(BaseModel):
    columns: list[ColumnAnalysis]