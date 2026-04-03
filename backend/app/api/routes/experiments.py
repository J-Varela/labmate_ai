from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experiment import Experiment
from app.schemas.experiment import ExperimentCreate, ExperimentResponse

router = APIRouter(prefix="/experiments", tags=["Experiments"])


@router.post("", response_model=ExperimentResponse)
def create_experiment(payload: ExperimentCreate, db: Session = Depends(get_db)):
    experiment = Experiment(
        title=payload.title,
        objective=payload.objective,
        hypothesis=payload.hypothesis,
        status=payload.status,
    )
    db.add(experiment)
    db.commit()
    db.refresh(experiment)
    return experiment


@router.get("", response_model=list[ExperimentResponse])
def list_experiments(db: Session = Depends(get_db)):
    experiments = db.query(Experiment).order_by(Experiment.created_at.desc()).all()
    return experiments


@router.get("/{experiment_id}", response_model=ExperimentResponse)
def get_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()

    if not experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")

    return experiment