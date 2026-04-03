from datetime import datetime
from sqlalchemy import ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Trial(Base):
    __tablename__ = "trials"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    experiment_id: Mapped[int] = mapped_column(ForeignKey("experiments.id"), nullable=False)
    trial_number: Mapped[int] = mapped_column(Integer, nullable=False)
    procedure: Mapped[str] = mapped_column(Text, nullable=False)
    variables: Mapped[str] = mapped_column(Text, nullable=False)
    observations: Mapped[str] = mapped_column(Text, nullable=False)
    result: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    experiment = relationship("Experiment", back_populates="trials")