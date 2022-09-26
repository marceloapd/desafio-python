import json
from ..configs.postgres import Database

sqlite = Database("sqlite:///test.db")
ENGINE = sqlite.engine

with open("./desafio_python/helpers/mock_data/user_mock.json") as f:
    mock_users = json.load(f)


def override_sqlite3_session():
    return sqlite
