"""empty message

Revision ID: a40272ea3d44
Revises: 6e361a26e2ed
Create Date: 2024-05-22 20:46:57.461020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a40272ea3d44'
down_revision = '6e361a26e2ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(), nullable=True),
    sa.Column('scientific_name', sa.String(), nullable=True),
    sa.Column('conservation_status', sa.String(), nullable=True),
    sa.Column('native_habitat', sa.String(), nullable=True),
    sa.Column('fun_fact', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptile')
    # ### end Alembic commands ###