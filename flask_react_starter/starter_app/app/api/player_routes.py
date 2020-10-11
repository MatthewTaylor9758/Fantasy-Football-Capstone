from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import Player, db

player_routes = Blueprint('players', __name__)

@player_routes.route('/')
def get_all_players():
  response = Player.query.all()
  return {'players': [player.to_dict() for player in response]}

@player_routes.route('/<playerId>', methods=['PUT'])
def get_single_player():
  data = request.json
  player = Player.query.filter(Player.id == data['player_id'])
  player_dict = player.to_dict()
  return {'player': player_dict}
