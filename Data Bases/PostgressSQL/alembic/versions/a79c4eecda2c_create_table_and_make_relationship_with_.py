"""create table and make relationship with users table after uncomenting the older code

Revision ID: a79c4eecda2c
Revises: 437cc45dfd24
Create Date: 2025-03-10 11:01:06.884988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a79c4eecda2c'
down_revision: Union[str, None] = '437cc45dfd24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
