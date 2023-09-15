"""Create genre model and association table event_genres

Revision ID: 0ce9221864a6
Revises: 072397f3f527
Create Date: 2023-09-15 20:29:41.935602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ce9221864a6'
down_revision: Union[str, None] = '072397f3f527'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'genres',
        sa.Column('genre_id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'event_genres',
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('events.event_id'), primary_key=True),
        sa.Column('genre_id', sa.Integer(), sa.ForeignKey('genres.genre_id'), primary_key=True)
    )

def downgrade():
    op.drop_table('event_genres')
    op.drop_table('genres')