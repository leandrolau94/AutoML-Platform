from app.schemas.feature_analysis import (FeatureAnalysisResponse, )

class FeatureAnalysisService:
    async def analyze(self, schema: dict, target_name: str):
        selected_features = []
        excluded_features = []
        for column in schema["columns"]:
            name = column["name"]
            dtype = column["dtype"]
            cardinality = column["cardinality"]
            missing_pct = column["missing_pct"]
            #first feature analysis decision rule
            if name == target_name:
                excluded_features.append({
                    "column": name,
                    "reason": "target column"
                })
                continue
            
            #second feature analysis decision rule
            if (name.lower() == "id" or name.lower().endswith("id") or name.lower().endswith("_id")):
                excluded_features.append({
                    "column": name,
                    "reason": "identifier column"
                })
                continue
            
            #third feature analysis decision rule
            if missing_pct > 70:
                excluded_features.append({
                    "column": name,
                    "reason": "too many missing values"
                })
                continue
            
            #fourth feature analysis decision rule
            if (dtype == "str" and cardinality > 0.5):
                excluded_features.append({
                    "column": name,
                    "reason": "high cardinality text"
                })
                continue
            
            #fivth feature analysis decision rule
            if cardinality > 0.95:
                excluded_features.append({
                    "column": name,
                    "reason": "high cardinality"
                })
                continue
            selected_features.append(name)
        return FeatureAnalysisResponse(selected_features=selected_features, excluded_features=excluded_features)