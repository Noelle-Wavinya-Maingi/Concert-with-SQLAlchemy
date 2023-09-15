"""Create the payment table

Revision ID: 0244a7edce95
Revises: 0ce9221864a6
Create Date: 2023-09-15 20:35:24.439246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0244a7edce95'
down_revision: Union[str, None] = '0ce9221864a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'payments',
        sa.Column('payment_id', sa.Integer(), primary_key=True),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('events.event_id'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False)
    )

def downgrade():
    op.drop_table('payments')