from sqlalchemy import VARCHAR, Column, DateTime, Integer, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    api_id = Column(Integer, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    username = Column(VARCHAR(20), nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    phone = Column(VARCHAR(30), nullable=False)
    website = Column(VARCHAR(50), nullable=False)
    company_id = Column(UUID(), ForeignKey("company.id"))
    address_id = Column(UUID(), ForeignKey("address.id"))
    created_at = Column(DateTime, nullable=False, default=text("CURRENT_TIMESTAMP"))

    company = relationship("Company", lazy="joined")
    address = relationship("Address", lazy="joined")