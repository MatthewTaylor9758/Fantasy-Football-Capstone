from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(100), nullable = False)

  # Set up many-to-one -> many-teams
  # Set up many-to-one -> many-leagues POSSIBLY

  def to_dict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email
    }

  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)

class League(db.Model):
  __tablename__ = 'leagues'

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  commish_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  # Set up many-to-one -> many-teams

class Team(db.Model):
  __tablename__ = 'teams'

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  league_id = db.Column(db.Integer, db.ForeignKey('leagues.id'))

  # Set up many-to-one -> many-FFSplayers

class Player(db.Model):
  __tablename__ = 'players'

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  full_name = db.Column(db.String(100), nullable = False, unique = True)
  first_name = db.Column(db.String(50), nullable = False)
  last_name = db.Column(db.String(50), nullable = False)
  nfl_team = db.Column(db.String(100), nullable = False)
  position = db.Column(db.String(5), nullable = False)
  height = db.Column(db.String(10), nullable = False)
  weight = db.Column(db.String(10), nullable = False)
  dob = db.Column(db.Date, nullable = False)
  college = db.Column(db.String(100), nullable = False)

class FFSplayer(db.Model):
  __tablename__ = 'ffsplayers'

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
  team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
