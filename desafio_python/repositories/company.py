from typing import List

from sqlalchemy.orm import Session

from ..models.company import Company


class CompanyRepository:
    def __init__(self, session_db: Session):
        self.session_db = session_db

    def create(self, company_data: dict):
        company = Company(**company_data)
        with self.session_db() as session:
            session.add(company)
            session.commit()
            session.refresh(company)
        return company
