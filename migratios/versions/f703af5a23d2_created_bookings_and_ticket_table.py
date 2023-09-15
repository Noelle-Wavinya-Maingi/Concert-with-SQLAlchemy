"""Created bookings and ticket table

Revision ID: f703af5a23d2
Revises: aa34b856e1d4
Create Date: 2023-09-15 15:22:00.538450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f703af5a23d2'
down_revision: Union[str, None] = 'aa34b856e1d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'bookings',
        sa.Column('booking_id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.user_id')),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('events.event_id')),
        sa.Column('ticket_id', sa.Integer(), sa.ForeignKey('tickets.ticket_id')),
        sa.Column('booking_date', sa.DateTime(), server_default=sa.func.now()),
    )

    op.create_table(
        'tickets',
        sa.Column('ticket_id', sa.Integer(), primary_key=True),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('events.event_id')),
        sa.Column('ticket_type', sa.String(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('availability', sa.Integer(), nullable=False),
    )

def downgrade():
    op.drop_table('bookings')
    op.drop_table('tickets')