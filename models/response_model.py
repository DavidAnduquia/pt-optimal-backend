from datetime import datetime
from typing import Any
from pydantic import BaseModel

class ResponseModel(BaseModel):
    timestamp: str   | None = None
    success: bool  | None = None
    message: str  | None = None
    status_code: int | None = None
    data: Any | None = None

    def create_response(self,success: bool  | None = None , message: str  | None = None, 
                        status_code : int | None = None, data: Any | None = None):
        return ResponseModel(
            timestamp=str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
            success=success,
            message=message,
            status_code=status_code,
            data=data).model_dump()
 
   
    
    