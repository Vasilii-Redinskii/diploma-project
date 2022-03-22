"""Add frenquency and power

Revision ID: c59937b2b8d3
Revises: 14c209a33c49
Create Date: 2022-02-23 06:13:58.610712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c59937b2b8d3'
down_revision = '14c209a33c49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('condenser', sa.Column('frenquency', sa.Float(), nullable=True))
    op.add_column('condenser', sa.Column('power', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('condenser', 'power')
    op.drop_column('condenser', 'frenquency')
    # ### end Alembic commands ###