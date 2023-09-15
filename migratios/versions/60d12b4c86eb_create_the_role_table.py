"""Create the Role table

Revision ID: 60d12b4c86eb
Revises: 477217251df0
Create Date: 2023-09-15 10:55:52.025666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d12b4c86eb'
down_revision = '477217251df0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable = True),
        sa.PrimaryKeyConstraint('role_id')
    )

def downgrade() -> None:
    op.drop_table('roles')
