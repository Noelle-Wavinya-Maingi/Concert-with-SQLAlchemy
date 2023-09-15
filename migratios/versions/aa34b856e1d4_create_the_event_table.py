"""Create the event table

Revision ID: aa34b856e1d4
Revises: ff3312e7df74
Create Date: 2023-09-15 15:13:54.303052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa34b856e1d4'
down_revision: Union[str, None] = 'ff3312e7df74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'events',
        sa.Column('event_id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('time', sa.Time()),
        sa.Column('location', sa.String()),
        sa.Column('description', sa.String()),
    )

def downgrade():
    op.drop_table('events')