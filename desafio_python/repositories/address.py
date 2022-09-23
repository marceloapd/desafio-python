
from sqlalchemy.orm import Session

from ..models.address import Address


class AdressRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def create(self, address_data: dict):
        address = Address(**address_data)
        with self.session_db() as session:
            session.add(address)
            session.commit()
            session.refresh(address)
        return address

    def bulk_create(self, address_data):
        with self.session_db() as session:
            for address in address_data:
                address_obj = Address(**address)
                try:
                    session.merge(address_obj)
                    session.commit()
                except Exception as e:
                    session.rollback()
