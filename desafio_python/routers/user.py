from fastapi import APIRouter, Depends

from ..dependencies.services import get_user_service
from ..services.users import UserService

router = APIRouter()


@router.get("/websites", status_code=200)
def get_websites(user_service: UserService = Depends(get_user_service)):
    websites = user_service.get_websites()

    return websites


@router.get("/details", status_code=200)
def get_details(user_service: UserService = Depends(get_user_service)):
    details = user_service.get_details()
    return details


@router.get("/", status_code=200)
def get_user_by_name(name: str, user_service: UserService = Depends(get_user_service)):
    if not name:
        return "Invalid username."
    user_by_name = user_service.get_user_by_name(name)
    return user_by_name
