"""drop comment table

Revision ID: 1918d440ef50
Revises: b5481d7ab695
Create Date: 2019-09-23 05:02:49.417759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1918d440ef50'
down_revision = 'b5481d7ab695'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    # ### end Alembic commands ###