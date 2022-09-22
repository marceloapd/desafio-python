"""create table company

Revision ID: 9469f707160e
Revises: 607e51409bc8
Create Date: 2022-09-21 21:42:20.690819

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9469f707160e"
down_revision = "607e51409bc8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "company",
        sa.Column(
            "id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True
        ),
        sa.Column("name", sa.VARCHAR(50), nullable=False),
        sa.Column("bs", sa.VARCHAR(50), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )


def downgrade() -> None:
    op.drop_table("company")
