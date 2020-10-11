from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import User, League, Team, Player, FFSplayer

with app.app_context():
  db.drop_all()
  db.create_all()

  ian = User(username = 'Ian', email = 'ian@aa.io', password= 'password')
  javier = User(username = 'Javier', email = 'javier@aa.io', password= 'password')
  dean = User(username = 'Dean', email = 'dean@aa.io', password= 'password')
  angela = User(username = 'Angela', email = 'angela@aa.io', password= 'password')
  soonmi = User(username = 'Soon-Mi', email = 'soonmi@aa.io', password= 'password')
  alissa = User(username = 'Alissa', email = 'alissa@aa.io', password= 'password')

  ian_league = League(name = 'Ian\'s League', commish_id = 1)
  javier_league = League(name = 'Javier\'s League', commish_id = 2)

  ian_team = Team(name = 'Ian\'s Team', owner_id = 1, league_id = 1)
  javier_team = Team(name = "Javier's Team", owner_id = 2, league_id = 2)
  angela_team = Team(name = "Angela's Team", owner_id = 4, league_id = 1)

  # Spot for players' seeders

  # Spot for ffsplayers' seeders

  db.session.add(ian)
  db.session.add(javier)
  db.session.add(dean)
  db.session.add(angela)
  db.session.add(soonmi)
  db.session.add(alissa)

  db.session.commit()

  db.session.add(ian_league)
  db.session.add(javier_league)
  db.session.commit()

  db.session.add(ian_team)
  db.session.add(javier_team)
  db.session.add(angela_team)

  db.session.commit()
