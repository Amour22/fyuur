"""empty message

Revision ID: 89e7ee669da9
Revises: 
Create Date: 2022-08-18 10:49:40.672636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89e7ee669da9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
