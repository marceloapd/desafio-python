"""create table address

Revision ID: 607e51409bc8
Revises: 7b9efa115217
Create Date: 2022-09-21 21:37:33.187565

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "607e51409bc8"
down_revision = "7b9efa115217"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column(
            "id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("street", sa.VARCHAR(50), nullable=False),
        sa.Column("suite", sa.VARCHAR(20), nullable=False),
        sa.Column("city", sa.VARCHAR(50), nullable=False),
        sa.Column("zipcode", sa.VARCHAR(20), nullable=False),
        sa.Column("lat", sa.VARCHAR(10), nullable=False),
        sa.Column("lng", sa.VARCHAR(10), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )
    op.create_foreign_key("user_id_fk", "address", "users", ["user_id"], ["id"])


def downgrade() -> None:
    op.drop_table("address")
