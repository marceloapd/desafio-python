from fastapi import APIRouter, Depends

from ..dependencies.services import get_auth_service
from ..services.auth import AuthService 

router = APIRouter()

@router.get(
    "/get-token",
    status_code=200,
    responses={404: {"description": "This team does not exist!"}},
)
def get_token(auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.generate_token()
