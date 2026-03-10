"""activities_table

Revision ID: 51433f76ad87
Revises: 680b39bae4af
Create Date: 2026-02-24 07:52:31.540097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51433f76ad87'
down_revision: Union[str, None] = '680b39bae4af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
