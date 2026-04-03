from fastapi import APIRouter

from app.api.routes import ai, experiments, trials

api_router = APIRouter()
api_router.include_router(ai.router)
api_router.include_router(experiments.router)
api_router.include_router(trials.router)


@api_router.get("/health")
def health_check():
    return {"status": "ok"}
