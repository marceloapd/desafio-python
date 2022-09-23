from .databases import get_postgres_session
from ..services.users import UserService
from ..services.auth import AuthService
from fastapi import Depends

def get_auth_service():
    auth_service = AuthService()
    return auth_service

def get_user_service(postgres= Depends(get_postgres_session)):
    user_service = UserService(postgres)
    return user_service
