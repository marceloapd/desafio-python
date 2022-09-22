from typing import List

from sqlalchemy.orm import Session

from ..models.users import User


class User:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def create(self, user_data: dict):
        users = User(**user_data)
        with self.session_db() as session:
            session.add(users)
            session.commit()
            session.refresh(users)
        return users
