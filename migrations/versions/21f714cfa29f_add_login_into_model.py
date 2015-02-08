"""add login into model

Revision ID: 21f714cfa29f
Revises: d6ac106b454
Create Date: 2015-01-22 17:08:14.386721

"""

# revision identifiers, used by Alembic.
revision = '21f714cfa29f'
down_revision = 'd6ac106b454'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', 'users')
    op.drop_table('users')
    ### end Alembic commands ###
