from flask import Blueprint, jsonify, url_for, request, redirect, render_template
from app.models import League, db

league_routes = Blueprint('leagues', __name__)

@league_routes.route('/:leagueId', method=['PUT'])
def get_league():
  data = request.json
  league = League.query.filter(League.id == data['league_id']).first()
  league_dict = league.to_dict()

@league_routes.route('/', ['POST'])
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
