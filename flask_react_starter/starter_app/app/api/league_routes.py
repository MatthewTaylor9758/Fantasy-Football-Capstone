from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import League, Team, db

league_routes = Blueprint('leagues', __name__)

@league_routes.route('/<leagueId>', methods=['PUT'])
def get_league(leagueId):
  data = request.json
  league = League.query.filter(League.id == leagueId).first()
  if league:
    league_dict = league.to_dict()
    return {'league': league_dict}
  else:
    return {'league': {'name': 'No League Yet'}}

@league_routes.route('/', methods=['POST'])
def create_league():
  data = request.json
  errors = {}
  league_exists = League.query.filter(League.name == data['name']).first()
  if league_exists:
    errors['1'] = 'The league name you requested already exists. Please pick a different one.'
    return {'errors': errors}
  new_league = League(
    name = data['name'],
    commish_id = data['commish_id']
  )
  db.session.add(new_league)
  db.session.commit()
  league_dict = league.to_dict()
  return {'league': league_dict}

@league_routes.route('/<teamId>', methods=['PUT'])
def add_team_to_league():
  data = request.json
  number_of_teams = Team.query.filter(Team.league_id == data['requested_league'])
  if number_of_teams < 12:
    data['league_id'] = data['requested_league']
  return data
