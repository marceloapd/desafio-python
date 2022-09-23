"""create table address

Revision ID: 89424284b6d9
Revises: ff2a744a7e15
Create Date: 2022-09-22 20:30:07.489265

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '89424284b6d9'
down_revision = 'ff2a744a7e15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", UUID(), nullable=False, primary_key=True),
        sa.Column("api_id", sa.Integer(), nullable=False),
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

    op.create_unique_constraint("uq_api_id_address", "address", ['api_id'])

def downgrade() -> None:
    op.drop_table("address")
