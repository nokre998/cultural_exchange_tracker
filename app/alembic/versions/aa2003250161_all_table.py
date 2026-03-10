"""all_table

Revision ID: aa2003250161
Revises: 77dc16db1410
Create Date: 2026-02-24 08:18:36.444407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa2003250161'
down_revision: Union[str, None] = '77dc16db1410'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
