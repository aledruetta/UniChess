"""Initial commit

Revision ID: 25bbc4288be5
Revises: 
Create Date: 2020-09-07 12:20:31.158857

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '25bbc4288be5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Unicode(), nullable=False),
    sa.Column('email', sa.Unicode(), nullable=False),
    sa.Column('password', sa.Unicode(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('random_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('host_id', sa.Integer(), nullable=False),
    sa.Column('host_time', sa.Time(), nullable=False),
    sa.Column('guest_id', sa.Integer(), nullable=True),
    sa.Column('guest_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['guest_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['host_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uci', sa.Unicode(), nullable=False),
    sa.Column('color', sa.Boolean(), nullable=False),
    sa.Column('board_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movement')
    op.drop_table('board')
    op.drop_table('user')
    # ### end Alembic commands ###
