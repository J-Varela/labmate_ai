from fastapi import FastAPI
from app.api.router import api_router
from app.core.database import Base, engine
from app.models import Experiment, Trial

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LabMate AI API")

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "LabMate AI backend is running"}