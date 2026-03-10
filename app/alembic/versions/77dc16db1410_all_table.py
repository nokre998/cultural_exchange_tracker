"""all_table

Revision ID: 77dc16db1410
Revises: 440936441e0e
Create Date: 2026-02-24 08:17:58.776083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77dc16db1410'
down_revision: Union[str, None] = '440936441e0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
