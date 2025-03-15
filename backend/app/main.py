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
from backend.app.database import Base, engine
import backend.app.models

app = FastAPI()

Base.metadata.create_all(bind=engine)