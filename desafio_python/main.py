from fastapi import Depends, FastAPI

from desafio_python.dependencies.databases import get_postgres_session
from desafio_python.dependencies.auth import check_token
from .routers import token, user
from .services.import_jsonplaceholder import ImportJsonplaceholder
import requests

app = FastAPI()

app.include_router(token.router, tags=["get_token"], prefix="/auth")
app.include_router(
    user.router,
    tags=["get_websites"],
    prefix="/users",
    dependencies=[Depends(check_token)],
)


@app.on_event("startup")
async def seed_db_event():
    api_response = requests.get("https://jsonplaceholder.typicode.com/users")
    if api_response.status_code != 200:
        raise ValueError("")
    postgres = get_postgres_session()
    user = ImportJsonplaceholder(postgres)
    return user.get_jsonplaceholder(api_response.json())


@app.get("/")
def index():
    return "Hello, world!"
