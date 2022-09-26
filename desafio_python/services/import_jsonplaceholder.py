from collections import defaultdict
from uuid import uuid4

from ..configs.postgres import Database
from ..repositories.address import AdressRepository
from ..repositories.company import CompanyRepository
from ..repositories.users import UsersRepository


class ImportJsonplaceholder:
    def __init__(self, postgres: Database):
        self.users_repository = UsersRepository(postgres.session)
        self.address_repository = AdressRepository(postgres.session)
        self.company_repository = CompanyRepository(postgres.session)

    def get_jsonplaceholder(self, api_response):

        data_to_bulk_save = defaultdict(list)
        for data in api_response:
            company = data["company"]
            company_id = str(uuid4())
            company["id"] = company_id
            company["api_id"] = data["id"]

            del company["catchPhrase"]

            address = {
                "street": data["address"]["street"],
                "suite": data["address"]["suite"],
                "city": data["address"]["city"],
                "zipcode": data["address"]["zipcode"],
                "lat": data["address"]["geo"]["lat"],
                "lng": data["address"]["geo"]["lng"],
            }
            address_id = str(uuid4())
            address["id"] = address_id
            address["api_id"] = data["id"]

            user = {
                "name": data["name"],
                "username": data["username"],
                "email": data["email"],
                "phone": data["phone"],
                "website": data["website"],
                "company_id": company_id,
                "address_id": address_id,
                "api_id": data["id"],
            }

            data_to_bulk_save["users"].append(user)
            data_to_bulk_save["companies"].append(company)
            data_to_bulk_save["address"].append(address)

        self.company_repository.bulk_create(data_to_bulk_save["companies"])
        self.address_repository.bulk_create(data_to_bulk_save["address"])
        self.users_repository.bulk_create(data_to_bulk_save["users"])
