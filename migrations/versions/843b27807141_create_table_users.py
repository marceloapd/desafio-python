"""create table users

Revision ID: 843b27807141
Revises: 89424284b6d9
Create Date: 2022-09-22 20:30:13.866533

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '843b27807141'
down_revision = '89424284b6d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("api_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.VARCHAR(50), nullable=False),
        sa.Column("username", sa.VARCHAR(20), nullable=False),
        sa.Column("email", sa.VARCHAR(50), nullable=False),
        sa.Column("phone", sa.VARCHAR(30), nullable=False),
        sa.Column("website", sa.VARCHAR(50), nullable=False),
        sa.Column("company_id", UUID(), nullable=False),
        sa.Column("address_id", UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.ForeignKeyConstraint(["company_id"], ["company.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["address_id"], ["address.id"], ondelete="CASCADE")
    )

    op.create_unique_constraint("uq_api_id_user", "users", ['api_id'])

def downgrade() -> None:
    op.drop_table("users")
