"""create table company

Revision ID: ff2a744a7e15
Revises: 
Create Date: 2022-09-22 20:29:56.698733

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'ff2a744a7e15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "company",
        sa.Column("id", UUID(), nullable=False, primary_key=True),
        sa.Column("api_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.VARCHAR(50), nullable=False),
        sa.Column("bs", sa.VARCHAR(50), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )

    op.create_unique_constraint("uq_api_id_company", "company", ['api_id'])

def downgrade() -> None:
    op.drop_table("company")
