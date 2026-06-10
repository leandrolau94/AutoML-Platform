class InsightsService:
    async def generate_insights(self, profile: dict):
        recommendations = []
        missing_columns = []
        
        for column, missing in profile["missing_values"].items():
            if missing > 0:
                missing_columns.append(column)
                recommendations.append(f"fill missing values in {column}")
        
        if len(profile["categorical_columns"]) > 0:
            recommendations.append("Encode categorical variables")
        
        target_candidates = []
        
        if "Survived" in profile["numeric_columns"]:
            target_candidates.append("Survived")
        
        return {
            "dataset_type": ("classification" if target_candidates else "unknown"),
            "target_candidates": target_candidates,
            "missing_columns": missing_columns,
            "recommendations": recommendations
        }