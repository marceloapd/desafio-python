from ..repositories.users import UsersRepository
from ..configs.postgres import Database

class UserService:
    def __init__(self, postgres: Database):
        self.users_repository = UsersRepository(postgres.session)

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
            detail["users"].append({"name": user.name,"email": user.email,"company": user.company.name})
        return detail

    def get_user_by_name(self, name):
        users = self.users_repository.get_user_by_name(name)
        user_by_name = {"users": []}
        for user in users:
            user_by_name["users"].append({"id": user.id,"name": user.name})
        return user_by_name
        