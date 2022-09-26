from sqlalchemy import VARCHAR, Column, DateTime, Integer, text
from sqlalchemy_utils import UUIDType

from .base import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(UUIDType(), primary_key=True)
    api_id = Column(Integer, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    bs = Column(VARCHAR(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))
