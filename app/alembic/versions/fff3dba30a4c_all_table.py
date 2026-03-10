"""all_table

Revision ID: fff3dba30a4c
Revises: aa2003250161
Create Date: 2026-02-24 08:20:02.926934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fff3dba30a4c'
down_revision: Union[str, None] = 'aa2003250161'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
