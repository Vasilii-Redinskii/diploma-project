"""Initial migration.

Revision ID: 71a30cc30af2
Revises: 
Create Date: 2021-09-29 11:09:30.684835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a30cc30af2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('transmission', sa.Boolean(), nullable=True),
    sa.Column('img_url_1', sa.String(length=128), nullable=True),
    sa.Column('img_url_2', sa.String(length=128), nullable=True),
    sa.Column('img_url_3', sa.String(length=128), nullable=True),
    sa.Column('img_url_4', sa.String(length=128), nullable=True),
    sa.Column('in_rent_or_free', sa.Boolean(), nullable=True),
    sa.Column('all_time_rent', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('total_cost_of_rent', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('arenda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('auto_id', sa.Integer(), nullable=True),
    sa.Column('date_rent', sa.DateTime(), nullable=True),
    sa.Column('date_free', sa.DateTime(), nullable=True),
    sa.Column('in_rent_or_free', sa.Boolean(), nullable=True),
    sa.Column('time_rent', sa.Float(), nullable=True),
    sa.Column('cost_of_rent', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['auto_id'], ['auto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arenda')
    op.drop_table('auto')
    # ### end Alembic commands ###
