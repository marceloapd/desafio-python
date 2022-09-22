from sqlalchemy import Column, DateTime, Integer, VARCHAR, UniqueConstraint, text
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False) 
    bs = Column(VARCHAR(50), nullable=False) 
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))