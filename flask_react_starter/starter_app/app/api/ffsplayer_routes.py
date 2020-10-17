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
  # Gets all players in league of the user
  # Then converts the players in the league into dicts
  # Then
  league_ffsplayers = FFSplayer.query.filter(FFSplayer.league_id == leagueId).all()
  league_ffsplayers_dict = [player.to_dict() for player in league_ffsplayers]
  team_ffsplayers = [player for player in league_ffsplayers_dict if int(player['team_id']) == int(teamId)]
  team_ffsplayers_ids = [player['player_id'] for player in team_ffsplayers]
  team_nfl_players = []
  for player_id in team_ffsplayers_ids:
    nfl_player = Player.query.filter(Player.player_id == player_id).first()
    team_nfl_players.append(nfl_player.to_dict())
  players_dict = {num: player for num, player in enumerate(team_nfl_players, 1)}
  return players_dict

@ffsplayers_routes.route('/<ffsplayerId>', methods=['DELETE'])
def remove_ffsplayer(ffsplayerId):
  ffsplayer = FFSplayer.query.get(ffsplayerId)
  db.session.delete(ffsplayer)
  db.session.commit()
  return 'ffsplayer removed'
