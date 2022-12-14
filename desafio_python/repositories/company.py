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

    def bulk_create(self, company_data):
        with self.session_db() as session:
            for company in company_data:
                company_obj = Company(**company)
                try:
                    session.merge(company_obj)
                    session.commit()
                except Exception as e:
                    session.rollback()

    def get_company_by_id(self, id):
        with self.session_db() as session:
            return session.query(Company).all()
