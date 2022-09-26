from fastapi import Depends, Header
from .services import get_auth_service
from ..services.auth import AuthService
from fastapi import HTTPException


def check_token(
    auth_service: AuthService = Depends(get_auth_service),
    authorization: str = Header(...),
):

    token = authorization.split(" ")
    if len(token) != 2:
        raise HTTPException(403, "Invalid authorization")
    auth_service.verify_token(token[1])
    return
