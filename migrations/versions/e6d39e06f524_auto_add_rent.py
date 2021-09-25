"""Auto. Add rent

Revision ID: e6d39e06f524
Revises: e167abcb2827
Create Date: 2021-09-25 08:21:39.892722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6d39e06f524'
down_revision = 'e167abcb2827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auto', sa.Column('in_rent_or_free', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auto', 'in_rent_or_free')
    # ### end Alembic commands ###