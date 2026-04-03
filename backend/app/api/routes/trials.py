from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experiment import Experiment
from app.models.trial import Trial
from app.schemas.trial import TrialCreate, TrialResponse

router = APIRouter(prefix="/experiments", tags=["Trials"])


@router.post("/{experiment_id}/trials", response_model=TrialResponse)
def create_trial(
    experiment_id: int,
    payload: TrialCreate,
    db: Session = Depends(get_db),
):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")

    trial = Trial(
        experiment_id=experiment_id,
        trial_number=payload.trial_number,
        procedure=payload.procedure,
        variables=payload.variables,
        observations=payload.observations,
        result=payload.result,
    )
    db.add(trial)
    db.commit()
    db.refresh(trial)
    return trial


@router.get("/{experiment_id}/trials", response_model=list[TrialResponse])
def list_trials(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")

    trials = (
        db.query(Trial)
        .filter(Trial.experiment_id == experiment_id)
        .order_by(Trial.trial_number.asc())
        .all()
    )
    return trials