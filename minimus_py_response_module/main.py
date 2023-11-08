from typing import Any
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def create_success_response(code: int = 200, data: Any = {}):
    json_data = jsonable_encoder(data)
    return JSONResponse(
        content={
            "status": "success",
            "data": json_data
        },
        status_code=code,
    )

def create_error_response(code: int = 400, message: str = "", error: Any = {}):
    json_error_data = jsonable_encoder(error)
    return JSONResponse(
        content={
            "status": "fail",
            "message": message,
            "data": json_error_data
        },
        status_code=code,
    )

def create_failure_response(code: int = 500, message: str = "", error: Any = {}):
    json_error_data = jsonable_encoder(error)
    return JSONResponse(
        content={
            "status": "fail",
            "message": message,
            "data": json_error_data
        },
        status_code=code,
    )
