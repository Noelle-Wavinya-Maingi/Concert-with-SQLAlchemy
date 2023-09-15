"""Created venust table

Revision ID: 96ff6007f556
Revises: f703af5a23d2
Create Date: 2023-09-15 15:33:58.222492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96ff6007f556'
down_revision: Union[str, None] = 'f703af5a23d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'venues',
        sa.Column('venue_id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String()),
        sa.Column('capacity', sa.Integer()),
    )

def downgrade():
    op.drop_table('venues')