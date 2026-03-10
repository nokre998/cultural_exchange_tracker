"""all

Revision ID: f7f375208785
Revises: fff3dba30a4c
Create Date: 2026-02-24 08:24:57.859085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7f375208785'
down_revision: Union[str, None] = 'fff3dba30a4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
