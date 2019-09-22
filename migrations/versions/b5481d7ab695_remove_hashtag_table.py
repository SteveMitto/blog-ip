"""remove hashtag table

Revision ID: b5481d7ab695
Revises: 964863ae418a
Create Date: 2019-09-21 19:33:22.489529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5481d7ab695'
down_revision = '964863ae418a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hashtags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtags',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tag', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['blogs.id'], name='hashtags_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='hashtags_pkey')
    )
    # ### end Alembic commands ###
