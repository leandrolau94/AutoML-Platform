from app.schemas.task_detection import (TaskDetectionResponse, )

class TaskDetectionService:
    async def detect(self, target_column: dict) -> TaskDetectionResponse:
        n_unique = target_column["n_unique"]
        is_numeric = target_column["is_numeric"]
        reasons = []
        
        #Binary Classification
        if n_unique == 2:
            reasons.append("target has exactly two classes")
            return TaskDetectionResponse(task_type="classification", problem_type="binary", confidence=0.99, reasons=reasons)
        
        #Multiclass Classification
        if not is_numeric:
            reasons.append("target is categorical")
            return TaskDetectionResponse(task_type="classification", problem_type="multiclass", confidence=0.95, reasons=reasons)
        
        #Numeric Classification
        if is_numeric and n_unique <= 10:
            reasons.append("numeric target with few classes")
            return TaskDetectionResponse(task_type="classification", problem_type="multiclass", confidence=0.90, reasons=reasons)
        
        #Regression
        if is_numeric and n_unique > 10:
            reasons.append("numeric target with many unique values")
            return TaskDetectionResponse(task_type="regression", problem_type="continuous", confidence=0.95, reasons=reasons)
        
        return TaskDetectionResponse(task_type="unknown", problem_type="unknown", confidence=0.5, reasons=["unable to determine task type"])