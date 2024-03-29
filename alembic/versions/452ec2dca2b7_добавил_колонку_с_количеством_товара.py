"""Добавил колонку с количеством товара

Revision ID: 452ec2dca2b7
Revises: c2a3920b3f18
Create Date: 2021-04-21 19:44:52.527928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2a3920b3f18'
down_revision = '53fdfa2db1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_table', sa.Column('amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_table', 'amount')
    # ### end Alembic commands ###
