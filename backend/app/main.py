# from fastapi import FastAPI
# from backend.app import models
# from backend.app import models
# from backend.app.database import Base, engine
#
# app = FastAPI()
#
# models.Base.metadata.create_all(bind=engine)

# backend/app/main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.database import Base, engine
from backend.app.routes.user_route import router as user_router
import backend.app.models

# app = FastAPI()
#
# Base.metadata.create_all(bind=engine)

from fastapi import FastAPI

from backend.app.exceptions.global_exception_handler import register_exception_handlers


def create_app():
    app = FastAPI(
        title="User Management API",
        description="API for managing user accounts",
        version="1.0.0"
    )
    Base.metadata.create_all(bind=engine)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    register_exception_handlers(app)

    app.include_router(user_router)

    return app


app = create_app()

