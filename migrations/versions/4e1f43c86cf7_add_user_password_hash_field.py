"""add user password hash field

Revision ID: 4e1f43c86cf7
Revises: 508f9a596a04
Create Date: 2015-05-04 13:37:33.033405

"""

# revision identifiers, used by Alembic.
revision = '4e1f43c86cf7'
down_revision = '508f9a596a04'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
