from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ExperimentBase(BaseModel):
    title: str
    objective: str
    hypothesis: str
    status: str = "draft"


class ExperimentCreate(ExperimentBase):
    pass


class ExperimentResponse(ExperimentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)