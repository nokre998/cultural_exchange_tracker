"""all_table

Revision ID: 673492fe8f9b
Revises: 790c9d3b96c0
Create Date: 2026-02-24 08:10:08.623394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '673492fe8f9b'
down_revision: Union[str, None] = '790c9d3b96c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
