"""create table users

Revision ID: 7b9efa115217
Revises: 
Create Date: 2022-09-21 21:30:00.706882

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7b9efa115217"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True
        ),
        sa.Column("name", sa.VARCHAR(50), nullable=False),
        sa.Column("username", sa.VARCHAR(20), nullable=False),
        sa.Column("email", sa.VARCHAR(50), nullable=False),
        sa.Column("phone", sa.VARCHAR(30), nullable=False),
        sa.Column("website", sa.VARCHAR(50), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )


def downgrade() -> None:
    op.drop_table("users")
