"""all_table

Revision ID: 440936441e0e
Revises: 673492fe8f9b
Create Date: 2026-02-24 08:17:10.020959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '440936441e0e'
down_revision: Union[str, None] = '673492fe8f9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
