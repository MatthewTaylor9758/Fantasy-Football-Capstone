from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import Player, FFSplayer, db

player_routes = Blueprint('players', __name__)

@player_routes.route('/<leagueId>')
def get_all_players(leagueId):
  ffsplayers = FFSplayer.query.filter(FFSplayer.league_id == int(leagueId)).all()
  ffsplayers_ids = [ffsplayer.to_dict()['player_id'] for ffsplayer in ffsplayers]
  response = Player.query.filter(Player.player_id.notin_(ffsplayers_ids)).all()
  # print('**********$$$$$$$$$', ffsplayers_dict)
  # response = Player.query.all()
  return {'players': [player.to_dict() for player in response]}

@player_routes.route('/<leagueId>/<position>')
def get_position_players(leagueId, position):
  ffsplayers = FFSplayer.query.filter(FFSplayer.league_id == int(leagueId)).all()
  ffsplayers_ids = [ffsplayer.to_dict()['player_id'] for ffsplayer in ffsplayers]
  response = Player.query.filter(Player.player_id.notin_(ffsplayers_ids), Player.position == position).all()
  # response = Player.query.filter(Player.position == position)
  return {'players': [player.to_dict() for player in response]}

@player_routes.route('/<playerId>', methods=['PUT'])
def get_single_player():
  data = request.json
  player = Player.query.filter(Player.id == data['player_id'])
  player_dict = player.to_dict()
  return {'player': player_dict}
