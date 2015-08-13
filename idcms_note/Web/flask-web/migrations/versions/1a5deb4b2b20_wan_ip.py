"""wan_ip

Revision ID: 1a5deb4b2b20
Revises: cf916d0cc4a
Create Date: 2015-08-11 11:07:37.312478

"""

# revision identifiers, used by Alembic.
revision = '1a5deb4b2b20'
down_revision = 'cf916d0cc4a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_cabinet_wan_ip', table_name='cabinet')
    op.create_index(op.f('ix_cabinet_wan_ip'), 'cabinet', ['wan_ip'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cabinet_wan_ip'), table_name='cabinet')
    op.create_index('ix_cabinet_wan_ip', 'cabinet', ['wan_ip'], unique=True)
    ### end Alembic commands ###