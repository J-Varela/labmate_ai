from pydantic import BaseModel


class ExperimentSummaryResponse(BaseModel):
    experiment_id: int
    summary: str