from flask import Blueprint, jsonify, url_for, request, redirect, render_template
# from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.models import User, db

user_routes = Blueprint('users', __name__)

# @user_routes.route("/current_user")
# def cur_user():
#     if current_user.is_authenticated:
#         user = current_user.to_dict()
#         return {"user": user }

@user_routes.route('/')
def index():
  response = User.query.all()
  print("user route______")
  return { "users": [user.to_dict() for user in response]}

@user_routes.route('/', methods=['PUT'])
def login():
  data = request.json
  if not data:
    return {'errors': ''}
  user = User.query.filter(User.username == data['username']).first()
  if user and user.check_password(data['password']):
    user_dict = user.to_dict()
    # login_user(user)
    return {'user': user_dict}
  else:
    error = {"1":"Incorrect password or username"}
    return {"errors":error}

@user_routes.route('/', methods=['POST'])
def signup():
  data = request.json
  errors = {}
  username_exists = User.query.filter(User.username == data['username']).first()
  email_exists = User.query.filter(User.email == data['email']).first()
  if username_exists:
    errors['1'] = 'That username is unavailable.'
  if email_exists:
    errors['2'] = 'That email is unavailable.'
  if errors:
    return {'errors': errors}
  new_user = User(
    username = data['username'],
    email = data['email'],
    password = data['password']
  )
  db.session.add(new_user)
  db.session.commit()
  user_dict = new_user.to_dict()
  return {'user': user_dict}
