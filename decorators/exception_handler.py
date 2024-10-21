from functools import wraps
from typing import Any, Callable
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from models.response_model import ResponseModel

responseModel = ResponseModel()

# Funcion que maneja las excepciones de los servicios
def service_exception_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(self, *args, **kwargs)
        except HTTPException as http_error:
             raise HTTPException(status_code=http_error.status_code, 
                   detail=http_error.detail)
        except SQLAlchemyError as sql_error:
            self.db.rollback()  # Rollback in case of error
            raise HTTPException(status_code=500, detail=f"Error en la base de datos. {str(sql_error)}")
        except Exception as e:
            self.db.rollback()  # Rollback in case of error
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            self.db.close() # Cerramos conexion
    return wrapper

# Funcion para manejar el retorno de las excepciones en el Controller
def controller_exception_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except HTTPException as http_error:
            return responseModel.create_response(
                success=False,
                message=http_error.detail,
                status_code=http_error.status_code
            )
        except SQLAlchemyError as sql_error:
            return responseModel.create_response(
                success=False,
                message=f"Error en la base de datos: {str(sql_error)}",
                status_code=500
            )
        except Exception as e:
            return responseModel.create_response(
                success=False,
                message=f"Error inesperado: {str(e)}",
                status_code=500
            )  
    return wrapper