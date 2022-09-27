import json
from ..configs.postgres import Database
import fakeredis

sqlite = Database("sqlite:///test.db")
ENGINE = sqlite.engine

redis_server = fakeredis.FakeServer()

with open("./desafio_python/helpers/mock_data/user_mock.json") as f:
    mock_users = json.load(f)


def override_sqlite3_session():
    return sqlite

def override_redis_db():
    redis_client = fakeredis.FakeStrictRedis(server=redis_server)
    yield redis_client
    redis_client.close()
