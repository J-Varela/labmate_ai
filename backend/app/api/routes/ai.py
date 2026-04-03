from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experiment import Experiment
from app.models.trial import Trial
from app.schemas.ai import ExperimentSummaryResponse
from app.services.ai_service import generate_experiment_summary

router = APIRouter(prefix="/experiments", tags=["AI"])


@router.post("/{experiment_id}/summarize", response_model=ExperimentSummaryResponse)
def summarize_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")

    trials = (
        db.query(Trial)
        .filter(Trial.experiment_id == experiment_id)
        .order_by(Trial.trial_number.asc())
        .all()
    )

    summary = generate_experiment_summary(experiment, trials)

    return ExperimentSummaryResponse(
        experiment_id=experiment_id,
        summary=summary,
    )