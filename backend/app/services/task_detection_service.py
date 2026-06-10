from app.schemas.task_detection import (TaskDetectionResponse, )

class TaskDetectionService:
    async def detect(self, target_column: dict) -> TaskDetectionResponse:
        n_unique = target_column["n_unique"]
        is_numeric = target_column["is_numeric"]
        reasons = []
        
        #state classification task decision rules
        if n_unique <= 20:
            reasons.append("target has low number of unique values")
            if is_numeric:
                reasons.append("numeric categorical target")
                confidence = 0.98
            else:
                reasons.append("categorical target")
                confidence = 0.90
            return TaskDetectionResponse(task_type="classification", confidence=confidence, reasons=reasons)
        
        #state regression task decision rules
        if is_numeric and n_unique > 20:
            return TaskDetectionResponse(task_type="regression", confidence=0.95, reasons=reasons)
        
        #state unknown task decision rules (clustering and others for future improvements)
        reasons.append("unable to confidently determine task type")
        
        return TaskDetectionResponse(task_type="unknown", confidence=0.5, reasons=reasons)