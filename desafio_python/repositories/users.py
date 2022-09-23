from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import desc

from ..models.users import Users


class UsersRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def create(self, user_data: dict):
        users = Users(**user_data)
        with self.session_db() as session:
            session.add(users)
            session.commit()
            session.refresh(users)
        return users

    def bulk_create(self, user_data):
        with self.session_db() as session:
            for user in user_data:
                user_obj = Users(**user)
                try:
                    session.merge(user_obj)
                    session.commit()
                except Exception as e:
                    print(e)
                    session.rollback()

    def get_users(self):
        with self.session_db() as session:
            return session.query(Users).all()
    
    def get_users_by_order(self):
        with self.session_db() as session:
            return session.query(Users).order_by(desc(Users.name)).all()
    
    def     get_user_by_name(self, name):
        with self.session_db() as session:
            return session.query(Users).filter(Users.name.match(f"%{name}%")).all()
