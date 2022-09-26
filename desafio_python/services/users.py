from fastapi import HTTPException
from ..repositories.users import UsersRepository
from ..configs.postgres import Database
from ..helpers.users import USERS_BY_NAME_KEY, ONE_HOUR
from redis import Redis
import json


class UserService:
    def __init__(self, postgres: Database, redis_client: Redis):
        self.users_repository = UsersRepository(postgres.session)
        self.redis_client = redis_client

    def get_websites(self):
        users = self.users_repository.get_users()
        websites = {"websites": []}
        for user in users:
            websites["websites"].append({"website": user.website})
        return websites

    def get_details(self):
        users = self.users_repository.get_users_by_order()
        detail = {"users": []}
        for user in users:
            detail["users"].append(
                {"name": user.name, "email": user.email, "company": user.company.name}
            )
        return detail

    def get_user_by_name(self, name):
        key_cache = USERS_BY_NAME_KEY.format(name)
        cached_data = self.redis_client.get(key_cache)
        if cached_data:
            return json.loads(cached_data)

        users = self.users_repository.get_user_by_name(name)
        user_by_name = {"users": []}
        if not users:
            raise HTTPException(404, "User not found")
        for user in users:
            user_by_name["users"].append({"id": user.id, "name": user.name})

        self.redis_client.setex(key_cache, ONE_HOUR, json.dumps(user_by_name))
        return user_by_name
