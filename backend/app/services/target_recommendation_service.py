class TargetRecommendationService:
    async def recommend(self, schema: dict):
        candidates = []
        for column in schema["columns"]:
            score = 0
            n_unique = column["n_unique"]
            cardinality = (column["cardinality"])
            missing_pct = (column["missing_pct"])
            is_numeric = (column["is_numeric"])
            column_name = column["name"].lower()
            reasons = []
            
            #decision rules
            #classification
            if n_unique <= 20:
                score += 30
            
            #low cardinality
            if cardinality < 0.1:
                score += 25
                reasons.append("low cardinality")
            if cardinality > 0.95:
                score -= 80
            
            #a little missing values
            if missing_pct < 5:
                score += 20
                reasons.append("low missing percentage")
            if missing_pct > 50:
                score -= 30
            
            #Penalize IDs
            if column_name == "id":
                score -= 80
            if column_name.endswith("_id"):
                score -= 80
            if column_name.endswith("id"):
                score -= 80
            
            if is_numeric and n_unique <= 10:
                score += 20
                reasons.append("numeric classification candidate")
            
            #Constants
            if n_unique == 1:
                score = 0
            
            candidates.append({
                "column": column["name"],
                "score": score,
                "reasons": reasons
            })
        candidates.sort(key=lambda x: x["score"], reverse=True)
        return {"candidates": candidates[:10]}