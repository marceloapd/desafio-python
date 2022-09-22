from sqlalchemy import (VARCHAR, Column, DateTime, Integer, UniqueConstraint,
                        text)

from .base import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)
    bs = Column(VARCHAR(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))
