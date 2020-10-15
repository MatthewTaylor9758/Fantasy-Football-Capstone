from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import FFSplayer, League, Team, Player, db

ffsplayers_routes = Blueprint('ffsplayers', __name__)

@ffsplayers_routes.route('/<ffsplayerId>', methods=['PUT'])
def get_ffsplayer():
  data = request.json
  ffsplayer = FFSplayer.query.filter(FFSplayer.id == data['id'])
  ffsplayer_dict = ffsplayer.to_dict()
  return {'ffsplayer': ffsplayer_dict}

@ffsplayers_routes.route('/', methods=['POST'])
def create_ffsplayer():
  data = request.json
  league_ffsplayers = FFSplayer.query.filter(FFSplayer.league_id == data['league_id'])
  ffsplayer_exists = FFSplayer.query.filter(FFSplayer.player_id == data['player_id'])
  if ffsplayer_exists:
    return {'error': 'That player is already on a team in your league!'}
  new_ffsplayer = FFSplayer(
    player_id = data['player_id'],
    team_id = data['team_id'],
    league_id = data['league_id']
  )
  db.session.add(new_ffsplayer)
  db.session.commit()
  ffsplayer_dict = ffsplayer.to_dict()
  return {'ffsplayer': ffsplayer_dict}

@ffsplayers_routes.route('/<leagueId>/<teamId>')
def get_team_ffsplayers(leagueId, teamId):
  league_ffsplayers = FFSplayer.query.filter(FFSplayer.league_id == leagueId)

  def find_team(player):
    if player['team_id'] == teamId:
      return True
    else:
      return False

  team_ffsplayers = league_ffsplayers.filter(find_team, league_ffsplayers)
  return [player.to_dict() for player in team_ffsplayers]

@ffsplayers_routes.route('/<ffsplayerId>', methods=['DELETE'])
def remove_ffsplayer(ffsplayerId):
  ffsplayer = FFSplayer.query.get(ffsplayerId)
  db.session.delete(ffsplayer)
  db.session.commit()
  return 'ffsplayer removed'
