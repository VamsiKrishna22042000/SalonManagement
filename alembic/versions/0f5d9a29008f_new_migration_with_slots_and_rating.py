"""new migration with slots and rating

Revision ID: 0f5d9a29008f
Revises: 
Create Date: 2025-11-19 08:43:24.768485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import ARRAY

# revision identifiers, used by Alembic.
revision: str = '0f5d9a29008f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Remove old slot column
    op.drop_column("Bookings", "slot")

    # Add new date + time columns
    op.add_column(
        "Bookings",
        sa.Column("date", sa.DateTime(timezone=True), nullable=False)
    )
    op.add_column(
        "Bookings",
        sa.Column("time", sa.String(length=20), nullable=False)
    )

    op.add_column(
        "Staffs",
        sa.Column(
            "slots",
            ARRAY(sa.String()),
            nullable=False,
            server_default=sa.text(
                """'{"9:00AM-10:00AM",
                    "10:00AM-11:00AM",
                    "11:00AM-12:00PM",
                    "12:00PM-1:00PM",
                    "1:00PM-2:00PM",
                    "2:00PM-3:00PM",
                    "3:00PM-4:00PM",
                    "4:00PM-5:00PM",
                    "5:00PM-6:00PM",
                    "6:00PM-7:00PM",
                    "7:00PM-8:00PM",
                    "8:00PM-9:00PM"}'"""
            )
        )
    )

    op.add_column(
        "Staffs",
        sa.Column(
            "rating",
            sa.Float(),
            nullable=True,
            server_default="0.0"
        )
    )

def downgrade() -> None:
   pass