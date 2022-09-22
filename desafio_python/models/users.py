from sqlalchemy import Column, DateTime, Integer, VARCHAR, UniqueConstraint, text
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False) 
    username = Column(VARCHAR(20), nullable=False) 
    email = Column(VARCHAR(50), nullable=False) 
    phone = Column(VARCHAR(30), nullable=False) 
    website = Column(VARCHAR(50), nullable=False) 
    company_id = Column(Integer(), nullable=False) 
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))