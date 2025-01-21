"""add Fullname Column in User Table

Revision ID: f95bfd84eb19
Revises: 742486c2a5b2
Create Date: 2025-01-21 11:15:10.502813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f95bfd84eb19'
down_revision: Union[str, None] = '742486c2a5b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=False))


def downgrade() -> None:
    pass
