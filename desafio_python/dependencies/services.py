from .databases import get_postgres_session, get_redis_client
from ..services.users import UserService
from ..services.auth import AuthService
from fastapi import Depends
from redis import Redis


def get_auth_service():
    auth_service = AuthService()
    return auth_service


def get_user_service(
    postgres=Depends(get_postgres_session),
    redis_client: Redis = Depends(get_redis_client),
):
    user_service = UserService(postgres, redis_client)
    return user_service
