"""activities_table

Revision ID: 790c9d3b96c0
Revises: 83b0cc9edaac
Create Date: 2026-02-24 08:00:25.475594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790c9d3b96c0'
down_revision: Union[str, None] = '83b0cc9edaac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
