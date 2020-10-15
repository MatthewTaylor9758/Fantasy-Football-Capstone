from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint
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

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'commish_id': self.commish_id
    }

  # Set up many-to-one -> many-teams

class Team(db.Model):
  __tablename__ = 'teams'
  __table_args__ = (
    # This is needed for the foreign key in the FFSplayer table
    UniqueConstraint('id', 'league_id', name = 'team_league_uidx'),
  )

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  league_id = db.Column(db.Integer, db.ForeignKey('leagues.id'))

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'owner_id': self.owner_id,
      'league_id': self.league_id
    }

  # Set up many-to-one -> many-FFSplayers

class Player(db.Model):
  __tablename__ = 'players'

  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  full_name = db.Column(db.String(100), nullable = False, unique = True)
  first_name = db.Column(db.String(50), nullable = False)
  last_name = db.Column(db.String(50), nullable = False)
  nfl_team = db.Column(db.String(100), nullable = False)
  position = db.Column(db.String(5), nullable = False)
  height = db.Column(db.String(10))
  weight = db.Column(db.String(10))
  dob = db.Column(db.String(50))
  college = db.Column(db.String(100))

  def to_dict(self):
    return {
      'id': self.id,
      'full_name': self.full_name,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'nfl_team': self.nfl_team,
      'position': self.position,
      'height': self.height,
      'weight': self.weight,
      'dob': self.dob,
      'college': self.college
    }

class FFSplayer(db.Model):
  __tablename__ = 'ffsplayers'
  __table_args__ = (
    ForeignKeyConstraint(['team_id', 'league_id'], ['teams.id', 'teams.league_id'], name='team_league_fk'),
    UniqueConstraint('player_id', 'league_id', name='player_in_league_only_once_uidx')
  )
  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable = False)
  team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = False)
  league_id = db.Column(db.Integer, nullable = False)

  def to_dict(self):
    return {
      'id': self.id,
      'player_id': self.player_id,
      'team_id': self.team_id,
      'league_id': self.league_id
    }
