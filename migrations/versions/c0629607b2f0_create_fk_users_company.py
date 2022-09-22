"""create fk_users_company

Revision ID: c0629607b2f0
Revises: 9469f707160e
Create Date: 2022-09-21 22:12:16.473516

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c0629607b2f0"
down_revision = "9469f707160e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key("company_id_fk", "users", "company", ["company_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint("company_id_fk", "users", "foreignkey")
