"""Create roles and users tables

Revision ID: ff3312e7df74
Revises: 60a982caf157
Create Date: 2023-09-15 11:20:51.383326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff3312e7df74'
down_revision: Union[str, None] = '60a982caf157'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the roles table
    op.create_table(
        'roles',
        sa.Column('role_id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), unique=True, nullable=False),
        sa.Column('description', sa.String()),
    )

    # Create the users table with a foreign key relationship to roles
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(), unique=True, nullable=False),
        sa.Column('email', sa.String(), unique=True, nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey("roles.role_id")),
    )

def downgrade():
    # Drop the tables in reverse order
    op.drop_table('users')
    op.drop_table('roles')