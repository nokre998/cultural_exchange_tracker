"""evenst_table

Revision ID: 83b0cc9edaac
Revises: 51433f76ad87
Create Date: 2026-02-24 07:54:54.313064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83b0cc9edaac'
down_revision: Union[str, None] = '51433f76ad87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
