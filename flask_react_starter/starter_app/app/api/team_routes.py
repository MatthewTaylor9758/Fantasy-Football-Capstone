from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import Team, League, db

team_routes = Blueprint('teams', __name__)

@team_routes.route('/')
def get_teams():
  response == Team.query.all()
  return { 'teams': [user.to_dict() for user in response]}

@team_routes.route('/<teamId>', method=['PUT']) # This route will be triggered by a login, or a return to the my-team page
def get_single_team():
  data = request.json
  team = Team.query.filter(Team.owner_id == data['id']).first()
  team_dict = team.to_dict()
  return {'team': team_dict}

@team_routes.route('/', method=['DELETE'])
def remove_team_from_league():
  data = request.json
  # leagues = Team.query.filter(Team.league_id == data['league_id']).all()
  # team = [team for team in leagues if team.id == data['id']]
  data['league_id'] = None
  return data
