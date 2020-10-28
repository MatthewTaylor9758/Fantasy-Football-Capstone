import os
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_migrate import Migrate
# from flask_login import LoginManager, current_user

from .models import db, User, Player, FFSplayer, Team, League
from .api.user_routes import user_routes
from .api.ffsplayer_routes import ffsplayers_routes
from .api.league_routes import league_routes
from .api.player_routes import player_routes
from .api.team_routes import team_routes
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(ffsplayers_routes, url_prefix='/api/ffsplayers')
app.register_blueprint(league_routes, url_prefix='/api/leagues')
app.register_blueprint(player_routes, url_prefix='/api/players')
app.register_blueprint(team_routes, url_prefix='/api/teams')
db.init_app(app)
Migrate(app, db)

# from migrate.changeset.constraint import ForeignKeyConstraint
## Application Security
CORS(app)
@app.after_request
def inject_csrf_token(response):
    response.set_cookie('csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') else False,
        samesite='Strict' if os.environ.get('FLASK_ENV') else None,
        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    print("path", path)
    if path == 'favicon.ico':
        print("favicon route_____")
        return app.send_static_file('favicon.ico')
    print("index route_____")
    return app.send_static_file('index.html')

# login = LoginManager(app)
# login.login_view = "users.login"

# @login.user_loader
# def load_user(id):
#     user = User.query.filter(User.id == id).first()
#     return user
