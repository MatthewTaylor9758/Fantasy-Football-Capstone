from flask import Blueprint, jsonify, url_for, request, redirect, render_template
# from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.models import User

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
  user_dict = user.to_dict()
  # login_user(user)
  return {'user': user_dict}
