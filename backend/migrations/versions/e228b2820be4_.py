"""empty message

Revision ID: e228b2820be4
Revises: aa5ddeae4e30
Create Date: 2018-04-15 18:53:57.041939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e228b2820be4'
down_revision = 'aa5ddeae4e30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persons')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('doc_id', sa.VARCHAR(length=11), autoincrement=False, nullable=True),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='persons_pkey'),
    sa.UniqueConstraint('doc_id', name='persons_doc_id_key'),
    sa.UniqueConstraint('email', name='persons_email_key')
    )
    # ### end Alembic commands ###
