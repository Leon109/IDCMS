"""change record username

Revision ID: 3d22ceeededa
Revises: 3bafb67190d0
Create Date: 2015-08-11 18:14:26.597810

"""

# revision identifiers, used by Alembic.
revision = '3d22ceeededa'
down_revision = '3bafb67190d0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('table', sa.String(length=32), nullable=True))
    op.add_column('record', sa.Column('table_id', sa.String(length=32), nullable=True))
    op.drop_column('record', 'item_id')
    op.drop_column('record', 'item')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('item', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('record', sa.Column('item_id', mysql.VARCHAR(length=32), nullable=True))
    op.drop_column('record', 'table_id')
    op.drop_column('record', 'table')
    ### end Alembic commands ###
