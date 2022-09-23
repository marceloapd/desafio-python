from sqlalchemy import (VARCHAR, Column, DateTime, Integer, text)
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(UUID(), primary_key=True)
    api_id = Column(Integer, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    bs = Column(VARCHAR(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    