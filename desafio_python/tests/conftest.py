from desafio_python.dependencies.databases import get_postgres_session

from desafio_python.main import app
from desafio_python.models.base import Base
from fastapi.testclient import TestClient
from ..services.auth import AuthService
from ..helpers.tests import mock_users
from ..services.import_jsonplaceholder import ImportJsonplaceholder

from pytest import fixture

from ..helpers.tests import ENGINE, override_sqlite3_session

app.dependency_overrides[get_postgres_session] = override_sqlite3_session


@fixture
def client():
    Base.metadata.create_all(bind=ENGINE)
    _client = TestClient(app)
    seed_db()
    yield _client
    Base.metadata.drop_all(bind=ENGINE)


@fixture
def sqlite():
    return override_sqlite3_session


@fixture
def get_token():
    auth = AuthService()
    return auth.generate_token()


def seed_db():
    sqlite_session = override_sqlite3_session()
    jsonplaceholder = ImportJsonplaceholder(sqlite_session)
    jsonplaceholder.get_jsonplaceholder(mock_users)
