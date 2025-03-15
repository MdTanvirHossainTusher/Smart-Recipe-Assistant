from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from backend.app.exceptions.custom_exception import BaseAPIException, DatabaseException

async def api_exception_handler(request: Request, exc: BaseAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    db_exc = DatabaseException(f"Database error: {str(exc)}")
    return JSONResponse(
        status_code=db_exc.status_code,
        content={"detail": db_exc.detail}
    )

def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseAPIException, api_exception_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)