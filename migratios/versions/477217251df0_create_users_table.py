"""Create users table

Revision ID: 477217251df0
Revises: f50f53b93b5c
Create Date: 2023-09-15 10:44:29.593234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477217251df0'
down_revision = 'f50f53b93b5c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable = True),
        sa.Column('password', sa.String(), nullable = True),
        sa.PrimaryKeyConstraint('user_id')
    )

def downgrade() -> None:
    op.drop_table('users')