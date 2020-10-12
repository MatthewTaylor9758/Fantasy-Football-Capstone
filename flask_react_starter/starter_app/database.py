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
        # {
        #     "playerId": "13",
        #     "jersey": "12",
        #     "last_name": "Brady",
        #     "first_name": "Tom",
        #     "full_name": "Tom Brady",
        #     "nfl_team": "TB",
        #     "position": "QB",
        #     "height": "6-4",
        #     "weight": "225",
        #     "dob": "1977-08-03",
        #     "college": "Michigan"
        # }
        # {
        #     "playerId": "14",
        #     "jersey": "9",
        #     "last_name": "Brees",
        #     "first_name": "Drew",
        #     "full_name": "Drew Brees",
        #     "nfl_team": "NO",
        #     "position": "QB",
        #     "height": "6-0",
        #     "weight": "209",
        #     "dob": "1979-01-15",
        #     "college": "Purdue"
        # }
        # {
        #     "playerId": "3379",
        #     "jersey": "22",
        #     "last_name": "McCaffrey",
        #     "first_name": "Christian",
        #     "full_name": "Christian McCaffrey",
        #     "nfl_team": "CAR",
        #     "position": "RB",
        #     "height": "5-11",
        #     "weight": "205",
        #     "dob": "1996-06-07",
        #     "college": "Stanford"
        # }
        # {
        #     "playerId": "3354",
        #     "jersey": "33",
        #     "last_name": "Cook",
        #     "first_name": "Dalvin",
        #     "full_name": "Dalvin Cook",
        #     "nfl_team": "MIN",
        #     "position": "RB",
        #     "height": "5-10",
        #     "weight": "210",
        #     "dob": "1995-08-10",
        #     "college": "Florida State"
        # }
        # {
        #     "playerId": "2338",
        #     "jersey": "10",
        #     "last_name": "Hopkins",
        #     "first_name": "DeAndre",
        #     "full_name": "DeAndre Hopkins",
        #     "nfl_team": "ARI",
        #     "position": "WR",
        #     "height": "6-1",
        #     "weight": "212",
        #     "dob": "1992-06-06",
        #     "college": "Clemson"
        # }
        # {
        #     "playerId": "1446",
        #     "jersey": "11",
        #     "last_name": "Jones",
        #     "first_name": "Julio",
        #     "full_name": "Julio Jones",
        #     "nfl_team": "ATL",
        #     "position": "WR",
        #     "height": "6-3",
        #     "weight": "220",
        #     "dob": "1989-02-08",
        #     "college": "Alabama"
        # }
        # {
        #     "playerId": "2596",
        #     "jersey": "17",
        #     "last_name": "Adams",
        #     "first_name": "Davante",
        #     "full_name": "Davante Adams",
        #     "nfl_team": "GB",
        #     "position": "WR",
        #     "height": "6-1",
        #     "weight": "215",
        #     "dob": "1992-12-24",
        #     "college": "Fresno State"
        # }
      #  {
      #       "playerId": "2198",

      #       "jersey": "87",
      #       "last_name": "Kelce",
      #       "first_name": "Travis",
      #       "full_name": "Travis Kelce",
      #       "nfl_team": "KC",
      #       "position": "TE",
      #       "height": "6-5",
      #       "weight": "260",
      #       "dob": "1989-10-05",
      #       "college": "Cincinnati"
      #   }
      #   {
      #       "playerId": "1189",

      #       "jersey": "87",
      #       "last_name": "Gronkowski",
      #       "first_name": "Rob",
      #       "full_name": "Rob Gronkowski",
      #       "nfl_team": "TB",
      #       "position": "TE",
      #       "height": "6-6",
      #       "weight": "265",
      #       "dob": "1989-05-14",
      #       "college": "Arizona"
      #   }
      #   {
      #       "playerId": "2079",

      #       "jersey": "9",
      #       "last_name": "Tucker",
      #       "first_name": "Justin",
      #       "full_name": "Justin Tucker",
      #       "nfl_team": "BAL",
      #       "position": "K",
      #       "height": "6-1",
      #       "weight": "183",
      #       "dob": "1989-11-21",
      #       "college": "Texas"
      #   }
      #  {
      #       "playerId": "769",

      #       "jersey": "5",
      #       "last_name": "Prater",
      #       "first_name": "Matt",
      #       "full_name": "Matt Prater",
      #       "nfl_team": "DET",
      #       "position": "K",
      #       "height": "5-10",
      #       "weight": "201",
      #       "dob": "1984-08-10",
      #       "college": "Central Florida"
      #   }
        # {
        #     "playerId": "1037",
        #     "jersey": "0",
        #     "last_name": "Steelers",
        #     "first_name": "Pittsburgh",
        #     "full_name": "Pittsburgh Steelers",
        #     "nfl_team": "PIT",
        #     "position": "DEF",
        #     "height": "",
        #     "weight": "",
        #     "dob": "0000-00-00",
        #     "college": ""
        # }
        # {
        #     "playerId": "1038",
        #     "jersey": "0",
        #     "last_name": "Ravens",
        #     "first_name": "Baltimore",
        #     "full_name": "Baltimore Ravens",
        #     "nfl_team": "BAL",
        #     "position": "DEF",
        #     "height": "",
        #     "weight": "",
        #     "dob": "0000-00-00",
        #     "college": ""
        # }




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
