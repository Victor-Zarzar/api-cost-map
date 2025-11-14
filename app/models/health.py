from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.db.base import Base


class HealthCheck(Base):
    __tablename__ = "health_checks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)
    details = Column(String(255))
    response_time = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
