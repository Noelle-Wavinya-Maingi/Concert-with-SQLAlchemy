"""Create artist table

Revision ID: 072397f3f527
Revises: 96ff6007f556
Create Date: 2023-09-15 20:18:48.506395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '072397f3f527'
down_revision: Union[str, None] = '96ff6007f556'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'artists',
        sa.Column('artist_id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'event_artists',
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('events.event_id'), primary_key=True),
        sa.Column('artist_id', sa.Integer(), sa.ForeignKey('artists.artist_id'), primary_key=True)
    )

def downgrade():
    op.drop_table('event_artists')
    op.drop_table('artists')
