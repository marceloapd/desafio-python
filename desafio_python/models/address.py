from sqlalchemy import (VARCHAR, Column, DateTime, Integer, UniqueConstraint,
                        text)
from sqlalchemy.orm import relationship

from .base import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    street = Column(VARCHAR(50), nullable=False)
    suite = Column(VARCHAR(20), nullable=False)
    city = Column(VARCHAR(50), nullable=False)
    zipcode = Column(VARCHAR(20), nullable=False)
    lat = Column(VARCHAR(10), nullable=False)
    lng = Column(VARCHAR(10), nullable=False)
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))
