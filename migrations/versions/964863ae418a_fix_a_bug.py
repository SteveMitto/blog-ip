"""fix a bug

Revision ID: 964863ae418a
Revises: 5ba6da7572c7
Create Date: 2019-09-21 19:23:12.669573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '964863ae418a'
down_revision = '5ba6da7572c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_comment_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('blogs_comment_id_fkey', 'blogs', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###
