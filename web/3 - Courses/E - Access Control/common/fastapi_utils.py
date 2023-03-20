__all__ = (
    'form_field_as_str',
    'form_field_as_file',
)

from contextvars import ContextVar

from fastapi import FastAPI, Request, UploadFile
from fastapi.datastructures import FormData


global_request : ContextVar[Request] = ContextVar("global_request")

def add_global_request_middleware(app: FastAPI):
    # https://fastapi.tiangolo.com/tutorial/middleware/#middleware
    @app.middleware("http")
    async def global_request_middleware(request: Request, call_next):
        global_request.set(request)
        response = await call_next(request)
        return response
    #:
    return global_request_middleware  # this returns the inner function
#:

def form_field_as_str(form_data: FormData, field_name: str) -> str:
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str')
#:

def form_field_as_file(form_data: FormData, field_name: str) -> UploadFile:
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is not UploadFile')
#:

