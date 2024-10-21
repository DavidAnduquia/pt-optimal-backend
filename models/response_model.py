from datetime import datetime
from typing import Any
from pydantic import BaseModel
import pytz

class ResponseModel(BaseModel):
    timestamp: str   | None = None
    success: bool  | None = None
    message: str  | None = None
    status_code: int | None = None
    data: Any | None = None

    def create_response(self,success: bool  | None = None , message: str  | None = None, 
                        status_code : int | None = None, data: Any | None = None):
        colombia_timezone = pytz.timezone("America/Bogota")
        return ResponseModel(
            timestamp=str(datetime.now(colombia_timezone).strftime("%d/%m/%Y %H:%M:%S")),
            success=success,
            message=message,
            status_code=status_code,
            data=data).model_dump()
 
   
    
    