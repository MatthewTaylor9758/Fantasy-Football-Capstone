"""empty message

Revision ID: f9784b3eb8b1
Revises: 68b6b86d59d6
Create Date: 2020-10-09 13:46:17.761157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9784b3eb8b1'
down_revision = '68b6b86d59d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # This step has to run before the next two in order for it to work
    op.create_unique_constraint('team_league_uidx', 'teams', ['id', 'league_id'])

    op.create_unique_constraint('player_in_league_only_once_uidx', 'ffsplayers', ['player_id', 'league_id'])
    op.create_foreign_key('team_league_fk', 'ffsplayers', 'teams', ['team_id', 'league_id'], ['id', 'league_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('team_league_fk', 'ffsplayers', type_='foreignkey')
    op.drop_constraint('player_in_league_only_once_uidx', 'ffsplayers', type_='unique')

    # This line needs to run after the previous two steps in order for it to work
    op.drop_constraint('team_league_uidx', 'teams', type_='unique')
    # ### end Alembic commands ###
