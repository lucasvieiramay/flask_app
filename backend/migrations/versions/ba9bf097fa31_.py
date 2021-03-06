"""empty message

Revision ID: ba9bf097fa31
Revises: 
Create Date: 2018-04-17 10:48:39.413916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba9bf097fa31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('doc_id', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('image', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('doc_id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persons')
    # ### end Alembic commands ###
