from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TrialBase(BaseModel):
    trial_number: int
    procedure: str
    variables: str
    observations: str
    result: str


class TrialCreate(TrialBase):
    pass


class TrialResponse(TrialBase):
    id: int
    experiment_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)