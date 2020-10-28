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
  javier_team = Team(name = "Javier's Team", owner_id = 2, league_id = 1)
  angela_team = Team(name = "Angela's Team", owner_id = 4, league_id = 2)

  # player_13 = Player(
  #           player_id = 13,
  #           full_name = "Tom Brady",
  #           first_name = "Tom",
  #           last_name = "Brady",
  #           nfl_team = "TB",
  #           position = "QB",
  #           height = "6-4",
  #           weight = "225",
  #           dob = "1977-08-03",
  #           college = "Michigan"
  # )
  # player_3379 = Player(
  #           player_id = 3379,
  #           full_name = "Christian McCaffrey",
  #           first_name = "Christian",
  #           last_name = "McCaffrey",
  #           nfl_team = "CAR",
  #           position = "RB",
  #           height = "5-11",
  #           weight = "205",
  #           dob = "1996-06-07",
  #           college = "Stanford"
  # )
  # player_14 = Player(
  #           player_id= 14,
  #           full_name = "Drew Brees",
  #           last_name = "Brees",
  #           first_name = "Drew",
  #           nfl_team = "NO",
  #           position = "QB",
  #           height = "6-0",
  #           weight = "209",
  #           dob = "1979-01-15",
  #           college = "Purdue"
  # )
  # player_3354 = Player(
  #           player_id = 3354,
  #           full_name = "Dalvin Cook",
  #           last_name = "Cook",
  #           first_name = "Dalvin",
  #           nfl_team = "MIN",
  #           position = "RB",
  #           height = "5-10",
  #           weight = "210",
  #           dob = "1995-08-10",
  #           college = "Florida State"
  # )
  # player_2338 = Player(
  #           player_id = 2338,
  #           full_name = "DeAndre Hopkins",
  #           last_name = "Hopkins",
  #           first_name = "DeAndre",
  #           nfl_team = "ARI",
  #           position = "WR",
  #           height = "6-1",
  #           weight = "212",
  #           dob = "1992-06-06",
  #           college = "Clemson"
  # )
  # player_1446 = Player(
  #           player_id = 1446,
  #           full_name = "Julio Jones",
  #           last_name = "Jones",
  #           first_name = "Julio",
  #           nfl_team = "ATL",
  #           position = "WR",
  #           height = "6-3",
  #           weight = "220",
  #           dob = "1989-02-08",
  #           college = "Alabama"
  # )
  # player_2596 = Player(
  #           player_id = 2596,
  #           full_name = "Davante Adams",
  #           last_name = "Adams",
  #           first_name = "Davante",
  #           nfl_team = "GB",
  #           position = "WR",
  #           height = "6-1",
  #           weight = "215",
  #           dob = "1992-12-24",
  #           college = "Fresno State"
  # )
  # player_2198 = Player(
  #           player_id = 2198,
  #           full_name = "Travis Kelce",
  #           last_name = "Kelce",
  #           first_name = "Travis",
  #           nfl_team = "KC",
  #           position = "TE",
  #           height = "6-5",
  #           weight = "260",
  #           dob = "1989-10-05",
  #           college = "Cincinnati"
  # )
  # player_1189 = Player(
  #           player_id = 1189,
  #           full_name = "Rob Gronkowski",
  #           last_name = "Gronkowski",
  #           first_name = "Rob",
  #           nfl_team = "TB",
  #           position = "TE",
  #           height = "6-6",
  #           weight = "265",
  #           dob = "1989-05-14",
  #           college = "Arizona"
  # )
  # player_2079 = Player(
  #           player_id = 2079,
  #           full_name = "Justin Tucker",
  #           last_name = "Tucker",
  #           first_name = "Justin",
  #           nfl_team = "BAL",
  #           position = "K",
  #           height = "6-1",
  #           weight = "183",
  #           dob = "1989-11-21",
  #           college = "Texas"
  # )
  # player_769 = Player(
  #           player_id = 769,
  #           full_name = "Matt Prater",
  #           last_name = "Prater",
  #           first_name = "Matt",
  #           nfl_team = "DET",
  #           position = "K",
  #           height = "5-10",
  #           weight = "201",
  #           dob = "1984-08-10",
  #           college = "Central Florida"
  # )
  # player_1037 = Player(
  #           player_id = 1037,
  #           full_name = "Pittsburgh Steelers",
  #           last_name = "Steelers",
  #           first_name = "Pittsburgh",
  #           nfl_team = "PIT",
  #           position = "DEF",
  #           height = "",
  #           weight = "",
  #           dob = "0000-00-00",
  #           college = ""
  # )
  # player_1038 = Player(
  #           player_id = 1038,
  #           full_name = "Baltimore Ravens",
  #           last_name = "Ravens",
  #           first_name = "Baltimore",
  #           nfl_team = "BAL",
  #           position = "DEF",
  #           height = "",
  #           weight = "",
  #           dob = "0000-00-00",
  #           college = ""
  # )
  player_3274 = Player(
    player_id = 3274,
    full_name = "Brandon Allen",
    last_name = "Allen",
    first_name = "Brandon",
    nfl_team = "CIN",
    position = "QB",
    height = "6-2",
    weight = "209",
    dob = "1992-09-05",
    college = "Arkansas"
  )

  player_3826 = Player(
    player_id = 3826,
    full_name = "Kyle Allen",
    last_name = "Allen",
    first_name = "Kyle",
    nfl_team = "WAS",
    position = "QB",
    height = "6-3",
    weight = "211",
    dob = "1996-03-08",
    college = "Houston"
  )

  player_3577 = Player(
    player_id = 3577,
    full_name = "Josh Allen",
    last_name = "Allen",
    first_name = "Josh",
    nfl_team = "BUF",
    position = "QB",
    height = "6-5",
    weight = "237",
    dob = "1996-05-21",
    college = "Wyoming"
  )

  player_3994 = Player(
    player_id = 3994,
    full_name = "Drew Anderson",
    last_name = "Anderson",
    first_name = "Drew",
    nfl_team = "ARI",
    position = "QB",
    height = "6-4",
    weight = "221",
    dob = "1995-10-18",
    college = "Murray State"
  )

  player_2168 = Player(
    player_id = 2168,
    full_name = "Matt Barkley",
    last_name = "Barkley",
    first_name = "Matt",
    nfl_team = "BUF",
    position = "QB",
    height = "6-2",
    weight = "234",
    dob = "1990-09-08",
    college = "Southern California"
  )

  player_3829 = Player(
    player_id = 3829,
    full_name = "J.T. Barrett IV",
    last_name = "Barrett IV",
    first_name = "J.T.",
    nfl_team = "PIT",
    position = "QB",
    height = "6-2",
    weight = "225",
    dob = "1995-01-23",
    college = "Ohio State"
  )

  player_3321 = Player(
    player_id = 3321,
    full_name = "C.J. Beathard",
    last_name = "Beathard",
    first_name = "C.J.",
    nfl_team = "SF",
    position = "QB",
    height = "6-2",
    weight = "215",
    dob = "1993-11-16",
    college = "Iowa"
  )

  player_3814 = Player(
    player_id = 3814,
    full_name = "Kurt Benkert",
    last_name = "Benkert",
    first_name = "Kurt",
    nfl_team = "ATL",
    position = "QB",
    height = "6-4",
    weight = "215",
    dob = "1995-07-17",
    college = "Virginia"
  )

  player_4028 = Player(
    player_id = 4028,
    full_name = "David Blough",
    last_name = "Blough",
    first_name = "David",
    nfl_team = "DET",
    position = "QB",
    height = "6-0",
    weight = "200",
    dob = "1995-07-31",
    college = "Purdue"
  )

  player_3784 = Player(
    player_id = 3784,
    full_name = "Tim Boyle",
    last_name = "Boyle",
    first_name = "Tim",
    nfl_team = "GB",
    position = "QB",
    height = "6-4",
    weight = "233",
    dob = "1994-10-03",
    college = "Eastern Kentucky"
  )

  player_13 = Player(
    player_id = 13,
    full_name = "Tom Brady",
    last_name = "Brady",
    first_name = "Tom",
    nfl_team = "TB",
    position = "QB",
    height = "6-4",
    weight = "225",
    dob = "1977-08-03",
    college = "Michigan"
  )

  player_2191 = Player(
    player_id = 2191,
    full_name = "Tyler Bray",
    last_name = "Bray",
    first_name = "Tyler",
    nfl_team = "CHI",
    position = "QB",
    height = "6-6",
    weight = "223",
    dob = "1991-12-27",
    college = "Tennessee"
  )

  player_14 = Player(
    player_id = 14,
    full_name = "Drew Brees",
    last_name = "Brees",
    first_name = "Drew",
    nfl_team = "NO",
    position = "QB",
    height = "6-0",
    weight = "209",
    dob = "1979-01-15",
    college = "Purdue"
  )

  player_2601 = Player(
    player_id = 2601,
    full_name = "Teddy Bridgewater",
    last_name = "Bridgewater",
    first_name = "Teddy",
    nfl_team = "CAR",
    position = "QB",
    height = "6-2",
    weight = "215",
    dob = "1992-11-10",
    college = "Louisville"
  )

  player_3030 = Player(
    player_id = 3030,
    full_name = "Jacoby Brissett",
    last_name = "Brissett",
    first_name = "Jacoby",
    nfl_team = "IND",
    position = "QB",
    height = "6-4",
    weight = "235",
    dob = "1992-12-11",
    college = "North Carolina State"
  )

  player_4049 = Player(
    player_id = 4049,
    full_name = "Jake Browning",
    last_name = "Browning",
    first_name = "Jake",
    nfl_team = "MIN",
    position = "QB",
    height = "6-2",
    weight = "209",
    dob = "1996-04-11",
    college = "Washington"
  )

  player_4139 = Player(
    player_id = 4139,
    full_name = "Joe Burrow",
    last_name = "Burrow",
    first_name = "Joe",
    nfl_team = "CIN",
    position = "QB",
    height = "6-4",
    weight = "216",
    dob = "1996-12-10",
    college = "Louisiana State"
  )

  player_2503 = Player(
    player_id = 2503,
    full_name = "Derek Carr",
    last_name = "Carr",
    first_name = "Derek",
    nfl_team = "LV",
    position = "QB",
    height = "6-3",
    weight = "210",
    dob = "1991-03-28",
    college = "Fresno State"
  )

  player_4206 = Player(
    player_id = 4206,
    full_name = "Case Cookus",
    last_name = "Cookus",
    first_name = "Case",
    nfl_team = "NYG",
    position = "QB",
    height = "6-4",
    weight = "205",
    dob = "1995-10-06",
    college = "Northern Arizona"
  )

  player_1805 = Player(
    player_id = 1805,
    full_name = "Kirk Cousins",
    last_name = "Cousins",
    first_name = "Kirk",
    nfl_team = "MIN",
    position = "QB",
    height = "6-3",
    weight = "202",
    dob = "1988-08-19",
    college = "Michigan State"
  )

  player_1391 = Player(
    player_id = 1391,
    full_name = "Andy Dalton",
    last_name = "Dalton",
    first_name = "Andy",
    nfl_team = "DAL",
    position = "QB",
    height = "6-2",
    weight = "220",
    dob = "1987-10-29",
    college = "Texas Christian"
  )

  player_786 = Player(
    player_id = 786,
    full_name = "Chase Daniel",
    last_name = "Daniel",
    first_name = "Chase",
    nfl_team = "DET",
    position = "QB",
    height = "6-0",
    weight = "229",
    dob = "1986-10-07",
    college = "Missouri"
  )

  player_3580 = Player(
    player_id = 3580,
    full_name = "Sam Darnold",
    last_name = "Darnold",
    first_name = "Sam",
    nfl_team = "NYJ",
    position = "QB",
    height = "6-3",
    weight = "225",
    dob = "1997-06-05",
    college = "Southern California"
  )

  player_4298 = Player(
    player_id = 4298,
    full_name = "Kevin Davidson",
    last_name = "Davidson",
    first_name = "Kevin",
    nfl_team = "CLE",
    position = "QB",
    height = "6-4",
    weight = "225",
    dob = "1997-08-01",
    college = "Princeton"
  )

  player_4198 = Player(
    player_id = 4198,
    full_name = "Ben DiNucci",
    last_name = "DiNucci",
    first_name = "Ben",
    nfl_team = "DAL",
    position = "QB",
    height = "6-3",
    weight = "210",
    dob = "1996-11-24",
    college = "James Madison"
  )

  player_3338 = Player(
    player_id = 3338,
    full_name = "Joshua Dobbs",
    last_name = "Dobbs",
    first_name = "Joshua",
    nfl_team = "PIT",
    position = "QB",
    height = "6-3",
    weight = "216",
    dob = "1995-01-26",
    college = "Tennessee"
  )

  player_4022 = Player(
    player_id = 4022,
    full_name = "Jacob Dolegala",
    last_name = "Dolegala",
    first_name = "Jacob",
    nfl_team = "CIN",
    position = "QB",
    height = "6-7",
    weight = "242",
    dob = "1996-10-07",
    college = "Central Connecticut State"
  )

  player_3064 = Player(
    player_id = 3064,
    full_name = "Jeff Driskel",
    last_name = "Driskel",
    first_name = "Jeff",
    nfl_team = "DEN",
    position = "QB",
    height = "6-4",
    weight = "235",
    dob = "1993-04-23",
    college = "Louisiana Tech"
  )

  player_4174 = Player(
    player_id = 4174,
    full_name = "Jacob Eason",
    last_name = "Eason",
    first_name = "Jacob",
    nfl_team = "IND",
    position = "QB",
    height = "6-6",
    weight = "227",
    dob = "1997-11-17",
    college = "Washington"
  )

  player_3623 = Player(
    player_id = 3623,
    full_name = "Danny Etling",
    last_name = "Etling",
    first_name = "Danny",
    nfl_team = "SEA",
    position = "QB",
    height = "6-3",
    weight = "220",
    dob = "1994-07-22",
    college = "Louisiana State"
  )

  player_2578 = Player(
    player_id = 2578,
    full_name = "David Fales",
    last_name = "Fales",
    first_name = "David",
    nfl_team = "NYJ",
    position = "QB",
    height = "6-1",
    weight = "219",
    dob = "1990-10-04",
    college = "San Jose State"
  )

  player_3911 = Player(
    player_id = 3911,
    full_name = "Ryan Finley",
    last_name = "Finley",
    first_name = "Ryan",
    nfl_team = "CIN",
    position = "QB",
    height = "6-4",
    weight = "207",
    dob = "1994-12-26",
    college = "North Carolina State"
  )

  player_34 = Player(
    player_id = 34,
    full_name = "Ryan Fitzpatrick",
    last_name = "Fitzpatrick",
    first_name = "Ryan",
    nfl_team = "MIA",
    position = "QB",
    height = "6-2",
    weight = "228",
    dob = "1982-11-24",
    college = "Harvard"
  )

  player_35 = Player(
    player_id = 35,
    full_name = "Joe Flacco",
    last_name = "Flacco",
    first_name = "Joe",
    nfl_team = "NYJ",
    position = "QB",
    height = "6-6",
    weight = "245",
    dob = "1985-01-16",
    college = "Delaware"
  )

  player_1801 = Player(
    player_id = 1801,
    full_name = "Nick Foles",
    last_name = "Foles",
    first_name = "Nick",
    nfl_team = "CHI",
    position = "QB",
    height = "6-6",
    weight = "243",
    dob = "1989-01-20",
    college = "Arizona"
  )

  player_4181 = Player(
    player_id = 4181,
    full_name = "Jake Fromm",
    last_name = "Fromm",
    first_name = "Jake",
    nfl_team = "BUF",
    position = "QB",
    height = "6-2",
    weight = "222",
    dob = "1998-07-30",
    college = "Georgia"
  )

  player_1393 = Player(
    player_id = 1393,
    full_name = "Blaine Gabbert",
    last_name = "Gabbert",
    first_name = "Blaine",
    nfl_team = "TB",
    position = "QB",
    height = "6-4",
    weight = "235",
    dob = "1989-10-15",
    college = "Missouri"
  )

  player_2441 = Player(
    player_id = 2441,
    full_name = "Jimmy Garoppolo",
    last_name = "Garoppolo",
    first_name = "Jimmy",
    nfl_team = "SF",
    position = "QB",
    height = "6-2",
    weight = "225",
    dob = "1991-11-02",
    college = "Eastern Illinois"
  )

  player_2540 = Player(
    player_id = 2540,
    full_name = "Garrett Gilbert",
    last_name = "Gilbert",
    first_name = "Garrett",
    nfl_team = "DAL",
    position = "QB",
    height = "6-4",
    weight = "230",
    dob = "1991-07-01",
    college = "Southern Methodist"
  )

  player_2392 = Player(
    player_id = 2392,
    full_name = "Mike Glennon",
    last_name = "Glennon",
    first_name = "Mike",
    nfl_team = "JAC",
    position = "QB",
    height = "6-7",
    weight = "225",
    dob = "1989-12-12",
    college = "North Carolina State"
  )

  player_3072 = Player(
    player_id = 3072,
    full_name = "Jared Goff",
    last_name = "Goff",
    first_name = "Jared",
    nfl_team = "LAR",
    position = "QB",
    height = "6-4",
    weight = "223",
    dob = "1994-10-14",
    college = "California"
  )

  player_4266 = Player(
    player_id = 4266,
    full_name = "Anthony Gordon",
    last_name = "Gordon",
    first_name = "Anthony",
    nfl_team = "SEA",
    position = "QB",
    height = "6-2",
    weight = "201",
    dob = "1996-08-28",
    college = "Washington State"
  )

  player_3942 = Player(
    player_id = 3942,
    full_name = "Will Grier",
    last_name = "Grier",
    first_name = "Will",
    nfl_team = "CAR",
    position = "QB",
    height = "6-1",
    weight = "220",
    dob = "1995-04-03",
    college = "West Virginia"
  )

  player_1806 = Player(
    player_id = 1806,
    full_name = "Robert Griffin III",
    last_name = "Griffin",
    first_name = "Robert",
    nfl_team = "BAL",
    position = "QB",
    height = "6-2",
    weight = "213",
    dob = "1990-02-12",
    college = "Baylor"
  )

  player_2385 = Player(
    player_id = 2385,
    full_name = "Ryan Griffin",
    last_name = "Griffin",
    first_name = "Ryan",
    nfl_team = "TB",
    position = "QB",
    height = "6-5",
    weight = "210",
    dob = "1989-11-17",
    college = "Tulane"
  )

  player_3873 = Player(
    player_id = 3873,
    full_name = "Dwayne Haskins",
    last_name = "Haskins",
    first_name = "Dwayne",
    nfl_team = "WAS",
    position = "QB",
    height = "6-4",
    weight = "230",
    dob = "1997-05-03",
    college = "Ohio State"
  )

  player_52 = Player(
    player_id = 52,
    full_name = "Chad Henne",
    last_name = "Henne",
    first_name = "Chad",
    nfl_team = "KC",
    position = "QB",
    height = "6-3",
    weight = "222",
    dob = "1985-07-02",
    college = "Michigan"
  )

  player_4135 = Player(
    player_id = 4135,
    full_name = "Justin Herbert",
    last_name = "Herbert",
    first_name = "Justin",
    nfl_team = "LAC",
    position = "QB",
    height = "6-6",
    weight = "237",
    dob = "1998-03-10",
    college = "Oregon"
  )

  player_3441 = Player(
    player_id = 3441,
    full_name = "Taysom Hill",
    last_name = "Hill",
    first_name = "Taysom",
    nfl_team = "NO",
    position = "QB",
    height = "6-2",
    weight = "221",
    dob = "1990-08-23",
    college = "Brigham Young"
  )

  player_4034 = Player(
    player_id = 4034,
    full_name = "Devlin Hodges",
    last_name = "Hodges",
    first_name = "Devlin",
    nfl_team = "PIT",
    position = "QB",
    height = "6-1",
    weight = "210",
    dob = "1996-04-12",
    college = "Samford"
  )

  player_901 = Player(
    player_id = 901,
    full_name = "Brian Hoyer",
    last_name = "Hoyer",
    first_name = "Brian",
    nfl_team = "NE",
    position = "QB",
    height = "6-2",
    weight = "215",
    dob = "1985-10-13",
    college = "Michigan State"
  )

  player_2790 = Player(
    player_id = 2790,
    full_name = "Brett Hundley",
    last_name = "Hundley",
    first_name = "Brett",
    nfl_team = "ARI",
    position = "QB",
    height = "6-3",
    weight = "226",
    dob = "1993-06-15",
    college = "UCLA"
  )

  player_4286 = Player(
    player_id = 4286,
    full_name = "Tyler Huntley",
    last_name = "Huntley",
    first_name = "Tyler",
    nfl_team = "BAL",
    position = "QB",
    height = "6-1",
    weight = "205",
    dob = "1998-02-03",
    college = "Utah"
  )

  player_4154 = Player(
    player_id = 4154,
    full_name = "Jalen Hurts",
    last_name = "Hurts",
    first_name = "Jalen",
    nfl_team = "PHI",
    position = "QB",
    height = "6-2",
    weight = "218",
    dob = "1998-08-07",
    college = "Oklahoma"
  )

  player_3596 = Player(
    player_id = 3596,
    full_name = "Lamar Jackson",
    last_name = "Jackson",
    first_name = "Lamar",
    nfl_team = "BAL",
    position = "QB",
    height = "6-2",
    weight = "212",
    dob = "1997-01-07",
    college = "Louisville"
  )

  player_3868 = Player(
    player_id = 3868,
    full_name = "Daniel Jones",
    last_name = "Jones",
    first_name = "Daniel",
    nfl_team = "NYG",
    position = "QB",
    height = "6-5",
    weight = "220",
    dob = "1997-05-27",
    college = "Duke"
  )

  player_1926 = Player(
    player_id = 1926,
    full_name = "Case Keenum",
    last_name = "Keenum",
    first_name = "Case",
    nfl_team = "CLE",
    position = "QB",
    height = "6-1",
    weight = "215",
    dob = "1988-02-17",
    college = "Houston"
  )

  player_3304 = Player(
    player_id = 3304,
    full_name = "Chad Kelly",
    last_name = "Kelly",
    first_name = "Chad",
    nfl_team = "IND",
    position = "QB",
    height = "6-2",
    weight = "216",
    dob = "1994-03-26",
    college = "Mississippi"
  )

  player_3334 = Player(
    player_id = 3334,
    full_name = "DeShone Kizer",
    last_name = "Kizer",
    first_name = "DeShone",
    nfl_team = "LV",
    position = "QB",
    height = "6-4",
    weight = "233",
    dob = "1996-01-03",
    college = "Notre Dame"
  )

  player_3632 = Player(
    player_id = 3632,
    full_name = "Kyle Lauletta",
    last_name = "Lauletta",
    first_name = "Kyle",
    nfl_team = "ATL",
    position = "QB",
    height = "6-2",
    weight = "222",
    dob = "1995-03-17",
    college = "Richmond"
  )

  player_4189 = Player(
    player_id = 4189,
    full_name = "Brian Lewerke",
    last_name = "Lewerke",
    first_name = "Brian",
    nfl_team = "NE",
    position = "QB",
    height = "6-3",
    weight = "216",
    dob = "1996-10-24",
    college = "Michigan State"
  )

  player_3879 = Player(
    player_id = 3879,
    full_name = "Drew Lock",
    last_name = "Lock",
    first_name = "Drew",
    nfl_team = "DEN",
    position = "QB",
    height = "6-4",
    weight = "228",
    dob = "1996-11-10",
    college = "Missouri"
  )

  player_4142 = Player(
    player_id = 4142,
    full_name = "Jordan Love",
    last_name = "Love",
    first_name = "Jordan",
    nfl_team = "GB",
    position = "QB",
    height = "6-4",
    weight = "220",
    dob = "1998-11-02",
    college = "Utah State"
  )

  player_4275 = Player(
    player_id = 4275,
    full_name = "Josh Love",
    last_name = "Love",
    first_name = "Josh",
    nfl_team = "LAR",
    position = "QB",
    height = "6-2",
    weight = "203",
    dob = "1996-11-28",
    college = "San Jose"
  )

  player_4333 = Player(
    player_id = 4333,
    full_name = "Jake Luton",
    last_name = "Luton",
    first_name = "Jake",
    nfl_team = "JAC",
    position = "QB",
    height = "6-6",
    weight = "236",
    dob = "1996-04-11",
    college = "Oregon State"
  )

  player_3051 = Player(
    player_id = 3051,
    full_name = "Paxton Lynch",
    last_name = "Lynch",
    first_name = "Paxton",
    nfl_team = "PIT",
    position = "QB",
    height = "6-7",
    weight = "244",
    dob = "1994-02-12",
    college = "Memphis"
  )

  player_3311 = Player(
    player_id = 3311,
    full_name = "Patrick Mahomes",
    last_name = "Mahomes",
    first_name = "Patrick",
    nfl_team = "KC",
    position = "QB",
    height = "6-3",
    weight = "230",
    dob = "1995-09-17",
    college = "Texas Tech"
  )

  player_2770 = Player(
    player_id = 2770,
    full_name = "Sean Mannion",
    last_name = "Mannion",
    first_name = "Sean",
    nfl_team = "MIN",
    position = "QB",
    height = "6-6",
    weight = "231",
    dob = "1992-04-25",
    college = "Oregon State"
  )

  player_2801 = Player(
    player_id = 2801,
    full_name = "Marcus Mariota",
    last_name = "Mariota",
    first_name = "Marcus",
    nfl_team = "LV",
    position = "QB",
    height = "6-4",
    weight = "222",
    dob = "1993-10-30",
    college = "Oregon"
  )

  player_3599 = Player(
    player_id = 3599,
    full_name = "Baker Mayfield",
    last_name = "Mayfield",
    first_name = "Baker",
    nfl_team = "CLE",
    position = "QB",
    height = "6-1",
    weight = "215",
    dob = "1995-04-14",
    college = "Oklahoma"
  )

  player_2554 = Player(
    player_id = 2554,
    full_name = "AJ McCarron",
    last_name = "McCarron",
    first_name = "AJ",
    nfl_team = "HOU",
    position = "QB",
    height = "6-3",
    weight = "220",
    dob = "1990-09-13",
    college = "Alabama"
  )

  player_1116 = Player(
    player_id = 1116,
    full_name = "Colt McCoy",
    last_name = "McCoy",
    first_name = "Colt",
    nfl_team = "NYG",
    position = "QB",
    height = "6-1",
    weight = "212",
    dob = "1986-09-05",
    college = "Texas"
  )

  player_4343 = Player(
    player_id = 4343,
    full_name = "Cole McDonald",
    last_name = "McDonald",
    first_name = "Cole",
    nfl_team = "TEN",
    position = "QB",
    height = "6-3",
    weight = "215",
    dob = "1998-05-20",
    college = "Hawai&#x27;i&#x27;"
  )

  player_3647 = Player(
    player_id = 3647,
    full_name = "Alex McGough",
    last_name = "McGough",
    first_name = "Alex",
    nfl_team = "HOU",
    position = "QB",
    height = "6-3",
    weight = "214",
    dob = "1995-11-19",
    college = "Florida International"
  )

  player_3907 = Player(
    player_id = 3907,
    full_name = "Trace McSorley",
    last_name = "McSorley",
    first_name = "Trace",
    nfl_team = "BAL",
    position = "QB",
    height = "6-0",
    weight = "202",
    dob = "1995-08-23",
    college = "Penn State"
  )

  player_3936 = Player(
    player_id = 3936,
    full_name = "Gardner Minshew",
    last_name = "Minshew",
    first_name = "Gardner",
    nfl_team = "JAC",
    position = "QB",
    height = "6-1",
    weight = "225",
    dob = "1996-05-16",
    college = "Washington State"
  )

  player_4220 = Player(
    player_id = 4220,
    full_name = "Steven Montez",
    last_name = "Montez",
    first_name = "Steven",
    nfl_team = "WAS",
    position = "QB",
    height = "6-5",
    weight = "230",
    dob = "1997-01-14",
    college = "Colorado"
  )

  player_72 = Player(
    player_id = 72,
    full_name = "Matt Moore",
    last_name = "Moore",
    first_name = "Matt",
    nfl_team = "KC",
    position = "QB",
    height = "6-3",
    weight = "219",
    dob = "1984-08-09",
    college = "Oregon State"
  )

  player_4151 = Player(
    player_id = 4151,
    full_name = "James Morgan",
    last_name = "Morgan",
    first_name = "James",
    nfl_team = "NYJ",
    position = "QB",
    height = "6-4",
    weight = "213",
    dob = "1997-02-28",
    college = "Florida International"
  )

  player_4314 = Player(
    player_id = 4314,
    full_name = "Jalen Morton",
    last_name = "Morton",
    first_name = "Jalen",
    nfl_team = "GB",
    position = "QB",
    height = "6-3",
    weight = "237",
    dob = "0000-00-00",
    college = "Prairie View A&amp;M"
  )

  player_3415 = Player(
    player_id = 3415,
    full_name = "Nick Mullens",
    last_name = "Mullens",
    first_name = "Nick",
    nfl_team = "SF",
    position = "QB",
    height = "6-1",
    weight = "210",
    dob = "1995-03-21",
    college = "Southern Mississippi"
  )

  player_3893 = Player(
    player_id = 3893,
    full_name = "Kyler Murray",
    last_name = "Murray",
    first_name = "Kyler",
    nfl_team = "ARI",
    position = "QB",
    height = "5-10",
    weight = "207",
    dob = "1997-08-07",
    college = "Oklahoma"
  )

  player_4225 = Player(
    player_id = 4225,
    full_name = "Riley Neal",
    last_name = "Neal",
    first_name = "Riley",
    nfl_team = "DEN",
    position = "QB",
    height = "6-6",
    weight = "225",
    dob = "1996-10-02",
    college = "Vanderbilt"
  )

  player_1398 = Player(
    player_id = 1398,
    full_name = "Cam Newton",
    last_name = "Newton",
    first_name = "Cam",
    nfl_team = "NE",
    position = "QB",
    height = "6-5",
    weight = "245",
    dob = "1989-05-11",
    college = "Auburn"
  )

  player_4374 = Player(
    player_id = 4374,
    full_name = "Shea Patterson",
    last_name = "Patterson",
    first_name = "Shea",
    nfl_team = "KC",
    position = "QB",
    height = "6-1",
    weight = "212",
    dob = "1997-01-17",
    college = "Michigan"
  )

  player_4276 = Player(
    player_id = 4276,
    full_name = "Bryce Perkins",
    last_name = "Perkins",
    first_name = "Bryce",
    nfl_team = "LAR",
    position = "QB",
    height = "6-3",
    weight = "215",
    dob = "1996-12-20",
    college = "Virginia"
  )

  player_3280 = Player(
    player_id = 3280,
    full_name = "Nathan Peterman",
    last_name = "Peterman",
    first_name = "Nathan",
    nfl_team = "LV",
    position = "QB",
    height = "6-2",
    weight = "225",
    dob = "1994-05-04",
    college = "Pittsburgh"
  )

  player_3036 = Player(
    player_id = 3036,
    full_name = "Dak Prescott",
    last_name = "Prescott",
    first_name = "Dak",
    nfl_team = "DAL",
    position = "QB",
    height = "6-2",
    weight = "238",
    dob = "1993-07-29",
    college = "Mississippi State"
  )

  player_86 = Player(
    player_id = 86,
    full_name = "Philip Rivers",
    last_name = "Rivers",
    first_name = "Philip",
    nfl_team = "IND",
    position = "QB",
    height = "6-5",
    weight = "228",
    dob = "1981-12-08",
    college = "North Carolina State"
  )

  player_87 = Player(
    player_id = 87,
    full_name = "Aaron Rodgers",
    last_name = "Rodgers",
    first_name = "Aaron",
    nfl_team = "GB",
    position = "QB",
    height = "6-2",
    weight = "225",
    dob = "1983-12-02",
    college = "California"
  )

  player_88 = Player(
    player_id = 88,
    full_name = "Ben Roethlisberger",
    last_name = "Roethlisberger",
    first_name = "Ben",
    nfl_team = "PIT",
    position = "QB",
    height = "6-5",
    weight = "240",
    dob = "1982-03-02",
    college = "Miami, O."
  )

  player_3591 = Player(
    player_id = 3591,
    full_name = "Josh Rosen",
    last_name = "Rosen",
    first_name = "Josh",
    nfl_team = "MIA",
    position = "QB",
    height = "6-4",
    weight = "226",
    dob = "1997-02-10",
    college = "UCLA"
  )

  player_3093 = Player(
    player_id = 3093,
    full_name = "Jake Rudock",
    last_name = "Rudock",
    first_name = "Jake",
    nfl_team = "MIA",
    position = "QB",
    height = "6-3",
    weight = "212",
    dob = "1993-01-21",
    college = "Michigan"
  )

  player_3601 = Player(
    player_id = 3601,
    full_name = "Mason Rudolph",
    last_name = "Rudolph",
    first_name = "Mason",
    nfl_team = "PIT",
    position = "QB",
    height = "6-5",
    weight = "235",
    dob = "1995-07-17",
    college = "Oklahoma State"
  )

  player_3478 = Player(
    player_id = 3478,
    full_name = "Cooper Rush",
    last_name = "Rush",
    first_name = "Cooper",
    nfl_team = "NYG",
    position = "QB",
    height = "6-3",
    weight = "225",
    dob = "1993-11-21",
    college = "Central Michigan"
  )

  player_4258 = Player(
    player_id = 4258,
    full_name = "Broc Rutter",
    last_name = "Rutter",
    first_name = "Broc",
    nfl_team = "SF",
    position = "QB",
    height = "6-2",
    weight = "204",
    dob = "1997-04-03",
    college = "North Central"
  )

  player_93 = Player(
    player_id = 93,
    full_name = "Matt Ryan",
    last_name = "Ryan",
    first_name = "Matt",
    nfl_team = "ATL",
    position = "QB",
    height = "6-4",
    weight = "217",
    dob = "1985-05-17",
    college = "Boston College"
  )

  player_3951 = Player(
    player_id = 3951,
    full_name = "Brett Rypien",
    last_name = "Rypien",
    first_name = "Brett",
    nfl_team = "DEN",
    position = "QB",
    height = "6-2",
    weight = "200",
    dob = "1996-07-09",
    college = "Boise State"
  )

  player_94 = Player(
    player_id = 94,
    full_name = "Matt Schaub",
    last_name = "Schaub",
    first_name = "Matt",
    nfl_team = "ATL",
    position = "QB",
    height = "6-6",
    weight = "245",
    dob = "1981-06-25",
    college = "Virginia"
  )

  player_3978 = Player(
    player_id = 3978,
    full_name = "Kyle Shurmur",
    last_name = "Shurmur",
    first_name = "Kyle",
    nfl_team = "KC",
    position = "QB",
    height = "6-4",
    weight = "225",
    dob = "1996-11-06",
    college = "Vanderbilt"
  )

  player_2750 = Player(
    player_id = 2750,
    full_name = "Trevor Siemian",
    last_name = "Siemian",
    first_name = "Trevor",
    nfl_team = "TEN",
    position = "QB",
    height = "6-3",
    weight = "220",
    dob = "1991-12-26",
    college = "Northwestern"
  )

  player_4365 = Player(
    player_id = 4365,
    full_name = "Reid Sinnett",
    last_name = "Sinnett",
    first_name = "Reid",
    nfl_team = "TB",
    position = "QB",
    height = "6-4",
    weight = "225",
    dob = "1997-02-05",
    college = "San Diego"
  )

  player_4190 = Player(
    player_id = 4190,
    full_name = "J'Mar Smith",
    last_name = "Smith",
    first_name = "J'Mar",
    nfl_team = "NE",
    position = "QB",
    height = "6-1",
    weight = "218",
    dob = "1996-09-24",
    college = "Louisiana Tech"
  )

  player_97 = Player(
    player_id = 97,
    full_name = "Alex Smith",
    last_name = "Smith",
    first_name = "Alex",
    nfl_team = "WAS",
    position = "QB",
    height = "6-4",
    weight = "213",
    dob = "1984-05-07",
    college = "Utah"
  )

  player_2146 = Player(
    player_id = 2146,
    full_name = "Geno Smith",
    last_name = "Smith",
    first_name = "Geno",
    nfl_team = "SEA",
    position = "QB",
    height = "6-3",
    weight = "221",
    dob = "1990-10-10",
    college = "West Virginia"
  )

  player_793 = Player(
    player_id = 793,
    full_name = "Matthew Stafford",
    last_name = "Stafford",
    first_name = "Matthew",
    nfl_team = "DET",
    position = "QB",
    height = "6-3",
    weight = "220",
    dob = "1988-02-07",
    college = "Georgia"
  )

  player_4318 = Player(
    player_id = 4318,
    full_name = "Nate Stanley",
    last_name = "Stanley",
    first_name = "Nate",
    nfl_team = "MIN",
    position = "QB",
    height = "6-4",
    weight = "243",
    dob = "1997-08-26",
    college = "Iowa"
  )

  player_3892 = Player(
    player_id = 3892,
    full_name = "Easton Stick",
    last_name = "Stick",
    first_name = "Easton",
    nfl_team = "LAC",
    position = "QB",
    height = "6-1",
    weight = "224",
    dob = "1995-09-15",
    college = "North Dakota State"
  )

  player_3861 = Player(
    player_id = 3861,
    full_name = "Jarrett Stidham",
    last_name = "Stidham",
    first_name = "Jarrett",
    nfl_team = "NE",
    position = "QB",
    height = "6-3",
    weight = "214",
    dob = "1996-08-08",
    college = "Auburn"
  )

  player_4126 = Player(
    player_id = 4126,
    full_name = "Chris Streveler",
    last_name = "Streveler",
    first_name = "Chris",
    nfl_team = "ARI",
    position = "QB",
    height = "6-3",
    weight = "215",
    dob = "1995-01-06",
    college = "South Dakota"
  )

  player_3047 = Player(
    player_id = 3047,
    full_name = "Nate Sudfeld",
    last_name = "Sudfeld",
    first_name = "Nate",
    nfl_team = "PHI",
    position = "QB",
    height = "6-6",
    weight = "227",
    dob = "1993-10-07",
    college = "Indiana"
  )

  player_4116 = Player(
    player_id = 4116,
    full_name = "Jordan Ta'amu",
    last_name = "Ta'amu",
    first_name = "Jordan",
    nfl_team = "KC",
    position = "QB",
    height = "6-3",
    weight = "221",
    dob = "1997-12-10",
    college = "Mississippi"
  )

  player_4129 = Player(
    player_id = 4129,
    full_name = "Tua Tagovailoa",
    last_name = "Tagovailoa",
    first_name = "Tua",
    nfl_team = "MIA",
    position = "QB",
    height = "6-1",
    weight = "218",
    dob = "1998-03-02",
    college = "Alabama"
  )

  player_1758 = Player(
    player_id = 1758,
    full_name = "Ryan Tannehill",
    last_name = "Tannehill",
    first_name = "Ryan",
    nfl_team = "TEN",
    position = "QB",
    height = "6-4",
    weight = "207",
    dob = "1988-07-27",
    college = "Texas A&amp;M"
  )

  player_2084 = Player(
    player_id = 2084,
    full_name = "Alex Tanney",
    last_name = "Tanney",
    first_name = "Alex",
    nfl_team = "NYG",
    position = "QB",
    height = "6-4",
    weight = "220",
    dob = "1987-11-11",
    college = "Monmouth, Ill."
  )

  player_1401 = Player(
    player_id = 1401,
    full_name = "Tyrod Taylor",
    last_name = "Taylor",
    first_name = "Tyrod",
    nfl_team = "LAC",
    position = "QB",
    height = "6-1",
    weight = "215",
    dob = "1989-08-03",
    college = "Virginia Tech"
  )

  player_3870 = Player(
    player_id = 3870,
    full_name = "Clayton Thorson",
    last_name = "Thorson",
    first_name = "Clayton",
    nfl_team = "DAL",
    position = "QB",
    height = "6-4",
    weight = "222",
    dob = "1995-06-15",
    college = "Northwestern"
  )

  player_4324 = Player(
    player_id = 4324,
    full_name = "Nick Tiano",
    last_name = "Tiano",
    first_name = "Nick",
    nfl_team = "HOU",
    position = "QB",
    height = "6-4",
    weight = "231",
    dob = "1996-12-10",
    college = "Chattanooga"
  )

  player_3342 = Player(
    player_id = 3342,
    full_name = "Mitchell Trubisky",
    last_name = "Trubisky",
    first_name = "Mitchell",
    nfl_team = "CHI",
    position = "QB",
    height = "6-2",
    weight = "215",
    dob = "1994-08-20",
    college = "North Carolina"
  )

  player_3453 = Player(
    player_id = 3453,
    full_name = "Phillip Walker",
    last_name = "Walker",
    first_name = "Phillip",
    nfl_team = "CAR",
    position = "QB",
    height = "5-11",
    weight = "212",
    dob = "1995-02-26",
    college = "Temple"
  )

  player_3360 = Player(
    player_id = 3360,
    full_name = "Deshaun Watson",
    last_name = "Watson",
    first_name = "Deshaun",
    nfl_team = "HOU",
    position = "QB",
    height = "6-2",
    weight = "221",
    dob = "1995-09-14",
    college = "Clemson"
  )

  player_3292 = Player(
    player_id = 3292,
    full_name = "Davis Webb",
    last_name = "Webb",
    first_name = "Davis",
    nfl_team = "BUF",
    position = "QB",
    height = "6-5",
    weight = "225",
    dob = "1995-01-22",
    college = "California"
  )

  player_3044 = Player(
    player_id = 3044,
    full_name = "Carson Wentz",
    last_name = "Wentz",
    first_name = "Carson",
    nfl_team = "PHI",
    position = "QB",
    height = "6-5",
    weight = "237",
    dob = "1992-12-30",
    college = "North Dakota State"
  )

  player_3628 = Player(
    player_id = 3628,
    full_name = "Mike White",
    last_name = "White",
    first_name = "Mike",
    nfl_team = "NYJ",
    position = "QB",
    height = "6-4",
    weight = "225",
    dob = "1995-03-25",
    college = "Western Kentucky"
  )

  player_4046 = Player(
    player_id = 4046,
    full_name = "Manny Wilkins",
    last_name = "Wilkins",
    first_name = "Manny",
    nfl_team = "GB",
    position = "QB",
    height = "6-2",
    weight = "193",
    dob = "1995-11-05",
    college = "Arizona State"
  )

  player_1847 = Player(
    player_id = 1847,
    full_name = "Russell Wilson",
    last_name = "Wilson",
    first_name = "Russell",
    nfl_team = "SEA",
    position = "QB",
    height = "5-11",
    weight = "215",
    dob = "1988-11-29",
    college = "Wisconsin"
  )

  player_2812 = Player(
    player_id = 2812,
    full_name = "Jameis Winston",
    last_name = "Winston",
    first_name = "Jameis",
    nfl_team = "NO",
    position = "QB",
    height = "6-4",
    weight = "231",
    dob = "1994-01-06",
    college = "Florida State"
  )

  player_3905 = Player(
    player_id = 3905,
    full_name = "John Wolford",
    last_name = "Wolford",
    first_name = "John",
    nfl_team = "LAR",
    position = "QB",
    height = "6-1",
    weight = "200",
    dob = "1995-10-16",
    college = "Wake Forest"
  )

  player_3652 = Player(
    player_id = 3652,
    full_name = "Logan Woodside",
    last_name = "Woodside",
    first_name = "Logan",
    nfl_team = "TEN",
    position = "QB",
    height = "6-1",
    weight = "213",
    dob = "1995-01-27",
    college = "Toledo"
  )

  player_2788 = Player(
    player_id = 2788,
    full_name = "Ameer Abdullah",
    last_name = "Abdullah",
    first_name = "Ameer",
    nfl_team = "MIN",
    position = "RB",
    height = "5-9",
    weight = "203",
    dob = "1993-06-13",
    college = "Nebraska"
  )

  player_3697 = Player(
    player_id = 3697,
    full_name = "Josh Adams",
    last_name = "Adams",
    first_name = "Josh",
    nfl_team = "NYJ",
    position = "RB",
    height = "6-2",
    weight = "225",
    dob = "1996-10-29",
    college = "Notre Dame"
  )

  player_4259 = Player(
    player_id = 4259,
    full_name = "Salvon Ahmed",
    last_name = "Ahmed",
    first_name = "Salvon",
    nfl_team = "MIA",
    position = "RB",
    height = "5-11",
    weight = "196",
    dob = "1998-12-29",
    college = "Washington"
  )

  player_4162 = Player(
    player_id = 4162,
    full_name = "Cam Akers",
    last_name = "Akers",
    first_name = "Cam",
    nfl_team = "LAR",
    position = "RB",
    height = "5-11",
    weight = "212",
    dob = "1999-06-22",
    college = "Florida State"
  )

  player_3912 = Player(
    player_id = 3912,
    full_name = "Rodney Anderson",
    last_name = "Anderson",
    first_name = "Rodney",
    nfl_team = "CIN",
    position = "RB",
    height = "6-0",
    weight = "224",
    dob = "1996-09-12",
    college = "Oklahoma"
  )

  player_4199 = Player(
    player_id = 4199,
    full_name = "Darius Anderson",
    last_name = "Anderson",
    first_name = "Darius",
    nfl_team = "DAL",
    position = "RB",
    height = "5-11",
    weight = "212",
    dob = "1997-09-10",
    college = "Texas Christian"
  )

  player_4085 = Player(
    player_id = 4085,
    full_name = "Bruce Anderson",
    last_name = "Anderson",
    first_name = "Bruce",
    nfl_team = "IND",
    position = "RB",
    height = "5-11",
    weight = "210",
    dob = "1997-06-20",
    college = "North Dakota State"
  )

  player_3571 = Player(
    player_id = 3571,
    full_name = "Alex Armah",
    last_name = "Armah",
    first_name = "Alex",
    nfl_team = "CAR",
    position = "RB",
    height = "6-2",
    weight = "255",
    dob = "1994-05-17",
    college = "West Georgia"
  )

  player_3937 = Player(
    player_id = 3937,
    full_name = "Ryquell Armstead",
    last_name = "Armstead",
    first_name = "Ryquell",
    nfl_team = "JAC",
    position = "RB",
    height = "5-11",
    weight = "220",
    dob = "1996-10-30",
    college = "Temple"
  )

  player_3952 = Player(
    player_id = 3952,
    full_name = "George Aston",
    last_name = "Aston",
    first_name = "George",
    nfl_team = "NYG",
    position = "RB",
    height = "6-0",
    weight = "240",
    dob = "1996-02-01",
    college = "Pittsburgh"
  )

  player_3620 = Player(
    player_id = 3620,
    full_name = "Kalen Ballage",
    last_name = "Ballage",
    first_name = "Kalen",
    nfl_team = "NYJ",
    position = "RB",
    height = "6-2",
    weight = "230",
    dob = "1995-12-22",
    college = "Arizona State"
  )

  player_3258 = Player(
    player_id = 3258,
    full_name = "Peyton Barber",
    last_name = "Barber",
    first_name = "Peyton",
    nfl_team = "WAS",
    position = "RB",
    height = "5-11",
    weight = "225",
    dob = "1994-06-27",
    college = "Auburn"
  )

  player_4322 = Player(
    player_id = 4322,
    full_name = "Jake Bargas",
    last_name = "Bargas",
    first_name = "Jake",
    nfl_team = "MIN",
    position = "RB",
    height = "6-2",
    weight = "250",
    dob = "1996-11-28",
    college = "North Carolina"
  )

  player_2378 = Player(
    player_id = 2378,
    full_name = "Kenjon Barner",
    last_name = "Barner",
    first_name = "Kenjon",
    nfl_team = "BAL",
    position = "RB",
    height = "5-9",
    weight = "195",
    dob = "1989-04-28",
    college = "Oregon"
  )

  player_3659 = Player(
    player_id = 3659,
    full_name = "Nick Bawden",
    last_name = "Bawden",
    first_name = "Nick",
    nfl_team = "DET",
    position = "RB",
    height = "6-2",
    weight = "245",
    dob = "1996-06-22",
    college = "San Diego State"
  )

  player_2289 = Player(
    player_id = 2289,
    full_name = "Le'Veon Bell",
    last_name = "Bell",
    first_name = "Le'Veon",
    nfl_team = "KC",
    position = "RB",
    height = "6-1",
    weight = "225",
    dob = "1992-02-18",
    college = "Michigan State"
  )

  player_4226 = Player(
    player_id = 4226,
    full_name = "LeVante Bellamy",
    last_name = "Bellamy",
    first_name = "LeVante",
    nfl_team = "DEN",
    position = "RB",
    height = "5-9",
    weight = "188",
    dob = "1996-11-28",
    college = "Western Michigan"
  )

  player_3779 = Player(
    player_id = 3779,
    full_name = "Nick Bellore",
    last_name = "Bellore",
    first_name = "Nick",
    nfl_team = "SEA",
    position = "RB",
    height = "6-1",
    weight = "250",
    dob = "1989-05-12",
    college = "Central Michigan"
  )

  player_4247 = Player(
    player_id = 4247,
    full_name = "Eno Benjamin",
    last_name = "Benjamin",
    first_name = "Eno",
    nfl_team = "ARI",
    position = "RB",
    height = "5-10",
    weight = "210",
    dob = "1999-04-13",
    college = "Arizona State"
  )

  player_2273 = Player(
    player_id = 2273,
    full_name = "Giovani Bernard",
    last_name = "Bernard",
    first_name = "Giovani",
    nfl_team = "CIN",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1991-11-22",
    college = "North Carolina"
  )

  player_4050 = Player(
    player_id = 4050,
    full_name = "Khari Blasingame",
    last_name = "Blasingame",
    first_name = "Khari",
    nfl_team = "TEN",
    position = "RB",
    height = "6-0",
    weight = "233",
    dob = "1996-07-01",
    college = "Vanderbilt"
  )

  player_1769 = Player(
    player_id = 1769,
    full_name = "Brandon Bolden",
    last_name = "Bolden",
    first_name = "Brandon",
    nfl_team = "NE",
    position = "RB",
    height = "5-11",
    weight = "220",
    dob = "1990-01-26",
    college = "Ole Miss"
  )

  player_3827 = Player(
    player_id = 3827,
    full_name = "Reggie Bonnafon",
    last_name = "Bonnafon",
    first_name = "Reggie",
    nfl_team = "CAR",
    position = "RB",
    height = "6-0",
    weight = "215",
    dob = "1996-01-04",
    college = "Louisville"
  )

  player_3052 = Player(
    player_id = 3052,
    full_name = "Devontae Booker",
    last_name = "Booker",
    first_name = "Devontae",
    nfl_team = "LV",
    position = "RB",
    height = "5-11",
    weight = "219",
    dob = "1992-05-27",
    college = "Utah"
  )

  player_3790 = Player(
    player_id = 3790,
    full_name = "Mike Boone",
    last_name = "Boone",
    first_name = "Mike",
    nfl_team = "MIN",
    position = "RB",
    height = "5-10",
    weight = "205",
    dob = "1995-07-30",
    college = "Cincinnati"
  )

  player_4239 = Player(
    player_id = 4239,
    full_name = "Darius Bradwell",
    last_name = "Bradwell",
    first_name = "Darius",
    nfl_team = "LAC",
    position = "RB",
    height = "6-1",
    weight = "230",
    dob = "1997-05-15",
    college = "Tulane"
  )

  player_3416 = Player(
    player_id = 3416,
    full_name = "Matt Breida",
    last_name = "Breida",
    first_name = "Matt",
    nfl_team = "MIA",
    position = "RB",
    height = "5-10",
    weight = "190",
    dob = "1995-02-28",
    college = "Georgia Southern"
  )

  player_4074 = Player(
    player_id = 4074,
    full_name = "Tony Brooks-James",
    last_name = "Brooks-James",
    first_name = "Tony",
    nfl_team = "MIN",
    position = "RB",
    height = "5-9",
    weight = "190",
    dob = "1994-12-06",
    college = "Oregon"
  )

  player_2937 = Player(
    player_id = 2937,
    full_name = "Malcolm Brown",
    last_name = "Brown",
    first_name = "Malcolm",
    nfl_team = "LAR",
    position = "RB",
    height = "5-11",
    weight = "222",
    dob = "1993-05-15",
    college = "Texas"
  )

  player_2274 = Player(
    player_id = 2274,
    full_name = "Rex Burkhead",
    last_name = "Burkhead",
    first_name = "Rex",
    nfl_team = "NE",
    position = "RB",
    height = "5-10",
    weight = "215",
    dob = "1990-07-02",
    college = "Nebraska"
  )

  player_2789 = Player(
    player_id = 2789,
    full_name = "Michael Burton",
    last_name = "Burton",
    first_name = "Michael",
    nfl_team = "NO",
    position = "RB",
    height = "6-0",
    weight = "240",
    dob = "1992-02-01",
    college = "Rutgers"
  )

  player_4366 = Player(
    player_id = 4366,
    full_name = "Raymond Calais",
    last_name = "Calais",
    first_name = "Raymond",
    nfl_team = "LAR",
    position = "RB",
    height = "5-9",
    weight = "185",
    dob = "1998-04-02",
    college = "Louisiana-Lafayette"
  )

  player_3626 = Player(
    player_id = 3626,
    full_name = "Trenton Cannon",
    last_name = "Cannon",
    first_name = "Trenton",
    nfl_team = "CAR",
    position = "RB",
    height = "5-11",
    weight = "185",
    dob = "1994-07-23",
    college = "Virginia State"
  )

  player_4267 = Player(
    player_id = 4267,
    full_name = "Patrick Carr",
    last_name = "Carr",
    first_name = "Patrick",
    nfl_team = "SEA",
    position = "RB",
    height = "5-8",
    weight = "207",
    dob = "1995-09-22",
    college = "Houston"
  )

  player_3192 = Player(
    player_id = 3192,
    full_name = "Tra Carson",
    last_name = "Carson",
    first_name = "Tra",
    nfl_team = "DET",
    position = "RB",
    height = "5-11",
    weight = "228",
    dob = "1992-10-24",
    college = "Texas A&amp;M"
  )

  player_3326 = Player(
    player_id = 3326,
    full_name = "Chris Carson",
    last_name = "Carson",
    first_name = "Chris",
    nfl_team = "SEA",
    position = "RB",
    height = "5-11",
    weight = "222",
    dob = "1994-09-16",
    college = "Oklahoma State"
  )

  player_4005 = Player(
    player_id = 4005,
    full_name = "Adam Choice",
    last_name = "Choice",
    first_name = "Adam",
    nfl_team = "SEA",
    position = "RB",
    height = "5-8",
    weight = "210",
    dob = "1995-11-30",
    college = "Clemson"
  )

  player_3600 = Player(
    player_id = 3600,
    full_name = "Nick Chubb",
    last_name = "Chubb",
    first_name = "Nick",
    nfl_team = "CLE",
    position = "RB",
    height = "5-11",
    weight = "225",
    dob = "1995-12-27",
    college = "Georgia"
  )

  player_3691 = Player(
    player_id = 3691,
    full_name = "Jordan Chunn",
    last_name = "Chunn",
    first_name = "Jordan",
    nfl_team = "DAL",
    position = "RB",
    height = "6-0",
    weight = "230",
    dob = "1995-01-02",
    college = "Troy"
  )

  player_3486 = Player(
    player_id = 3486,
    full_name = "Corey Clement",
    last_name = "Clement",
    first_name = "Corey",
    nfl_team = "PHI",
    position = "RB",
    height = "5-10",
    weight = "220",
    dob = "1994-11-02",
    college = "Wisconsin"
  )

  player_3343 = Player(
    player_id = 3343,
    full_name = "Tarik Cohen",
    last_name = "Cohen",
    first_name = "Tarik",
    nfl_team = "CHI",
    position = "RB",
    height = "5-6",
    weight = "191",
    dob = "1995-07-26",
    college = "North Carolina A&amp;T"
  )

  player_2806 = Player(
    player_id = 2806,
    full_name = "Tevin Coleman",
    last_name = "Coleman",
    first_name = "Tevin",
    nfl_team = "SF",
    position = "RB",
    height = "6-1",
    weight = "210",
    dob = "1993-04-16",
    college = "Indiana"
  )

  player_3339 = Player(
    player_id = 3339,
    full_name = "James Conner",
    last_name = "Conner",
    first_name = "James",
    nfl_team = "PIT",
    position = "RB",
    height = "6-1",
    weight = "233",
    dob = "1995-05-05",
    college = "Pittsburgh"
  )

  player_3354 = Player(
    player_id = 3354,
    full_name = "Dalvin Cook",
    last_name = "Cook",
    first_name = "Dalvin",
    nfl_team = "MIN",
    position = "RB",
    height = "5-10",
    weight = "210",
    dob = "1995-08-10",
    college = "Florida State"
  )

  player_4334 = Player(
    player_id = 4334,
    full_name = "Nathan Cottrell",
    last_name = "Cottrell",
    first_name = "Nathan",
    nfl_team = "JAC",
    position = "RB",
    height = "5-11",
    weight = "193",
    dob = "1996-08-02",
    college = "Georgia Tech"
  )

  player_3860 = Player(
    player_id = 3860,
    full_name = "Chandler Cox",
    last_name = "Cox",
    first_name = "Chandler",
    nfl_team = "MIA",
    position = "RB",
    height = "6-1",
    weight = "240",
    dob = "1996-07-29",
    college = "Auburn"
  )

  player_3988 = Player(
    player_id = 3988,
    full_name = "Jeremy Cox",
    last_name = "Cox",
    first_name = "Jeremy",
    nfl_team = "DEN",
    position = "RB",
    height = "6-0",
    weight = "235",
    dob = "1996-08-16",
    college = "Old Dominion"
  )

  player_4101 = Player(
    player_id = 4101,
    full_name = "Damarea Crockett",
    last_name = "Crockett",
    first_name = "Damarea",
    nfl_team = "GB",
    position = "RB",
    height = "5-11",
    weight = "225",
    dob = "1997-12-22",
    college = "Missouri"
  )

  player_4268 = Player(
    player_id = 4268,
    full_name = "DeeJay Dallas",
    last_name = "Dallas",
    first_name = "DeeJay",
    nfl_team = "SEA",
    position = "RB",
    height = "5-10",
    weight = "214",
    dob = "1998-09-16",
    college = "Miami"
  )

  player_4350 = Player(
    player_id = 4350,
    full_name = "Mikey Daniel",
    last_name = "Daniel",
    first_name = "Mikey",
    nfl_team = "ATL",
    position = "RB",
    height = "6-2",
    weight = "235",
    dob = "1996-11-03",
    college = "South Dakota State"
  )

  player_2763 = Player(
    player_id = 2763,
    full_name = "Mike Davis",
    last_name = "Davis",
    first_name = "Mike",
    nfl_team = "CAR",
    position = "RB",
    height = "5-9",
    weight = "221",
    dob = "1993-02-19",
    college = "South Carolina"
  )

  player_3807 = Player(
    player_id = 3807,
    full_name = "Dalyn Dawkins",
    last_name = "Dawkins",
    first_name = "Dalyn",
    nfl_team = "TEN",
    position = "RB",
    height = "5-7",
    weight = "183",
    dob = "1994-12-26",
    college = "Colorado State"
  )

  player_1381 = Player(
    player_id = 1381,
    full_name = "James Develin",
    last_name = "Develin",
    first_name = "James",
    nfl_team = "NE",
    position = "RB",
    height = "6-3",
    weight = "255",
    dob = "1988-07-23",
    college = "Brown"
  )

  player_4172 = Player(
    player_id = 4172,
    full_name = "AJ Dillon",
    last_name = "Dillon",
    first_name = "AJ",
    nfl_team = "GB",
    position = "RB",
    height = "6-1",
    weight = "250",
    dob = "1998-05-02",
    college = "Boston College"
  )

  player_1720 = Player(
    player_id = 1720,
    full_name = "Patrick DiMarco",
    last_name = "DiMarco",
    first_name = "Patrick",
    nfl_team = "BUF",
    position = "RB",
    height = "6-1",
    weight = "234",
    dob = "1989-04-30",
    college = "South Carolina"
  )

  player_3077 = Player(
    player_id = 3077,
    full_name = "Kenneth Dixon",
    last_name = "Dixon",
    first_name = "Kenneth",
    nfl_team = "NYJ",
    position = "RB",
    height = "5-10",
    weight = "228",
    dob = "1994-01-21",
    college = "Louisiana Tech"
  )

  player_4164 = Player(
    player_id = 4164,
    full_name = "JK Dobbins",
    last_name = "Dobbins",
    first_name = "JK",
    nfl_team = "BAL",
    position = "RB",
    height = "5-10",
    weight = "214",
    dob = "1998-12-17",
    college = "Ohio State"
  )

  player_4200 = Player(
    player_id = 4200,
    full_name = "Rico Dowdle",
    last_name = "Dowdle",
    first_name = "Rico",
    nfl_team = "DAL",
    position = "RB",
    height = "6-0",
    weight = "215",
    dob = "1998-06-14",
    college = "South Carolina"
  )

  player_3026 = Player(
    player_id = 3026,
    full_name = "Kenyan Drake",
    last_name = "Drake",
    first_name = "Kenyan",
    nfl_team = "ARI",
    position = "RB",
    height = "6-1",
    weight = "211",
    dob = "1994-01-26",
    college = "Alabama"
  )

  player_3642 = Player(
    player_id = 3642,
    full_name = "Chase Edmonds",
    last_name = "Edmonds",
    first_name = "Chase",
    nfl_team = "ARI",
    position = "RB",
    height = "5-9",
    weight = "210",
    dob = "1996-04-13",
    college = "Fordham"
  )

  player_3548 = Player(
    player_id = 3548,
    full_name = "Trey Edmunds",
    last_name = "Edmunds",
    first_name = "Trey",
    nfl_team = "PIT",
    position = "RB",
    height = "6-2",
    weight = "223",
    dob = "1994-12-30",
    college = "Maryland"
  )

  player_3751 = Player(
    player_id = 3751,
    full_name = "Gus Edwards",
    last_name = "Edwards",
    first_name = "Gus",
    nfl_team = "BAL",
    position = "RB",
    height = "6-1",
    weight = "238",
    dob = "1995-04-13",
    college = "Rutgers"
  )

  player_4133 = Player(
    player_id = 4133,
    full_name = "Clyde Edwards-Helaire",
    last_name = "Edwards-Helaire",
    first_name = "Clyde",
    nfl_team = "KC",
    position = "RB",
    height = "5-8",
    weight = "209",
    dob = "1999-04-11",
    college = "Louisiana State"
  )

  player_3392 = Player(
    player_id = 3392,
    full_name = "Austin Ekeler",
    last_name = "Ekeler",
    first_name = "Austin",
    nfl_team = "LAC",
    position = "RB",
    height = "5-10",
    weight = "200",
    dob = "1995-05-17",
    college = "Western State, Colo."
  )

  player_3037 = Player(
    player_id = 3037,
    full_name = "Ezekiel Elliott",
    last_name = "Elliott",
    first_name = "Ezekiel",
    nfl_team = "DAL",
    position = "RB",
    height = "6-0",
    weight = "228",
    dob = "1995-07-22",
    college = "Ohio State"
  )

  player_3102 = Player(
    player_id = 3102,
    full_name = "Tyler Ervin",
    last_name = "Ervin",
    first_name = "Tyler",
    nfl_team = "GB",
    position = "RB",
    height = "5-10",
    weight = "185",
    dob = "1993-10-07",
    college = "San Jose State"
  )

  player_4178 = Player(
    player_id = 4178,
    full_name = "Darrynton Evans",
    last_name = "Evans",
    first_name = "Darrynton",
    nfl_team = "TEN",
    position = "RB",
    height = "5-11",
    weight = "200",
    dob = "1998-07-09",
    college = "Appalachian State"
  )

  player_4335 = Player(
    player_id = 4335,
    full_name = "Tavien Feaster",
    last_name = "Feaster",
    first_name = "Tavien",
    nfl_team = "NYG",
    position = "RB",
    height = "5-11",
    weight = "221",
    dob = "1997-12-31",
    college = "South Carolina"
  )

  player_3256 = Player(
    player_id = 3256,
    full_name = "Josh Ferguson",
    last_name = "Ferguson",
    first_name = "Josh",
    nfl_team = "WAS",
    position = "RB",
    height = "5-10",
    weight = "205",
    dob = "1993-05-23",
    college = "Illinois"
  )

  player_3129 = Player(
    player_id = 3129,
    full_name = "D.J. Foster",
    last_name = "Foster",
    first_name = "D.J.",
    nfl_team = "ARI",
    position = "RB",
    height = "6-0",
    weight = "205",
    dob = "1993-11-22",
    college = "Arizona State"
  )

  player_3364 = Player(
    player_id = 3364,
    full_name = "Leonard Fournette",
    last_name = "Fournette",
    first_name = "Leonard",
    nfl_team = "TB",
    position = "RB",
    height = "6-0",
    weight = "228",
    dob = "1995-01-18",
    college = "Louisiana State"
  )

  player_3588 = Player(
    player_id = 3588,
    full_name = "Royce Freeman",
    last_name = "Freeman",
    first_name = "Royce",
    nfl_team = "DEN",
    position = "RB",
    height = "6-0",
    weight = "238",
    dob = "1996-02-24",
    college = "Oregon"
  )

  player_2651 = Player(
    player_id = 2651,
    full_name = "Devonta Freeman",
    last_name = "Freeman",
    first_name = "Devonta",
    nfl_team = "NYG",
    position = "RB",
    height = "5-8",
    weight = "206",
    dob = "1992-03-15",
    college = "Florida State"
  )

  player_3293 = Player(
    player_id = 3293,
    full_name = "Wayne Gallman",
    last_name = "Gallman",
    first_name = "Wayne",
    nfl_team = "NYG",
    position = "RB",
    height = "6-0",
    weight = "210",
    dob = "1994-10-01",
    college = "Clemson"
  )

  player_3859 = Player(
    player_id = 3859,
    full_name = "Myles Gaskin",
    last_name = "Gaskin",
    first_name = "Myles",
    nfl_team = "MIA",
    position = "RB",
    height = "5-10",
    weight = "200",
    dob = "1997-02-15",
    college = "Washington"
  )

  player_4155 = Player(
    player_id = 4155,
    full_name = "Antonio Gibson",
    last_name = "Gibson",
    first_name = "Antonio",
    nfl_team = "WAS",
    position = "RB",
    height = "6-2",
    weight = "221",
    dob = "1998-06-23",
    college = "Memphis"
  )

  player_4277 = Player(
    player_id = 4277,
    full_name = "James Gilbert",
    last_name = "Gilbert",
    first_name = "James",
    nfl_team = "LAR",
    position = "RB",
    height = "5-9",
    weight = "198",
    dob = "1995-11-10",
    college = "Kansas State"
  )

  player_3933 = Player(
    player_id = 3933,
    full_name = "Cullen Gillaspia",
    last_name = "Gillaspia",
    first_name = "Cullen",
    nfl_team = "HOU",
    position = "RB",
    height = "6-2",
    weight = "235",
    dob = "1995-05-12",
    college = "Texas A&amp;M"
  )

  player_2759 = Player(
    player_id = 2759,
    full_name = "Melvin Gordon",
    last_name = "Gordon",
    first_name = "Melvin",
    nfl_team = "DEN",
    position = "RB",
    height = "6-1",
    weight = "215",
    dob = "1993-04-13",
    college = "Wisconsin"
  )

  player_4107 = Player(
    player_id = 4107,
    full_name = "Derrick Gore",
    last_name = "Gore",
    first_name = "Derrick",
    nfl_team = "LAC",
    position = "RB",
    height = "5-10",
    weight = "212",
    dob = "1994-12-13",
    college = "Louisiana-Monroe"
  )

  player_180 = Player(
    player_id = 180,
    full_name = "Frank Gore",
    last_name = "Gore",
    first_name = "Frank",
    nfl_team = "NYJ",
    position = "RB",
    height = "5-9",
    weight = "212",
    dob = "1983-05-14",
    college = "Miami"
  )

  player_2771 = Player(
    player_id = 2771,
    full_name = "Todd Gurley",
    last_name = "Gurley",
    first_name = "Todd",
    nfl_team = "ATL",
    position = "RB",
    height = "6-1",
    weight = "224",
    dob = "1994-08-03",
    college = "Georgia"
  )

  player_4024 = Player(
    player_id = 4024,
    full_name = "Darrin Hall",
    last_name = "Hall",
    first_name = "Darrin",
    nfl_team = "PIT",
    position = "RB",
    height = "6-0",
    weight = "225",
    dob = "1996-09-06",
    college = "Pittsburgh"
  )

  player_3226 = Player(
    player_id = 3226,
    full_name = "C.J. Ham",
    last_name = "Ham",
    first_name = "C.J.",
    nfl_team = "MIN",
    position = "RB",
    height = "5-11",
    weight = "235",
    dob = "1993-07-22",
    college = "Augustana, S.D."
  )

  player_3862 = Player(
    player_id = 3862,
    full_name = "Damien Harris",
    last_name = "Harris",
    first_name = "Damien",
    nfl_team = "NE",
    position = "RB",
    height = "5-11",
    weight = "213",
    dob = "1997-02-11",
    college = "Alabama"
  )

  player_4260 = Player(
    player_id = 4260,
    full_name = "JaMycal Hasty",
    last_name = "Hasty",
    first_name = "JaMycal",
    nfl_team = "SF",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1996-09-12",
    college = "Baylor"
  )

  player_3906 = Player(
    player_id = 3906,
    full_name = "Darrell Henderson",
    last_name = "Henderson",
    first_name = "Darrell",
    nfl_team = "LAR",
    position = "RB",
    height = "5-8",
    weight = "200",
    dob = "1997-08-19",
    college = "Memphis"
  )

  player_3112 = Player(
    player_id = 3112,
    full_name = "Derrick Henry",
    last_name = "Henry",
    first_name = "Derrick",
    nfl_team = "TEN",
    position = "RB",
    height = "6-3",
    weight = "247",
    dob = "1994-01-04",
    college = "Alabama"
  )

  player_4299 = Player(
    player_id = 4299,
    full_name = "Brian Herrien",
    last_name = "Herrien",
    first_name = "Brian",
    nfl_team = "CLE",
    position = "RB",
    height = "5-11",
    weight = "208",
    dob = "1998-02-07",
    college = "Georgia"
  )

  player_4054 = Player(
    player_id = 4054,
    full_name = "Karan Higdon",
    last_name = "Higdon",
    first_name = "Karan",
    nfl_team = "HOU",
    position = "RB",
    height = "5-10",
    weight = "202",
    dob = "1996-09-08",
    college = "Michigan"
  )

  player_3376 = Player(
    player_id = 3376,
    full_name = "Brian Hill",
    last_name = "Hill",
    first_name = "Brian",
    nfl_team = "ATL",
    position = "RB",
    height = "6-1",
    weight = "219",
    dob = "1995-11-09",
    college = "Wyoming"
  )

  player_3908 = Player(
    player_id = 3908,
    full_name = "Justice Hill",
    last_name = "Hill",
    first_name = "Justice",
    nfl_team = "BAL",
    position = "RB",
    height = "5-10",
    weight = "200",
    dob = "1997-11-14",
    college = "Oklahoma State"
  )

  player_2555 = Player(
    player_id = 2555,
    full_name = "Jeremy Hill",
    last_name = "Hill",
    first_name = "Jeremy",
    nfl_team = "LV",
    position = "RB",
    height = "6-1",
    weight = "230",
    dob = "1992-10-20",
    college = "LSU"
  )

  player_3766 = Player(
    player_id = 3766,
    full_name = "Dontrell Hilliard",
    last_name = "Hilliard",
    first_name = "Dontrell",
    nfl_team = "CLE",
    position = "RB",
    height = "5-11",
    weight = "202",
    dob = "1995-02-26",
    college = "Tulane"
  )

  player_3971 = Player(
    player_id = 3971,
    full_name = "Jonathan Hilliman",
    last_name = "Hilliman",
    first_name = "Jonathan",
    nfl_team = "NYG",
    position = "RB",
    height = "5-11",
    weight = "216",
    dob = "1995-11-14",
    college = "Rutgers"
  )

  player_3995 = Player(
    player_id = 3995,
    full_name = "Wes Hills",
    last_name = "Hills",
    first_name = "Wes",
    nfl_team = "DET",
    position = "RB",
    height = "6-0",
    weight = "218",
    dob = "1995-06-05",
    college = "Slippery Rock"
  )

  player_3667 = Player(
    player_id = 3667,
    full_name = "Nyheim Hines",
    last_name = "Hines",
    first_name = "Nyheim",
    nfl_team = "IND",
    position = "RB",
    height = "5-9",
    weight = "198",
    dob = "1996-11-12",
    college = "North Carolina State"
  )

  player_4248 = Player(
    player_id = 4248,
    full_name = "Sirgeo Hoffman",
    last_name = "Hoffman",
    first_name = "Sirgeo",
    nfl_team = "ARI",
    position = "RB",
    height = "6-0",
    weight = "215",
    dob = "0000-00-00",
    college = "Portland State"
  )

  player_4261 = Player(
    player_id = 4261,
    full_name = "Josh Hokit",
    last_name = "Hokit",
    first_name = "Josh",
    nfl_team = "SF",
    position = "RB",
    height = "6-1",
    weight = "225",
    dob = "1997-11-12",
    college = "Fresno State"
  )

  player_4240 = Player(
    player_id = 4240,
    full_name = "Bobby Holly",
    last_name = "Holly",
    first_name = "Bobby",
    nfl_team = "LAC",
    position = "RB",
    height = "5-11",
    weight = "240",
    dob = "1997-06-04",
    college = "Louisiana Tech"
  )

  player_4079 = Player(
    player_id = 4079,
    full_name = "Elijah Holyfield",
    last_name = "Holyfield",
    first_name = "Elijah",
    nfl_team = "PHI",
    position = "RB",
    height = "5-10",
    weight = "215",
    dob = "1997-11-30",
    college = "Georgia"
  )

  player_3901 = Player(
    player_id = 3901,
    full_name = "Travis Homer",
    last_name = "Homer",
    first_name = "Travis",
    nfl_team = "SEA",
    position = "RB",
    height = "5-10",
    weight = "202",
    dob = "1998-08-07",
    college = "Miami"
  )

  player_3091 = Player(
    player_id = 3091,
    full_name = "Jordan Howard",
    last_name = "Howard",
    first_name = "Jordan",
    nfl_team = "MIA",
    position = "RB",
    height = "6-0",
    weight = "224",
    dob = "1994-11-02",
    college = "Indiana"
  )

  player_3684 = Player(
    player_id = 3684,
    full_name = "Buddy Howell",
    last_name = "Howell",
    first_name = "Buddy",
    nfl_team = "HOU",
    position = "RB",
    height = "6-1",
    weight = "218",
    dob = "1996-03-27",
    college = "Florida Atlantic"
  )

  player_3312 = Player(
    player_id = 3312,
    full_name = "Kareem Hunt",
    last_name = "Hunt",
    first_name = "Kareem",
    nfl_team = "CLE",
    position = "RB",
    height = "5-11",
    weight = "216",
    dob = "1995-08-06",
    college = "Toledo"
  )

  player_4310 = Player(
    player_id = 4310,
    full_name = "Jason Huntley",
    last_name = "Huntley",
    first_name = "Jason",
    nfl_team = "PHI",
    position = "RB",
    height = "5-9",
    weight = "193",
    dob = "1998-04-20",
    college = "New Mexico State"
  )

  player_2530 = Player(
    player_id = 2530,
    full_name = "Carlos Hyde",
    last_name = "Hyde",
    first_name = "Carlos",
    nfl_team = "SEA",
    position = "RB",
    height = "6-0",
    weight = "229",
    dob = "1990-09-20",
    college = "Ohio State"
  )

  player_3985 = Player(
    player_id = 3985,
    full_name = "Alec Ingold",
    last_name = "Ingold",
    first_name = "Alec",
    nfl_team = "LV",
    position = "RB",
    height = "6-1",
    weight = "242",
    dob = "1996-07-09",
    college = "Wisconsin"
  )

  player_1415 = Player(
    player_id = 1415,
    full_name = "Mark Ingram",
    last_name = "Ingram",
    first_name = "Mark",
    nfl_team = "BAL",
    position = "RB",
    height = "5-9",
    weight = "215",
    dob = "1989-12-21",
    college = "Alabama"
  )

  player_3640 = Player(
    player_id = 3640,
    full_name = "Justin Jackson",
    last_name = "Jackson",
    first_name = "Justin",
    nfl_team = "LAC",
    position = "RB",
    height = "6-0",
    weight = "200",
    dob = "1996-04-22",
    college = "Northwestern"
  )

  player_3038 = Player(
    player_id = 3038,
    full_name = "Darius Jackson",
    last_name = "Jackson",
    first_name = "Darius",
    nfl_team = "IND",
    position = "RB",
    height = "6-0",
    weight = "220",
    dob = "1993-12-01",
    college = "Eastern Michigan"
  )

  player_3889 = Player(
    player_id = 3889,
    full_name = "Josh Jacobs",
    last_name = "Jacobs",
    first_name = "Josh",
    nfl_team = "LV",
    position = "RB",
    height = "5-10",
    weight = "220",
    dob = "1998-02-11",
    college = "Alabama"
  )

  player_3053 = Player(
    player_id = 3053,
    full_name = "Andy Janovich",
    last_name = "Janovich",
    first_name = "Andy",
    nfl_team = "CLE",
    position = "RB",
    height = "6-1",
    weight = "238",
    dob = "1993-05-23",
    college = "Nebraska"
  )

  player_3604 = Player(
    player_id = 3604,
    full_name = "Kerryon Johnson",
    last_name = "Johnson",
    first_name = "Kerryon",
    nfl_team = "DET",
    position = "RB",
    height = "5-11",
    weight = "212",
    dob = "1997-06-30",
    college = "Auburn"
  )

  player_3863 = Player(
    player_id = 3863,
    full_name = "Jakob Johnson",
    last_name = "Johnson",
    first_name = "Jakob",
    nfl_team = "NE",
    position = "RB",
    height = "6-3",
    weight = "255",
    dob = "1994-12-15",
    college = "Tennessee"
  )

  player_3923 = Player(
    player_id = 3923,
    full_name = "Ty Johnson",
    last_name = "Johnson",
    first_name = "Ty",
    nfl_team = "NYJ",
    position = "RB",
    height = "5-10",
    weight = "210",
    dob = "1997-09-17",
    college = "Maryland"
  )

  player_4030 = Player(
    player_id = 4030,
    full_name = "D'Ernest Johnson",
    last_name = "Johnson",
    first_name = "D'Ernest",
    nfl_team = "CLE",
    position = "RB",
    height = "5-10",
    weight = "208",
    dob = "1996-02-27",
    college = "South Florida"
  )

  player_2760 = Player(
    player_id = 2760,
    full_name = "David Johnson",
    last_name = "Johnson",
    first_name = "David",
    nfl_team = "HOU",
    position = "RB",
    height = "6-1",
    weight = "224",
    dob = "1991-12-16",
    college = "Northern Iowa"
  )

  player_2781 = Player(
    player_id = 2781,
    full_name = "Duke Johnson",
    last_name = "Johnson",
    first_name = "Duke",
    nfl_team = "HOU",
    position = "RB",
    height = "5-9",
    weight = "210",
    dob = "1993-09-23",
    college = "Miami"
  )

  player_3349 = Player(
    player_id = 3349,
    full_name = "Aaron Jones",
    last_name = "Jones",
    first_name = "Aaron",
    nfl_team = "GB",
    position = "RB",
    height = "5-9",
    weight = "208",
    dob = "1994-12-02",
    college = "Texas-El Paso"
  )

  player_3614 = Player(
    player_id = 3614,
    full_name = "Ronald Jones",
    last_name = "Jones",
    first_name = "Ronald",
    nfl_team = "TB",
    position = "RB",
    height = "5-11",
    weight = "208",
    dob = "1997-08-03",
    college = "Southern California"
  )

  player_1416 = Player(
    player_id = 1416,
    full_name = "Taiwan Jones",
    last_name = "Jones",
    first_name = "Taiwan",
    nfl_team = "BUF",
    position = "RB",
    height = "6-0",
    weight = "195",
    dob = "1988-07-26",
    college = "Eastern Washington"
  )

  player_4269 = Player(
    player_id = 4269,
    full_name = "Anthony Jones",
    last_name = "Jones",
    first_name = "Anthony",
    nfl_team = "SEA",
    position = "RB",
    height = "5-10",
    weight = "209",
    dob = "0000-00-00",
    college = "Florida International"
  )

  player_4278 = Player(
    player_id = 4278,
    full_name = "Xavier Jones",
    last_name = "Jones",
    first_name = "Xavier",
    nfl_team = "LAR",
    position = "RB",
    height = "5-11",
    weight = "208",
    dob = "1997-08-24",
    college = "Southern Methodist"
  )

  player_4317 = Player(
    player_id = 4317,
    full_name = "Jordan Jones",
    last_name = "Jones",
    first_name = "Jordan",
    nfl_team = "GB",
    position = "RB",
    height = "6-1",
    weight = "255",
    dob = "0000-00-00",
    college = "Prairie View A&amp;M"
  )

  player_4362 = Player(
    player_id = 4362,
    full_name = "Tony Jones Jr",
    last_name = "Jones Jr",
    first_name = "Tony",
    nfl_team = "NO",
    position = "RB",
    height = "5-11",
    weight = "225",
    dob = "1997-11-24",
    college = "Notre Dame"
  )

  player_2265 = Player(
    player_id = 2265,
    full_name = "Kyle Juszczyk",
    last_name = "Juszczyk",
    first_name = "Kyle",
    nfl_team = "SF",
    position = "RB",
    height = "6-1",
    weight = "240",
    dob = "1991-04-23",
    college = "Harvard"
  )

  player_3384 = Player(
    player_id = 3384,
    full_name = "Alvin Kamara",
    last_name = "Kamara",
    first_name = "Alvin",
    nfl_team = "NO",
    position = "RB",
    height = "5-10",
    weight = "215",
    dob = "1995-07-25",
    college = "Tennessee"
  )

  player_4160 = Player(
    player_id = 4160,
    full_name = "Joshua Kelley",
    last_name = "Kelley",
    first_name = "Joshua",
    nfl_team = "LAC",
    position = "RB",
    height = "5-11",
    weight = "219",
    dob = "1997-11-20",
    college = "UCLA"
  )

  player_3649 = Player(
    player_id = 3649,
    full_name = "John Kelly",
    last_name = "Kelly",
    first_name = "John",
    nfl_team = "LAR",
    position = "RB",
    height = "5-10",
    weight = "205",
    dob = "1996-10-04",
    college = "Tennessee"
  )

  player_4213 = Player(
    player_id = 4213,
    full_name = "Adrian Killins Jr",
    last_name = "Killins Jr",
    first_name = "Adrian",
    nfl_team = "PHI",
    position = "RB",
    height = "5-8",
    weight = "164",
    dob = "1998-01-02",
    college = "Central Florida"
  )

  player_3961 = Player(
    player_id = 3961,
    full_name = "Patrick Laird",
    last_name = "Laird",
    first_name = "Patrick",
    nfl_team = "MIA",
    position = "RB",
    height = "6-0",
    weight = "205",
    dob = "1995-08-17",
    college = "California"
  )

  player_4207 = Player(
    player_id = 4207,
    full_name = "Javon Leake",
    last_name = "Leake",
    first_name = "Javon",
    nfl_team = "NYG",
    position = "RB",
    height = "6-0",
    weight = "215",
    dob = "1998-08-01",
    college = "Maryland"
  )

  player_4300 = Player(
    player_id = 4300,
    full_name = "Benny LeMay",
    last_name = "LeMay",
    first_name = "Benny",
    nfl_team = "CLE",
    position = "RB",
    height = "5-9",
    weight = "218",
    dob = "1997-10-18",
    college = "North Carolina-Charlotte"
  )

  player_1418 = Player(
    player_id = 1418,
    full_name = "Dion Lewis",
    last_name = "Lewis",
    first_name = "Dion",
    nfl_team = "NYG",
    position = "RB",
    height = "5-8",
    weight = "195",
    dob = "1990-09-27",
    college = "Pittsburgh"
  )

  player_3707 = Player(
    player_id = 3707,
    full_name = "Phillip Lindsay",
    last_name = "Lindsay",
    first_name = "Phillip",
    nfl_team = "DEN",
    position = "RB",
    height = "5-8",
    weight = "190",
    dob = "1994-07-24",
    college = "Colorado"
  )

  player_2326 = Player(
    player_id = 2326,
    full_name = "Zach Line",
    last_name = "Line",
    first_name = "Zach",
    nfl_team = "NO",
    position = "RB",
    height = "6-1",
    weight = "233",
    dob = "1990-04-26",
    college = "SMU"
  )

  player_3317 = Player(
    player_id = 3317,
    full_name = "T.J. Logan",
    last_name = "Logan",
    first_name = "T.J.",
    nfl_team = "TB",
    position = "RB",
    height = "5-11",
    weight = "195",
    dob = "1994-09-03",
    college = "North Carolina"
  )

  player_3874 = Player(
    player_id = 3874,
    full_name = "Bryce Love",
    last_name = "Love",
    first_name = "Bryce",
    nfl_team = "WAS",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1997-07-08",
    college = "Stanford"
  )

  player_3362 = Player(
    player_id = 3362,
    full_name = "Marlon Mack",
    last_name = "Mack",
    first_name = "Marlon",
    nfl_team = "IND",
    position = "RB",
    height = "6-0",
    weight = "210",
    dob = "1996-03-07",
    college = "South Florida"
  )

  player_3979 = Player(
    player_id = 3979,
    full_name = "Marcus Marshall",
    last_name = "Marshall",
    first_name = "Marcus",
    nfl_team = "KC",
    position = "RB",
    height = "5-10",
    weight = "200",
    dob = "1997-02-23",
    college = "James Madison"
  )

  player_3929 = Player(
    player_id = 3929,
    full_name = "Alexander Mattison",
    last_name = "Mattison",
    first_name = "Alexander",
    nfl_team = "MIN",
    position = "RB",
    height = "5-11",
    weight = "220",
    dob = "1998-06-19",
    college = "Boise State"
  )

  player_4306 = Player(
    player_id = 4306,
    full_name = "Napoleon Maxwell",
    last_name = "Maxwell",
    first_name = "Napoleon",
    nfl_team = "CHI",
    position = "RB",
    height = "6-0",
    weight = "215",
    dob = "0000-00-00",
    college = "Florida International"
  )

  player_3379 = Player(
    player_id = 3379,
    full_name = "Christian McCaffrey",
    last_name = "McCaffrey",
    first_name = "Christian",
    nfl_team = "CAR",
    position = "RB",
    height = "5-11",
    weight = "205",
    dob = "1996-06-07",
    college = "Stanford"
  )

  player_810 = Player(
    player_id = 810,
    full_name = "LeSean McCoy",
    last_name = "McCoy",
    first_name = "LeSean",
    nfl_team = "TB",
    position = "RB",
    height = "5-11",
    weight = "210",
    dob = "1988-07-12",
    college = "Pittsburgh"
  )

  player_4168 = Player(
    player_id = 4168,
    full_name = "Anthony McFarland Jr",
    last_name = "McFarland Jr",
    first_name = "Anthony",
    nfl_team = "PIT",
    position = "RB",
    height = "5-9",
    weight = "198",
    dob = "1999-03-04",
    college = "Maryland"
  )

  player_4063 = Player(
    player_id = 4063,
    full_name = "Taj McGowan",
    last_name = "McGowan",
    first_name = "Taj",
    nfl_team = "JAC",
    position = "RB",
    height = "6-1",
    weight = "210",
    dob = "1996-12-30",
    college = "Central Florida"
  )

  player_3283 = Player(
    player_id = 3283,
    full_name = "Elijah McGuire",
    last_name = "McGuire",
    first_name = "Elijah",
    nfl_team = "KC",
    position = "RB",
    height = "5-10",
    weight = "214",
    dob = "1994-06-01",
    college = "Louisiana-Lafayette"
  )

  player_2602 = Player(
    player_id = 2602,
    full_name = "Jerick McKinnon",
    last_name = "McKinnon",
    first_name = "Jerick",
    nfl_team = "SF",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1992-05-03",
    college = "Georgia Southern"
  )

  player_3245 = Player(
    player_id = 3245,
    full_name = "J.D. McKissic",
    last_name = "McKissic",
    first_name = "J.D.",
    nfl_team = "WAS",
    position = "RB",
    height = "5-10",
    weight = "195",
    dob = "1993-08-15",
    college = "Arkansas State"
  )

  player_3387 = Player(
    player_id = 3387,
    full_name = "Jeremy McNichols",
    last_name = "McNichols",
    first_name = "Jeremy",
    nfl_team = "TEN",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1995-12-26",
    college = "Boise State"
  )

  player_3579 = Player(
    player_id = 3579,
    full_name = "Sony Michel",
    last_name = "Michel",
    first_name = "Sony",
    nfl_team = "NE",
    position = "RB",
    height = "5-11",
    weight = "215",
    dob = "1995-02-17",
    college = "Georgia"
  )

  player_1761 = Player(
    player_id = 1761,
    full_name = "Lamar Miller",
    last_name = "Miller",
    first_name = "Lamar",
    nfl_team = "CHI",
    position = "RB",
    height = "5-10",
    weight = "221",
    dob = "1991-04-25",
    college = "Miami (FL)"
  )

  player_3329 = Player(
    player_id = 3329,
    full_name = "Joe Mixon",
    last_name = "Mixon",
    first_name = "Joe",
    nfl_team = "CIN",
    position = "RB",
    height = "6-1",
    weight = "220",
    dob = "1996-07-24",
    college = "Oklahoma"
  )

  player_3920 = Player(
    player_id = 3920,
    full_name = "David Montgomery",
    last_name = "Montgomery",
    first_name = "David",
    nfl_team = "CHI",
    position = "RB",
    height = "5-10",
    weight = "222",
    dob = "1997-06-07",
    college = "Iowa State"
  )

  player_2792 = Player(
    player_id = 2792,
    full_name = "Ty Montgomery",
    last_name = "Montgomery",
    first_name = "Ty",
    nfl_team = "NO",
    position = "RB",
    height = "6-0",
    weight = "216",
    dob = "1993-01-22",
    college = "Stanford"
  )

  player_4124 = Player(
    player_id = 4124,
    full_name = "Jalin Moore",
    last_name = "Moore",
    first_name = "Jalin",
    nfl_team = "NYJ",
    position = "RB",
    height = "5-10",
    weight = "211",
    dob = "1995-11-28",
    college = "Appalachian State"
  )

  player_4147 = Player(
    player_id = 4147,
    full_name = "Zack Moss",
    last_name = "Moss",
    first_name = "Zack",
    nfl_team = "BUF",
    position = "RB",
    height = "5-10",
    weight = "215",
    dob = "1997-12-15",
    college = "Utah"
  )

  player_2898 = Player(
    player_id = 2898,
    full_name = "Raheem Mostert",
    last_name = "Mostert",
    first_name = "Raheem",
    nfl_team = "SF",
    position = "RB",
    height = "5-10",
    weight = "197",
    dob = "1992-04-09",
    college = "Purdue"
  )

  player_3371 = Player(
    player_id = 3371,
    full_name = "Khalfani Muhammad",
    last_name = "Muhammad",
    first_name = "Khalfani",
    nfl_team = "DEN",
    position = "RB",
    height = "5-7",
    weight = "174",
    dob = "1994-09-26",
    college = "California"
  )

  player_2811 = Player(
    player_id = 2811,
    full_name = "Marcus Murphy",
    last_name = "Murphy",
    first_name = "Marcus",
    nfl_team = "CAR",
    position = "RB",
    height = "5-9",
    weight = "195",
    dob = "1991-10-03",
    college = "Missouri"
  )

  player_2201 = Player(
    player_id = 2201,
    full_name = "Latavius Murray",
    last_name = "Murray",
    first_name = "Latavius",
    nfl_team = "NO",
    position = "RB",
    height = "6-3",
    weight = "230",
    dob = "1990-01-18",
    college = "Central Florida"
  )

  player_4245 = Player(
    player_id = 4245,
    full_name = "Gabe Nabers",
    last_name = "Nabers",
    first_name = "Gabe",
    nfl_team = "LAC",
    position = "RB",
    height = "6-3",
    weight = "243",
    dob = "1997-11-05",
    college = "Florida State"
  )

  player_3776 = Player(
    player_id = 3776,
    full_name = "Ryan Nall",
    last_name = "Nall",
    first_name = "Ryan",
    nfl_team = "CHI",
    position = "RB",
    height = "6-2",
    weight = "237",
    dob = "1995-12-27",
    college = "Oregon State"
  )

  player_4305 = Player(
    player_id = 4305,
    full_name = "Spencer Nigh",
    last_name = "Nigh",
    first_name = "Spencer",
    nfl_team = "PIT",
    position = "RB",
    height = "6-0",
    weight = "267",
    dob = "0000-00-00",
    college = "Auburn"
  )

  player_2730 = Player(
    player_id = 2730,
    full_name = "Roosevelt Nix-Jones",
    last_name = "Nix-Jones",
    first_name = "Roosevelt",
    nfl_team = "IND",
    position = "RB",
    height = "5-11",
    weight = "248",
    dob = "1992-03-30",
    college = "Kent State"
  )

  player_3524 = Player(
    player_id = 3524,
    full_name = "Dare Ogunbowale",
    last_name = "Ogunbowale",
    first_name = "Dare",
    nfl_team = "JAC",
    position = "RB",
    height = "5-10",
    weight = "205",
    dob = "1994-05-04",
    college = "Wisconsin"
  )

  player_1990 = Player(
    player_id = 1990,
    full_name = "Jamize Olawale",
    last_name = "Olawale",
    first_name = "Jamize",
    nfl_team = "DAL",
    position = "RB",
    height = "6-1",
    weight = "242",
    dob = "1989-04-17",
    college = "North Texas"
  )

  player_3941 = Player(
    player_id = 3941,
    full_name = "Qadree Ollison",
    last_name = "Ollison",
    first_name = "Qadree",
    nfl_team = "ATL",
    position = "RB",
    height = "6-1",
    weight = "232",
    dob = "1996-09-08",
    college = "Pittsburgh"
  )

  player_4201 = Player(
    player_id = 4201,
    full_name = "Sewo Olonilua",
    last_name = "Olonilua",
    first_name = "Sewo",
    nfl_team = "DAL",
    position = "RB",
    height = "6-3",
    weight = "240",
    dob = "1997-11-27",
    college = "Texas Christian"
  )

  player_3426 = Player(
    player_id = 3426,
    full_name = "Ricky Ortiz",
    last_name = "Ortiz",
    first_name = "Ricky",
    nfl_team = "NO",
    position = "RB",
    height = "6-0",
    weight = "236",
    dob = "1994-04-15",
    college = "Oregon State"
  )

  player_4081 = Player(
    player_id = 4081,
    full_name = "Devine Ozigbo",
    last_name = "Ozigbo",
    first_name = "Devine",
    nfl_team = "JAC",
    position = "RB",
    height = "6-2",
    weight = "225",
    dob = "1996-10-02",
    college = "Nebraska"
  )

  player_4140 = Player(
    player_id = 4140,
    full_name = "Jacques Patrick",
    last_name = "Patrick",
    first_name = "Jacques",
    nfl_team = "CIN",
    position = "RB",
    height = "6-3",
    weight = "234",
    dob = "1997-01-07",
    college = "Florida State"
  )

  player_3595 = Player(
    player_id = 3595,
    full_name = "Rashaad Penny",
    last_name = "Penny",
    first_name = "Rashaad",
    nfl_team = "SEA",
    position = "RB",
    height = "5-11",
    weight = "220",
    dob = "1996-02-02",
    college = "San Diego State"
  )

  player_3173 = Player(
    player_id = 3173,
    full_name = "Elijhaa Penny",
    last_name = "Penny",
    first_name = "Elijhaa",
    nfl_team = "NYG",
    position = "RB",
    height = "6-2",
    weight = "234",
    dob = "1993-08-17",
    college = "Idaho"
  )

  player_4152 = Player(
    player_id = 4152,
    full_name = "La'Mical Perine",
    last_name = "Perine",
    first_name = "La'Mical",
    nfl_team = "NYJ",
    position = "RB",
    height = "5-11",
    weight = "220",
    dob = "1998-01-30",
    college = "Florida"
  )

  player_3300 = Player(
    player_id = 3300,
    full_name = "Samaje Perine",
    last_name = "Perine",
    first_name = "Samaje",
    nfl_team = "CIN",
    position = "RB",
    height = "5-11",
    weight = "240",
    dob = "1995-09-16",
    college = "Oklahoma"
  )

  player_3040 = Player(
    player_id = 3040,
    full_name = "Paul Perkins",
    last_name = "Perkins",
    first_name = "Paul",
    nfl_team = "JAC",
    position = "RB",
    height = "5-11",
    weight = "208",
    dob = "1994-11-16",
    college = "UCLA"
  )

  player_2581 = Player(
    player_id = 2581,
    full_name = "Senorise Perry",
    last_name = "Perry",
    first_name = "Senorise",
    nfl_team = "TEN",
    position = "RB",
    height = "6-0",
    weight = "210",
    dob = "1991-09-19",
    college = "Louisville"
  )

  player_4186 = Player(
    player_id = 4186,
    full_name = "Malcolm Perry",
    last_name = "Perry",
    first_name = "Malcolm",
    nfl_team = "MIA",
    position = "RB",
    height = "5-9",
    weight = "190",
    dob = "1997-04-19",
    college = "Navy"
  )

  player_259 = Player(
    player_id = 259,
    full_name = "Adrian Peterson",
    last_name = "Peterson",
    first_name = "Adrian",
    nfl_team = "DET",
    position = "RB",
    height = "6-1",
    weight = "220",
    dob = "1985-03-21",
    college = "Oklahoma"
  )

  player_4325 = Player(
    player_id = 4325,
    full_name = "Scottie Phillips",
    last_name = "Phillips",
    first_name = "Scottie",
    nfl_team = "HOU",
    position = "RB",
    height = "5-8",
    weight = "211",
    dob = "1997-10-06",
    college = "Mississippi"
  )

  player_4307 = Player(
    player_id = 4307,
    full_name = "Artavis Pierce",
    last_name = "Pierce",
    first_name = "Artavis",
    nfl_team = "CHI",
    position = "RB",
    height = "5-11",
    weight = "208",
    dob = "1996-05-17",
    college = "Oregon State"
  )

  player_4373 = Player(
    player_id = 4373,
    full_name = "Sandro Platzgummer",
    last_name = "Platzgummer",
    first_name = "Sandro",
    nfl_team = "NYG",
    position = "RB",
    height = "5-11",
    weight = "197",
    dob = "1997-03-10",
    college = "No College"
  )

  player_3866 = Player(
    player_id = 3866,
    full_name = "Tony Pollard",
    last_name = "Pollard",
    first_name = "Tony",
    nfl_team = "DAL",
    position = "RB",
    height = "6-0",
    weight = "209",
    dob = "1997-04-30",
    college = "Memphis"
  )

  player_3265 = Player(
    player_id = 3265,
    full_name = "Troymaine Pope",
    last_name = "Pope",
    first_name = "Troymaine",
    nfl_team = "LAC",
    position = "RB",
    height = "5-9",
    weight = "205",
    dob = "1993-11-26",
    college = "Jacksonville State"
  )

  player_3069 = Player(
    player_id = 3069,
    full_name = "C.J. Prosise",
    last_name = "Prosise",
    first_name = "C.J.",
    nfl_team = "HOU",
    position = "RB",
    height = "6-1",
    weight = "225",
    dob = "1994-05-20",
    college = "Notre Dame"
  )

  player_4287 = Player(
    player_id = 4287,
    full_name = "Bronson Rechsteiner",
    last_name = "Rechsteiner",
    first_name = "Bronson",
    nfl_team = "BAL",
    position = "RB",
    height = "6-0",
    weight = "230",
    dob = "1997-10-24",
    college = "Kennesaw State"
  )

  player_3976 = Player(
    player_id = 3976,
    full_name = "Craig Reynolds",
    last_name = "Reynolds",
    first_name = "Craig",
    nfl_team = "ATL",
    position = "RB",
    height = "5-11",
    weight = "215",
    dob = "1996-06-15",
    college = "Kutztown"
  )

  player_3846 = Player(
    player_id = 3846,
    full_name = "Patrick Ricard",
    last_name = "Ricard",
    first_name = "Patrick",
    nfl_team = "BAL",
    position = "RB",
    height = "6-3",
    weight = "311",
    dob = "1994-05-27",
    college = "Maine"
  )

  player_3156 = Player(
    player_id = 3156,
    full_name = "Jalen Richard",
    last_name = "Richard",
    first_name = "Jalen",
    nfl_team = "LV",
    position = "RB",
    height = "5-8",
    weight = "207",
    dob = "1993-10-15",
    college = "Southern Mississippi"
  )

  player_2305 = Player(
    player_id = 2305,
    full_name = "Theo Riddick",
    last_name = "Riddick",
    first_name = "Theo",
    nfl_team = "LV",
    position = "RB",
    height = "5-9",
    weight = "201",
    dob = "1991-05-04",
    college = "Notre Dame"
  )

  player_4336 = Player(
    player_id = 4336,
    full_name = "James Robinson",
    last_name = "Robinson",
    first_name = "James",
    nfl_team = "JAC",
    position = "RB",
    height = "5-10",
    weight = "220",
    dob = "1998-08-09",
    college = "Illinois State"
  )

  player_3657 = Player(
    player_id = 3657,
    full_name = "Jaylen Samuels",
    last_name = "Samuels",
    first_name = "Jaylen",
    nfl_team = "PIT",
    position = "RB",
    height = "6-0",
    weight = "225",
    dob = "1996-07-20",
    college = "North Carolina State"
  )

  player_3871 = Player(
    player_id = 3871,
    full_name = "Miles Sanders",
    last_name = "Sanders",
    first_name = "Miles",
    nfl_team = "PHI",
    position = "RB",
    height = "5-11",
    weight = "211",
    dob = "1997-05-01",
    college = "Penn State"
  )

  player_3629 = Player(
    player_id = 3629,
    full_name = "Bo Scarbrough",
    last_name = "Scarbrough",
    first_name = "Bo",
    nfl_team = "DET",
    position = "RB",
    height = "6-1",
    weight = "235",
    dob = "1996-09-29",
    college = "Alabama"
  )

  player_3943 = Player(
    player_id = 3943,
    full_name = "Jordan Scarlett",
    last_name = "Scarlett",
    first_name = "Jordan",
    nfl_team = "CAR",
    position = "RB",
    height = "5-11",
    weight = "210",
    dob = "1995-07-08",
    college = "Florida"
  )

  player_4344 = Player(
    player_id = 4344,
    full_name = "Cameron Scarlett",
    last_name = "Scarlett",
    first_name = "Cameron",
    nfl_team = "TEN",
    position = "RB",
    height = "6-0",
    weight = "219",
    dob = "0000-00-00",
    college = "Stanford"
  )

  player_3676 = Player(
    player_id = 3676,
    full_name = "Boston Scott",
    last_name = "Scott",
    first_name = "Boston",
    nfl_team = "PHI",
    position = "RB",
    height = "5-6",
    weight = "203",
    dob = "1995-04-27",
    college = "Louisiana Tech"
  )

  player_4311 = Player(
    player_id = 4311,
    full_name = "Luke Sellers",
    last_name = "Sellers",
    first_name = "Luke",
    nfl_team = "DET",
    position = "RB",
    height = "6-1",
    weight = "250",
    dob = "0000-00-00",
    college = "South Dakota State"
  )

  player_1427 = Player(
    player_id = 1427,
    full_name = "Anthony Sherman",
    last_name = "Sherman",
    first_name = "Anthony",
    nfl_team = "KC",
    position = "RB",
    height = "5-10",
    weight = "242",
    dob = "1988-12-11",
    college = "Connecticut"
  )

  player_3855 = Player(
    player_id = 3855,
    full_name = "Devin Singletary",
    last_name = "Singletary",
    first_name = "Devin",
    nfl_team = "BUF",
    position = "RB",
    height = "5-7",
    weight = "203",
    dob = "1997-09-03",
    college = "Florida Atlantic"
  )

  player_4337 = Player(
    player_id = 4337,
    full_name = "Connor Slomka",
    last_name = "Slomka",
    first_name = "Connor",
    nfl_team = "JAC",
    position = "RB",
    height = "6-0",
    weight = "240",
    dob = "0000-00-00",
    college = "Army"
  )

  player_3045 = Player(
    player_id = 3045,
    full_name = "Wendell Smallwood",
    last_name = "Smallwood",
    first_name = "Wendell",
    nfl_team = "PIT",
    position = "RB",
    height = "5-10",
    weight = "208",
    dob = "1994-01-20",
    college = "West Virginia"
  )

  player_4356 = Player(
    player_id = 4356,
    full_name = "Rodney Smith",
    last_name = "Smith",
    first_name = "Rodney",
    nfl_team = "CAR",
    position = "RB",
    height = "5-11",
    weight = "210",
    dob = "1996-02-28",
    college = "Minnesota"
  )

  player_3673 = Player(
    player_id = 3673,
    full_name = "Ito Smith",
    last_name = "Smith",
    first_name = "Ito",
    nfl_team = "ATL",
    position = "RB",
    height = "5-9",
    weight = "195",
    dob = "1995-09-11",
    college = "Southern Mississippi"
  )

  player_2934 = Player(
    player_id = 2934,
    full_name = "Rod Smith",
    last_name = "Smith",
    first_name = "Rod",
    nfl_team = "LV",
    position = "RB",
    height = "6-3",
    weight = "235",
    dob = "1992-01-10",
    college = "Ohio State"
  )

  player_3263 = Player(
    player_id = 3263,
    full_name = "Keith Smith",
    last_name = "Smith",
    first_name = "Keith",
    nfl_team = "ATL",
    position = "RB",
    height = "6-0",
    weight = "240",
    dob = "1992-04-08",
    college = "San Jose State"
  )

  player_3917 = Player(
    player_id = 3917,
    full_name = "Benny Snell Jr",
    last_name = "Snell Jr",
    first_name = "Benny",
    nfl_team = "PIT",
    position = "RB",
    height = "5-10",
    weight = "223",
    dob = "1998-02-26",
    college = "Kentucky"
  )

  player_3443 = Player(
    player_id = 3443,
    full_name = "William Stanback",
    last_name = "Stanback",
    first_name = "William",
    nfl_team = "LV",
    position = "RB",
    height = "6-0",
    weight = "231",
    dob = "1994-07-06",
    college = "Virginia Union"
  )

  player_3792 = Player(
    player_id = 3792,
    full_name = "Johnny Stanton",
    last_name = "Stanton",
    first_name = "Johnny",
    nfl_team = "CLE",
    position = "RB",
    height = "6-2",
    weight = "240",
    dob = "1994-09-07",
    college = "UNLV"
  )

  player_4171 = Player(
    player_id = 4171,
    full_name = "D'Andre Swift",
    last_name = "Swift",
    first_name = "D'Andre",
    nfl_team = "DET",
    position = "RB",
    height = "5-10",
    weight = "211",
    dob = "1999-01-14",
    college = "Georgia"
  )

  player_4369 = Player(
    player_id = 4369,
    full_name = "JJ Taylor",
    last_name = "Taylor",
    first_name = "JJ",
    nfl_team = "NE",
    position = "RB",
    height = "5-6",
    weight = "185",
    dob = "1998-01-04",
    college = "Arizona"
  )

  player_4175 = Player(
    player_id = 4175,
    full_name = "Jonathan Taylor",
    last_name = "Taylor",
    first_name = "Jonathan",
    nfl_team = "IND",
    position = "RB",
    height = "5-11",
    weight = "221",
    dob = "1999-01-19",
    college = "Wisconsin"
  )

  player_4315 = Player(
    player_id = 4315,
    full_name = "Patrick Taylor Jr",
    last_name = "Taylor Jr",
    first_name = "Patrick",
    nfl_team = "GB",
    position = "RB",
    height = "6-2",
    weight = "217",
    dob = "1998-04-29",
    college = "Memphis"
  )

  player_3886 = Player(
    player_id = 3886,
    full_name = "Darwin Thompson",
    last_name = "Thompson",
    first_name = "Darwin",
    nfl_team = "KC",
    position = "RB",
    height = "5-8",
    weight = "200",
    dob = "1997-02-12",
    college = "Utah State"
  )

  player_2176 = Player(
    player_id = 2176,
    full_name = "Chris Thompson",
    last_name = "Thompson",
    first_name = "Chris",
    nfl_team = "JAC",
    position = "RB",
    height = "5-8",
    weight = "195",
    dob = "1990-10-20",
    college = "Florida State"
  )

  player_3752 = Player(
    player_id = 3752,
    full_name = "Mark Thompson",
    last_name = "Thompson",
    first_name = "Mark",
    nfl_team = "LV",
    position = "RB",
    height = "6-1",
    weight = "235",
    dob = "1994-12-09",
    college = "Florida"
  )

  player_3753 = Player(
    player_id = 3753,
    full_name = "De'Lance Turner",
    last_name = "Turner",
    first_name = "De'Lance",
    nfl_team = "MIA",
    position = "RB",
    height = "5-11",
    weight = "214",
    dob = "1995-08-23",
    college = "Alcorn State"
  )

  player_4180 = Player(
    player_id = 4180,
    full_name = "Ke'Shawn Vaughn",
    last_name = "Vaughn",
    first_name = "Ke'Shawn",
    nfl_team = "TB",
    position = "RB",
    height = "5-10",
    weight = "215",
    dob = "1997-05-04",
    college = "Vanderbilt"
  )

  player_3120 = Player(
    player_id = 3120,
    full_name = "Dan Vitale",
    last_name = "Vitale",
    first_name = "Dan",
    nfl_team = "NE",
    position = "RB",
    height = "6-0",
    weight = "239",
    dob = "1993-10-26",
    college = "Northwestern"
  )

  player_3849 = Player(
    player_id = 3849,
    full_name = "Christian Wade",
    last_name = "Wade",
    first_name = "Christian",
    nfl_team = "BUF",
    position = "RB",
    height = "5-9",
    weight = "196",
    dob = "1991-05-15",
    college = "No College"
  )

  player_4249 = Player(
    player_id = 4249,
    full_name = "Jonathan Ward",
    last_name = "Ward",
    first_name = "Jonathan",
    nfl_team = "ARI",
    position = "RB",
    height = "6-0",
    weight = "202",
    dob = "1997-09-30",
    college = "Central Michigan"
  )

  player_4108 = Player(
    player_id = 4108,
    full_name = "Aca'Cedric Ware",
    last_name = "Ware",
    first_name = "Aca'Cedric",
    nfl_team = "TB",
    position = "RB",
    height = "6-0",
    weight = "205",
    dob = "1997-06-29",
    college = "USC"
  )

  player_4214 = Player(
    player_id = 4214,
    full_name = "Michael Warren II",
    last_name = "Warren II",
    first_name = "Michael",
    nfl_team = "PHI",
    position = "RB",
    height = "5-11",
    weight = "224",
    dob = "1998-11-12",
    college = "Cincinnati"
  )

  player_3094 = Player(
    player_id = 3094,
    full_name = "Dwayne Washington",
    last_name = "Washington",
    first_name = "Dwayne",
    nfl_team = "NO",
    position = "RB",
    height = "6-1",
    weight = "223",
    dob = "1994-04-24",
    college = "Washington"
  )

  player_3060 = Player(
    player_id = 3060,
    full_name = "DeAndre Washington",
    last_name = "Washington",
    first_name = "DeAndre",
    nfl_team = "KC",
    position = "RB",
    height = "5-8",
    weight = "210",
    dob = "1993-02-22",
    college = "Texas Tech"
  )

  player_3062 = Player(
    player_id = 3062,
    full_name = "Derek Watt",
    last_name = "Watt",
    first_name = "Derek",
    nfl_team = "PIT",
    position = "RB",
    height = "6-2",
    weight = "234",
    dob = "1992-11-07",
    college = "Wisconsin"
  )

  player_3686 = Player(
    player_id = 3686,
    full_name = "Ralph Webb",
    last_name = "Webb",
    first_name = "Ralph",
    nfl_team = "PIT",
    position = "RB",
    height = "5-10",
    weight = "200",
    dob = "1994-11-21",
    college = "Vanderbilt"
  )

  player_3867 = Player(
    player_id = 3867,
    full_name = "Mike Weber",
    last_name = "Weber",
    first_name = "Mike",
    nfl_team = "KC",
    position = "RB",
    height = "5-10",
    weight = "210",
    dob = "1997-08-27",
    college = "Ohio State"
  )

  player_3706 = Player(
    player_id = 3706,
    full_name = "Elijah Wellman",
    last_name = "Wellman",
    first_name = "Elijah",
    nfl_team = "GB",
    position = "RB",
    height = "6-1",
    weight = "241",
    dob = "1994-09-20",
    college = "West Virginia"
  )

  player_4295 = Player(
    player_id = 4295,
    full_name = "Devwah Whaley",
    last_name = "Whaley",
    first_name = "Devwah",
    nfl_team = "CIN",
    position = "RB",
    height = "5-10",
    weight = "211",
    dob = "1997-11-03",
    college = "Arkansas"
  )

  player_2444 = Player(
    player_id = 2444,
    full_name = "James White",
    last_name = "White",
    first_name = "James",
    nfl_team = "NE",
    position = "RB",
    height = "5-10",
    weight = "205",
    dob = "1992-02-03",
    college = "Wisconsin"
  )

  player_3921 = Player(
    player_id = 3921,
    full_name = "Kerrith Whyte",
    last_name = "Whyte",
    first_name = "Kerrith",
    nfl_team = "PIT",
    position = "RB",
    height = "5-10",
    weight = "204",
    dob = "1996-10-31",
    college = "Florida Atlantic"
  )

  player_3668 = Player(
    player_id = 3668,
    full_name = "Jordan Wilkins",
    last_name = "Wilkins",
    first_name = "Jordan",
    nfl_team = "IND",
    position = "RB",
    height = "6-1",
    weight = "217",
    dob = "1994-07-18",
    college = "Mississippi"
  )

  player_1542 = Player(
    player_id = 1542,
    full_name = "Jonathan Williams",
    last_name = "Williams",
    first_name = "Jonathan",
    nfl_team = "DET",
    position = "RB",
    height = "6-0",
    weight = "217",
    dob = "1994-02-02",
    college = "Arkansas"
  )

  player_3351 = Player(
    player_id = 3351,
    full_name = "Jamaal Williams",
    last_name = "Williams",
    first_name = "Jamaal",
    nfl_team = "GB",
    position = "RB",
    height = "6-0",
    weight = "213",
    dob = "1995-04-03",
    college = "Brigham Young"
  )

  player_3913 = Player(
    player_id = 3913,
    full_name = "Trayveon Williams",
    last_name = "Williams",
    first_name = "Trayveon",
    nfl_team = "CIN",
    position = "RB",
    height = "5-8",
    weight = "206",
    dob = "1997-10-18",
    college = "Texas A&amp;M"
  )

  player_3927 = Player(
    player_id = 3927,
    full_name = "Dexter Williams",
    last_name = "Williams",
    first_name = "Dexter",
    nfl_team = "GB",
    position = "RB",
    height = "5-11",
    weight = "212",
    dob = "1997-01-06",
    college = "Notre Dame"
  )

  player_4183 = Player(
    player_id = 4183,
    full_name = "Antonio Williams",
    last_name = "Williams",
    first_name = "Antonio",
    nfl_team = "BUF",
    position = "RB",
    height = "5-11",
    weight = "210",
    dob = "1997-10-22",
    college = "North Carolina"
  )

  player_3712 = Player(
    player_id = 3712,
    full_name = "Darrel Williams",
    last_name = "Williams",
    first_name = "Darrel",
    nfl_team = "KC",
    position = "RB",
    height = "5-11",
    weight = "224",
    dob = "1995-04-15",
    college = "Louisiana State"
  )

  player_2435 = Player(
    player_id = 2435,
    full_name = "Damien Williams",
    last_name = "Williams",
    first_name = "Damien",
    nfl_team = "KC",
    position = "RB",
    height = "5-11",
    weight = "224",
    dob = "1992-04-03",
    college = "Oklahoma"
  )

  player_4288 = Player(
    player_id = 4288,
    full_name = "Ty'Son Williams",
    last_name = "Williams",
    first_name = "Ty'Son",
    nfl_team = "BAL",
    position = "RB",
    height = "6-0",
    weight = "220",
    dob = "1996-09-04",
    college = "Brigham Young"
  )

  player_3740 = Player(
    player_id = 3740,
    full_name = "Jeff Wilson",
    last_name = "Wilson",
    first_name = "Jeff",
    nfl_team = "SF",
    position = "RB",
    height = "6-0",
    weight = "194",
    dob = "1995-11-16",
    college = "North Texas"
  )

  player_3835 = Player(
    player_id = 3835,
    full_name = "Shaun Wilson",
    last_name = "Wilson",
    first_name = "Shaun",
    nfl_team = "TEN",
    position = "RB",
    height = "5-9",
    weight = "185",
    dob = "1995-12-02",
    college = "Duke"
  )

  player_2878 = Player(
    player_id = 2878,
    full_name = "T.J. Yeldon",
    last_name = "Yeldon",
    first_name = "T.J.",
    nfl_team = "BUF",
    position = "RB",
    height = "6-1",
    weight = "223",
    dob = "1993-10-02",
    college = "Alabama"
  )

  player_3355 = Player(
    player_id = 3355,
    full_name = "Rodney Adams",
    last_name = "Adams",
    first_name = "Rodney",
    nfl_team = "CHI",
    position = "WR",
    height = "6-1",
    weight = "189",
    dob = "1994-09-15",
    college = "South Florida"
  )

  player_2596 = Player(
    player_id = 2596,
    full_name = "Davante Adams",
    last_name = "Adams",
    first_name = "Davante",
    nfl_team = "GB",
    position = "WR",
    height = "6-1",
    weight = "215",
    dob = "1992-12-24",
    college = "Fresno State"
  )

  player_3344 = Player(
    player_id = 3344,
    full_name = "Bralon Addison",
    last_name = "Addison",
    first_name = "Bralon",
    nfl_team = "MIN",
    position = "WR",
    height = "5-9",
    weight = "197",
    dob = "1993-10-12",
    college = "Oregon"
  )

  player_3427 = Player(
    player_id = 3427,
    full_name = "Quincy Adeboyejo",
    last_name = "Adeboyejo",
    first_name = "Quincy",
    nfl_team = "NE",
    position = "WR",
    height = "6-3",
    weight = "200",
    dob = "1995-05-26",
    college = "Ole Miss"
  )

  player_2744 = Player(
    player_id = 2744,
    full_name = "Nelson Agholor",
    last_name = "Agholor",
    first_name = "Nelson",
    nfl_team = "LV",
    position = "WR",
    height = "6-0",
    weight = "198",
    dob = "1993-05-24",
    college = "Southern California"
  )

  player_4381 = Player(
    player_id = 4381,
    full_name = "Jamal Agnew",
    last_name = "Agnew",
    first_name = "Jamal",
    nfl_team = "DET",
    position = "WR",
    height = "5-10",
    weight = "190",
    dob = "1995-04-03",
    college = "San Diego"
  )

  player_4136 = Player(
    player_id = 4136,
    full_name = "Brandon Aiyuk",
    last_name = "Aiyuk",
    first_name = "Brandon",
    nfl_team = "SF",
    position = "WR",
    height = "6-1",
    weight = "206",
    dob = "1998-03-17",
    college = "Arizona State"
  )

  player_2215 = Player(
    player_id = 2215,
    full_name = "Keenan Allen",
    last_name = "Allen",
    first_name = "Keenan",
    nfl_team = "LAC",
    position = "WR",
    height = "6-2",
    weight = "211",
    dob = "1992-04-27",
    college = "California"
  )

  player_3223 = Player(
    player_id = 3223,
    full_name = "Geronimo Allison",
    last_name = "Allison",
    first_name = "Geronimo",
    nfl_team = "DET",
    position = "WR",
    height = "6-3",
    weight = "202",
    dob = "1994-01-18",
    college = "Illinois"
  )

  player_323 = Player(
    player_id = 323,
    full_name = "Danny Amendola",
    last_name = "Amendola",
    first_name = "Danny",
    nfl_team = "DET",
    position = "WR",
    height = "5-11",
    weight = "185",
    dob = "1985-11-02",
    college = "Texas Tech"
  )

  player_3259 = Player(
    player_id = 3259,
    full_name = "Robby Anderson",
    last_name = "Anderson",
    first_name = "Robby",
    nfl_team = "CAR",
    position = "WR",
    height = "6-3",
    weight = "190",
    dob = "1993-05-09",
    college = "Temple"
  )

  player_3872 = Player(
    player_id = 3872,
    full_name = "JJ Arcega-Whiteside",
    last_name = "Arcega-Whiteside",
    first_name = "JJ",
    nfl_team = "PHI",
    position = "WR",
    height = "6-2",
    weight = "225",
    dob = "1996-12-31",
    college = "Stanford"
  )

  player_3639 = Player(
    player_id = 3639,
    full_name = "Marcell Ateman",
    last_name = "Ateman",
    first_name = "Marcell",
    nfl_team = "LV",
    position = "WR",
    height = "6-4",
    weight = "215",
    dob = "1994-09-16",
    college = "Oklahoma State"
  )

  player_2257 = Player(
    player_id = 2257,
    full_name = "Tavon Austin",
    last_name = "Austin",
    first_name = "Tavon",
    nfl_team = "SF",
    position = "WR",
    height = "5-8",
    weight = "179",
    dob = "1990-03-15",
    college = "West Virginia"
  )

  player_4230 = Player(
    player_id = 4230,
    full_name = "Andre Baccellia",
    last_name = "Baccellia",
    first_name = "Andre",
    nfl_team = "NE",
    position = "WR",
    height = "5-10",
    weight = "175",
    dob = "0000-00-00",
    college = "Washington"
  )

  player_4009 = Player(
    player_id = 4009,
    full_name = "Alex Bachman",
    last_name = "Bachman",
    first_name = "Alex",
    nfl_team = "NYG",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1996-05-29",
    college = "Wake Forest"
  )

  player_4215 = Player(
    player_id = 4215,
    full_name = "Manasseh Bailey",
    last_name = "Bailey",
    first_name = "Manasseh",
    nfl_team = "PHI",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1997-06-27",
    college = "Morgan State"
  )

  player_3809 = Player(
    player_id = 3809,
    full_name = "Cameron Batson",
    last_name = "Batson",
    first_name = "Cameron",
    nfl_team = "TEN",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "1995-12-20",
    college = "Texas Tech"
  )

  player_4357 = Player(
    player_id = 4357,
    full_name = "Omar Bayless",
    last_name = "Bayless",
    first_name = "Omar",
    nfl_team = "CAR",
    position = "WR",
    height = "6-1",
    weight = "210",
    dob = "1996-12-15",
    college = "Arkansas State"
  )

  player_1787 = Player(
    player_id = 1787,
    full_name = "Cole Beasley",
    last_name = "Beasley",
    first_name = "Cole",
    nfl_team = "BUF",
    position = "WR",
    height = "5-8",
    weight = "174",
    dob = "1989-04-26",
    college = "Southern Methodist"
  )

  player_2465 = Player(
    player_id = 2465,
    full_name = "Odell Beckham Jr.",
    last_name = "Beckham Jr.",
    first_name = "Odell",
    nfl_team = "CLE",
    position = "WR",
    height = "5-11",
    weight = "198",
    dob = "1992-11-05",
    college = "Louisiana State"
  )

  player_3794 = Player(
    player_id = 3794,
    full_name = "Chad Beebe",
    last_name = "Beebe",
    first_name = "Chad",
    nfl_team = "MIN",
    position = "WR",
    height = "5-10",
    weight = "185",
    dob = "1994-06-01",
    college = "Northern Illinois"
  )

  player_4128 = Player(
    player_id = 4128,
    full_name = "Reggie Begelton",
    last_name = "Begelton",
    first_name = "Reggie",
    nfl_team = "GB",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1993-08-31",
    college = "Lamar"
  )

  player_2006 = Player(
    player_id = 2006,
    full_name = "Josh Bellamy",
    last_name = "Bellamy",
    first_name = "Josh",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-0",
    weight = "208",
    dob = "1989-05-18",
    college = "Louisville"
  )

  player_1883 = Player(
    player_id = 1883,
    full_name = "Travis Benjamin",
    last_name = "Benjamin",
    first_name = "Travis",
    nfl_team = "SF",
    position = "WR",
    height = "5-10",
    weight = "175",
    dob = "1989-12-29",
    college = "Miami (FL)"
  )

  player_3881 = Player(
    player_id = 3881,
    full_name = "Trinity Benson",
    last_name = "Benson",
    first_name = "Trinity",
    nfl_team = "DEN",
    position = "WR",
    height = "6-0",
    weight = "180",
    dob = "1997-01-16",
    college = "East Central"
  )

  player_3624 = Player(
    player_id = 3624,
    full_name = "Braxton Berrios",
    last_name = "Berrios",
    first_name = "Braxton",
    nfl_team = "NYJ",
    position = "WR",
    height = "5-9",
    weight = "190",
    dob = "1995-10-06",
    college = "Miami"
  )

  player_3720 = Player(
    player_id = 3720,
    full_name = "Saeed Blacknall",
    last_name = "Blacknall",
    first_name = "Saeed",
    nfl_team = "PIT",
    position = "WR",
    height = "6-2",
    weight = "208",
    dob = "1996-03-17",
    college = "Penn State"
  )

  player_3819 = Player(
    player_id = 3819,
    full_name = "Christian Blake",
    last_name = "Blake",
    first_name = "Christian",
    nfl_team = "ATL",
    position = "WR",
    height = "6-1",
    weight = "181",
    dob = "1996-06-08",
    college = "Northern Illinois"
  )

  player_3428 = Player(
    player_id = 3428,
    full_name = "C.J. Board",
    last_name = "Board",
    first_name = "C.J.",
    nfl_team = "NYG",
    position = "WR",
    height = "6-1",
    weight = "180",
    dob = "1993-12-12",
    college = "Chattanooga"
  )

  player_3417 = Player(
    player_id = 3417,
    full_name = "Victor Bolden Jr.",
    last_name = "Bolden Jr.",
    first_name = "Victor",
    nfl_team = "DET",
    position = "WR",
    height = "5-8",
    weight = "178",
    dob = "1995-04-04",
    college = "Oregon State"
  )

  player_3418 = Player(
    player_id = 3418,
    full_name = "Kendrick Bourne",
    last_name = "Bourne",
    first_name = "Kendrick",
    nfl_team = "SF",
    position = "WR",
    height = "6-1",
    weight = "203",
    dob = "1995-08-04",
    college = "Eastern Washington"
  )

  player_4158 = Player(
    player_id = 4158,
    full_name = "Lynn Bowden Jr",
    last_name = "Bowden Jr",
    first_name = "Lynn",
    nfl_team = "MIA",
    position = "WR",
    height = "6-0",
    weight = "201",
    dob = "1997-10-14",
    college = "Kentucky"
  )

  player_3081 = Player(
    player_id = 3081,
    full_name = "Tyler Boyd",
    last_name = "Boyd",
    first_name = "Tyler",
    nfl_team = "CIN",
    position = "WR",
    height = "6-2",
    weight = "203",
    dob = "1994-11-15",
    college = "Pittsburgh"
  )

  player_3909 = Player(
    player_id = 3909,
    full_name = "Miles Boykin",
    last_name = "Boykin",
    first_name = "Miles",
    nfl_team = "BAL",
    position = "WR",
    height = "6-4",
    weight = "220",
    dob = "1996-10-12",
    college = "Notre Dame"
  )

  player_4301 = Player(
    player_id = 4301,
    full_name = "Ja'Marcus Bradley",
    last_name = "Bradley",
    first_name = "Ja'Marcus",
    nfl_team = "CLE",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1996-12-11",
    college = "Louisiana-Lafayette"
  )

  player_4250 = Player(
    player_id = 4250,
    full_name = "Jermiah Braswell",
    last_name = "Braswell",
    first_name = "Jermiah",
    nfl_team = "ARI",
    position = "WR",
    height = "6-0",
    weight = "210",
    dob = "1997-05-15",
    college = "Youngstown State"
  )

  player_3910 = Player(
    player_id = 3910,
    full_name = "Marquise Brown",
    last_name = "Brown",
    first_name = "Marquise",
    nfl_team = "BAL",
    position = "WR",
    height = "5-9",
    weight = "170",
    dob = "1997-06-04",
    college = "Oklahoma"
  )

  player_3939 = Player(
    player_id = 3939,
    full_name = "AJ Brown",
    last_name = "Brown",
    first_name = "AJ",
    nfl_team = "TEN",
    position = "WR",
    height = "6-0",
    weight = "226",
    dob = "1997-06-30",
    college = "Mississippi"
  )

  player_3747 = Player(
    player_id = 3747,
    full_name = "Fred Brown",
    last_name = "Brown",
    first_name = "Fred",
    nfl_team = "DEN",
    position = "WR",
    height = "6-1",
    weight = "196",
    dob = "1993-12-01",
    college = "Mississippi State"
  )

  player_2223 = Player(
    player_id = 2223,
    full_name = "Jaron Brown",
    last_name = "Brown",
    first_name = "Jaron",
    nfl_team = "SF",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1990-01-08",
    college = "Clemson"
  )

  player_4302 = Player(
    player_id = 4302,
    full_name = "Tony Brown",
    last_name = "Brown",
    first_name = "Tony",
    nfl_team = "WAS",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1997-08-08",
    college = "Colorado"
  )

  player_3290 = Player(
    player_id = 3290,
    full_name = "Noah Brown",
    last_name = "Brown",
    first_name = "Noah",
    nfl_team = "DAL",
    position = "WR",
    height = "6-2",
    weight = "225",
    dob = "1996-01-06",
    college = "Ohio State"
  )

  player_2523 = Player(
    player_id = 2523,
    full_name = "John Brown",
    last_name = "Brown",
    first_name = "John",
    nfl_team = "BUF",
    position = "WR",
    height = "5-11",
    weight = "179",
    dob = "1990-04-03",
    college = "Pittsburg State"
  )

  player_4025 = Player(
    player_id = 4025,
    full_name = "Ventell Bryant",
    last_name = "Bryant",
    first_name = "Ventell",
    nfl_team = "DAL",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1996-08-24",
    college = "Temple"
  )

  player_3810 = Player(
    player_id = 3810,
    full_name = "Deontay Burnett",
    last_name = "Burnett",
    first_name = "Deontay",
    nfl_team = "PHI",
    position = "WR",
    height = "6-0",
    weight = "186",
    dob = "1997-10-04",
    college = "Southern California"
  )

  player_3894 = Player(
    player_id = 3894,
    full_name = "Hakeem Butler",
    last_name = "Butler",
    first_name = "Hakeem",
    nfl_team = "PHI",
    position = "WR",
    height = "6-5",
    weight = "227",
    dob = "1996-05-16",
    college = "Iowa State"
  )

  player_3954 = Player(
    player_id = 3954,
    full_name = "Emmanuel Butler",
    last_name = "Butler",
    first_name = "Emmanuel",
    nfl_team = "NO",
    position = "WR",
    height = "6-4",
    weight = "220",
    dob = "1996-08-27",
    college = "Northern Arizona"
  )

  player_3016 = Player(
    player_id = 3016,
    full_name = "Damiere Byrd",
    last_name = "Byrd",
    first_name = "Damiere",
    nfl_team = "NE",
    position = "WR",
    height = "5-9",
    weight = "180",
    dob = "1993-01-27",
    college = "South Carolina"
  )

  player_4251 = Player(
    player_id = 4251,
    full_name = "Cedric Byrd II",
    last_name = "Byrd II",
    first_name = "Cedric",
    nfl_team = "ARI",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "0000-00-00",
    college = "Hawai&#x27;i&#x27;"
  )

  player_4196 = Player(
    player_id = 4196,
    full_name = "Lawrence Cager",
    last_name = "Cager",
    first_name = "Lawrence",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-5",
    weight = "220",
    dob = "1997-08-20",
    college = "Georgia"
  )

  player_3669 = Player(
    player_id = 3669,
    full_name = "Deon Cain",
    last_name = "Cain",
    first_name = "Deon",
    nfl_team = "PIT",
    position = "WR",
    height = "6-2",
    weight = "202",
    dob = "1996-08-09",
    college = "Clemson"
  )

  player_4363 = Player(
    player_id = 4363,
    full_name = "Marquez Callaway",
    last_name = "Callaway",
    first_name = "Marquez",
    nfl_team = "NO",
    position = "WR",
    height = "6-2",
    weight = "204",
    dob = "1998-03-27",
    college = "Tennessee"
  )

  player_3935 = Player(
    player_id = 3935,
    full_name = "Parris Campbell",
    last_name = "Campbell",
    first_name = "Parris",
    nfl_team = "IND",
    position = "WR",
    height = "6-0",
    weight = "205",
    dob = "1997-07-16",
    college = "Ohio State"
  )

  player_4197 = Player(
    player_id = 4197,
    full_name = "George Campbell",
    last_name = "Campbell",
    first_name = "George",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-4",
    weight = "183",
    dob = "1996-10-12",
    college = "West Virginia"
  )

  player_3402 = Player(
    player_id = 3402,
    full_name = "Austin Carr",
    last_name = "Carr",
    first_name = "Austin",
    nfl_team = "NO",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1993-12-25",
    college = "Northwestern"
  )

  player_2840 = Player(
    player_id = 2840,
    full_name = "DeAndre Carter",
    last_name = "Carter",
    first_name = "DeAndre",
    nfl_team = "HOU",
    position = "WR",
    height = "5-8",
    weight = "190",
    dob = "1993-04-10",
    college = "Sacramento State"
  )

  player_4312 = Player(
    player_id = 4312,
    full_name = "Quintez Cephus",
    last_name = "Cephus",
    first_name = "Quintez",
    nfl_team = "DET",
    position = "WR",
    height = "6-1",
    weight = "205",
    dob = "1998-04-01",
    college = "Wisconsin"
  )

  player_3609 = Player(
    player_id = 3609,
    full_name = "D.J. Chark",
    last_name = "Chark",
    first_name = "D.J.",
    nfl_team = "JAC",
    position = "WR",
    height = "6-4",
    weight = "198",
    dob = "1996-09-23",
    college = "Louisiana State"
  )

  player_3314 = Player(
    player_id = 3314,
    full_name = "Jehu Chesson",
    last_name = "Chesson",
    first_name = "Jehu",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-2",
    weight = "204",
    dob = "1993-01-29",
    college = "Michigan"
  )

  player_4319 = Player(
    player_id = 4319,
    full_name = "Dan Chisena",
    last_name = "Chisena",
    first_name = "Dan",
    nfl_team = "MIN",
    position = "WR",
    height = "6-3",
    weight = "202",
    dob = "1997-02-25",
    college = "Penn State"
  )

  player_4169 = Player(
    player_id = 4169,
    full_name = "Chase Claypool",
    last_name = "Claypool",
    first_name = "Chase",
    nfl_team = "PIT",
    position = "WR",
    height = "6-4",
    weight = "227",
    dob = "1998-07-07",
    college = "Notre Dame"
  )

  player_4227 = Player(
    player_id = 4227,
    full_name = "Tyrie Cleveland",
    last_name = "Cleveland",
    first_name = "Tyrie",
    nfl_team = "DEN",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1997-09-20",
    college = "Florida"
  )

  player_1437 = Player(
    player_id = 1437,
    full_name = "Randall Cobb",
    last_name = "Cobb",
    first_name = "Randall",
    nfl_team = "HOU",
    position = "WR",
    height = "5-10",
    weight = "192",
    dob = "1990-08-22",
    college = "Kentucky"
  )

  player_4187 = Player(
    player_id = 4187,
    full_name = "Matthew Cole",
    last_name = "Cole",
    first_name = "Matthew",
    nfl_team = "MIA",
    position = "WR",
    height = "5-10",
    weight = "200",
    dob = "1996-11-07",
    college = "McKendree"
  )

  player_3534 = Player(
    player_id = 3534,
    full_name = "Keelan Cole",
    last_name = "Cole",
    first_name = "Keelan",
    nfl_team = "JAC",
    position = "WR",
    height = "6-1",
    weight = "194",
    dob = "1993-04-20",
    college = "Kentucky Wesleyan"
  )

  player_3084 = Player(
    player_id = 3084,
    full_name = "Corey Coleman",
    last_name = "Coleman",
    first_name = "Corey",
    nfl_team = "NYG",
    position = "WR",
    height = "5-11",
    weight = "185",
    dob = "1994-07-06",
    college = "Baylor"
  )

  player_2754 = Player(
    player_id = 2754,
    full_name = "Chris Conley",
    last_name = "Conley",
    first_name = "Chris",
    nfl_team = "JAC",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1992-10-25",
    college = "Georgia"
  )

  player_2669 = Player(
    player_id = 2669,
    full_name = "Brandin Cooks",
    last_name = "Cooks",
    first_name = "Brandin",
    nfl_team = "HOU",
    position = "WR",
    height = "5-10",
    weight = "183",
    dob = "1993-09-25",
    college = "Oregon State"
  )

  player_3073 = Player(
    player_id = 3073,
    full_name = "Pharoh Cooper",
    last_name = "Cooper",
    first_name = "Pharoh",
    nfl_team = "CAR",
    position = "WR",
    height = "5-11",
    weight = "207",
    dob = "1995-03-07",
    college = "South Carolina"
  )

  player_2756 = Player(
    player_id = 2756,
    full_name = "Amari Cooper",
    last_name = "Cooper",
    first_name = "Amari",
    nfl_team = "DAL",
    position = "WR",
    height = "6-1",
    weight = "211",
    dob = "1994-06-17",
    college = "Alabama"
  )

  player_3082 = Player(
    player_id = 3082,
    full_name = "Cody Core",
    last_name = "Core",
    first_name = "Cody",
    nfl_team = "NYG",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1994-04-17",
    college = "Ole Miss"
  )

  player_4241 = Player(
    player_id = 4241,
    full_name = "Jeff Cotton",
    last_name = "Cotton",
    first_name = "Jeff",
    nfl_team = "LAC",
    position = "WR",
    height = "6-2",
    weight = "204",
    dob = "1997-04-17",
    college = "Idaho"
  )

  player_4326 = Player(
    player_id = 4326,
    full_name = "Isaiah Coulter",
    last_name = "Coulter",
    first_name = "Isaiah",
    nfl_team = "HOU",
    position = "WR",
    height = "6-3",
    weight = "190",
    dob = "1998-09-18",
    college = "Rhode Island"
  )

  player_3665 = Player(
    player_id = 3665,
    full_name = "Keke Coutee",
    last_name = "Coutee",
    first_name = "Keke",
    nfl_team = "HOU",
    position = "WR",
    height = "5-11",
    weight = "180",
    dob = "1997-01-14",
    college = "Texas Tech"
  )

  player_3589 = Player(
    player_id = 3589,
    full_name = "River Cracraft",
    last_name = "Cracraft",
    first_name = "River",
    nfl_team = "SF",
    position = "WR",
    height = "6-0",
    weight = "200",
    dob = "1994-11-01",
    college = "Washington State"
  )

  player_2748 = Player(
    player_id = 2748,
    full_name = "Jamison Crowder",
    last_name = "Crowder",
    first_name = "Jamison",
    nfl_team = "NYJ",
    position = "WR",
    height = "5-9",
    weight = "177",
    dob = "1993-06-17",
    college = "Duke"
  )

  player_3981 = Player(
    player_id = 3981,
    full_name = "Jamal Custis",
    last_name = "Custis",
    first_name = "Jamal",
    nfl_team = "PIT",
    position = "WR",
    height = "6-5",
    weight = "213",
    dob = "1995-11-06",
    college = "Syracuse"
  )

  player_3327 = Player(
    player_id = 3327,
    full_name = "Amara Darboh",
    last_name = "Darboh",
    first_name = "Amara",
    nfl_team = "PIT",
    position = "WR",
    height = "6-2",
    weight = "219",
    dob = "1994-02-01",
    college = "Michigan"
  )

  player_3096 = Player(
    player_id = 3096,
    full_name = "Trevor Davis",
    last_name = "Davis",
    first_name = "Trevor",
    nfl_team = "CHI",
    position = "WR",
    height = "6-1",
    weight = "188",
    dob = "1993-07-04",
    college = "California"
  )

  player_3372 = Player(
    player_id = 3372,
    full_name = "Corey Davis",
    last_name = "Davis",
    first_name = "Corey",
    nfl_team = "TEN",
    position = "WR",
    height = "6-3",
    weight = "209",
    dob = "1995-01-11",
    college = "Western Michigan"
  )

  player_4148 = Player(
    player_id = 4148,
    full_name = "Gabriel Davis",
    last_name = "Davis",
    first_name = "Gabriel",
    nfl_team = "BUF",
    position = "WR",
    height = "6-3",
    weight = "213",
    dob = "1999-04-01",
    college = "Central Florida"
  )

  player_2743 = Player(
    player_id = 2743,
    full_name = "Geremy Davis",
    last_name = "Davis",
    first_name = "Geremy",
    nfl_team = "DET",
    position = "WR",
    height = "6-3",
    weight = "211",
    dob = "1992-01-10",
    college = "Connecticut"
  )

  player_4051 = Player(
    player_id = 4051,
    full_name = "Davion Davis",
    last_name = "Davis",
    first_name = "Davion",
    nfl_team = "MIN",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1996-10-23",
    college = "Sam Houston State"
  )

  player_3542 = Player(
    player_id = 3542,
    full_name = "Reggie Davis",
    last_name = "Davis",
    first_name = "Reggie",
    nfl_team = "CHI",
    position = "WR",
    height = "6-0",
    weight = "170",
    dob = "1995-11-22",
    college = "Georgia"
  )

  player_4320 = Player(
    player_id = 4320,
    full_name = "Quartney Davis",
    last_name = "Davis",
    first_name = "Quartney",
    nfl_team = "MIN",
    position = "WR",
    height = "6-1",
    weight = "200",
    dob = "1998-04-07",
    college = "Texas A&amp;M"
  )

  player_3301 = Player(
    player_id = 3301,
    full_name = "Robert Davis",
    last_name = "Davis",
    first_name = "Robert",
    nfl_team = "PHI",
    position = "WR",
    height = "6-3",
    weight = "210",
    dob = "1995-04-02",
    college = "Georgia State"
  )

  player_3583 = Player(
    player_id = 3583,
    full_name = "Rashard Davis",
    last_name = "Davis",
    first_name = "Rashard",
    nfl_team = "TEN",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "1995-09-14",
    college = "James Madison"
  )

  player_3982 = Player(
    player_id = 3982,
    full_name = "Felton Davis III",
    last_name = "Davis III",
    first_name = "Felton",
    nfl_team = "KC",
    position = "WR",
    height = "6-3",
    weight = "211",
    dob = "1997-02-25",
    college = "Michigan State"
  )

  player_4270 = Player(
    player_id = 4270,
    full_name = "Seth Dawkins",
    last_name = "Dawkins",
    first_name = "Seth",
    nfl_team = "SEA",
    position = "WR",
    height = "6-3",
    weight = "218",
    dob = "1998-08-16",
    college = "Louisville"
  )

  player_4289 = Player(
    player_id = 4289,
    full_name = "Michael Dereus",
    last_name = "Dereus",
    first_name = "Michael",
    nfl_team = "BAL",
    position = "WR",
    height = "5-11",
    weight = "207",
    dob = "0000-00-00",
    college = "Georgetown"
  )

  player_3492 = Player(
    player_id = 3492,
    full_name = "Gehrig Dieter",
    last_name = "Dieter",
    first_name = "Gehrig",
    nfl_team = "KC",
    position = "WR",
    height = "6-3",
    weight = "207",
    dob = "1993-02-24",
    college = "Alabama"
  )

  player_2794 = Player(
    player_id = 2794,
    full_name = "Stefon Diggs",
    last_name = "Diggs",
    first_name = "Stefon",
    nfl_team = "BUF",
    position = "WR",
    height = "6-0",
    weight = "191",
    dob = "1993-11-29",
    college = "Maryland"
  )

  player_4208 = Player(
    player_id = 4208,
    full_name = "Derrick Dillon",
    last_name = "Dillon",
    first_name = "Derrick",
    nfl_team = "NYG",
    position = "WR",
    height = "5-11",
    weight = "186",
    dob = "1995-10-28",
    college = "Louisiana State"
  )

  player_4056 = Player(
    player_id = 4056,
    full_name = "Johnnie Dixon",
    last_name = "Dixon",
    first_name = "Johnnie",
    nfl_team = "ARI",
    position = "WR",
    height = "5-11",
    weight = "198",
    dob = "1994-09-16",
    college = "Ohio State"
  )

  player_3050 = Player(
    player_id = 3050,
    full_name = "Josh Doctson",
    last_name = "Doctson",
    first_name = "Josh",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1992-12-03",
    college = "TCU"
  )

  player_2800 = Player(
    player_id = 2800,
    full_name = "Phillip Dorsett",
    last_name = "Dorsett",
    first_name = "Phillip",
    nfl_team = "SEA",
    position = "WR",
    height = "5-10",
    weight = "192",
    dob = "1993-01-05",
    college = "Miami (FL)"
  )

  player_3966 = Player(
    player_id = 3966,
    full_name = "Greg Dortch",
    last_name = "Dortch",
    first_name = "Greg",
    nfl_team = "LAR",
    position = "WR",
    height = "5-7",
    weight = "175",
    dob = "1998-05-29",
    college = "Wake Forest"
  )

  player_3987 = Player(
    player_id = 3987,
    full_name = "Keelan Doss",
    last_name = "Doss",
    first_name = "Keelan",
    nfl_team = "LV",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1996-03-21",
    college = "California-Davis"
  )

  player_4044 = Player(
    player_id = 4044,
    full_name = "Jonathan Duhart",
    last_name = "Duhart",
    first_name = "Jonathan",
    nfl_team = "DET",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1996-06-26",
    college = "Old Dominion"
  )

  player_4059 = Player(
    player_id = 4059,
    full_name = "Ashton Dulin",
    last_name = "Dulin",
    first_name = "Ashton",
    nfl_team = "IND",
    position = "WR",
    height = "6-1",
    weight = "215",
    dob = "1997-05-15",
    college = "Malone"
  )

  player_4165 = Player(
    player_id = 4165,
    full_name = "Devin Duvernay",
    last_name = "Duvernay",
    first_name = "Devin",
    nfl_team = "BAL",
    position = "WR",
    height = "5-11",
    weight = "210",
    dob = "1997-09-12",
    college = "Texas"
  )

  player_3956 = Player(
    player_id = 3956,
    full_name = "Nick Easley",
    last_name = "Easley",
    first_name = "Nick",
    nfl_team = "BUF",
    position = "WR",
    height = "5-11",
    weight = "203",
    dob = "1997-01-14",
    college = "Iowa"
  )

  player_832 = Player(
    player_id = 832,
    full_name = "Julian Edelman",
    last_name = "Edelman",
    first_name = "Julian",
    nfl_team = "NE",
    position = "WR",
    height = "5-10",
    weight = "200",
    dob = "1986-05-22",
    college = "Kent State"
  )

  player_4159 = Player(
    player_id = 4159,
    full_name = "Bryan Edwards",
    last_name = "Edwards",
    first_name = "Bryan",
    nfl_team = "LV",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1998-11-13",
    college = "South Carolina"
  )

  player_4279 = Player(
    player_id = 4279,
    full_name = "Earnest Edwards",
    last_name = "Edwards",
    first_name = "Earnest",
    nfl_team = "LAR",
    position = "WR",
    height = "5-10",
    weight = "175",
    dob = "1998-03-30",
    college = "Maine"
  )

  player_2451 = Player(
    player_id = 2451,
    full_name = "Quincy Enunwa",
    last_name = "Enunwa",
    first_name = "Quincy",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-2",
    weight = "225",
    dob = "1992-05-31",
    college = "Nebraska"
  )

  player_3195 = Player(
    player_id = 3195,
    full_name = "Alex Erickson",
    last_name = "Erickson",
    first_name = "Alex",
    nfl_team = "CIN",
    position = "WR",
    height = "6-0",
    weight = "195",
    dob = "1992-11-06",
    college = "Wisconsin"
  )

  player_2677 = Player(
    player_id = 2677,
    full_name = "Mike Evans",
    last_name = "Evans",
    first_name = "Mike",
    nfl_team = "TB",
    position = "WR",
    height = "6-5",
    weight = "231",
    dob = "1993-08-21",
    college = "Texas A&amp;M"
  )

  player_4231 = Player(
    player_id = 4231,
    full_name = "Maurice Ffrench",
    last_name = "Ffrench",
    first_name = "Maurice",
    nfl_team = "KC",
    position = "WR",
    height = "5-11",
    weight = "200",
    dob = "1998-01-01",
    college = "Pittsburgh"
  )

  player_4262 = Player(
    player_id = 4262,
    full_name = "Chris Finke",
    last_name = "Finke",
    first_name = "Chris",
    nfl_team = "SF",
    position = "WR",
    height = "5-9",
    weight = "186",
    dob = "1996-05-02",
    college = "Notre Dame"
  )

  player_394 = Player(
    player_id = 394,
    full_name = "Larry Fitzgerald",
    last_name = "Fitzgerald",
    first_name = "Larry",
    nfl_team = "ARI",
    position = "WR",
    height = "6-3",
    weight = "218",
    dob = "1983-08-31",
    college = "Pittsburgh"
  )

  player_3282 = Player(
    player_id = 3282,
    full_name = "Isaiah Ford",
    last_name = "Ford",
    first_name = "Isaiah",
    nfl_team = "MIA",
    position = "WR",
    height = "6-2",
    weight = "195",
    dob = "1996-02-09",
    college = "Virginia Tech"
  )

  player_3984 = Player(
    player_id = 3984,
    full_name = "Joe Fortson",
    last_name = "Fortson",
    first_name = "Joe",
    nfl_team = "KC",
    position = "WR",
    height = "6-6",
    weight = "230",
    dob = "1995-12-07",
    college = "Valdosta State"
  )

  player_3681 = Player(
    player_id = 3681,
    full_name = "Robert Foster",
    last_name = "Foster",
    first_name = "Robert",
    nfl_team = "BUF",
    position = "WR",
    height = "6-2",
    weight = "194",
    dob = "1994-05-07",
    college = "Alabama"
  )

  player_3670 = Player(
    player_id = 3670,
    full_name = "Daurice Fountain",
    last_name = "Fountain",
    first_name = "Daurice",
    nfl_team = "IND",
    position = "WR",
    height = "6-2",
    weight = "210",
    dob = "1995-12-22",
    college = "Northern Iowa"
  )

  player_2490 = Player(
    player_id = 2490,
    full_name = "Bennie Fowler",
    last_name = "Fowler",
    first_name = "Bennie",
    nfl_team = "NO",
    position = "WR",
    height = "6-1",
    weight = "212",
    dob = "1991-06-10",
    college = "Michigan State"
  )

  player_4146 = Player(
    player_id = 4146,
    full_name = "John Franklin",
    last_name = "Franklin",
    first_name = "John",
    nfl_team = "TB",
    position = "WR",
    height = "6-1",
    weight = "186",
    dob = "1994-09-21",
    college = "Florida Atlantic"
  )

  player_3924 = Player(
    player_id = 3924,
    full_name = "Travis Fulgham",
    last_name = "Fulgham",
    first_name = "Travis",
    nfl_team = "PHI",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1995-09-13",
    college = "Old Dominion"
  )

  player_3103 = Player(
    player_id = 3103,
    full_name = "Will Fuller",
    last_name = "Fuller",
    first_name = "Will",
    nfl_team = "HOU",
    position = "WR",
    height = "6-0",
    weight = "184",
    dob = "1994-04-16",
    college = "Notre Dame"
  )

  player_4271 = Player(
    player_id = 4271,
    full_name = "Aaron Fuller",
    last_name = "Fuller",
    first_name = "Aaron",
    nfl_team = "SEA",
    position = "WR",
    height = "5-11",
    weight = "188",
    dob = "1997-09-30",
    college = "Washington"
  )

  player_2809 = Player(
    player_id = 2809,
    full_name = "Devin Funchess",
    last_name = "Funchess",
    first_name = "Devin",
    nfl_team = "GB",
    position = "WR",
    height = "6-4",
    weight = "225",
    dob = "1994-05-21",
    college = "Michigan"
  )

  player_4096 = Player(
    player_id = 4096,
    full_name = "Rico Gafford",
    last_name = "Gafford",
    first_name = "Rico",
    nfl_team = "LV",
    position = "WR",
    height = "5-10",
    weight = "185",
    dob = "1996-05-23",
    college = "Wyoming"
  )

  player_3674 = Player(
    player_id = 3674,
    full_name = "Russell Gage",
    last_name = "Gage",
    first_name = "Russell",
    nfl_team = "ATL",
    position = "WR",
    height = "6-0",
    weight = "184",
    dob = "1996-01-22",
    college = "Louisiana State"
  )

  player_3581 = Player(
    player_id = 3581,
    full_name = "Michael Gallup",
    last_name = "Gallup",
    first_name = "Michael",
    nfl_team = "DAL",
    position = "WR",
    height = "6-1",
    weight = "200",
    dob = "1996-03-04",
    college = "Colorado State"
  )

  player_4221 = Player(
    player_id = 4221,
    full_name = "Antonio Gandy-Golden",
    last_name = "Gandy-Golden",
    first_name = "Antonio",
    nfl_team = "WAS",
    position = "WR",
    height = "6-4",
    weight = "220",
    dob = "1998-04-11",
    college = "Liberty"
  )

  player_3298 = Player(
    player_id = 3298,
    full_name = "Shelton Gibson",
    last_name = "Gibson",
    first_name = "Shelton",
    nfl_team = "PHI",
    position = "WR",
    height = "5-11",
    weight = "191",
    dob = "1994-03-20",
    college = "West Virginia"
  )

  player_406 = Player(
    player_id = 406,
    full_name = "Ted Ginn Jr.",
    last_name = "Ginn Jr.",
    first_name = "Ted",
    nfl_team = "CHI",
    position = "WR",
    height = "5-11",
    weight = "180",
    dob = "1985-04-12",
    college = "Ohio State"
  )

  player_3389 = Player(
    player_id = 3389,
    full_name = "Chris Godwin",
    last_name = "Godwin",
    first_name = "Chris",
    nfl_team = "TB",
    position = "WR",
    height = "6-1",
    weight = "209",
    dob = "1996-02-27",
    college = "Penn State"
  )

  player_3944 = Player(
    player_id = 3944,
    full_name = "Terry Godwin",
    last_name = "Godwin",
    first_name = "Terry",
    nfl_team = "JAC",
    position = "WR",
    height = "5-11",
    weight = "185",
    dob = "1996-10-23",
    college = "Georgia"
  )

  player_3347 = Player(
    player_id = 3347,
    full_name = "Kenny Golladay",
    last_name = "Golladay",
    first_name = "Kenny",
    nfl_team = "DET",
    position = "WR",
    height = "6-4",
    weight = "213",
    dob = "1993-11-03",
    college = "Northern Illinois"
  )

  player_2118 = Player(
    player_id = 2118,
    full_name = "Marquise Goodwin",
    last_name = "Goodwin",
    first_name = "Marquise",
    nfl_team = "PHI",
    position = "WR",
    height = "5-9",
    weight = "185",
    dob = "1990-11-19",
    college = "Texas"
  )

  player_2092 = Player(
    player_id = 2092,
    full_name = "Josh Gordon",
    last_name = "Gordon",
    first_name = "Josh",
    nfl_team = "SEA",
    position = "WR",
    height = "6-3",
    weight = "225",
    dob = "1991-04-13",
    college = "Utah"
  )

  player_3028 = Player(
    player_id = 3028,
    full_name = "Jakeem Grant",
    last_name = "Grant",
    first_name = "Jakeem",
    nfl_team = "MIA",
    position = "WR",
    height = "5-7",
    weight = "169",
    dob = "1992-10-30",
    college = "Texas Tech"
  )

  player_3821 = Player(
    player_id = 3821,
    full_name = "Devin Gray",
    last_name = "Gray",
    first_name = "Devin",
    nfl_team = "ATL",
    position = "WR",
    height = "6-0",
    weight = "192",
    dob = "1995-06-15",
    college = "Cincinnati"
  )

  player_3422 = Player(
    player_id = 3422,
    full_name = "Cyril Grayson",
    last_name = "Grayson",
    first_name = "Cyril",
    nfl_team = "TB",
    position = "WR",
    height = "5-9",
    weight = "183",
    dob = "1993-12-05",
    college = "Louisiana State"
  )

  player_3940 = Player(
    player_id = 3940,
    full_name = "Marcus Green",
    last_name = "Green",
    first_name = "Marcus",
    nfl_team = "PHI",
    position = "WR",
    height = "5-8",
    weight = "191",
    dob = "1996-08-13",
    college = "Louisiana-Monroe"
  )

  player_1441 = Player(
    player_id = 1441,
    full_name = "A.J. Green",
    last_name = "Green",
    first_name = "A.J.",
    nfl_team = "CIN",
    position = "WR",
    height = "6-4",
    weight = "210",
    dob = "1988-07-31",
    college = "Georgia"
  )

  player_4351 = Player(
    player_id = 4351,
    full_name = "Juwan Green",
    last_name = "Green",
    first_name = "Juwan",
    nfl_team = "ATL",
    position = "WR",
    height = "6-0",
    weight = "187",
    dob = "1998-07-01",
    college = "Albany, N.Y."
  )

  player_4372 = Player(
    player_id = 4372,
    full_name = "Stephen Guidry",
    last_name = "Guidry",
    first_name = "Stephen",
    nfl_team = "DAL",
    position = "WR",
    height = "6-4",
    weight = "200",
    dob = "1997-03-25",
    college = "Mississippi State"
  )

  player_3968 = Player(
    player_id = 3968,
    full_name = "Jalen Guyton",
    last_name = "Guyton",
    first_name = "Jalen",
    nfl_team = "LAC",
    position = "WR",
    height = "6-1",
    weight = "212",
    dob = "1997-06-07",
    college = "North Texas"
  )

  player_3158 = Player(
    player_id = 3158,
    full_name = "Marvin Hall",
    last_name = "Hall",
    first_name = "Marvin",
    nfl_team = "DET",
    position = "WR",
    height = "5-10",
    weight = "190",
    dob = "1993-04-10",
    college = "Washington"
  )

  player_4038 = Player(
    player_id = 4038,
    full_name = "Emanuel Hall",
    last_name = "Hall",
    first_name = "Emanuel",
    nfl_team = "WAS",
    position = "WR",
    height = "6-3",
    weight = "195",
    dob = "1997-05-21",
    college = "Missouri"
  )

  player_3637 = Player(
    player_id = 3637,
    full_name = "DaeSean Hamilton",
    last_name = "Hamilton",
    first_name = "DaeSean",
    nfl_team = "DEN",
    position = "WR",
    height = "6-1",
    weight = "206",
    dob = "1995-03-10",
    college = "Penn State"
  )

  player_4156 = Player(
    player_id = 4156,
    full_name = "KJ Hamler",
    last_name = "Hamler",
    first_name = "KJ",
    nfl_team = "DEN",
    position = "WR",
    height = "5-9",
    weight = "176",
    dob = "1999-07-08",
    college = "Penn State"
  )

  player_4338 = Player(
    player_id = 4338,
    full_name = "Josh Hammond",
    last_name = "Hammond",
    first_name = "Josh",
    nfl_team = "JAC",
    position = "WR",
    height = "6-0",
    weight = "194",
    dob = "1998-07-24",
    college = "Florida"
  )

  player_3284 = Player(
    player_id = 3284,
    full_name = "Chad Hansen",
    last_name = "Hansen",
    first_name = "Chad",
    nfl_team = "HOU",
    position = "WR",
    height = "6-2",
    weight = "202",
    dob = "1995-01-18",
    college = "California"
  )

  player_3888 = Player(
    player_id = 3888,
    full_name = "Mecole Hardman",
    last_name = "Hardman",
    first_name = "Mecole",
    nfl_team = "KC",
    position = "WR",
    height = "5-10",
    weight = "187",
    dob = "1998-03-12",
    college = "Georgia"
  )

  player_3875 = Player(
    player_id = 3875,
    full_name = "Kelvin Harmon",
    last_name = "Harmon",
    first_name = "Kelvin",
    nfl_team = "WAS",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1996-12-15",
    college = "North Carolina State"
  )

  player_3152 = Player(
    player_id = 3152,
    full_name = "Maurice Harris",
    last_name = "Harris",
    first_name = "Maurice",
    nfl_team = "NO",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1992-11-11",
    college = "California"
  )

  player_4329 = Player(
    player_id = 4329,
    full_name = "De'Michael Harris",
    last_name = "Harris",
    first_name = "De'Michael",
    nfl_team = "IND",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "1998-07-12",
    college = "Southern Mississippi"
  )

  player_4082 = Player(
    player_id = 4082,
    full_name = "Deonte Harris",
    last_name = "Harris",
    first_name = "Deonte",
    nfl_team = "NO",
    position = "WR",
    height = "5-6",
    weight = "170",
    dob = "1997-12-04",
    college = "Assumption"
  )

  player_3864 = Player(
    player_id = 3864,
    full_name = "N'Keal Harry",
    last_name = "Harry",
    first_name = "N'Keal",
    nfl_team = "NE",
    position = "WR",
    height = "6-4",
    weight = "225",
    dob = "1997-12-17",
    college = "Arizona State"
  )

  player_4060 = Player(
    player_id = 4060,
    full_name = "Penny Hart",
    last_name = "Hart",
    first_name = "Penny",
    nfl_team = "SEA",
    position = "WR",
    height = "5-8",
    weight = "180",
    dob = "1996-07-05",
    college = "Georgia State"
  )

  player_4191 = Player(
    player_id = 4191,
    full_name = "Will Hastings",
    last_name = "Hastings",
    first_name = "Will",
    nfl_team = "NE",
    position = "WR",
    height = "5-10",
    weight = "174",
    dob = "1996-07-30",
    college = "Auburn"
  )

  player_3411 = Player(
    player_id = 3411,
    full_name = "Keon Hatcher",
    last_name = "Hatcher",
    first_name = "Keon",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-1",
    weight = "215",
    dob = "1994-09-11",
    college = "Arkansas"
  )

  player_3772 = Player(
    player_id = 3772,
    full_name = "Quadree Henderson",
    last_name = "Henderson",
    first_name = "Quadree",
    nfl_team = "PIT",
    position = "WR",
    height = "5-8",
    weight = "192",
    dob = "1996-09-12",
    college = "Pittsburgh"
  )

  player_4002 = Player(
    player_id = 4002,
    full_name = "Malik Henry",
    last_name = "Henry",
    first_name = "Malik",
    nfl_team = "IND",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1997-04-16",
    college = "West Georgia"
  )

  player_4232 = Player(
    player_id = 4232,
    full_name = "Aleva Hifo",
    last_name = "Hifo",
    first_name = "Aleva",
    nfl_team = "KC",
    position = "WR",
    height = "5-10",
    weight = "187",
    dob = "0000-00-00",
    college = "BYU"
  )

  player_3086 = Player(
    player_id = 3086,
    full_name = "Rashard Higgins",
    last_name = "Higgins",
    first_name = "Rashard",
    nfl_team = "CLE",
    position = "WR",
    height = "6-1",
    weight = "198",
    dob = "1994-10-07",
    college = "Colorado State"
  )

  player_4166 = Player(
    player_id = 4166,
    full_name = "Tee Higgins",
    last_name = "Higgins",
    first_name = "Tee",
    nfl_team = "CIN",
    position = "WR",
    height = "6-4",
    weight = "210",
    dob = "1999-01-18",
    college = "Clemson"
  )

  player_4216 = Player(
    player_id = 4216,
    full_name = "John Hightower",
    last_name = "Hightower",
    first_name = "John",
    nfl_team = "PHI",
    position = "WR",
    height = "6-2",
    weight = "172",
    dob = "1996-05-31",
    college = "Boise State"
  )

  player_4358 = Player(
    player_id = 4358,
    full_name = "TreVontae Hights",
    last_name = "Hights",
    first_name = "TreVontae",
    nfl_team = "CAR",
    position = "WR",
    height = "6-3",
    weight = "195",
    dob = "1997-02-07",
    college = "TCU"
  )

  player_4242 = Player(
    player_id = 4242,
    full_name = "KJ Hill",
    last_name = "Hill",
    first_name = "KJ",
    nfl_team = "LAC",
    position = "WR",
    height = "6-0",
    weight = "197",
    dob = "1997-09-15",
    college = "Ohio State"
  )

  player_3056 = Player(
    player_id = 3056,
    full_name = "Tyreek Hill",
    last_name = "Hill",
    first_name = "Tyreek",
    nfl_team = "KC",
    position = "WR",
    height = "5-10",
    weight = "185",
    dob = "1994-03-01",
    college = "West Alabama"
  )

  player_1937 = Player(
    player_id = 1937,
    full_name = "T.Y. Hilton",
    last_name = "Hilton",
    first_name = "T.Y.",
    nfl_team = "IND",
    position = "WR",
    height = "5-10",
    weight = "183",
    dob = "1989-11-14",
    college = "Florida International"
  )

  player_4228 = Player(
    player_id = 4228,
    full_name = "Kendall Hinton",
    last_name = "Hinton",
    first_name = "Kendall",
    nfl_team = "DEN",
    position = "WR",
    height = "6-0",
    weight = "195",
    dob = "1997-02-19",
    college = "Wake Forest"
  )

  player_3748 = Player(
    player_id = 3748,
    full_name = "KhaDarel Hodge",
    last_name = "Hodge",
    first_name = "KhaDarel",
    nfl_team = "CLE",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1995-01-03",
    college = "Prairie View"
  )

  player_4184 = Player(
    player_id = 4184,
    full_name = "Isaiah Hodgins",
    last_name = "Hodgins",
    first_name = "Isaiah",
    nfl_team = "BUF",
    position = "WR",
    height = "6-3",
    weight = "201",
    dob = "1998-10-21",
    college = "Oregon State"
  )

  player_1590 = Player(
    player_id = 1590,
    full_name = "Chris Hogan",
    last_name = "Hogan",
    first_name = "Chris",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-1",
    weight = "210",
    dob = "1987-10-24",
    college = "Monmouth, N.J."
  )

  player_3503 = Player(
    player_id = 3503,
    full_name = "Krishawn Hogan",
    last_name = "Hogan",
    first_name = "Krishawn",
    nfl_team = "TEN",
    position = "WR",
    height = "6-3",
    weight = "217",
    dob = "1995-05-12",
    college = "Marian"
  )

  player_4052 = Player(
    player_id = 4052,
    full_name = "Alexander Hollins",
    last_name = "Hollins",
    first_name = "Alexander",
    nfl_team = "MIN",
    position = "WR",
    height = "6-1",
    weight = "166",
    dob = "1996-11-24",
    college = "Eastern Illinois"
  )

  player_3299 = Player(
    player_id = 3299,
    full_name = "Mack Hollins",
    last_name = "Hollins",
    first_name = "Mack",
    nfl_team = "MIA",
    position = "WR",
    height = "6-4",
    weight = "221",
    dob = "1993-09-16",
    college = "North Carolina"
  )

  player_3403 = Player(
    player_id = 3403,
    full_name = "Cody Hollister",
    last_name = "Hollister",
    first_name = "Cody",
    nfl_team = "TEN",
    position = "WR",
    height = "6-4",
    weight = "209",
    dob = "1993-11-18",
    college = "Arkansas"
  )

  player_3160 = Player(
    player_id = 3160,
    full_name = "Johnny Holton",
    last_name = "Holton",
    first_name = "Johnny",
    nfl_team = "NYG",
    position = "WR",
    height = "6-3",
    weight = "190",
    dob = "1990-08-22",
    college = "Cincinnati"
  )

  player_2338 = Player(
    player_id = 2338,
    full_name = "DeAndre Hopkins",
    last_name = "Hopkins",
    first_name = "DeAndre",
    nfl_team = "ARI",
    position = "WR",
    height = "6-1",
    weight = "212",
    dob = "1992-06-06",
    college = "Clemson"
  )

  player_4083 = Player(
    player_id = 4083,
    full_name = "Lil-Jordan Humphrey",
    last_name = "Humphrey",
    first_name = "Lil-Jordan",
    nfl_team = "NO",
    position = "WR",
    height = "6-4",
    weight = "225",
    dob = "1998-04-19",
    college = "Texas"
  )

  player_2979 = Player(
    player_id = 2979,
    full_name = "Adam Humphries",
    last_name = "Humphries",
    first_name = "Adam",
    nfl_team = "TEN",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1993-06-24",
    college = "Clemson"
  )

  player_3898 = Player(
    player_id = 3898,
    full_name = "Jalen Hurd",
    last_name = "Hurd",
    first_name = "Jalen",
    nfl_team = "SF",
    position = "WR",
    height = "6-5",
    weight = "230",
    dob = "1996-01-23",
    college = "Baylor"
  )

  player_2633 = Player(
    player_id = 2633,
    full_name = "Allen Hurns",
    last_name = "Hurns",
    first_name = "Allen",
    nfl_team = "MIA",
    position = "WR",
    height = "6-3",
    weight = "195",
    dob = "1991-11-12",
    college = "Miami (FL)"
  )

  player_4378 = Player(
    player_id = 4378,
    full_name = "John Hurst",
    last_name = "Hurst",
    first_name = "John",
    nfl_team = "TB",
    position = "WR",
    height = "6-2",
    weight = "190",
    dob = "1996-11-02",
    college = "West Georgia"
  )

  player_3915 = Player(
    player_id = 3915,
    full_name = "Ishmael Hyman",
    last_name = "Hyman",
    first_name = "Ishmael",
    nfl_team = "CAR",
    position = "WR",
    height = "6-0",
    weight = "196",
    dob = "1995-08-23",
    college = "James Madison"
  )

  player_1594 = Player(
    player_id = 1594,
    full_name = "Dontrelle Inman",
    last_name = "Inman",
    first_name = "Dontrelle",
    nfl_team = "WAS",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1989-01-31",
    college = "Virginia"
  )

  player_3962 = Player(
    player_id = 3962,
    full_name = "Trenton Irwin",
    last_name = "Irwin",
    first_name = "Trenton",
    nfl_team = "CIN",
    position = "WR",
    height = "6-2",
    weight = "207",
    dob = "1995-12-10",
    college = "Stanford"
  )

  player_3895 = Player(
    player_id = 3895,
    full_name = "Andy Isabella",
    last_name = "Isabella",
    first_name = "Andy",
    nfl_team = "ARI",
    position = "WR",
    height = "5-9",
    weight = "190",
    dob = "1996-11-18",
    college = "Massachusetts"
  )

  player_3802 = Player(
    player_id = 3802,
    full_name = "Steve Ishmael",
    last_name = "Ishmael",
    first_name = "Steve",
    nfl_team = "IND",
    position = "WR",
    height = "6-2",
    weight = "212",
    dob = "1995-07-18",
    college = "Syracuse"
  )

  player_4039 = Player(
    player_id = 4039,
    full_name = "Thomas Ives",
    last_name = "Ives",
    first_name = "Thomas",
    nfl_team = "CHI",
    position = "WR",
    height = "6-4",
    weight = "218",
    dob = "1997-06-25",
    college = "Colgate"
  )

  player_4280 = Player(
    player_id = 4280,
    full_name = "Trishton Jackson",
    last_name = "Jackson",
    first_name = "Trishton",
    nfl_team = "LAR",
    position = "WR",
    height = "6-1",
    weight = "191",
    dob = "1998-03-09",
    college = "Syracuse"
  )

  player_441 = Player(
    player_id = 441,
    full_name = "DeSean Jackson",
    last_name = "Jackson",
    first_name = "DeSean",
    nfl_team = "PHI",
    position = "WR",
    height = "5-10",
    weight = "175",
    dob = "1986-12-01",
    college = "California"
  )

  player_3645 = Player(
    player_id = 3645,
    full_name = "Richie James",
    last_name = "James",
    first_name = "Richie",
    nfl_team = "SF",
    position = "WR",
    height = "5-9",
    weight = "185",
    dob = "1995-09-05",
    college = "Middle Tennessee"
  )

  player_4080 = Player(
    player_id = 4080,
    full_name = "Damion Jeanpiere Jr",
    last_name = "Jeanpiere Jr",
    first_name = "Damion",
    nfl_team = "CAR",
    position = "WR",
    height = "6-1",
    weight = "185",
    dob = "1996-12-08",
    college = "Nicholls State"
  )

  player_4144 = Player(
    player_id = 4144,
    full_name = "Justin Jefferson",
    last_name = "Jefferson",
    first_name = "Justin",
    nfl_team = "MIN",
    position = "WR",
    height = "6-3",
    weight = "192",
    dob = "1999-06-16",
    college = "Louisiana State"
  )

  player_4163 = Player(
    player_id = 4163,
    full_name = "Van Jefferson",
    last_name = "Jefferson",
    first_name = "Van",
    nfl_team = "LAR",
    position = "WR",
    height = "6-2",
    weight = "197",
    dob = "1996-07-26",
    college = "Florida"
  )

  player_1895 = Player(
    player_id = 1895,
    full_name = "Alshon Jeffery",
    last_name = "Jeffery",
    first_name = "Alshon",
    nfl_team = "PHI",
    position = "WR",
    height = "6-3",
    weight = "218",
    dob = "1990-02-14",
    college = "South Carolina"
  )

  player_2945 = Player(
    player_id = 2945,
    full_name = "Darius Jennings",
    last_name = "Jennings",
    first_name = "Darius",
    nfl_team = "LAC",
    position = "WR",
    height = "5-10",
    weight = "180",
    dob = "1992-06-28",
    college = "Virginia"
  )

  player_4263 = Player(
    player_id = 4263,
    full_name = "Jauan Jennings",
    last_name = "Jennings",
    first_name = "Jauan",
    nfl_team = "SF",
    position = "WR",
    height = "6-3",
    weight = "214",
    dob = "1997-07-10",
    college = "Tennessee"
  )

  player_3902 = Player(
    player_id = 3902,
    full_name = "Gary Jennings Jr",
    last_name = "Jennings Jr",
    first_name = "Gary",
    nfl_team = "MIA",
    position = "WR",
    height = "6-1",
    weight = "216",
    dob = "1997-03-07",
    college = "West Virginia"
  )

  player_4132 = Player(
    player_id = 4132,
    full_name = "Jerry Jeudy",
    last_name = "Jeudy",
    first_name = "Jerry",
    nfl_team = "DEN",
    position = "WR",
    height = "6-1",
    weight = "192",
    dob = "1999-04-24",
    college = "Alabama"
  )

  player_4364 = Player(
    player_id = 4364,
    full_name = "Juwan Johnson",
    last_name = "Johnson",
    first_name = "Juwan",
    nfl_team = "NO",
    position = "WR",
    height = "6-4",
    weight = "231",
    dob = "1996-09-13",
    college = "Oregon"
  )

  player_4367 = Player(
    player_id = 4367,
    full_name = "Tyler Johnson",
    last_name = "Johnson",
    first_name = "Tyler",
    nfl_team = "TB",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1998-08-25",
    college = "Minnesota"
  )

  player_3896 = Player(
    player_id = 3896,
    full_name = "KeeSean Johnson",
    last_name = "Johnson",
    first_name = "KeeSean",
    nfl_team = "ARI",
    position = "WR",
    height = "6-1",
    weight = "199",
    dob = "1996-10-09",
    college = "Fresno State"
  )

  player_3143 = Player(
    player_id = 3143,
    full_name = "Marcus Johnson",
    last_name = "Johnson",
    first_name = "Marcus",
    nfl_team = "IND",
    position = "WR",
    height = "6-1",
    weight = "207",
    dob = "1994-08-05",
    college = "Texas"
  )

  player_3918 = Player(
    player_id = 3918,
    full_name = "Diontae Johnson",
    last_name = "Johnson",
    first_name = "Diontae",
    nfl_team = "PIT",
    position = "WR",
    height = "5-10",
    weight = "181",
    dob = "1996-07-05",
    college = "Toledo"
  )

  player_3930 = Player(
    player_id = 3930,
    full_name = "Olabisi Johnson",
    last_name = "Johnson",
    first_name = "Olabisi",
    nfl_team = "MIN",
    position = "WR",
    height = "6-0",
    weight = "203",
    dob = "1997-03-17",
    college = "Colorado State"
  )

  player_4222 = Player(
    player_id = 4222,
    full_name = "Johnathon Johnson",
    last_name = "Johnson",
    first_name = "Johnathon",
    nfl_team = "WAS",
    position = "WR",
    height = "5-10",
    weight = "180",
    dob = "0000-00-00",
    college = "Missouri"
  )

  player_3969 = Player(
    player_id = 3969,
    full_name = "Jon'Vea Johnson",
    last_name = "Johnson",
    first_name = "Jon'Vea",
    nfl_team = "DAL",
    position = "WR",
    height = "6-0",
    weight = "192",
    dob = "1995-12-23",
    college = "Toledo"
  )

  player_4057 = Player(
    player_id = 4057,
    full_name = "Tyron Johnson",
    last_name = "Johnson",
    first_name = "Tyron",
    nfl_team = "LAC",
    position = "WR",
    height = "6-1",
    weight = "193",
    dob = "1996-01-08",
    college = "Oklahoma State"
  )

  player_4339 = Player(
    player_id = 4339,
    full_name = "Collin Johnson",
    last_name = "Johnson",
    first_name = "Collin",
    nfl_team = "JAC",
    position = "WR",
    height = "6-6",
    weight = "215",
    dob = "1997-09-23",
    college = "Texas"
  )

  player_4086 = Player(
    player_id = 4086,
    full_name = "Anthony Johnson",
    last_name = "Johnson",
    first_name = "Anthony",
    nfl_team = "PIT",
    position = "WR",
    height = "6-2",
    weight = "220",
    dob = "1995-01-29",
    college = "Buffalo"
  )

  player_3135 = Player(
    player_id = 3135,
    full_name = "Andy Jones",
    last_name = "Jones",
    first_name = "Andy",
    nfl_team = "MIA",
    position = "WR",
    height = "6-1",
    weight = "217",
    dob = "1994-06-28",
    college = "Jacksonville"
  )

  player_1872 = Player(
    player_id = 1872,
    full_name = "Marvin Jones",
    last_name = "Jones",
    first_name = "Marvin",
    nfl_team = "DET",
    position = "WR",
    height = "6-2",
    weight = "198",
    dob = "1990-03-12",
    college = "California"
  )

  player_3232 = Player(
    player_id = 3232,
    full_name = "Tevin Jones",
    last_name = "Jones",
    first_name = "Tevin",
    nfl_team = "DAL",
    position = "WR",
    height = "6-2",
    weight = "225",
    dob = "1992-12-26",
    college = "Memphis"
  )

  player_1446 = Player(
    player_id = 1446,
    full_name = "Julio Jones",
    last_name = "Jones",
    first_name = "Julio",
    nfl_team = "ATL",
    position = "WR",
    height = "6-3",
    weight = "220",
    dob = "1989-02-08",
    college = "Alabama"
  )

  player_3281 = Player(
    player_id = 3281,
    full_name = "Zay Jones",
    last_name = "Jones",
    first_name = "Zay",
    nfl_team = "LV",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1995-03-30",
    college = "East Carolina"
  )

  player_4379 = Player(
    player_id = 4379,
    full_name = "Travis Jonsen",
    last_name = "Jonsen",
    first_name = "Travis",
    nfl_team = "TB",
    position = "WR",
    height = "6-4",
    weight = "211",
    dob = "0000-00-00",
    college = "Montana State"
  )

  player_3493 = Player(
    player_id = 3493,
    full_name = "Marcus Kemp",
    last_name = "Kemp",
    first_name = "Marcus",
    nfl_team = "KC",
    position = "WR",
    height = "6-4",
    weight = "210",
    dob = "1995-08-14",
    college = "Hawaii"
  )

  player_4045 = Player(
    player_id = 4045,
    full_name = "Tom Kennedy",
    last_name = "Kennedy",
    first_name = "Tom",
    nfl_team = "DET",
    position = "WR",
    height = "5-10",
    weight = "194",
    dob = "1996-07-29",
    college = "Bryant"
  )

  player_3702 = Player(
    player_id = 3702,
    full_name = "Darvin Kidsy",
    last_name = "Kidsy",
    first_name = "Darvin",
    nfl_team = "WAS",
    position = "WR",
    height = "6-0",
    weight = "180",
    dob = "1995-03-19",
    college = "Texas Southern"
  )

  player_4345 = Player(
    player_id = 4345,
    full_name = "Mason Kinsey",
    last_name = "Kinsey",
    first_name = "Mason",
    nfl_team = "TEN",
    position = "WR",
    height = "6-0",
    weight = "195",
    dob = "1998-08-29",
    college = "Berry"
  )

  player_3593 = Player(
    player_id = 3593,
    full_name = "Christian Kirk",
    last_name = "Kirk",
    first_name = "Christian",
    nfl_team = "ARI",
    position = "WR",
    height = "5-11",
    weight = "200",
    dob = "1996-11-18",
    college = "Texas A&amp;M"
  )

  player_3830 = Player(
    player_id = 3830,
    full_name = "Keith Kirkwood",
    last_name = "Kirkwood",
    first_name = "Keith",
    nfl_team = "CAR",
    position = "WR",
    height = "6-3",
    weight = "210",
    dob = "1994-12-26",
    college = "Temple"
  )

  player_4281 = Player(
    player_id = 4281,
    full_name = "JJ Koski",
    last_name = "Koski",
    first_name = "JJ",
    nfl_team = "LAR",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1996-12-27",
    college = "Cal Poly"
  )

  player_2845 = Player(
    player_id = 2845,
    full_name = "Jake Kumerow",
    last_name = "Kumerow",
    first_name = "Jake",
    nfl_team = "GB",
    position = "WR",
    height = "6-4",
    weight = "209",
    dob = "1992-02-17",
    college = "Wisconsin-Whitewater"
  )

  player_3559 = Player(
    player_id = 3559,
    full_name = "Cooper Kupp",
    last_name = "Kupp",
    first_name = "Cooper",
    nfl_team = "LAR",
    position = "WR",
    height = "6-2",
    weight = "208",
    dob = "1993-06-15",
    college = "Eastern Washington"
  )

  player_3781 = Player(
    player_id = 3781,
    full_name = "Chris Lacy",
    last_name = "Lacy",
    first_name = "Chris",
    nfl_team = "DET",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1996-01-28",
    college = "Oklahoma State"
  )

  player_4130 = Player(
    player_id = 4130,
    full_name = "CeeDee Lamb",
    last_name = "Lamb",
    first_name = "CeeDee",
    nfl_team = "DAL",
    position = "WR",
    height = "6-2",
    weight = "189",
    dob = "1999-04-08",
    college = "Oklahoma"
  )

  player_2437 = Player(
    player_id = 2437,
    full_name = "Jarvis Landry",
    last_name = "Landry",
    first_name = "Jarvis",
    nfl_team = "CLE",
    position = "WR",
    height = "5-11",
    weight = "196",
    dob = "1992-11-28",
    college = "Louisiana State"
  )

  player_2492 = Player(
    player_id = 2492,
    full_name = "Cody Latimer",
    last_name = "Latimer",
    first_name = "Cody",
    nfl_team = "WAS",
    position = "WR",
    height = "6-3",
    weight = "222",
    dob = "1992-10-10",
    college = "Indiana"
  )

  player_3805 = Player(
    player_id = 3805,
    full_name = "Allen Lazard",
    last_name = "Lazard",
    first_name = "Allen",
    nfl_team = "GB",
    position = "WR",
    height = "6-5",
    weight = "227",
    dob = "1995-12-11",
    college = "Iowa State"
  )

  player_4252 = Player(
    player_id = 4252,
    full_name = "Shane Leatherbury",
    last_name = "Leatherbury",
    first_name = "Shane",
    nfl_team = "ARI",
    position = "WR",
    height = "5-11",
    weight = "190",
    dob = "0000-00-00",
    college = "Towson"
  )

  player_2634 = Player(
    player_id = 2634,
    full_name = "Marqise Lee",
    last_name = "Lee",
    first_name = "Marqise",
    nfl_team = "NE",
    position = "WR",
    height = "6-0",
    weight = "196",
    dob = "1991-11-25",
    college = "USC"
  )

  player_3480 = Player(
    player_id = 3480,
    full_name = "Lance Lenoir",
    last_name = "Lenoir",
    first_name = "Lance",
    nfl_team = "SEA",
    position = "WR",
    height = "6-0",
    weight = "201",
    dob = "1995-02-09",
    college = "Western Illinois"
  )

  player_3270 = Player(
    player_id = 3270,
    full_name = "Tommylee Lewis",
    last_name = "Lewis",
    first_name = "Tommylee",
    nfl_team = "CAR",
    position = "WR",
    height = "5-7",
    weight = "168",
    dob = "1992-10-24",
    college = "Northern Illinois"
  )

  player_4233 = Player(
    player_id = 4233,
    full_name = "Kalija Lipscomb",
    last_name = "Lipscomb",
    first_name = "Kalija",
    nfl_team = "KC",
    position = "WR",
    height = "6-1",
    weight = "200",
    dob = "1997-10-06",
    college = "Vanderbilt"
  )

  player_2769 = Player(
    player_id = 2769,
    full_name = "Tyler Lockett",
    last_name = "Lockett",
    first_name = "Tyler",
    nfl_team = "SEA",
    position = "WR",
    height = "5-10",
    weight = "182",
    dob = "1992-09-28",
    college = "Kansas State"
  )

  player_4087 = Player(
    player_id = 4087,
    full_name = "DaMarkus Lodge",
    last_name = "Lodge",
    first_name = "DaMarkus",
    nfl_team = "CIN",
    position = "WR",
    height = "6-2",
    weight = "202",
    dob = "1997-05-12",
    college = "Ole Miss"
  )

  player_3087 = Player(
    player_id = 3087,
    full_name = "Ricardo Louis",
    last_name = "Louis",
    first_name = "Ricardo",
    nfl_team = "MIA",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1994-03-23",
    college = "Auburn"
  )

  player_4210 = Player(
    player_id = 4210,
    full_name = "Austin Mack",
    last_name = "Mack",
    first_name = "Austin",
    nfl_team = "NYG",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1997-08-31",
    college = "Ohio State"
  )

  player_3330 = Player(
    player_id = 3330,
    full_name = "Josh Malone",
    last_name = "Malone",
    first_name = "Josh",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1996-03-21",
    college = "Tennessee"
  )

  player_4229 = Player(
    player_id = 4229,
    full_name = "Zimari Manning",
    last_name = "Manning",
    first_name = "Zimari",
    nfl_team = "DEN",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "0000-00-00",
    college = "Tarleton State"
  )

  player_4236 = Player(
    player_id = 4236,
    full_name = "Siaosi Mariner",
    last_name = "Mariner",
    first_name = "Siaosi",
    nfl_team = "LV",
    position = "WR",
    height = "6-2",
    weight = "190",
    dob = "0000-00-00",
    college = "Utah State"
  )

  player_4352 = Player(
    player_id = 4352,
    full_name = "Jalen McCleskey",
    last_name = "McCleskey",
    first_name = "Jalen",
    nfl_team = "ATL",
    position = "WR",
    height = "5-11",
    weight = "165",
    dob = "1997-08-06",
    college = "Tulane"
  )

  player_3618 = Player(
    player_id = 3618,
    full_name = "Ray-Ray McCloud",
    last_name = "McCloud",
    first_name = "Ray-Ray",
    nfl_team = "PIT",
    position = "WR",
    height = "5-9",
    weight = "190",
    dob = "1996-10-15",
    college = "Clemson"
  )

  player_3307 = Player(
    player_id = 3307,
    full_name = "Isaiah McKenzie",
    last_name = "McKenzie",
    first_name = "Isaiah",
    nfl_team = "BUF",
    position = "WR",
    height = "5-8",
    weight = "173",
    dob = "1995-04-09",
    college = "Georgia"
  )

  player_3953 = Player(
    player_id = 3953,
    full_name = "Kelvin McKnight",
    last_name = "McKnight",
    first_name = "Kelvin",
    nfl_team = "DEN",
    position = "WR",
    height = "5-8",
    weight = "186",
    dob = "1997-04-25",
    college = "Samford"
  )

  player_3876 = Player(
    player_id = 3876,
    full_name = "Terry McLaurin",
    last_name = "McLaurin",
    first_name = "Terry",
    nfl_team = "WAS",
    position = "WR",
    height = "6-0",
    weight = "210",
    dob = "1995-09-15",
    college = "Ohio State"
  )

  player_4253 = Player(
    player_id = 4253,
    full_name = "Rashad Medaris",
    last_name = "Medaris",
    first_name = "Rashad",
    nfl_team = "ARI",
    position = "WR",
    height = "5-11",
    weight = "178",
    dob = "1996-10-09",
    college = "Cincinnati"
  )

  player_4188 = Player(
    player_id = 4188,
    full_name = "Kirk Merritt",
    last_name = "Merritt",
    first_name = "Kirk",
    nfl_team = "MIA",
    position = "WR",
    height = "6-0",
    weight = "210",
    dob = "1997-01-05",
    college = "Arkansas State"
  )

  player_3903 = Player(
    player_id = 3903,
    full_name = "DK Metcalf",
    last_name = "Metcalf",
    first_name = "DK",
    nfl_team = "SEA",
    position = "WR",
    height = "6-4",
    weight = "230",
    dob = "1997-12-14",
    college = "Mississippi"
  )

  player_3949 = Player(
    player_id = 3949,
    full_name = "Jakobi Meyers",
    last_name = "Meyers",
    first_name = "Jakobi",
    nfl_team = "NE",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1996-11-09",
    college = "North Carolina State"
  )

  player_3228 = Player(
    player_id = 3228,
    full_name = "Marken Michel",
    last_name = "Michel",
    first_name = "Marken",
    nfl_team = "CAR",
    position = "WR",
    height = "5-11",
    weight = "190",
    dob = "1993-07-06",
    college = "Massachusetts"
  )

  player_3162 = Player(
    player_id = 3162,
    full_name = "Jaydon Mickens",
    last_name = "Mickens",
    first_name = "Jaydon",
    nfl_team = "TB",
    position = "WR",
    height = "5-11",
    weight = "170",
    dob = "1994-04-21",
    college = "Washington"
  )

  player_3603 = Player(
    player_id = 3603,
    full_name = "Anthony Miller",
    last_name = "Miller",
    first_name = "Anthony",
    nfl_team = "CHI",
    position = "WR",
    height = "5-11",
    weight = "199",
    dob = "1994-10-09",
    college = "Memphis"
  )

  player_3946 = Player(
    player_id = 3946,
    full_name = "Scott Miller",
    last_name = "Miller",
    first_name = "Scott",
    nfl_team = "TB",
    position = "WR",
    height = "5-11",
    weight = "174",
    dob = "1997-07-31",
    college = "Bowling Green"
  )

  player_4153 = Player(
    player_id = 4153,
    full_name = "Denzel Mims",
    last_name = "Mims",
    first_name = "Denzel",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-3",
    weight = "207",
    dob = "1997-10-10",
    college = "Baylor"
  )

  player_3844 = Player(
    player_id = 3844,
    full_name = "Bryant Mitchell",
    last_name = "Mitchell",
    first_name = "Bryant",
    nfl_team = "TB",
    position = "WR",
    height = "6-2",
    weight = "198",
    dob = "1992-08-16",
    college = "Northwestern State"
  )

  player_3931 = Player(
    player_id = 3931,
    full_name = "Dillon Mitchell",
    last_name = "Mitchell",
    first_name = "Dillon",
    nfl_team = "MIN",
    position = "WR",
    height = "6-1",
    weight = "202",
    dob = "1997-05-16",
    college = "Oregon"
  )

  player_3749 = Player(
    player_id = 3749,
    full_name = "Steven Mitchell",
    last_name = "Mitchell",
    first_name = "Steven",
    nfl_team = "HOU",
    position = "WR",
    height = "5-10",
    weight = "186",
    dob = "1994-05-02",
    college = "Southern California"
  )

  player_4017 = Player(
    player_id = 4017,
    full_name = "Sean Modster",
    last_name = "Modster",
    first_name = "Sean",
    nfl_team = "BAL",
    position = "WR",
    height = "5-11",
    weight = "183",
    dob = "1995-11-13",
    college = "Boise State"
  )

  player_2622 = Player(
    player_id = 2622,
    full_name = "Donte Moncrief",
    last_name = "Moncrief",
    first_name = "Donte",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-2",
    weight = "216",
    dob = "1993-08-06",
    college = "Mississippi"
  )

  player_4032 = Player(
    player_id = 4032,
    full_name = "DJ Montgomery",
    last_name = "Montgomery",
    first_name = "DJ",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-1",
    weight = "201",
    dob = "1996-11-17",
    college = "Austin Peay"
  )

  player_4308 = Player(
    player_id = 4308,
    full_name = "Darnell Mooney",
    last_name = "Mooney",
    first_name = "Darnell",
    nfl_team = "CHI",
    position = "WR",
    height = "5-11",
    weight = "172",
    dob = "1997-10-29",
    college = "Tulane"
  )

  player_3328 = Player(
    player_id = 3328,
    full_name = "David Moore",
    last_name = "Moore",
    first_name = "David",
    nfl_team = "SEA",
    position = "WR",
    height = "6-0",
    weight = "215",
    dob = "1995-01-15",
    college = "East Central"
  )

  player_3080 = Player(
    player_id = 3080,
    full_name = "Chris Moore",
    last_name = "Moore",
    first_name = "Chris",
    nfl_team = "BAL",
    position = "WR",
    height = "6-1",
    weight = "200",
    dob = "1993-06-16",
    college = "Cincinnati"
  )

  player_3612 = Player(
    player_id = 3612,
    full_name = "D.J. Moore",
    last_name = "Moore",
    first_name = "D.J.",
    nfl_team = "CAR",
    position = "WR",
    height = "5-11",
    weight = "215",
    dob = "1997-04-14",
    college = "Maryland"
  )

  player_3660 = Player(
    player_id = 3660,
    full_name = "J'Mon Moore",
    last_name = "Moore",
    first_name = "J'Mon",
    nfl_team = "CLE",
    position = "WR",
    height = "6-3",
    weight = "205",
    dob = "1995-05-23",
    college = "Missouri"
  )

  player_3989 = Player(
    player_id = 3989,
    full_name = "Jason Moore",
    last_name = "Moore",
    first_name = "Jason",
    nfl_team = "LAC",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1995-06-23",
    college = "Findlay"
  )

  player_4290 = Player(
    player_id = 4290,
    full_name = "Jaylon Moore",
    last_name = "Moore",
    first_name = "Jaylon",
    nfl_team = "BAL",
    position = "WR",
    height = "6-2",
    weight = "190",
    dob = "1997-07-01",
    college = "Tennessee-Martin"
  )

  player_4026 = Player(
    player_id = 4026,
    full_name = "Stanley Morgan Jr",
    last_name = "Morgan Jr",
    first_name = "Stanley",
    nfl_team = "CIN",
    position = "WR",
    height = "6-0",
    weight = "205",
    dob = "1996-09-07",
    college = "Nebraska"
  )

  player_3459 = Player(
    player_id = 3459,
    full_name = "JoJo Natson",
    last_name = "Natson",
    first_name = "Bruce",
    nfl_team = "CLE",
    position = "WR",
    height = "5-7",
    weight = "153",
    dob = "1994-02-01",
    college = "Akron"
  )

  player_2761 = Player(
    player_id = 2761,
    full_name = "JJ Nelson",
    last_name = "Nelson",
    first_name = "JJ",
    nfl_team = "SF",
    position = "WR",
    height = "5-10",
    weight = "160",
    dob = "1992-04-24",
    college = "UAB"
  )

  player_3965 = Player(
    player_id = 3965,
    full_name = "Gunner Olszewski",
    last_name = "Olszewski",
    first_name = "Gunner",
    nfl_team = "NE",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1996-11-26",
    college = "Bemidji State"
  )

  player_4321 = Player(
    player_id = 4321,
    full_name = "KJ Osborn",
    last_name = "Osborn",
    first_name = "KJ",
    nfl_team = "MIN",
    position = "WR",
    height = "6-0",
    weight = "200",
    dob = "1997-06-10",
    college = "Miami"
  )

  player_4202 = Player(
    player_id = 4202,
    full_name = "Aaron Parker",
    last_name = "Parker",
    first_name = "Aaron",
    nfl_team = "DAL",
    position = "WR",
    height = "6-3",
    weight = "191",
    dob = "1998-05-21",
    college = "Rhode Island"
  )

  player_2737 = Player(
    player_id = 2737,
    full_name = "DeVante Parker",
    last_name = "Parker",
    first_name = "DeVante",
    nfl_team = "MIA",
    position = "WR",
    height = "6-3",
    weight = "216",
    dob = "1993-01-20",
    college = "Louisville"
  )

  player_3409 = Player(
    player_id = 3409,
    full_name = "Zach Pascal",
    last_name = "Pascal",
    first_name = "Zach",
    nfl_team = "IND",
    position = "WR",
    height = "6-2",
    weight = "214",
    dob = "1994-12-18",
    college = "Old Dominion"
  )

  player_4330 = Player(
    player_id = 4330,
    full_name = "Dezmon Patmon",
    last_name = "Patmon",
    first_name = "Dezmon",
    nfl_team = "IND",
    position = "WR",
    height = "6-4",
    weight = "220",
    dob = "1998-08-06",
    college = "Washington State"
  )

  player_3429 = Player(
    player_id = 3429,
    full_name = "Tim Patrick",
    last_name = "Patrick",
    first_name = "Tim",
    nfl_team = "DEN",
    position = "WR",
    height = "6-4",
    weight = "212",
    dob = "1993-11-23",
    college = "Utah"
  )

  player_2328 = Player(
    player_id = 2328,
    full_name = "Cordarrelle Patterson",
    last_name = "Patterson",
    first_name = "Cordarrelle",
    nfl_team = "CHI",
    position = "WR",
    height = "6-2",
    weight = "238",
    dob = "1991-03-17",
    college = "Tennessee"
  )

  player_3498 = Player(
    player_id = 3498,
    full_name = "Andre Patton",
    last_name = "Patton",
    first_name = "Andre",
    nfl_team = "ARI",
    position = "WR",
    height = "6-4",
    weight = "200",
    dob = "1994-05-28",
    college = "Rutgers"
  )

  player_3035 = Player(
    player_id = 3035,
    full_name = "Charone Peake",
    last_name = "Peake",
    first_name = "Charone",
    nfl_team = "PIT",
    position = "WR",
    height = "6-2",
    weight = "209",
    dob = "1992-10-16",
    college = "Clemson"
  )

  player_4380 = Player(
    player_id = 4380,
    full_name = "Josh Pearson",
    last_name = "Pearson",
    first_name = "Josh",
    nfl_team = "TB",
    position = "WR",
    height = "6-4",
    weight = "205",
    dob = "1997-06-13",
    college = "Jacksonville State"
  )

  player_4303 = Player(
    player_id = 4303,
    full_name = "Donovan Peoples-Jones",
    last_name = "Peoples-Jones",
    first_name = "Donovan",
    nfl_team = "CLE",
    position = "WR",
    height = "6-2",
    weight = "208",
    dob = "1999-02-19",
    college = "Michigan"
  )

  player_2774 = Player(
    player_id = 2774,
    full_name = "Breshad Perriman",
    last_name = "Perriman",
    first_name = "Breshad",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1993-09-10",
    college = "Central Florida"
  )

  player_3594 = Player(
    player_id = 3594,
    full_name = "Dante Pettis",
    last_name = "Pettis",
    first_name = "Dante",
    nfl_team = "SF",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1995-10-23",
    college = "Washington"
  )

  player_4254 = Player(
    player_id = 4254,
    full_name = "Devin Phelps",
    last_name = "Phelps",
    first_name = "Devin",
    nfl_team = "ARI",
    position = "WR",
    height = "6-1",
    weight = "190",
    dob = "0000-00-00",
    college = "Shepherd"
  )

  player_3682 = Player(
    player_id = 3682,
    full_name = "Cam Phillips",
    last_name = "Phillips",
    first_name = "Cam",
    nfl_team = "CAR",
    position = "WR",
    height = "6-0",
    weight = "201",
    dob = "1995-12-16",
    college = "Virginia Tech"
  )

  player_3853 = Player(
    player_id = 3853,
    full_name = "De'Mornay Pierson-El",
    last_name = "Pierson-El",
    first_name = "De'Mornay",
    nfl_team = "LV",
    position = "WR",
    height = "5-9",
    weight = "195",
    dob = "1995-12-26",
    college = "Nebraska"
  )

  player_4176 = Player(
    player_id = 4176,
    full_name = "Michael Pittman Jr",
    last_name = "Pittman Jr",
    first_name = "Michael",
    nfl_team = "IND",
    position = "WR",
    height = "6-4",
    weight = "220",
    dob = "1997-10-05",
    college = "Southern California"
  )

  player_4003 = Player(
    player_id = 4003,
    full_name = "Shawn Poindexter",
    last_name = "Poindexter",
    first_name = "Shawn",
    nfl_team = "SF",
    position = "WR",
    height = "6-5",
    weight = "213",
    dob = "1995-12-13",
    college = "Arizona"
  )

  player_4282 = Player(
    player_id = 4282,
    full_name = "Brandon Polk",
    last_name = "Polk",
    first_name = "Brandon",
    nfl_team = "LAR",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "1996-12-10",
    college = "James Madison"
  )

  player_3782 = Player(
    player_id = 3782,
    full_name = "Brandon Powell",
    last_name = "Powell",
    first_name = "Brandon",
    nfl_team = "ATL",
    position = "WR",
    height = "5-8",
    weight = "189",
    dob = "1995-09-12",
    college = "Florida"
  )

  player_3714 = Player(
    player_id = 3714,
    full_name = "Byron Pringle",
    last_name = "Pringle",
    first_name = "Byron",
    nfl_team = "KC",
    position = "WR",
    height = "6-1",
    weight = "205",
    dob = "1993-11-17",
    college = "Kansas State"
  )

  player_4291 = Player(
    player_id = 4291,
    full_name = "James Proche",
    last_name = "Proche",
    first_name = "James",
    nfl_team = "BAL",
    position = "WR",
    height = "6-0",
    weight = "193",
    dob = "1996-09-21",
    college = "Southern Methodist"
  )

  player_3635 = Player(
    player_id = 3635,
    full_name = "Trey Quinn",
    last_name = "Quinn",
    first_name = "Trey",
    nfl_team = "WAS",
    position = "WR",
    height = "6-0",
    weight = "202",
    dob = "1995-12-07",
    college = "Southern Methodist"
  )

  player_3656 = Player(
    player_id = 3656,
    full_name = "Damion Ratley",
    last_name = "Ratley",
    first_name = "Damion",
    nfl_team = "NYG",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1995-04-16",
    college = "Texas A&amp;M"
  )

  player_4072 = Player(
    player_id = 4072,
    full_name = "Anthony Ratliff Williams",
    last_name = "Ratliff Williams",
    first_name = "Anthony",
    nfl_team = "LV",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1997-06-17",
    college = "North Carolina"
  )

  player_3308 = Player(
    player_id = 3308,
    full_name = "Kalif Raymond",
    last_name = "Raymond",
    first_name = "Kalif",
    nfl_team = "TEN",
    position = "WR",
    height = "5-8",
    weight = "182",
    dob = "1994-08-08",
    college = "Holy Cross"
  )

  player_4131 = Player(
    player_id = 4131,
    full_name = "Jalen Reagor",
    last_name = "Reagor",
    first_name = "Jalen",
    nfl_team = "PHI",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1999-01-02",
    college = "Texas Christian"
  )

  player_4243 = Player(
    player_id = 4243,
    full_name = "Joe Reed",
    last_name = "Reed",
    first_name = "Joe",
    nfl_team = "LAC",
    position = "WR",
    height = "6-1",
    weight = "215",
    dob = "1998-01-04",
    college = "Virginia"
  )

  player_3890 = Player(
    player_id = 3890,
    full_name = "Hunter Renfrow",
    last_name = "Renfrow",
    first_name = "Hunter",
    nfl_team = "LV",
    position = "WR",
    height = "5-10",
    weight = "185",
    dob = "1995-12-21",
    college = "Clemson"
  )

  player_3560 = Player(
    player_id = 3560,
    full_name = "Josh Reynolds",
    last_name = "Reynolds",
    first_name = "Josh",
    nfl_team = "LAR",
    position = "WR",
    height = "6-3",
    weight = "196",
    dob = "1995-02-16",
    college = "Texas A&amp;M"
  )

  player_3998 = Player(
    player_id = 3998,
    full_name = "AJ Richardson",
    last_name = "Richardson",
    first_name = "AJ",
    nfl_team = "ARI",
    position = "WR",
    height = "6-0",
    weight = "212",
    dob = "1995-06-02",
    college = "Boise State"
  )

  player_2537 = Player(
    player_id = 2537,
    full_name = "Paul Richardson",
    last_name = "Richardson",
    first_name = "Paul",
    nfl_team = "SEA",
    position = "WR",
    height = "6-0",
    weight = "180",
    dob = "1992-04-13",
    college = "Colorado"
  )

  player_3611 = Player(
    player_id = 3611,
    full_name = "Calvin Ridley",
    last_name = "Ridley",
    first_name = "Calvin",
    nfl_team = "ATL",
    position = "WR",
    height = "6-1",
    weight = "190",
    dob = "1994-12-20",
    college = "Alabama"
  )

  player_3922 = Player(
    player_id = 3922,
    full_name = "Riley Ridley",
    last_name = "Ridley",
    first_name = "Riley",
    nfl_team = "CHI",
    position = "WR",
    height = "6-1",
    weight = "200",
    dob = "1996-07-21",
    college = "Georgia"
  )

  player_4192 = Player(
    player_id = 4192,
    full_name = "Sean Riley",
    last_name = "Riley",
    first_name = "Sean",
    nfl_team = "NE",
    position = "WR",
    height = "5-8",
    weight = "178",
    dob = "1997-10-31",
    college = "Syracuse"
  )

  player_1166 = Player(
    player_id = 1166,
    full_name = "Andre Roberts",
    last_name = "Roberts",
    first_name = "Andre",
    nfl_team = "BUF",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1988-01-09",
    college = "Citadel"
  )

  player_2508 = Player(
    player_id = 2508,
    full_name = "Seth Roberts",
    last_name = "Roberts",
    first_name = "Seth",
    nfl_team = "CAR",
    position = "WR",
    height = "6-2",
    weight = "195",
    dob = "1991-02-22",
    college = "West Alabama"
  )

  player_2635 = Player(
    player_id = 2635,
    full_name = "Allen Robinson",
    last_name = "Robinson",
    first_name = "Allen",
    nfl_team = "CHI",
    position = "WR",
    height = "6-2",
    weight = "220",
    dob = "1993-08-24",
    college = "Penn State"
  )

  player_3057 = Player(
    player_id = 3057,
    full_name = "Demarcus Robinson",
    last_name = "Robinson",
    first_name = "Demarcus",
    nfl_team = "KC",
    position = "WR",
    height = "6-1",
    weight = "203",
    dob = "1994-09-21",
    college = "Florida"
  )

  player_3108 = Player(
    player_id = 3108,
    full_name = "Chester Rogers",
    last_name = "Rogers",
    first_name = "Chester",
    nfl_team = "MIA",
    position = "WR",
    height = "6-0",
    weight = "184",
    dob = "1994-01-12",
    college = "Grambling"
  )

  player_4203 = Player(
    player_id = 4203,
    full_name = "Kendrick Rogers",
    last_name = "Rogers",
    first_name = "Kendrick",
    nfl_team = "DAL",
    position = "WR",
    height = "6-4",
    weight = "204",
    dob = "1997-08-07",
    college = "Texas A&amp;M"
  )

  player_3331 = Player(
    player_id = 3331,
    full_name = "John Ross",
    last_name = "Ross",
    first_name = "John",
    nfl_team = "CIN",
    position = "WR",
    height = "5-11",
    weight = "194",
    dob = "1995-11-27",
    college = "Washington"
  )

  player_3811 = Player(
    player_id = 3811,
    full_name = "Devin Ross",
    last_name = "Ross",
    first_name = "Devin",
    nfl_team = "NE",
    position = "WR",
    height = "5-11",
    weight = "185",
    dob = "1995-08-12",
    college = "Colorado"
  )

  player_4340 = Player(
    player_id = 4340,
    full_name = "Marvelle Ross",
    last_name = "Ross",
    first_name = "Marvelle",
    nfl_team = "JAC",
    position = "WR",
    height = "5-9",
    weight = "180",
    dob = "0000-00-00",
    college = "Notre Dame of Ohio"
  )

  player_4353 = Player(
    player_id = 4353,
    full_name = "Chris Rowland",
    last_name = "Rowland",
    first_name = "Chris",
    nfl_team = "ATL",
    position = "WR",
    height = "5-8",
    weight = "180",
    dob = "1997-12-19",
    college = "Tennessee State"
  )

  player_4134 = Player(
    player_id = 4134,
    full_name = "Henry Ruggs III",
    last_name = "Ruggs III",
    first_name = "Henry",
    nfl_team = "LV",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1999-01-24",
    college = "Alabama"
  )

  player_3381 = Player(
    player_id = 3381,
    full_name = "Curtis Samuel",
    last_name = "Samuel",
    first_name = "Curtis",
    nfl_team = "CAR",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1996-08-11",
    college = "Ohio State"
  )

  player_3899 = Player(
    player_id = 3899,
    full_name = "Deebo Samuel",
    last_name = "Samuel",
    first_name = "Deebo",
    nfl_team = "SF",
    position = "WR",
    height = "6-0",
    weight = "215",
    dob = "1996-01-15",
    college = "South Carolina"
  )

  player_1168 = Player(
    player_id = 1168,
    full_name = "Emmanuel Sanders",
    last_name = "Sanders",
    first_name = "Emmanuel",
    nfl_team = "NO",
    position = "WR",
    height = "5-11",
    weight = "180",
    dob = "1987-03-17",
    college = "Southern Methodist"
  )

  player_1875 = Player(
    player_id = 1875,
    full_name = "Mohamed Sanu",
    last_name = "Sanu",
    first_name = "Mohamed",
    nfl_team = "SF",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1989-08-22",
    college = "Rutgers"
  )

  player_4088 = Player(
    player_id = 4088,
    full_name = "Spencer Schnell",
    last_name = "Schnell",
    first_name = "Spencer",
    nfl_team = "TB",
    position = "WR",
    height = "5-8",
    weight = "178",
    dob = "1994-12-07",
    college = "Illinois State"
  )

  player_4244 = Player(
    player_id = 4244,
    full_name = "Dalton Schoen",
    last_name = "Schoen",
    first_name = "Dalton",
    nfl_team = "LAC",
    position = "WR",
    height = "6-1",
    weight = "206",
    dob = "1996-10-13",
    college = "Kansas State"
  )

  player_3651 = Player(
    player_id = 3651,
    full_name = "Jaleel Scott",
    last_name = "Scott",
    first_name = "Jaleel",
    nfl_team = "BAL",
    position = "WR",
    height = "6-5",
    weight = "210",
    dob = "1995-02-23",
    college = "New Mexico State"
  )

  player_3499 = Player(
    player_id = 3499,
    full_name = "Artavis Scott",
    last_name = "Scott",
    first_name = "Artavis",
    nfl_team = "IND",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1994-10-12",
    college = "Clemson"
  )

  player_3769 = Player(
    player_id = 3769,
    full_name = "Da'Mari Scott",
    last_name = "Scott",
    first_name = "Da'Mari",
    nfl_team = "NYG",
    position = "WR",
    height = "6-0",
    weight = "205",
    dob = "1995-08-08",
    college = "Fresno State"
  )

  player_3113 = Player(
    player_id = 3113,
    full_name = "Tajae Sharpe",
    last_name = "Sharpe",
    first_name = "Tajae",
    nfl_team = "MIN",
    position = "WR",
    height = "6-2",
    weight = "194",
    dob = "1994-12-23",
    college = "Massachusetts"
  )

  player_4234 = Player(
    player_id = 4234,
    full_name = "Justice Shelton-Mosley",
    last_name = "Shelton-Mosley",
    first_name = "Justice",
    nfl_team = "KC",
    position = "WR",
    height = "5-10",
    weight = "196",
    dob = "0000-00-00",
    college = "Vanderbilt"
  )

  player_4177 = Player(
    player_id = 4177,
    full_name = "Laviska Shenault Jr",
    last_name = "Shenault Jr",
    first_name = "Laviska",
    nfl_team = "JAC",
    position = "WR",
    height = "6-2",
    weight = "220",
    dob = "1998-10-05",
    college = "Colorado"
  )

  player_3042 = Player(
    player_id = 3042,
    full_name = "Sterling Shepard",
    last_name = "Shepard",
    first_name = "Sterling",
    nfl_team = "NYG",
    position = "WR",
    height = "5-10",
    weight = "201",
    dob = "1993-02-10",
    college = "Oklahoma"
  )

  player_4048 = Player(
    player_id = 4048,
    full_name = "Darrius Shepherd",
    last_name = "Shepherd",
    first_name = "Darrius",
    nfl_team = "GB",
    position = "WR",
    height = "5-11",
    weight = "188",
    dob = "1995-11-01",
    college = "North Dakota State"
  )

  player_3734 = Player(
    player_id = 3734,
    full_name = "Trent Sherfield",
    last_name = "Sherfield",
    first_name = "Trent",
    nfl_team = "ARI",
    position = "WR",
    height = "6-1",
    weight = "219",
    dob = "1996-02-25",
    college = "Vanderbilt"
  )

  player_3957 = Player(
    player_id = 3957,
    full_name = "David Sills",
    last_name = "Sills",
    first_name = "David",
    nfl_team = "NYG",
    position = "WR",
    height = "6-3",
    weight = "211",
    dob = "1996-05-29",
    college = "West Virginia"
  )

  player_4327 = Player(
    player_id = 4327,
    full_name = "Tyler Simmons",
    last_name = "Simmons",
    first_name = "Tyler",
    nfl_team = "HOU",
    position = "WR",
    height = "6-0",
    weight = "201",
    dob = "1997-12-30",
    college = "Georgia"
  )

  player_3703 = Player(
    player_id = 3703,
    full_name = "Cam Sims",
    last_name = "Sims",
    first_name = "Cam",
    nfl_team = "WAS",
    position = "WR",
    height = "6-5",
    weight = "214",
    dob = "1996-01-06",
    college = "Alabama"
  )

  player_3878 = Player(
    player_id = 3878,
    full_name = "Steven Sims",
    last_name = "Sims Jr",
    first_name = "Steven",
    nfl_team = "WAS",
    position = "WR",
    height = "5-10",
    weight = "176",
    dob = "1997-03-31",
    college = "Kansas"
  )

  player_537 = Player(
    player_id = 537,
    full_name = "Matthew Slater",
    last_name = "Slater",
    first_name = "Matthew",
    nfl_team = "NE",
    position = "WR",
    height = "6-0",
    weight = "205",
    dob = "1985-09-09",
    college = "UCLA"
  )

  player_3869 = Player(
    player_id = 3869,
    full_name = "Darius Slayton",
    last_name = "Slayton",
    first_name = "Darius",
    nfl_team = "NYG",
    position = "WR",
    height = "6-1",
    weight = "190",
    dob = "1997-01-12",
    college = "Auburn"
  )

  player_3617 = Player(
    player_id = 3617,
    full_name = "Tre'Quan Smith",
    last_name = "Smith",
    first_name = "Tre'Quan",
    nfl_team = "NO",
    position = "WR",
    height = "6-2",
    weight = "210",
    dob = "1996-01-07",
    college = "Central Florida"
  )

  player_3967 = Player(
    player_id = 3967,
    full_name = "Jeff Smith",
    last_name = "Smith",
    first_name = "Jeff",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-1",
    weight = "195",
    dob = "1997-04-21",
    college = "Boston College"
  )

  player_2740 = Player(
    player_id = 2740,
    full_name = "Devin Smith",
    last_name = "Smith",
    first_name = "Devin",
    nfl_team = "DAL",
    position = "WR",
    height = "6-1",
    weight = "199",
    dob = "1992-03-03",
    college = "Ohio State"
  )

  player_3800 = Player(
    player_id = 3800,
    full_name = "Vyncint Smith",
    last_name = "Smith",
    first_name = "Vyncint",
    nfl_team = "NYJ",
    position = "WR",
    height = "6-3",
    weight = "202",
    dob = "1996-06-09",
    college = "Limestone"
  )

  player_3340 = Player(
    player_id = 3340,
    full_name = "JuJu Smith-Schuster",
    last_name = "Smith-Schuster",
    first_name = "JuJu",
    nfl_team = "PIT",
    position = "WR",
    height = "6-1",
    weight = "215",
    dob = "1996-11-22",
    college = "Southern California"
  )

  player_2571 = Player(
    player_id = 2571,
    full_name = "Willie Snead",
    last_name = "Snead",
    first_name = "Willie",
    nfl_team = "BAL",
    position = "WR",
    height = "5-11",
    weight = "205",
    dob = "1992-10-17",
    college = "Ball State"
  )

  player_2697 = Player(
    player_id = 2697,
    full_name = "Diontae Spencer",
    last_name = "Spencer",
    first_name = "Diontae",
    nfl_team = "DEN",
    position = "WR",
    height = "5-8",
    weight = "170",
    dob = "1992-03-19",
    college = "McNeese State"
  )

  player_3661 = Player(
    player_id = 3661,
    full_name = "Equanimeous St. Brown",
    last_name = "St. Brown",
    first_name = "Equanimeous",
    nfl_team = "GB",
    position = "WR",
    height = "6-5",
    weight = "214",
    dob = "1996-09-30",
    college = "Notre Dame"
  )

  player_4316 = Player(
    player_id = 4316,
    full_name = "Darrell Stewart Jr",
    last_name = "Stewart Jr",
    first_name = "Darrell",
    nfl_team = "CAR",
    position = "WR",
    height = "6-0",
    weight = "212",
    dob = "1996-07-14",
    college = "Michigan State"
  )

  player_2388 = Player(
    player_id = 2388,
    full_name = "Kenny Stills",
    last_name = "Stills",
    first_name = "Kenny",
    nfl_team = "HOU",
    position = "WR",
    height = "6-1",
    weight = "202",
    dob = "1992-04-22",
    college = "Oklahoma"
  )

  player_4272 = Player(
    player_id = 4272,
    full_name = "Stephen Sullivan",
    last_name = "Sullivan",
    first_name = "Stephen",
    nfl_team = "SEA",
    position = "WR",
    height = "6-5",
    weight = "242",
    dob = "1996-11-28",
    college = "Louisiana State"
  )

  player_4273 = Player(
    player_id = 4273,
    full_name = "Freddie Swain",
    last_name = "Swain",
    first_name = "Freddie",
    nfl_team = "SEA",
    position = "WR",
    height = "6-0",
    weight = "199",
    dob = "1998-08-04",
    college = "Florida"
  )

  player_3291 = Player(
    player_id = 3291,
    full_name = "Ryan Switzer",
    last_name = "Switzer",
    first_name = "Ryan",
    nfl_team = "PIT",
    position = "WR",
    height = "5-8",
    weight = "185",
    dob = "1994-11-04",
    college = "North Carolina"
  )

  player_3654 = Player(
    player_id = 3654,
    full_name = "Auden Tate",
    last_name = "Tate",
    first_name = "Auden",
    nfl_team = "CIN",
    position = "WR",
    height = "6-5",
    weight = "228",
    dob = "1997-02-03",
    college = "Florida State"
  )

  player_4217 = Player(
    player_id = 4217,
    full_name = "Khalil Tate",
    last_name = "Tate",
    first_name = "Khalil",
    nfl_team = "PHI",
    position = "WR",
    height = "6-0",
    weight = "216",
    dob = "1998-10-23",
    college = "Arizona"
  )

  player_1170 = Player(
    player_id = 1170,
    full_name = "Golden Tate",
    last_name = "Tate",
    first_name = "Golden",
    nfl_team = "NYG",
    position = "WR",
    height = "5-10",
    weight = "197",
    dob = "1988-08-02",
    college = "Notre Dame"
  )

  player_4102 = Player(
    player_id = 4102,
    full_name = "Malik Taylor",
    last_name = "Taylor",
    first_name = "Malik",
    nfl_team = "GB",
    position = "WR",
    height = "6-2",
    weight = "216",
    dob = "1995-12-21",
    college = "Ferris State"
  )

  player_3374 = Player(
    player_id = 3374,
    full_name = "Taywan Taylor",
    last_name = "Taylor",
    first_name = "Taywan",
    nfl_team = "CLE",
    position = "WR",
    height = "5-11",
    weight = "203",
    dob = "1995-03-02",
    college = "Western Kentucky"
  )

  player_3323 = Player(
    player_id = 3323,
    full_name = "Trent Taylor",
    last_name = "Taylor",
    first_name = "Trent",
    nfl_team = "SF",
    position = "WR",
    height = "5-8",
    weight = "181",
    dob = "1994-04-30",
    college = "Louisiana Tech"
  )

  player_2330 = Player(
    player_id = 2330,
    full_name = "Adam Thielen",
    last_name = "Thielen",
    first_name = "Adam",
    nfl_team = "MIN",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1990-08-22",
    college = "Minn. State-Mankato"
  )

  player_3119 = Player(
    player_id = 3119,
    full_name = "Michael Thomas",
    last_name = "Thomas",
    first_name = "Michael",
    nfl_team = "NO",
    position = "WR",
    height = "6-3",
    weight = "212",
    dob = "1993-03-03",
    college = "Ohio State"
  )

  player_860 = Player(
    player_id = 860,
    full_name = "Mike Thomas",
    last_name = "Thomas",
    first_name = "Mike",
    nfl_team = "CIN",
    position = "WR",
    height = "6-1",
    weight = "189",
    dob = "1994-08-16",
    college = "Southern Mississippi"
  )

  player_4193 = Player(
    player_id = 4193,
    full_name = "Jeff Thomas",
    last_name = "Thomas",
    first_name = "Jeff",
    nfl_team = "NE",
    position = "WR",
    height = "5-10",
    weight = "174",
    dob = "1997-06-17",
    college = "Miami (FL)"
  )

  player_2496 = Player(
    player_id = 2496,
    full_name = "De'Anthony Thomas",
    last_name = "Thomas",
    first_name = "De'Anthony",
    nfl_team = "BAL",
    position = "WR",
    height = "5-8",
    weight = "176",
    dob = "1993-01-05",
    college = "Oregon"
  )

  player_3975 = Player(
    player_id = 3975,
    full_name = "DeAndre Thompkins",
    last_name = "Thompkins",
    first_name = "DeAndre",
    nfl_team = "PIT",
    position = "WR",
    height = "5-11",
    weight = "188",
    dob = "1995-10-01",
    college = "Penn State"
  )

  player_3983 = Player(
    player_id = 3983,
    full_name = "Cody Thompson",
    last_name = "Thompson",
    first_name = "Cody",
    nfl_team = "SEA",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1996-01-11",
    college = "Toledo"
  )

  player_3990 = Player(
    player_id = 3990,
    full_name = "Trevion Thompson",
    last_name = "Thompson",
    first_name = "Trevion",
    nfl_team = "TEN",
    position = "WR",
    height = "6-2",
    weight = "205",
    dob = "1995-11-14",
    college = "Clemson"
  )

  player_3529 = Player(
    player_id = 3529,
    full_name = "Chris Thompson",
    last_name = "Thompson",
    first_name = "Chris",
    nfl_team = "SF",
    position = "WR",
    height = "6-0",
    weight = "175",
    dob = "1994-05-09",
    college = "Florida"
  )

  player_3100 = Player(
    player_id = 3100,
    full_name = "Laquon Treadwell",
    last_name = "Treadwell",
    first_name = "Laquon",
    nfl_team = "ATL",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1995-06-14",
    college = "Mississippi"
  )

  player_3744 = Player(
    player_id = 3744,
    full_name = "Malik Turner",
    last_name = "Turner",
    first_name = "Malik",
    nfl_team = "DAL",
    position = "WR",
    height = "6-2",
    weight = "200",
    dob = "1996-01-30",
    college = "Illinois"
  )

  player_3904 = Player(
    player_id = 3904,
    full_name = "John Ursua",
    last_name = "Ursua",
    first_name = "John",
    nfl_team = "SEA",
    position = "WR",
    height = "5-9",
    weight = "182",
    dob = "1994-01-17",
    college = "Hawaii"
  )

  player_3662 = Player(
    player_id = 3662,
    full_name = "Marquez Valdes-Scantling",
    last_name = "Valdes-Scantling",
    first_name = "Marquez",
    nfl_team = "GB",
    position = "WR",
    height = "6-4",
    weight = "207",
    dob = "1994-10-10",
    college = "South Florida"
  )

  player_3812 = Player(
    player_id = 3812,
    full_name = "Jordan Veasy",
    last_name = "Veasy",
    first_name = "Jordan",
    nfl_team = "WAS",
    position = "WR",
    height = "6-3",
    weight = "221",
    dob = "1995-06-23",
    college = "California"
  )

  player_4211 = Player(
    player_id = 4211,
    full_name = "Binjimen Victor",
    last_name = "Victor",
    first_name = "Binjimen",
    nfl_team = "NYG",
    position = "WR",
    height = "6-4",
    weight = "199",
    dob = "1997-01-15",
    college = "Ohio State"
  )

  player_4309 = Player(
    player_id = 4309,
    full_name = "Ahmad Wagner",
    last_name = "Wagner",
    first_name = "Ahmad",
    nfl_team = "CHI",
    position = "WR",
    height = "6-5",
    weight = "234",
    dob = "0000-00-00",
    college = "Kentucky"
  )

  player_4067 = Player(
    player_id = 4067,
    full_name = "Michael Walker",
    last_name = "Walker",
    first_name = "Michael",
    nfl_team = "JAC",
    position = "WR",
    height = "5-11",
    weight = "195",
    dob = "1996-10-29",
    college = "Boston College"
  )

  player_3487 = Player(
    player_id = 3487,
    full_name = "Greg Ward",
    last_name = "Ward",
    first_name = "Greg",
    nfl_team = "PHI",
    position = "WR",
    height = "5-11",
    weight = "190",
    dob = "1995-07-12",
    college = "Houston"
  )

  player_4255 = Player(
    player_id = 4255,
    full_name = "JoJo Ward",
    last_name = "Ward",
    first_name = "JoJo",
    nfl_team = "ARI",
    position = "WR",
    height = "5-9",
    weight = "175",
    dob = "1997-12-09",
    college = "Hawaii"
  )

  player_3602 = Player(
    player_id = 3602,
    full_name = "James Washington",
    last_name = "Washington",
    first_name = "James",
    nfl_team = "PIT",
    position = "WR",
    height = "5-11",
    weight = "213",
    dob = "1996-04-02",
    college = "Oklahoma State"
  )

  player_4296 = Player(
    player_id = 4296,
    full_name = "Scotty Washington",
    last_name = "Washington",
    first_name = "Scotty",
    nfl_team = "CIN",
    position = "WR",
    height = "6-5",
    weight = "225",
    dob = "1996-07-26",
    college = "Wake Forest"
  )

  player_4218 = Player(
    player_id = 4218,
    full_name = "Quez Watkins",
    last_name = "Watkins",
    first_name = "Quez",
    nfl_team = "PHI",
    position = "WR",
    height = "6-0",
    weight = "193",
    dob = "1998-06-09",
    college = "Southern Miss"
  )

  player_2432 = Player(
    player_id = 2432,
    full_name = "Sammy Watkins",
    last_name = "Watkins",
    first_name = "Sammy",
    nfl_team = "KC",
    position = "WR",
    height = "6-1",
    weight = "211",
    dob = "1993-06-14",
    college = "Clemson"
  )

  player_3678 = Player(
    player_id = 3678,
    full_name = "Justin Watson",
    last_name = "Watson",
    first_name = "Justin",
    nfl_team = "TB",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1996-04-04",
    college = "Pennsylvania"
  )

  player_3801 = Player(
    player_id = 3801,
    full_name = "Jester Weah",
    last_name = "Weah",
    first_name = "Jester",
    nfl_team = "WAS",
    position = "WR",
    height = "6-3",
    weight = "209",
    dob = "1995-02-07",
    college = "Pittsburgh"
  )

  player_4012 = Player(
    player_id = 4012,
    full_name = "Nsimba Webster",
    last_name = "Webster",
    first_name = "Nsimba",
    nfl_team = "LAR",
    position = "WR",
    height = "5-10",
    weight = "180",
    dob = "1996-01-27",
    college = "Eastern Washington"
  )

  player_3972 = Player(
    player_id = 3972,
    full_name = "Alex Wesley",
    last_name = "Wesley",
    first_name = "Alex",
    nfl_team = "CHI",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1995-10-27",
    college = "Northern Colorado"
  )

  player_4019 = Player(
    player_id = 4019,
    full_name = "Antoine Wesley",
    last_name = "Wesley",
    first_name = "Antoine",
    nfl_team = "BAL",
    position = "WR",
    height = "6-4",
    weight = "206",
    dob = "1997-10-22",
    college = "Texas Tech"
  )

  player_4377 = Player(
    player_id = 4377,
    full_name = "Nick Westbrook",
    last_name = "Westbrook",
    first_name = "Nick",
    nfl_team = "TEN",
    position = "WR",
    height = "6-2",
    weight = "211",
    dob = "0000-00-00",
    college = "Indiana"
  )

  player_3369 = Player(
    player_id = 3369,
    full_name = "Dede Westbrook",
    last_name = "Westbrook",
    first_name = "Dede",
    nfl_team = "JAC",
    position = "WR",
    height = "6-0",
    weight = "176",
    dob = "1993-11-21",
    college = "Oklahoma"
  )

  player_2837 = Player(
    player_id = 2837,
    full_name = "DeAndrew White",
    last_name = "White",
    first_name = "DeAndrew",
    nfl_team = "BAL",
    position = "WR",
    height = "6-0",
    weight = "195",
    dob = "1991-10-16",
    college = "Alabama"
  )

  player_3430 = Player(
    player_id = 3430,
    full_name = "Tim White",
    last_name = "White",
    first_name = "Tim",
    nfl_team = "NO",
    position = "WR",
    height = "5-10",
    weight = "185",
    dob = "1994-07-15",
    college = "Arizona State"
  )

  player_4235 = Player(
    player_id = 4235,
    full_name = "Cody White",
    last_name = "White",
    first_name = "Cody",
    nfl_team = "DEN",
    position = "WR",
    height = "6-3",
    weight = "217",
    dob = "1998-11-28",
    college = "Michigan State"
  )

  player_2787 = Player(
    player_id = 2787,
    full_name = "Kevin White",
    last_name = "White",
    first_name = "Kevin",
    nfl_team = "SF",
    position = "WR",
    height = "6-3",
    weight = "216",
    dob = "1992-06-25",
    college = "West Virginia"
  )

  player_3973 = Player(
    player_id = 3973,
    full_name = "Reggie White Jr",
    last_name = "White Jr",
    first_name = "Reggie",
    nfl_team = "NYG",
    position = "WR",
    height = "6-2",
    weight = "212",
    dob = "1996-03-10",
    college = "Monmouth"
  )

  player_3412 = Player(
    player_id = 3412,
    full_name = "Isaac Whitney",
    last_name = "Whitney",
    first_name = "Isaac",
    nfl_team = "HOU",
    position = "WR",
    height = "6-2",
    weight = "204",
    dob = "1994-06-22",
    college = "USC"
  )

  player_4346 = Player(
    player_id = 4346,
    full_name = "Kristian Wilkerson",
    last_name = "Wilkerson",
    first_name = "Kristian",
    nfl_team = "TEN",
    position = "WR",
    height = "6-1",
    weight = "214",
    dob = "1997-01-10",
    college = "Southeast Missouri"
  )

  player_3842 = Player(
    player_id = 3842,
    full_name = "Duke Williams",
    last_name = "Williams",
    first_name = "Duke",
    nfl_team = "BUF",
    position = "WR",
    height = "6-3",
    weight = "225",
    dob = "1992-05-13",
    college = "Auburn"
  )

  player_2920 = Player(
    player_id = 2920,
    full_name = "Tyrell Williams",
    last_name = "Williams",
    first_name = "Tyrell",
    nfl_team = "LV",
    position = "WR",
    height = "6-4",
    weight = "205",
    dob = "1992-02-12",
    college = "Western Oregon"
  )

  player_3963 = Player(
    player_id = 3963,
    full_name = "Preston Williams",
    last_name = "Williams",
    first_name = "Preston",
    nfl_team = "MIA",
    position = "WR",
    height = "6-5",
    weight = "218",
    dob = "1997-03-27",
    college = "Colorado State"
  )

  player_3316 = Player(
    player_id = 3316,
    full_name = "Mike Williams",
    last_name = "Williams",
    first_name = "Mike",
    nfl_team = "LAC",
    position = "WR",
    height = "6-4",
    weight = "218",
    dob = "1994-10-04",
    college = "Clemson"
  )

  player_3320 = Player(
    player_id = 3320,
    full_name = "Chad Williams",
    last_name = "Williams",
    first_name = "Chad",
    nfl_team = "IND",
    position = "WR",
    height = "6-2",
    weight = "204",
    dob = "1994-10-19",
    college = "Grambling State"
  )

  player_4347 = Player(
    player_id = 4347,
    full_name = "Kyle Williams",
    last_name = "Williams",
    first_name = "Kyle",
    nfl_team = "TEN",
    position = "WR",
    height = "5-10",
    weight = "192",
    dob = "1998-10-15",
    college = "Arizona State"
  )

  player_4027 = Player(
    player_id = 4027,
    full_name = "Damion Willis",
    last_name = "Willis",
    first_name = "Damion",
    nfl_team = "CLE",
    position = "WR",
    height = "6-3",
    weight = "204",
    dob = "1997-06-20",
    college = "Troy"
  )

  player_3630 = Player(
    player_id = 3630,
    full_name = "Cedrick Wilson",
    last_name = "Wilson",
    first_name = "Cedrick",
    nfl_team = "DAL",
    position = "WR",
    height = "6-5",
    weight = "188",
    dob = "1995-11-20",
    college = "Boise State"
  )

  player_2501 = Player(
    player_id = 2501,
    full_name = "Albert Wilson",
    last_name = "Wilson",
    first_name = "Albert",
    nfl_team = "MIA",
    position = "WR",
    height = "5-9",
    weight = "195",
    dob = "1992-07-12",
    college = "Georgia State"
  )

  player_3658 = Player(
    player_id = 3658,
    full_name = "Javon Wims",
    last_name = "Wims",
    first_name = "Javon",
    nfl_team = "CHI",
    position = "WR",
    height = "6-2",
    weight = "221",
    dob = "1994-09-11",
    college = "Georgia"
  )

  player_3883 = Player(
    player_id = 3883,
    full_name = "Juwann Winfree",
    last_name = "Winfree",
    first_name = "Juwann",
    nfl_team = "DEN",
    position = "WR",
    height = "6-3",
    weight = "215",
    dob = "1996-09-04",
    college = "Colorado"
  )

  player_4283 = Player(
    player_id = 4283,
    full_name = "Easop Winston Jr",
    last_name = "Winston Jr",
    first_name = "Easop",
    nfl_team = "LAR",
    position = "WR",
    height = "6-0",
    weight = "192",
    dob = "1996-12-10",
    college = "Washington State"
  )

  player_2122 = Player(
    player_id = 2122,
    full_name = "Robert Woods",
    last_name = "Woods",
    first_name = "Robert",
    nfl_team = "LAR",
    position = "WR",
    height = "6-0",
    weight = "193",
    dob = "1992-04-10",
    college = "Southern California"
  )

  player_4223 = Player(
    player_id = 4223,
    full_name = "Isaiah Wright",
    last_name = "Wright",
    first_name = "Isaiah",
    nfl_team = "WAS",
    position = "WR",
    height = "6-2",
    weight = "220",
    dob = "1997-01-13",
    college = "Temple"
  )

  player_4007 = Player(
    player_id = 4007,
    full_name = "Terry Wright",
    last_name = "Wright",
    first_name = "Terry",
    nfl_team = "MIA",
    position = "WR",
    height = "5-10",
    weight = "177",
    dob = "1997-01-28",
    college = "Purdue"
  )

  player_4078 = Player(
    player_id = 4078,
    full_name = "Olamide Zaccheaus",
    last_name = "Zaccheaus",
    first_name = "Olamide",
    nfl_team = "ATL",
    position = "WR",
    height = "5-8",
    weight = "193",
    dob = "1997-07-23",
    college = "Virginia"
  )

  player_4370 = Player(
    player_id = 4370,
    full_name = "Isaiah Zuber",
    last_name = "Zuber",
    first_name = "Isaiah",
    nfl_team = "NE",
    position = "WR",
    height = "6-0",
    weight = "190",
    dob = "1997-04-15",
    college = "Mississippi State"
  )

  player_3605 = Player(
    player_id = 3605,
    full_name = "Brandon Zylstra",
    last_name = "Zylstra",
    first_name = "Brandon",
    nfl_team = "CAR",
    position = "WR",
    height = "6-2",
    weight = "215",
    dob = "1993-03-25",
    college = "Concordia, Minn"
  )

  player_3043 = Player(
    player_id = 3043,
    full_name = "Jerell Adams",
    last_name = "Adams",
    first_name = "Jerell",
    nfl_team = "BAL",
    position = "TE",
    height = "6-5",
    weight = "254",
    dob = "1992-12-31",
    college = "South Carolina"
  )

  player_3616 = Player(
    player_id = 3616,
    full_name = "Jordan Akins",
    last_name = "Akins",
    first_name = "Jordan",
    nfl_team = "HOU",
    position = "TE",
    height = "6-4",
    weight = "243",
    dob = "1992-04-19",
    college = "Central Florida"
  )

  player_3363 = Player(
    player_id = 3363,
    full_name = "Mo Alie-Cox",
    last_name = "Alie-Cox",
    first_name = "Mo",
    nfl_team = "IND",
    position = "TE",
    height = "6-5",
    weight = "267",
    dob = "1993-09-19",
    college = "Virginia Commonwealth"
  )

  player_3235 = Player(
    player_id = 3235,
    full_name = "Stephen Anderson",
    last_name = "Anderson",
    first_name = "Stephen",
    nfl_team = "LAC",
    position = "TE",
    height = "6-3",
    weight = "230",
    dob = "1993-01-30",
    college = "California"
  )

  player_3615 = Player(
    player_id = 3615,
    full_name = "Mark Andrews",
    last_name = "Andrews",
    first_name = "Mark",
    nfl_team = "BAL",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1995-09-06",
    college = "Oklahoma"
  )

  player_3566 = Player(
    player_id = 3566,
    full_name = "Dan Arnold",
    last_name = "Arnold",
    first_name = "Dan",
    nfl_team = "ARI",
    position = "TE",
    height = "6-6",
    weight = "220",
    dob = "1995-03-15",
    college = "Wisconsin-Platteville"
  )

  player_4149 = Player(
    player_id = 4149,
    full_name = "Devin Asiasi",
    last_name = "Asiasi",
    first_name = "Devin",
    nfl_team = "NE",
    position = "TE",
    height = "6-3",
    weight = "260",
    dob = "1997-08-14",
    college = "UCLA"
  )

  player_3553 = Player(
    player_id = 3553,
    full_name = "Antony Auclair",
    last_name = "Auclair",
    first_name = "Antony",
    nfl_team = "TB",
    position = "TE",
    height = "6-6",
    weight = "256",
    dob = "1993-05-28",
    college = "Laval, Can."
  )

  player_3721 = Player(
    player_id = 3721,
    full_name = "Marcus Baugh",
    last_name = "Baugh",
    first_name = "Marcus",
    nfl_team = "WAS",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1994-12-09",
    college = "Ohio State"
  )

  player_3530 = Player(
    player_id = 3530,
    full_name = "Evan Baylis",
    last_name = "Baylis",
    first_name = "Evan",
    nfl_team = "ARI",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1993-11-18",
    college = "Oregon"
  )

  player_3950 = Player(
    player_id = 3950,
    full_name = "Andrew Beck",
    last_name = "Beck",
    first_name = "Andrew",
    nfl_team = "DEN",
    position = "TE",
    height = "6-3",
    weight = "255",
    dob = "1996-05-15",
    college = "Texas"
  )

  player_4256 = Player(
    player_id = 4256,
    full_name = "Ryan Becker",
    last_name = "Becker",
    first_name = "Ryan",
    nfl_team = "ARI",
    position = "TE",
    height = "6-5",
    weight = "248",
    dob = "1997-12-23",
    college = "SMU"
  )

  player_4091 = Player(
    player_id = 4091,
    full_name = "Nate Becker",
    last_name = "Becker",
    first_name = "Nate",
    nfl_team = "BUF",
    position = "TE",
    height = "6-5",
    weight = "264",
    dob = "1996-03-24",
    college = "Miami, O."
  )

  player_2767 = Player(
    player_id = 2767,
    full_name = "Blake Bell",
    last_name = "Bell",
    first_name = "Blake",
    nfl_team = "DAL",
    position = "TE",
    height = "6-6",
    weight = "252",
    dob = "1991-08-07",
    college = "Oklahoma"
  )

  player_4371 = Player(
    player_id = 4371,
    full_name = "Rashod Berry",
    last_name = "Berry",
    first_name = "Rashod",
    nfl_team = "NE",
    position = "TE",
    height = "6-4",
    weight = "255",
    dob = "1996-10-14",
    college = "Ohio State"
  )

  player_4013 = Player(
    player_id = 4013,
    full_name = "Kendall Blanton",
    last_name = "Blanton",
    first_name = "Kendall",
    nfl_team = "LAR",
    position = "TE",
    height = "6-6",
    weight = "260",
    dob = "1995-11-10",
    college = "Missouri"
  )

  player_3099 = Player(
    player_id = 3099,
    full_name = "Moritz Boehringer",
    last_name = "Boehringer",
    first_name = "Moritz",
    nfl_team = "CIN",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1993-10-16",
    college = "--"
  )

  player_4237 = Player(
    player_id = 4237,
    full_name = "Nick Bowers",
    last_name = "Bowers",
    first_name = "Nick",
    nfl_team = "LV",
    position = "TE",
    height = "6-4",
    weight = "260",
    dob = "1996-05-26",
    college = "Penn State"
  )

  player_2776 = Player(
    player_id = 2776,
    full_name = "Nick Boyle",
    last_name = "Boyle",
    first_name = "Nick",
    nfl_team = "BAL",
    position = "TE",
    height = "6-4",
    weight = "270",
    dob = "1993-02-17",
    college = "Delaware"
  )

  player_2681 = Player(
    player_id = 2681,
    full_name = "Cameron Brate",
    last_name = "Brate",
    first_name = "Cam",
    nfl_team = "TB",
    position = "TE",
    height = "6-5",
    weight = "245",
    dob = "1991-07-03",
    college = "Harvard"
  )

  player_3210 = Player(
    player_id = 3210,
    full_name = "Ben Braunecker",
    last_name = "Braunecker",
    first_name = "Ben",
    nfl_team = "CHI",
    position = "TE",
    height = "6-3",
    weight = "247",
    dob = "1994-02-07",
    college = "Harvard"
  )

  player_4292 = Player(
    player_id = 4292,
    full_name = "Jacob Breeland",
    last_name = "Breeland",
    first_name = "Jacob",
    nfl_team = "BAL",
    position = "TE",
    height = "6-6",
    weight = "252",
    dob = "1996-09-20",
    college = "Oregon"
  )

  player_2113 = Player(
    player_id = 2113,
    full_name = "Beau Brinkley",
    last_name = "Brinkley",
    first_name = "Beau",
    nfl_team = "TEN",
    position = "TE",
    height = "6-4",
    weight = "260",
    dob = "1990-01-25",
    college = "Missouri"
  )

  player_3414 = Player(
    player_id = 3414,
    full_name = "Pharaoh Brown",
    last_name = "Brown",
    first_name = "Pharaoh",
    nfl_team = "HOU",
    position = "TE",
    height = "6-6",
    weight = "258",
    dob = "1994-05-04",
    college = "Oregon"
  )

  player_3000 = Player(
    player_id = 3000,
    full_name = "Daniel Brown",
    last_name = "Brown",
    first_name = "Daniel",
    nfl_team = "NYJ",
    position = "TE",
    height = "6-5",
    weight = "247",
    dob = "1992-05-26",
    college = "James Madison"
  )

  player_3555 = Player(
    player_id = 3555,
    full_name = "Billy Brown",
    last_name = "Brown",
    first_name = "Billy",
    nfl_team = "IND",
    position = "TE",
    height = "6-4",
    weight = "248",
    dob = "1993-03-20",
    college = "Shepherd"
  )

  player_4167 = Player(
    player_id = 4167,
    full_name = "Harrison Bryant",
    last_name = "Bryant",
    first_name = "Harrison",
    nfl_team = "CLE",
    position = "TE",
    height = "6-5",
    weight = "240",
    dob = "1998-04-23",
    college = "Florida Atlantic"
  )

  player_4313 = Player(
    player_id = 4313,
    full_name = "Hunter Bryant",
    last_name = "Bryant",
    first_name = "Hunter",
    nfl_team = "DET",
    position = "TE",
    height = "6-2",
    weight = "239",
    dob = "1998-08-20",
    college = "Washington"
  )

  player_4040 = Player(
    player_id = 4040,
    full_name = "Ian Bunting",
    last_name = "Bunting",
    first_name = "Ian",
    nfl_team = "IND",
    position = "TE",
    height = "6-7",
    weight = "255",
    dob = "1996-02-10",
    college = "California"
  )

  player_4194 = Player(
    player_id = 4194,
    full_name = "Jake Burt",
    last_name = "Burt",
    first_name = "Jake",
    nfl_team = "NE",
    position = "TE",
    height = "6-3",
    weight = "260",
    dob = "1996-08-25",
    college = "Boston College"
  )

  player_2474 = Player(
    player_id = 2474,
    full_name = "Trey Burton",
    last_name = "Burton",
    first_name = "Trey",
    nfl_team = "IND",
    position = "TE",
    height = "6-2",
    weight = "238",
    dob = "1991-10-29",
    college = "Florida"
  )

  player_3722 = Player(
    player_id = 3722,
    full_name = "Paul Butler",
    last_name = "Butler",
    first_name = "Paul",
    nfl_team = "LV",
    position = "TE",
    height = "6-6",
    weight = "250",
    dob = "1993-04-26",
    college = "California (PA)"
  )

  player_3309 = Player(
    player_id = 3309,
    full_name = "Jake Butt",
    last_name = "Butt",
    first_name = "Jake",
    nfl_team = "DEN",
    position = "TE",
    height = "6-6",
    weight = "250",
    dob = "1995-07-11",
    college = "Michigan"
  )

  player_3641 = Player(
    player_id = 3641,
    full_name = "Dylan Cantrell",
    last_name = "Cantrell",
    first_name = "Dylan",
    nfl_team = "ARI",
    position = "TE",
    height = "6-3",
    weight = "226",
    dob = "1994-06-29",
    college = "Texas Tech"
  )

  player_4033 = Player(
    player_id = 4033,
    full_name = "Stephen Carlson",
    last_name = "Carlson",
    first_name = "Stephen",
    nfl_team = "CLE",
    position = "TE",
    height = "6-4",
    weight = "240",
    dob = "1996-12-12",
    college = "Princeton"
  )

  player_1825 = Player(
    player_id = 1825,
    full_name = "Derek Carrier",
    last_name = "Carrier",
    first_name = "Derek",
    nfl_team = "LV",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1990-07-25",
    college = "Beloit"
  )

  player_3436 = Player(
    player_id = 3436,
    full_name = "Cethan Carter",
    last_name = "Carter",
    first_name = "Cethan",
    nfl_team = "CIN",
    position = "TE",
    height = "6-3",
    weight = "248",
    dob = "1995-09-05",
    college = "Nebraska"
  )

  player_4127 = Player(
    player_id = 4127,
    full_name = "Darion Clark",
    last_name = "Clark",
    first_name = "Darion",
    nfl_team = "CHI",
    position = "TE",
    height = "6-7",
    weight = "220",
    dob = "1994-04-09",
    college = "USC"
  )

  player_3663 = Player(
    player_id = 3663,
    full_name = "Tyler Conklin",
    last_name = "Conklin",
    first_name = "Tyler",
    nfl_team = "MIN",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1995-12-21",
    college = "Florida State"
  )

  player_3974 = Player(
    player_id = 3974,
    full_name = "CJ Conrad",
    last_name = "Conrad",
    first_name = "CJ",
    nfl_team = "NYG",
    position = "TE",
    height = "6-4",
    weight = "248",
    dob = "1996-05-09",
    college = "Kentucky"
  )

  player_872 = Player(
    player_id = 872,
    full_name = "Jared Cook",
    last_name = "Cook",
    first_name = "Jared",
    nfl_team = "NO",
    position = "TE",
    height = "6-5",
    weight = "254",
    dob = "1987-04-07",
    college = "South Carolina"
  )

  player_3472 = Player(
    player_id = 3472,
    full_name = "Jason Croom",
    last_name = "Croom",
    first_name = "Jason",
    nfl_team = "PHI",
    position = "TE",
    height = "6-5",
    weight = "246",
    dob = "1994-02-28",
    college = "Tennessee"
  )

  player_3460 = Player(
    player_id = 3460,
    full_name = "Darrell Daniels",
    last_name = "Daniels",
    first_name = "Darrell",
    nfl_team = "ARI",
    position = "TE",
    height = "6-3",
    weight = "256",
    dob = "1994-11-22",
    college = "Washington"
  )

  player_4341 = Player(
    player_id = 4341,
    full_name = "Tyler Davis",
    last_name = "Davis",
    first_name = "Tyler",
    nfl_team = "JAC",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1997-04-02",
    college = "Georgia Tech"
  )

  player_4173 = Player(
    player_id = 4173,
    full_name = "Josiah Deguara",
    last_name = "Deguara",
    first_name = "Josiah",
    nfl_team = "GB",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1997-02-14",
    college = "Cincinnati"
  )

  player_3085 = Player(
    player_id = 3085,
    full_name = "Seth DeValve",
    last_name = "DeValve",
    first_name = "Seth",
    nfl_team = "CAR",
    position = "TE",
    height = "6-3",
    weight = "245",
    dob = "1993-01-29",
    college = "Princeton"
  )

  player_3696 = Player(
    player_id = 3696,
    full_name = "Garrett Dickerson",
    last_name = "Dickerson",
    first_name = "Garrett",
    nfl_team = "NYG",
    position = "TE",
    height = "6-3",
    weight = "248",
    dob = "1995-12-30",
    college = "Northwestern"
  )

  player_4053 = Player(
    player_id = 4053,
    full_name = "Brandon Dillon",
    last_name = "Dillon",
    first_name = "Brandon",
    nfl_team = "MIN",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1997-04-30",
    college = "Marian, Ind."
  )

  player_3648 = Player(
    player_id = 3648,
    full_name = "Will Dissly",
    last_name = "Dissly",
    first_name = "Will",
    nfl_team = "SEA",
    position = "TE",
    height = "6-4",
    weight = "267",
    dob = "1996-07-08",
    college = "Washington"
  )

  player_2364 = Player(
    player_id = 2364,
    full_name = "Jack Doyle",
    last_name = "Doyle",
    first_name = "Jack",
    nfl_team = "IND",
    position = "TE",
    height = "6-6",
    weight = "262",
    dob = "1990-05-05",
    college = "Western Kentucky"
  )

  player_3646 = Player(
    player_id = 3646,
    full_name = "Ross Dwelley",
    last_name = "Dwelley",
    first_name = "Ross",
    nfl_team = "SF",
    position = "TE",
    height = "6-5",
    weight = "240",
    dob = "1995-01-26",
    college = "San Diego"
  )

  player_2587 = Player(
    player_id = 2587,
    full_name = "Eric Ebron",
    last_name = "Ebron",
    first_name = "Eric",
    nfl_team = "PIT",
    position = "TE",
    height = "6-4",
    weight = "253",
    dob = "1993-04-10",
    college = "North Carolina"
  )

  player_2279 = Player(
    player_id = 2279,
    full_name = "Tyler Eifert",
    last_name = "Eifert",
    first_name = "Tyler",
    nfl_team = "JAC",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1990-09-08",
    college = "Notre Dame"
  )

  player_4342 = Player(
    player_id = 4342,
    full_name = "Ben Ellefson",
    last_name = "Ellefson",
    first_name = "Ben",
    nfl_team = "JAC",
    position = "TE",
    height = "6-3",
    weight = "250",
    dob = "1996-09-01",
    college = "North Dakota State"
  )

  player_3240 = Player(
    player_id = 3240,
    full_name = "Alex Ellis",
    last_name = "Ellis",
    first_name = "Alex",
    nfl_team = "PHI",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1993-02-10",
    college = "Tennessee"
  )

  player_3296 = Player(
    player_id = 3296,
    full_name = "Evan Engram",
    last_name = "Engram",
    first_name = "Evan",
    nfl_team = "NYG",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1994-09-02",
    college = "Mississippi"
  )

  player_2173 = Player(
    player_id = 2173,
    full_name = "Zach Ertz",
    last_name = "Ertz",
    first_name = "Zach",
    nfl_team = "PHI",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1990-11-10",
    college = "Stanford"
  )

  player_3562 = Player(
    player_id = 3562,
    full_name = "Gerald Everett",
    last_name = "Everett",
    first_name = "Gerald",
    nfl_team = "LAR",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1994-06-25",
    college = "South Alabama"
  )

  player_3884 = Player(
    player_id = 3884,
    full_name = "Noah Fant",
    last_name = "Fant",
    first_name = "Noah",
    nfl_team = "DEN",
    position = "TE",
    height = "6-4",
    weight = "249",
    dob = "1997-11-20",
    college = "Iowa"
  )

  player_2249 = Player(
    player_id = 2249,
    full_name = "Darren Fells",
    last_name = "Fells",
    first_name = "Darren",
    nfl_team = "HOU",
    position = "TE",
    height = "6-7",
    weight = "270",
    dob = "1986-04-22",
    college = "California-Irvine"
  )

  player_3405 = Player(
    player_id = 3405,
    full_name = "Anthony Firkser",
    last_name = "Firkser",
    first_name = "Anthony",
    nfl_team = "TEN",
    position = "TE",
    height = "6-2",
    weight = "246",
    dob = "1995-02-19",
    college = "Harvard"
  )

  player_3885 = Player(
    player_id = 3885,
    full_name = "Austin Fort",
    last_name = "Fort",
    first_name = "Austin",
    nfl_team = "DEN",
    position = "TE",
    height = "6-4",
    weight = "244",
    dob = "1995-05-14",
    college = "Wyoming"
  )

  player_3764 = Player(
    player_id = 3764,
    full_name = "Jordan Franks",
    last_name = "Franks",
    first_name = "Jordan",
    nfl_team = "CIN",
    position = "TE",
    height = "6-4",
    weight = "239",
    dob = "1996-02-01",
    college = "Central Florida"
  )

  player_3638 = Player(
    player_id = 3638,
    full_name = "Troy Fumagalli",
    last_name = "Fumagalli",
    first_name = "Troy",
    nfl_team = "DEN",
    position = "TE",
    height = "6-6",
    weight = "248",
    dob = "1995-02-17",
    college = "Wisconsin"
  )

  player_3919 = Player(
    player_id = 3919,
    full_name = "Zach Gentry",
    last_name = "Gentry",
    first_name = "Zach",
    nfl_team = "PIT",
    position = "TE",
    height = "6-8",
    weight = "265",
    dob = "1996-09-10",
    college = "Michigan"
  )

  player_3578 = Player(
    player_id = 3578,
    full_name = "Mike Gesicki",
    last_name = "Gesicki",
    first_name = "Mike",
    nfl_team = "MIA",
    position = "TE",
    height = "6-6",
    weight = "252",
    dob = "1995-10-03",
    college = "Penn State"
  )

  player_4182 = Player(
    player_id = 4182,
    full_name = "Reggie Gilliam",
    last_name = "Gilliam",
    first_name = "Reggie",
    nfl_team = "BUF",
    position = "TE",
    height = "6-1",
    weight = "255",
    dob = "1997-08-20",
    college = "Toledo"
  )

  player_3584 = Player(
    player_id = 3584,
    full_name = "Dallas Goedert",
    last_name = "Goedert",
    first_name = "Dallas",
    nfl_team = "PHI",
    position = "TE",
    height = "6-5",
    weight = "256",
    dob = "1995-01-03",
    college = "South Dakota State"
  )

  player_1187 = Player(
    player_id = 1187,
    full_name = "Jimmy Graham",
    last_name = "Graham",
    first_name = "Jimmy",
    nfl_team = "CHI",
    position = "TE",
    height = "6-7",
    weight = "265",
    dob = "1986-11-24",
    college = "Miami"
  )

  player_3823 = Player(
    player_id = 3823,
    full_name = "Jaeden Graham",
    last_name = "Graham",
    first_name = "Jaeden",
    nfl_team = "ATL",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1995-10-10",
    college = "Yale"
  )

  player_1463 = Player(
    player_id = 1463,
    full_name = "Virgil Green",
    last_name = "Green",
    first_name = "Virgil",
    nfl_team = "LAC",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1988-08-03",
    college = "Nevada"
  )

  player_4331 = Player(
    player_id = 4331,
    full_name = "Farrod Green",
    last_name = "Green",
    first_name = "Farrod",
    nfl_team = "IND",
    position = "TE",
    height = "6-4",
    weight = "240",
    dob = "1997-06-10",
    college = "Mississippi State"
  )

  player_2342 = Player(
    player_id = 2342,
    full_name = "Ryan Griffin",
    last_name = "Griffin",
    first_name = "Ryan",
    nfl_team = "NYJ",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1990-01-11",
    college = "Connecticut"
  )

  player_3254 = Player(
    player_id = 3254,
    full_name = "Garrett Griffin",
    last_name = "Griffin",
    first_name = "Garrett",
    nfl_team = "NO",
    position = "TE",
    height = "6-4",
    weight = "240",
    dob = "1994-03-04",
    college = "Air Force"
  )

  player_4323 = Player(
    player_id = 4323,
    full_name = "Nakia Griffin-Stewart",
    last_name = "Griffin-Stewart",
    first_name = "Nakia",
    nfl_team = "MIN",
    position = "TE",
    height = "6-5",
    weight = "260",
    dob = "1996-11-12",
    college = "Pittsburgh"
  )

  player_2466 = Player(
    player_id = 2466,
    full_name = "Xavier Grimble",
    last_name = "Grimble",
    first_name = "Xavier",
    nfl_team = "IND",
    position = "TE",
    height = "6-4",
    weight = "261",
    dob = "1992-09-22",
    college = "Southern California"
  )

  player_1189 = Player(
    player_id = 1189,
    full_name = "Rob Gronkowski",
    last_name = "Gronkowski",
    first_name = "Rob",
    nfl_team = "TB",
    position = "TE",
    height = "6-6",
    weight = "265",
    dob = "1989-05-14",
    college = "Arizona"
  )

  player_4264 = Player(
    player_id = 4264,
    full_name = "Chase Harrell",
    last_name = "Harrell",
    first_name = "Chase",
    nfl_team = "SF",
    position = "TE",
    height = "6-4",
    weight = "249",
    dob = "1996-05-16",
    college = "Arkansas"
  )

  player_649 = Player(
    player_id = 649,
    full_name = "Clark Harris",
    last_name = "Harris",
    first_name = "Clark",
    nfl_team = "CIN",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1984-07-10",
    college = "Rutgers"
  )

  player_2197 = Player(
    player_id = 2197,
    full_name = "Demetrius Harris",
    last_name = "Harris",
    first_name = "Demetrius",
    nfl_team = "CHI",
    position = "TE",
    height = "6-7",
    weight = "230",
    dob = "1991-07-29",
    college = "Wisconsin-Milwaukee"
  )

  player_3992 = Player(
    player_id = 3992,
    full_name = "Daniel Helm",
    last_name = "Helm",
    first_name = "Daniel",
    nfl_team = "SF",
    position = "TE",
    height = "6-4",
    weight = "248",
    dob = "1995-04-20",
    college = "Duke"
  )

  player_3075 = Player(
    player_id = 3075,
    full_name = "Temarrick Hemingway",
    last_name = "Hemingway",
    first_name = "Temarrick",
    nfl_team = "WAS",
    position = "TE",
    height = "6-5",
    weight = "245",
    dob = "1993-07-30",
    college = "South Carolina State"
  )

  player_3063 = Player(
    player_id = 3063,
    full_name = "Hunter Henry",
    last_name = "Henry",
    first_name = "Hunter",
    nfl_team = "LAC",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1994-12-07",
    college = "Arkansas"
  )

  player_4061 = Player(
    player_id = 4061,
    full_name = "Hale Hentges",
    last_name = "Hentges",
    first_name = "Hale",
    nfl_team = "WAS",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1996-08-19",
    college = "Alabama"
  )

  player_4020 = Player(
    player_id = 4020,
    full_name = "Cole Herdman",
    last_name = "Herdman",
    first_name = "Cole",
    nfl_team = "TEN",
    position = "TE",
    height = "6-4",
    weight = "238",
    dob = "1995-06-27",
    college = "Purdue"
  )

  player_3627 = Player(
    player_id = 3627,
    full_name = "Chris Herndon",
    last_name = "Herndon",
    first_name = "Chris",
    nfl_team = "NYJ",
    position = "TE",
    height = "6-4",
    weight = "252",
    dob = "1996-02-23",
    college = "Miami"
  )

  player_4073 = Player(
    player_id = 4073,
    full_name = "Parker Hesse",
    last_name = "Hesse",
    first_name = "Parker",
    nfl_team = "TEN",
    position = "TE",
    height = "6-3",
    weight = "261",
    dob = "1995-05-26",
    college = "Iowa"
  )

  player_2752 = Player(
    player_id = 2752,
    full_name = "Jeff Heuerman",
    last_name = "Heuerman",
    first_name = "Jeff",
    nfl_team = "DEN",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1992-11-24",
    college = "Ohio State"
  )

  player_3076 = Player(
    player_id = 3076,
    full_name = "Tyler Higbee",
    last_name = "Higbee",
    first_name = "Tyler",
    nfl_team = "LAR",
    position = "TE",
    height = "6-6",
    weight = "257",
    dob = "1993-01-01",
    college = "Western Kentucky"
  )

  player_3420 = Player(
    player_id = 3420,
    full_name = "Cole Hikutini",
    last_name = "Hikutini",
    first_name = "Cole",
    nfl_team = "DAL",
    position = "TE",
    height = "6-4",
    weight = "240",
    dob = "1994-06-11",
    college = "Louisville"
  )

  player_2389 = Player(
    player_id = 2389,
    full_name = "Josh Hill",
    last_name = "Hill",
    first_name = "Josh",
    nfl_team = "NO",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1990-05-21",
    college = "Idaho State"
  )

  player_3925 = Player(
    player_id = 3925,
    full_name = "TJ Hockenson",
    last_name = "Hockenson",
    first_name = "TJ",
    nfl_team = "DET",
    position = "TE",
    height = "6-5",
    weight = "248",
    dob = "1997-07-03",
    college = "Iowa"
  )

  player_3404 = Player(
    player_id = 3404,
    full_name = "Jacob Hollister",
    last_name = "Hollister",
    first_name = "Jacob",
    nfl_team = "SEA",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1993-11-18",
    college = "Wyoming"
  )

  player_3201 = Player(
    player_id = 3201,
    full_name = "J.P. Holtz",
    last_name = "Holtz",
    first_name = "J.P.",
    nfl_team = "CHI",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1993-08-28",
    college = "Pittsburgh"
  )

  player_3115 = Player(
    player_id = 3115,
    full_name = "Austin Hooper",
    last_name = "Hooper",
    first_name = "Austin",
    nfl_team = "CLE",
    position = "TE",
    height = "6-4",
    weight = "254",
    dob = "1994-10-29",
    college = "Stanford"
  )

  player_4284 = Player(
    player_id = 4284,
    full_name = "Brycen Hopkins",
    last_name = "Hopkins",
    first_name = "Brycen",
    nfl_team = "LAR",
    position = "TE",
    height = "6-5",
    weight = "245",
    dob = "1997-03-27",
    college = "Purdue"
  )

  player_4041 = Player(
    player_id = 4041,
    full_name = "Jesper Horsted",
    last_name = "Horsted",
    first_name = "Jesper",
    nfl_team = "CHI",
    position = "TE",
    height = "6-3",
    weight = "237",
    dob = "1997-02-27",
    college = "Princeton"
  )

  player_4257 = Player(
    player_id = 4257,
    full_name = "Parker Houston",
    last_name = "Houston",
    first_name = "Parker",
    nfl_team = "ARI",
    position = "TE",
    height = "6-3",
    weight = "250",
    dob = "1997-12-06",
    college = "San Diego State"
  )

  player_3390 = Player(
    player_id = 3390,
    full_name = "O.J. Howard",
    last_name = "Howard",
    first_name = "O.J.",
    nfl_team = "TB",
    position = "TE",
    height = "6-6",
    weight = "250",
    dob = "1994-11-18",
    college = "Alabama"
  )

  player_3457 = Player(
    player_id = 3457,
    full_name = "Bug Howard",
    last_name = "Howard",
    first_name = "Bug",
    nfl_team = "DEN",
    position = "TE",
    height = "6-4",
    weight = "214",
    dob = "1994-11-28",
    college = "North Carolina"
  )

  player_4348 = Player(
    player_id = 4348,
    full_name = "Tommy Hudson",
    last_name = "Hudson",
    first_name = "Tommy",
    nfl_team = "TEN",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1997-02-22",
    college = "Arizona State"
  )

  player_3839 = Player(
    player_id = 3839,
    full_name = "Tanner Hudson",
    last_name = "Hudson",
    first_name = "Tanner",
    nfl_team = "TB",
    position = "TE",
    height = "6-5",
    weight = "239",
    dob = "1994-11-12",
    college = "Southern Arkansas"
  )

  player_3597 = Player(
    player_id = 3597,
    full_name = "Hayden Hurst",
    last_name = "Hurst",
    first_name = "Hayden",
    nfl_team = "ATL",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1993-08-24",
    college = "South Carolina"
  )

  player_3625 = Player(
    player_id = 3625,
    full_name = "Ryan Izzo",
    last_name = "Izzo",
    first_name = "Ryan",
    nfl_team = "NE",
    position = "TE",
    height = "6-3",
    weight = "254",
    dob = "1995-07-30",
    college = "Central Michigan"
  )

  player_2785 = Player(
    player_id = 2785,
    full_name = "Jesse James",
    last_name = "James",
    first_name = "Jesse",
    nfl_team = "DET",
    position = "TE",
    height = "6-7",
    weight = "250",
    dob = "1994-06-04",
    college = "Penn State"
  )

  player_3481 = Player(
    player_id = 3481,
    full_name = "Blake Jarwin",
    last_name = "Jarwin",
    first_name = "Blake",
    nfl_team = "DAL",
    position = "TE",
    height = "6-5",
    weight = "260",
    dob = "1994-07-16",
    college = "Oklahoma State"
  )

  player_4209 = Player(
    player_id = 4209,
    full_name = "Rysen John",
    last_name = "John",
    first_name = "Rysen",
    nfl_team = "NYG",
    position = "TE",
    height = "6-7",
    weight = "220",
    dob = "1997-12-20",
    college = "Simon Fraser"
  )

  player_4098 = Player(
    player_id = 4098,
    full_name = "Justin Johnson",
    last_name = "Johnson",
    first_name = "Justin",
    nfl_team = "SEA",
    position = "TE",
    height = "6-3",
    weight = "245",
    dob = "1996-11-08",
    college = "Mississippi State"
  )

  player_4069 = Player(
    player_id = 4069,
    full_name = "Charles Jones",
    last_name = "Jones",
    first_name = "Charles",
    nfl_team = "JAC",
    position = "TE",
    height = "6-4",
    weight = "255",
    dob = "1996-08-05",
    college = "Tulane"
  )

  player_4150 = Player(
    player_id = 4150,
    full_name = "Dalton Keene",
    last_name = "Keene",
    first_name = "Dalton",
    nfl_team = "NE",
    position = "TE",
    height = "6-4",
    weight = "251",
    dob = "1999-04-14",
    college = "Virginia Tech"
  )

  player_3758 = Player(
    player_id = 3758,
    full_name = "Nick Keizer",
    last_name = "Keizer",
    first_name = "Nick",
    nfl_team = "KC",
    position = "TE",
    height = "6-4",
    weight = "251",
    dob = "1995-05-02",
    college = "Grand Valley State"
  )

  player_2198 = Player(
    player_id = 2198,
    full_name = "Travis Kelce",
    last_name = "Kelce",
    first_name = "Travis",
    nfl_team = "KC",
    position = "TE",
    height = "6-5",
    weight = "260",
    dob = "1989-10-05",
    college = "Cincinnati"
  )

  player_3324 = Player(
    player_id = 3324,
    full_name = "George Kittle",
    last_name = "Kittle",
    first_name = "George",
    nfl_team = "SF",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1993-10-09",
    college = "Iowa"
  )

  player_4170 = Player(
    player_id = 4170,
    full_name = "Cole Kmet",
    last_name = "Kmet",
    first_name = "Cole",
    nfl_team = "CHI",
    position = "TE",
    height = "6-6",
    weight = "258",
    dob = "1999-03-10",
    college = "Notre Dame"
  )

  player_3857 = Player(
    player_id = 3857,
    full_name = "Dawson Knox",
    last_name = "Knox",
    first_name = "Dawson",
    nfl_team = "BUF",
    position = "TE",
    height = "6-4",
    weight = "254",
    dob = "1996-11-14",
    college = "Mississippi"
  )

  player_2779 = Player(
    player_id = 2779,
    full_name = "Tyler Kroft",
    last_name = "Kroft",
    first_name = "Tyler",
    nfl_team = "BUF",
    position = "TE",
    height = "6-6",
    weight = "250",
    dob = "1992-10-15",
    college = "Rutgers"
  )

  player_2897 = Player(
    player_id = 2897,
    full_name = "Matt LaCosse",
    last_name = "LaCosse",
    first_name = "Matt",
    nfl_team = "NE",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1992-09-21",
    college = "Illinois"
  )

  player_2867 = Player(
    player_id = 2867,
    full_name = "Khari Lee",
    last_name = "Lee",
    first_name = "Khari",
    nfl_team = "ATL",
    position = "TE",
    height = "6-4",
    weight = "253",
    dob = "1992-01-16",
    college = "Bowie State"
  )

  player_3287 = Player(
    player_id = 3287,
    full_name = "Jordan Leggett",
    last_name = "Leggett",
    first_name = "Jordan",
    nfl_team = "TB",
    position = "TE",
    height = "6-5",
    weight = "258",
    dob = "1995-01-31",
    college = "Clemson"
  )

  player_2846 = Player(
    player_id = 2846,
    full_name = "Matt Lengel",
    last_name = "Lengel",
    first_name = "Matt",
    nfl_team = "IND",
    position = "TE",
    height = "6-7",
    weight = "265",
    dob = "1990-12-27",
    college = "Eastern Kentucky"
  )

  player_668 = Player(
    player_id = 668,
    full_name = "Marcedes Lewis",
    last_name = "Lewis",
    first_name = "Marcedes",
    nfl_team = "GB",
    position = "TE",
    height = "6-6",
    weight = "267",
    dob = "1984-05-19",
    college = "UCLA"
  )

  player_4143 = Player(
    player_id = 4143,
    full_name = "James Looney",
    last_name = "Looney",
    first_name = "James",
    nfl_team = "GB",
    position = "TE",
    height = "6-3",
    weight = "287",
    dob = "1995-05-15",
    college = "California"
  )

  player_4274 = Player(
    player_id = 4274,
    full_name = "Tyler Mabry",
    last_name = "Mabry",
    first_name = "Tyler",
    nfl_team = "SEA",
    position = "TE",
    height = "6-4",
    weight = "248",
    dob = "1996-11-21",
    college = "Maryland"
  )

  player_3945 = Player(
    player_id = 3945,
    full_name = "Alize Mack",
    last_name = "Mack",
    first_name = "Alize",
    nfl_team = "KC",
    position = "TE",
    height = "6-4",
    weight = "249",
    dob = "1997-03-29",
    college = "Notre Dame"
  )

  player_2724 = Player(
    player_id = 2724,
    full_name = "Chris Manhertz",
    last_name = "Manhertz",
    first_name = "Chris",
    nfl_team = "CAR",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1992-04-10",
    college = "Canisius"
  )

  player_4212 = Player(
    player_id = 4212,
    full_name = "Kyle Markway",
    last_name = "Markway",
    first_name = "Kyle",
    nfl_team = "NYG",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1997-03-04",
    college = "South Carolina"
  )

  player_2242 = Player(
    player_id = 2242,
    full_name = "Vance McDonald",
    last_name = "McDonald",
    first_name = "Vance",
    nfl_team = "PIT",
    position = "TE",
    height = "6-4",
    weight = "267",
    dob = "1990-06-13",
    college = "Rice"
  )

  player_3750 = Player(
    player_id = 3750,
    full_name = "Codey McElroy",
    last_name = "McElroy",
    first_name = "Codey",
    nfl_team = "TB",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1992-12-13",
    college = "Oklahoma State"
  )

  player_4204 = Player(
    player_id = 4204,
    full_name = "Sean McKeon",
    last_name = "McKeon",
    first_name = "Sean",
    nfl_team = "DAL",
    position = "TE",
    height = "6-5",
    weight = "246",
    dob = "1997-12-28",
    college = "Michigan"
  )

  player_4118 = Player(
    player_id = 4118,
    full_name = "Carson Meier",
    last_name = "Meier",
    first_name = "Carson",
    nfl_team = "ATL",
    position = "TE",
    height = "6-5",
    weight = "254",
    dob = "1995-06-29",
    college = "Oklahoma"
  )

  player_3891 = Player(
    player_id = 3891,
    full_name = "Foster Moreau",
    last_name = "Moreau",
    first_name = "Foster",
    nfl_team = "LV",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1997-05-06",
    college = "Louisiana State"
  )

  player_4224 = Player(
    player_id = 4224,
    full_name = "Thaddeus Moss",
    last_name = "Moss",
    first_name = "Thaddeus",
    nfl_team = "WAS",
    position = "TE",
    height = "6-3",
    weight = "249",
    dob = "1998-05-14",
    college = "LSU"
  )

  player_3563 = Player(
    player_id = 3563,
    full_name = "Johnny Mundt",
    last_name = "Mundt",
    first_name = "Johnny",
    nfl_team = "LAR",
    position = "TE",
    height = "6-4",
    weight = "232",
    dob = "1994-11-23",
    college = "Oregon"
  )

  player_3964 = Player(
    player_id = 3964,
    full_name = "Chris Myarick",
    last_name = "Myarick",
    first_name = "Chris",
    nfl_team = "MIA",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1995-10-06",
    college = "Temple"
  )

  player_3926 = Player(
    player_id = 3926,
    full_name = "Isaac Nauta",
    last_name = "Nauta",
    first_name = "Isaac",
    nfl_team = "DET",
    position = "TE",
    height = "6-3",
    weight = "246",
    dob = "1997-05-21",
    college = "Georgia"
  )

  player_2240 = Player(
    player_id = 2240,
    full_name = "Kyle Nelson",
    last_name = "Nelson",
    first_name = "Kyle",
    nfl_team = "SF",
    position = "TE",
    height = "6-2",
    weight = "240",
    dob = "1986-10-03",
    college = "New Mexico State"
  )

  player_3336 = Player(
    player_id = 3336,
    full_name = "David Njoku",
    last_name = "Njoku",
    first_name = "David",
    nfl_team = "CLE",
    position = "TE",
    height = "6-4",
    weight = "246",
    dob = "1996-07-10",
    college = "Miami (FL)"
  )

  player_2734 = Player(
    player_id = 2734,
    full_name = "Nick O'Leary",
    last_name = "O'Leary",
    first_name = "Nick",
    nfl_team = "LV",
    position = "TE",
    height = "6-3",
    weight = "252",
    dob = "1992-08-31",
    college = "Florida State"
  )

  player_2755 = Player(
    player_id = 2755,
    full_name = "James O'Shaughnessy",
    last_name = "O'Shaughnessy",
    first_name = "James",
    nfl_team = "JAC",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1992-01-14",
    college = "Illinois State"
  )

  player_4157 = Player(
    player_id = 4157,
    full_name = "Albert Okwuegbunam",
    last_name = "Okwuegbunam",
    first_name = "Albert",
    nfl_team = "DEN",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1998-04-25",
    college = "Missouri"
  )

  player_3938 = Player(
    player_id = 3938,
    full_name = "Josh Oliver",
    last_name = "Oliver",
    first_name = "Josh",
    nfl_team = "JAC",
    position = "TE",
    height = "6-5",
    weight = "249",
    dob = "1997-03-21",
    college = "San Jose"
  )

  player_684 = Player(
    player_id = 684,
    full_name = "Greg Olsen",
    last_name = "Olsen",
    first_name = "Greg",
    nfl_team = "SEA",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1985-03-11",
    college = "Miami"
  )

  player_4093 = Player(
    player_id = 4093,
    full_name = "Donald Parham",
    last_name = "Parham",
    first_name = "Donald",
    nfl_team = "LAC",
    position = "TE",
    height = "6-8",
    weight = "237",
    dob = "1997-08-16",
    college = "Stetson University"
  )

  player_4161 = Player(
    player_id = 4161,
    full_name = "Colby Parkinson",
    last_name = "Parkinson",
    first_name = "Colby",
    nfl_team = "SEA",
    position = "TE",
    height = "6-7",
    weight = "251",
    dob = "1999-01-08",
    college = "Stanford"
  )

  player_3246 = Player(
    player_id = 3246,
    full_name = "Joshua Perkins",
    last_name = "Perkins",
    first_name = "Joshua",
    nfl_team = "PHI",
    position = "TE",
    height = "6-3",
    weight = "223",
    dob = "1993-08-05",
    college = "Washington"
  )

  player_4354 = Player(
    player_id = 4354,
    full_name = "Jared Pinkney",
    last_name = "Pinkney",
    first_name = "Jared",
    nfl_team = "ATL",
    position = "TE",
    height = "6-4",
    weight = "255",
    dob = "1997-08-21",
    college = "Vanderbilt"
  )

  player_2795 = Player(
    player_id = 2795,
    full_name = "MyCole Pruitt",
    last_name = "Pruitt",
    first_name = "MyCole",
    nfl_team = "TEN",
    position = "TE",
    height = "6-2",
    weight = "243",
    dob = "1992-03-24",
    college = "Southern Illinois"
  )

  player_3787 = Player(
    player_id = 3787,
    full_name = "Kevin Rader",
    last_name = "Rader",
    first_name = "Kevin",
    nfl_team = "PIT",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1995-04-26",
    college = "Youngstown State"
  )

  player_4042 = Player(
    player_id = 4042,
    full_name = "Dax Raymond",
    last_name = "Raymond",
    first_name = "Dax",
    nfl_team = "CHI",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1994-11-30",
    college = "Utah State"
  )

  player_2181 = Player(
    player_id = 2181,
    full_name = "Jordan Reed",
    last_name = "Reed",
    first_name = "Jordan",
    nfl_team = "SF",
    position = "TE",
    height = "6-2",
    weight = "242",
    dob = "1990-07-03",
    college = "Florida"
  )

  player_4355 = Player(
    player_id = 4355,
    full_name = "Caleb Repp",
    last_name = "Repp",
    first_name = "Caleb",
    nfl_team = "ATL",
    position = "TE",
    height = "6-5",
    weight = "225",
    dob = "0000-00-00",
    college = "Utah State"
  )

  player_4359 = Player(
    player_id = 4359,
    full_name = "Giovanni Ricci",
    last_name = "Ricci",
    first_name = "Giovanni",
    nfl_team = "CAR",
    position = "TE",
    height = "6-3",
    weight = "240",
    dob = "1996-10-16",
    college = "Western Michigan"
  )

  player_4246 = Player(
    player_id = 4246,
    full_name = "Jared Rice",
    last_name = "Rice",
    first_name = "Jared",
    nfl_team = "LAC",
    position = "TE",
    height = "6-5",
    weight = "235",
    dob = "1995-12-28",
    college = "Fresno State"
  )

  player_3348 = Player(
    player_id = 3348,
    full_name = "Michael Roberts",
    last_name = "Roberts",
    first_name = "Michael",
    nfl_team = "MIA",
    position = "TE",
    height = "6-5",
    weight = "265",
    dob = "1994-05-07",
    college = "Toledo"
  )

  player_2600 = Player(
    player_id = 2600,
    full_name = "Richard Rodgers",
    last_name = "Rodgers",
    first_name = "Richard",
    nfl_team = "PHI",
    position = "TE",
    height = "6-4",
    weight = "257",
    dob = "1992-01-22",
    college = "California"
  )

  player_1467 = Player(
    player_id = 1467,
    full_name = "Kyle Rudolph",
    last_name = "Rudolph",
    first_name = "Kyle",
    nfl_team = "MIN",
    position = "TE",
    height = "6-6",
    weight = "265",
    dob = "1989-11-09",
    college = "Notre Dame"
  )

  player_3914 = Player(
    player_id = 3914,
    full_name = "Drew Sample",
    last_name = "Sample",
    first_name = "Drew",
    nfl_team = "CIN",
    position = "TE",
    height = "6-4",
    weight = "259",
    dob = "1996-04-16",
    college = "Washington"
  )

  player_3378 = Player(
    player_id = 3378,
    full_name = "Eric Saubert",
    last_name = "Saubert",
    first_name = "Eric",
    nfl_team = "CHI",
    position = "TE",
    height = "6-5",
    weight = "253",
    dob = "1994-05-01",
    college = "Drake"
  )

  player_4021 = Player(
    player_id = 4021,
    full_name = "Charles Scarff",
    last_name = "Scarff",
    first_name = "Charles",
    nfl_team = "BAL",
    position = "TE",
    height = "6-5",
    weight = "249",
    dob = "1996-05-03",
    college = "Delaware"
  )

  player_3332 = Player(
    player_id = 3332,
    full_name = "Mason Schreck",
    last_name = "Schreck",
    first_name = "Mason",
    nfl_team = "CIN",
    position = "TE",
    height = "6-5",
    weight = "252",
    dob = "1993-11-04",
    college = "Buffalo"
  )

  player_3631 = Player(
    player_id = 3631,
    full_name = "Dalton Schultz",
    last_name = "Schultz",
    first_name = "Dalton",
    nfl_team = "DAL",
    position = "TE",
    height = "6-5",
    weight = "242",
    dob = "1996-07-11",
    college = "Stanford"
  )

  player_3775 = Player(
    player_id = 3775,
    full_name = "Christian Scotland-Williamson",
    last_name = "Scotland-Williamson",
    first_name = "Christian",
    nfl_team = "PIT",
    position = "TE",
    height = "6-9",
    weight = "274",
    dob = "1993-07-05",
    college = "--"
  )

  player_3504 = Player(
    player_id = 3504,
    full_name = "Ricky Seals-Jones",
    last_name = "Seals-Jones",
    first_name = "Ricky",
    nfl_team = "KC",
    position = "TE",
    height = "6-5",
    weight = "243",
    dob = "1995-03-15",
    college = "Texas A&amp;M"
  )

  player_3345 = Player(
    player_id = 3345,
    full_name = "Adam Shaheen",
    last_name = "Shaheen",
    first_name = "Adam",
    nfl_team = "MIA",
    position = "TE",
    height = "6-6",
    weight = "257",
    dob = "1994-10-24",
    college = "Ashland"
  )

  player_3375 = Player(
    player_id = 3375,
    full_name = "Jonnu Smith",
    last_name = "Smith",
    first_name = "Jonnu",
    nfl_team = "TEN",
    position = "TE",
    height = "6-3",
    weight = "248",
    dob = "1995-08-22",
    college = "Florida International"
  )

  player_3900 = Player(
    player_id = 3900,
    full_name = "Kaden Smith",
    last_name = "Smith",
    first_name = "Kaden",
    nfl_team = "NYG",
    position = "TE",
    height = "6-5",
    weight = "252",
    dob = "1997-04-24",
    college = "Stanford"
  )

  player_1468 = Player(
    player_id = 1468,
    full_name = "Lee Smith",
    last_name = "Smith",
    first_name = "Lee",
    nfl_team = "BUF",
    position = "TE",
    height = "6-6",
    weight = "265",
    dob = "1987-11-21",
    college = "Marshall"
  )

  player_3932 = Player(
    player_id = 3932,
    full_name = "Irv Smith Jr",
    last_name = "Smith Jr",
    first_name = "Irv",
    nfl_team = "MIN",
    position = "TE",
    height = "6-2",
    weight = "240",
    dob = "1998-08-09",
    college = "Alabama"
  )

  player_3621 = Player(
    player_id = 3621,
    full_name = "Durham Smythe",
    last_name = "Smythe",
    first_name = "Durham",
    nfl_team = "MIA",
    position = "TE",
    height = "6-6",
    weight = "260",
    dob = "1995-08-09",
    college = "Notre Dame"
  )

  player_3993 = Player(
    player_id = 3993,
    full_name = "Matt Sokol",
    last_name = "Sokol",
    first_name = "Matt",
    nfl_team = "DET",
    position = "TE",
    height = "6-5",
    weight = "249",
    dob = "1995-11-09",
    college = "Michigan State"
  )

  player_3303 = Player(
    player_id = 3303,
    full_name = "Jeremy Sprinkle",
    last_name = "Sprinkle",
    first_name = "Jeremy",
    nfl_team = "WAS",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1994-08-10",
    college = "Arkansas"
  )

  player_4328 = Player(
    player_id = 4328,
    full_name = "Dylan Stapleton",
    last_name = "Stapleton",
    first_name = "Dylan",
    nfl_team = "HOU",
    position = "TE",
    height = "6-5",
    weight = "242",
    dob = "0000-00-00",
    college = "James Madison"
  )

  player_3928 = Player(
    player_id = 3928,
    full_name = "Jace Sternberger",
    last_name = "Sternberger",
    first_name = "Jace",
    nfl_team = "GB",
    position = "TE",
    height = "6-4",
    weight = "250",
    dob = "1996-06-26",
    college = "Texas A&amp;M"
  )

  player_4361 = Player(
    player_id = 4361,
    full_name = "Tommy Stevens",
    last_name = "Stevens",
    first_name = "Tommy",
    nfl_team = "NO",
    position = "TE",
    height = "6-5",
    weight = "235",
    dob = "1996-12-15",
    college = "Mississippi State"
  )

  player_1469 = Player(
    player_id = 1469,
    full_name = "Luke Stocker",
    last_name = "Stocker",
    first_name = "Luke",
    nfl_team = "ATL",
    position = "TE",
    height = "6-5",
    weight = "253",
    dob = "1988-07-17",
    college = "Tennessee"
  )

  player_4360 = Player(
    player_id = 4360,
    full_name = "Cam Sutton",
    last_name = "Sutton",
    first_name = "Cam",
    nfl_team = "CAR",
    position = "TE",
    height = "6-6",
    weight = "226",
    dob = "0000-00-00",
    college = "Fresno State"
  )

  player_2741 = Player(
    player_id = 2741,
    full_name = "Geoff Swaim",
    last_name = "Swaim",
    first_name = "Geoff",
    nfl_team = "TEN",
    position = "TE",
    height = "6-4",
    weight = "260",
    dob = "1993-09-16",
    college = "Texas"
  )

  player_3858 = Player(
    player_id = 3858,
    full_name = "Tommy Sweeney",
    last_name = "Sweeney",
    first_name = "Tommy",
    nfl_team = "BUF",
    position = "TE",
    height = "6-5",
    weight = "251",
    dob = "1995-07-01",
    college = "Boston College"
  )

  player_4205 = Player(
    player_id = 4205,
    full_name = "Charlie Taumoepeau",
    last_name = "Taumoepeau",
    first_name = "Charlie",
    nfl_team = "DAL",
    position = "TE",
    height = "6-3",
    weight = "245",
    dob = "1998-03-25",
    college = "Portland State"
  )

  player_3666 = Player(
    player_id = 3666,
    full_name = "Jordan Thomas",
    last_name = "Thomas",
    first_name = "Jordan",
    nfl_team = "ARI",
    position = "TE",
    height = "6-5",
    weight = "277",
    dob = "1996-08-02",
    college = "Mississippi State"
  )

  player_3675 = Player(
    player_id = 3675,
    full_name = "Ian Thomas",
    last_name = "Thomas",
    first_name = "Ian",
    nfl_team = "CAR",
    position = "TE",
    height = "6-3",
    weight = "260",
    dob = "1996-06-06",
    college = "Indiana"
  )

  player_2520 = Player(
    player_id = 2520,
    full_name = "Logan Thomas",
    last_name = "Thomas",
    first_name = "Logan",
    nfl_team = "WAS",
    position = "TE",
    height = "6-6",
    weight = "250",
    dob = "1991-07-01",
    college = "Virginia Tech"
  )

  player_3554 = Player(
    player_id = 3554,
    full_name = "Colin Thompson",
    last_name = "Thompson",
    first_name = "Colin",
    nfl_team = "CAR",
    position = "TE",
    height = "6-4",
    weight = "255",
    dob = "1993-12-15",
    college = "Temple"
  )

  player_4219 = Player(
    player_id = 4219,
    full_name = "Noah Togiai",
    last_name = "Togiai",
    first_name = "Noah",
    nfl_team = "IND",
    position = "TE",
    height = "6-4",
    weight = "246",
    dob = "1997-07-06",
    college = "Oregon State"
  )

  player_2375 = Player(
    player_id = 2375,
    full_name = "Levine Toilolo",
    last_name = "Toilolo",
    first_name = "Levine",
    nfl_team = "NYG",
    position = "TE",
    height = "6-8",
    weight = "268",
    dob = "1991-07-30",
    college = "Stanford"
  )

  player_2903 = Player(
    player_id = 2903,
    full_name = "Eric Tomlinson",
    last_name = "Tomlinson",
    first_name = "Eric",
    nfl_team = "NYG",
    position = "TE",
    height = "6-6",
    weight = "263",
    dob = "1992-04-22",
    college = "Texas-El Paso"
  )

  player_3522 = Player(
    player_id = 3522,
    full_name = "Robert Tonyan",
    last_name = "Tonyan Jr.",
    first_name = "Robert",
    nfl_team = "GB",
    position = "TE",
    height = "6-5",
    weight = "237",
    dob = "1994-04-30",
    college = "Indiana State"
  )

  player_4179 = Player(
    player_id = 4179,
    full_name = "Adam Trautman",
    last_name = "Trautman",
    first_name = "Adam",
    nfl_team = "NO",
    position = "TE",
    height = "6-6",
    weight = "253",
    dob = "1997-02-05",
    college = "Dayton"
  )

  player_3058 = Player(
    player_id = 3058,
    full_name = "Ross Travis",
    last_name = "Travis",
    first_name = "Ross",
    nfl_team = "NYJ",
    position = "TE",
    height = "6-6",
    weight = "248",
    dob = "1993-01-09",
    college = "Penn State"
  )

  player_2780 = Player(
    player_id = 2780,
    full_name = "C.J. Uzomah",
    last_name = "Uzomah",
    first_name = "C.J.",
    nfl_team = "CIN",
    position = "TE",
    height = "6-6",
    weight = "260",
    dob = "1993-01-14",
    college = "Auburn"
  )

  player_3288 = Player(
    player_id = 3288,
    full_name = "Jason Vander Laan",
    last_name = "Vander Laan",
    first_name = "Jason",
    nfl_team = "NO",
    position = "TE",
    height = "6-3",
    weight = "245",
    dob = "1992-09-22",
    college = "Ferris State"
  )

  player_3071 = Player(
    player_id = 3071,
    full_name = "Nick Vannett",
    last_name = "Vannett",
    first_name = "Nick",
    nfl_team = "DEN",
    position = "TE",
    height = "6-6",
    weight = "261",
    dob = "1993-03-06",
    college = "Ohio State"
  )

  player_3738 = Player(
    player_id = 3738,
    full_name = "Andrew Vollert",
    last_name = "Vollert",
    first_name = "Andrew",
    nfl_team = "CAR",
    position = "TE",
    height = "6-5",
    weight = "245",
    dob = "1995-03-15",
    college = "Weber State"
  )

  player_2775 = Player(
    player_id = 2775,
    full_name = "Darren Waller",
    last_name = "Waller",
    first_name = "Darren",
    nfl_team = "LV",
    position = "TE",
    height = "6-6",
    weight = "255",
    dob = "1992-09-13",
    college = "Georgia Tech"
  )

  player_3934 = Player(
    player_id = 3934,
    full_name = "Kahale Warring",
    last_name = "Warring",
    first_name = "Kahale",
    nfl_team = "HOU",
    position = "TE",
    height = "6-5",
    weight = "250",
    dob = "1997-03-23",
    college = "San Diego State"
  )

  player_3865 = Player(
    player_id = 3865,
    full_name = "Trevon Wesco",
    last_name = "Wesco",
    first_name = "Trevon",
    nfl_team = "NYJ",
    position = "TE",
    height = "6-3",
    weight = "267",
    dob = "1995-09-12",
    college = "West Virginia"
  )

  player_3216 = Player(
    player_id = 3216,
    full_name = "Cole Wick",
    last_name = "Wick",
    first_name = "Cole",
    nfl_team = "NO",
    position = "TE",
    height = "6-6",
    weight = "257",
    dob = "1993-11-30",
    college = "Incarnate Word"
  )

  player_4304 = Player(
    player_id = 4304,
    full_name = "Nate Wieting",
    last_name = "Wieting",
    first_name = "Nate",
    nfl_team = "CLE",
    position = "TE",
    height = "6-4",
    weight = "244",
    dob = "1997-02-20",
    college = "Iowa"
  )

  player_4297 = Player(
    player_id = 4297,
    full_name = "Mitchell Wilcox",
    last_name = "Wilcox",
    first_name = "Mitchell",
    nfl_team = "CIN",
    position = "TE",
    height = "6-4",
    weight = "245",
    dob = "1996-11-07",
    college = "South Florida"
  )

  player_2777 = Player(
    player_id = 2777,
    full_name = "Maxx Williams",
    last_name = "Williams",
    first_name = "Maxx",
    nfl_team = "ARI",
    position = "TE",
    height = "6-4",
    weight = "252",
    dob = "1994-04-12",
    college = "Minnesota"
  )

  player_2251 = Player(
    player_id = 2251,
    full_name = "Luke Willson",
    last_name = "Willson",
    first_name = "Luke",
    nfl_team = "SEA",
    position = "TE",
    height = "6-5",
    weight = "254",
    dob = "1990-01-15",
    college = "Rice"
  )

  player_3897 = Player(
    player_id = 3897,
    full_name = "Caleb Wilson",
    last_name = "Wilson",
    first_name = "Caleb",
    nfl_team = "PHI",
    position = "TE",
    height = "6-4",
    weight = "240",
    dob = "1996-07-15",
    college = "UCLA"
  )

  player_733 = Player(
    player_id = 733,
    full_name = "Jason Witten",
    last_name = "Witten",
    first_name = "Jason",
    nfl_team = "LV",
    position = "TE",
    height = "6-6",
    weight = "263",
    dob = "1982-05-06",
    college = "Tennessee"
  )

  player_4265 = Player(
    player_id = 4265,
    full_name = "Charlie Woerner",
    last_name = "Woerner",
    first_name = "Charlie",
    nfl_team = "SF",
    position = "TE",
    height = "6-5",
    weight = "245",
    dob = "1997-10-16",
    college = "Georgia"
  )

  player_4293 = Player(
    player_id = 4293,
    full_name = "Eli Wolf",
    last_name = "Wolf",
    first_name = "Eli",
    nfl_team = "BAL",
    position = "TE",
    height = "6-4",
    weight = "236",
    dob = "1997-03-11",
    college = "Georgia"
  )

  player_3813 = Player(
    player_id = 3813,
    full_name = "Ethan Wolf",
    last_name = "Wolf",
    first_name = "Ethan",
    nfl_team = "LAR",
    position = "TE",
    height = "6-5",
    weight = "255",
    dob = "1995-11-07",
    college = "Tennessee"
  )

  player_4375 = Player(
    player_id = 4375,
    full_name = "Dominick WoodAnderson",
    last_name = "WoodAnderson",
    first_name = "Dominick",
    nfl_team = "SEA",
    position = "TE",
    height = "6-4",
    weight = "257",
    dob = "0000-00-00",
    college = "Tennessee"
  )

  player_3833 = Player(
    player_id = 3833,
    full_name = "Deon Yelder",
    last_name = "Yelder",
    first_name = "Deon",
    nfl_team = "KC",
    position = "TE",
    height = "6-4",
    weight = "255",
    dob = "1995-03-06",
    college = "Western Kentucky"
  )

  player_4141 = Player(
    player_id = 4141,
    full_name = "Ramiz Ahmed",
    last_name = "Ahmed",
    first_name = "Ramiz",
    nfl_team = "CHI",
    position = "K",
    height = "6-0",
    weight = "190",
    dob = "1995-07-27",
    college = "Nevada"
  )

  player_3803 = Player(
    player_id = 3803,
    full_name = "Mike Badgley",
    last_name = "Badgley",
    first_name = "Mike",
    nfl_team = "LAC",
    position = "K",
    height = "5-10",
    weight = "183",
    dob = "1995-07-28",
    college = "Miami"
  )

  player_1685 = Player(
    player_id = 1685,
    full_name = "Dan Bailey",
    last_name = "Bailey",
    first_name = "Dan",
    nfl_team = "MIN",
    position = "K",
    height = "6-0",
    weight = "190",
    dob = "1988-01-26",
    college = "Oklahoma State"
  )

  player_4185 = Player(
    player_id = 4185,
    full_name = "Tyler Bass",
    last_name = "Bass",
    first_name = "Tyler",
    nfl_team = "BUF",
    position = "K",
    height = "5-10",
    weight = "185",
    dob = "1997-02-14",
    college = "Georgia Southern"
  )

  player_4332 = Player(
    player_id = 4332,
    full_name = "Rodrigo Blankenship",
    last_name = "Blankenship",
    first_name = "Rodrigo",
    nfl_team = "IND",
    position = "K",
    height = "6-1",
    weight = "191",
    dob = "1997-01-29",
    college = "Georgia"
  )

  player_2617 = Player(
    player_id = 2617,
    full_name = "Chris Boswell",
    last_name = "Boswell",
    first_name = "Chris",
    nfl_team = "PIT",
    position = "K",
    height = "6-2",
    weight = "185",
    dob = "1991-03-16",
    college = "Rice"
  )

  player_3198 = Player(
    player_id = 3198,
    full_name = "Jon Brown",
    last_name = "Brown",
    first_name = "Jon",
    nfl_team = "JAC",
    position = "K",
    height = "5-10",
    weight = "194",
    dob = "1992-12-07",
    college = "Louisville"
  )

  player_1930 = Player(
    player_id = 1930,
    full_name = "Randy Bullock",
    last_name = "Bullock",
    first_name = "Randy",
    nfl_team = "CIN",
    position = "K",
    height = "5-9",
    weight = "210",
    dob = "1989-12-16",
    college = "Texas A&amp;M"
  )

  player_3383 = Player(
    player_id = 3383,
    full_name = "Harrison Butker",
    last_name = "Butker",
    first_name = "Harrison",
    nfl_team = "KC",
    position = "K",
    height = "6-4",
    weight = "205",
    dob = "1995-07-14",
    college = "Georgia Tech"
  )

  player_3664 = Player(
    player_id = 3664,
    full_name = "Daniel Carlson",
    last_name = "Carlson",
    first_name = "Daniel",
    nfl_team = "LV",
    position = "K",
    height = "6-5",
    weight = "215",
    dob = "1995-01-23",
    college = "Auburn"
  )

  player_2528 = Player(
    player_id = 2528,
    full_name = "Chandler Catanzaro",
    last_name = "Catanzaro",
    first_name = "Chandler",
    nfl_team = "NYG",
    position = "K",
    height = "6-3",
    weight = "200",
    dob = "1991-02-26",
    college = "Clemson"
  )

  player_747 = Player(
    player_id = 747,
    full_name = "Mason Crosby",
    last_name = "Crosby",
    first_name = "Mason",
    nfl_team = "GB",
    position = "K",
    height = "6-1",
    weight = "207",
    dob = "1984-09-03",
    college = "Colorado"
  )

  player_4238 = Player(
    player_id = 4238,
    full_name = "Dominik Eberle",
    last_name = "Eberle",
    first_name = "Dominik",
    nfl_team = "LV",
    position = "K",
    height = "6-2",
    weight = "190",
    dob = "1996-07-04",
    college = "Utah State"
  )

  player_3333 = Player(
    player_id = 3333,
    full_name = "Jake Elliott",
    last_name = "Elliott",
    first_name = "Jake",
    nfl_team = "PHI",
    position = "K",
    height = "5-9",
    weight = "167",
    dob = "1995-01-21",
    college = "Memphis"
  )

  player_3269 = Player(
    player_id = 3269,
    full_name = "Ka'imi Fairbairn",
    last_name = "Fairbairn",
    first_name = "Ka'imi",
    nfl_team = "HOU",
    position = "K",
    height = "6-0",
    weight = "183",
    dob = "1994-01-29",
    college = "UCLA"
  )

  player_3575 = Player(
    player_id = 3575,
    full_name = "Sam Ficken",
    last_name = "Ficken",
    first_name = "Sam",
    nfl_team = "NYJ",
    position = "K",
    height = "6-1",
    weight = "192",
    dob = "1992-12-14",
    college = "Penn State"
  )

  player_751 = Player(
    player_id = 751,
    full_name = "Nick Folk",
    last_name = "Folk",
    first_name = "Nick",
    nfl_team = "NE",
    position = "K",
    height = "6-1",
    weight = "222",
    dob = "1984-11-05",
    college = "Arizona"
  )

  player_1687 = Player(
    player_id = 1687,
    full_name = "Kai Forbath",
    last_name = "Forbath",
    first_name = "Kai",
    nfl_team = "DAL",
    position = "K",
    height = "5-11",
    weight = "197",
    dob = "1987-09-02",
    college = "UCLA"
  )

  player_4100 = Player(
    player_id = 4100,
    full_name = "Elliott Fry",
    last_name = "Fry",
    first_name = "Elliott",
    nfl_team = "ATL",
    position = "K",
    height = "6-0",
    weight = "170",
    dob = "1994-12-12",
    college = "South Carolina"
  )

  player_1031 = Player(
    player_id = 1031,
    full_name = "Graham Gano",
    last_name = "Gano",
    first_name = "Graham",
    nfl_team = "NYG",
    position = "K",
    height = "6-2",
    weight = "202",
    dob = "1987-04-09",
    college = "Florida State"
  )

  player_3337 = Player(
    player_id = 3337,
    full_name = "Zane Gonzalez",
    last_name = "Gonzalez",
    first_name = "Zane",
    nfl_team = "ARI",
    position = "K",
    height = "6-0",
    weight = "202",
    dob = "1995-05-07",
    college = "Arizona State"
  )

  player_752 = Player(
    player_id = 752,
    full_name = "Stephen Gostkowski",
    last_name = "Gostkowski",
    first_name = "Stephen",
    nfl_team = "TEN",
    position = "K",
    height = "6-1",
    weight = "215",
    dob = "1984-01-28",
    college = "Memphis"
  )

  player_753 = Player(
    player_id = 753,
    full_name = "Robbie Gould",
    last_name = "Gould",
    first_name = "Robbie",
    nfl_team = "SF",
    position = "K",
    height = "6-0",
    weight = "190",
    dob = "1982-12-06",
    college = "Penn State"
  )

  player_4137 = Player(
    player_id = 4137,
    full_name = "Lirim Hajrullahu",
    last_name = "Hajrullahu",
    first_name = "Lirim",
    nfl_team = "LAR",
    position = "K",
    height = "5-11",
    weight = "205",
    dob = "1990-04-24",
    college = "Western Ontario"
  )

  player_758 = Player(
    player_id = 758,
    full_name = "Steven Hauschka",
    last_name = "Hauschka",
    first_name = "Steven",
    nfl_team = "JAC",
    position = "K",
    height = "6-4",
    weight = "210",
    dob = "1985-06-29",
    college = "North Carolina State"
  )

  player_2124 = Player(
    player_id = 2124,
    full_name = "Dustin Hopkins",
    last_name = "Hopkins",
    first_name = "Dustin",
    nfl_team = "WAS",
    position = "K",
    height = "6-2",
    weight = "203",
    dob = "1990-10-01",
    college = "Florida State"
  )

  player_3685 = Player(
    player_id = 3685,
    full_name = "Greg Joseph",
    last_name = "Joseph",
    first_name = "Greg",
    nfl_team = "TEN",
    position = "K",
    height = "6-0",
    weight = "210",
    dob = "1994-08-04",
    college = "Florida Atlantic"
  )

  player_3395 = Player(
    player_id = 3395,
    full_name = "Younghoe Koo",
    last_name = "Koo",
    first_name = "Younghoe",
    nfl_team = "ATL",
    position = "K",
    height = "5-10",
    weight = "195",
    dob = "1994-08-03",
    college = "Georgia Southern"
  )

  player_2924 = Player(
    player_id = 2924,
    full_name = "Josh Lambo",
    last_name = "Lambo",
    first_name = "Josh",
    nfl_team = "JAC",
    position = "K",
    height = "6-0",
    weight = "215",
    dob = "1990-11-19",
    college = "Texas A&amp;M"
  )

  player_3190 = Player(
    player_id = 3190,
    full_name = "Wil Lutz",
    last_name = "Lutz",
    first_name = "Wil",
    nfl_team = "NO",
    position = "K",
    height = "5-11",
    weight = "184",
    dob = "1994-07-07",
    college = "Georgia State"
  )

  player_4138 = Player(
    player_id = 4138,
    full_name = "Austin MacGinnis",
    last_name = "MacGinnis",
    first_name = "Austin",
    nfl_team = "LAR",
    position = "K",
    height = "5-10",
    weight = "185",
    dob = "1995-05-04",
    college = "Kentucky"
  )

  player_2154 = Player(
    player_id = 2154,
    full_name = "Brett Maher",
    last_name = "Maher",
    first_name = "Brett",
    nfl_team = "NYJ",
    position = "K",
    height = "6-1",
    weight = "185",
    dob = "1989-11-21",
    college = "Nebraska"
  )

  player_2309 = Player(
    player_id = 2309,
    full_name = "Sam Martin",
    last_name = "Martin",
    first_name = "Sam",
    nfl_team = "DEN",
    position = "K",
    height = "6-1",
    weight = "205",
    dob = "0000-00-00",
    college = "Appalachian State"
  )

  player_4349 = Player(
    player_id = 4349,
    full_name = "Tucker McCann",
    last_name = "McCann",
    first_name = "Tucker",
    nfl_team = "TEN",
    position = "K",
    height = "6-2",
    weight = "215",
    dob = "1997-11-10",
    college = "Missouri"
  )

  player_3960 = Player(
    player_id = 3960,
    full_name = "Chase McLaughlin",
    last_name = "McLaughlin",
    first_name = "Chase",
    nfl_team = "IND",
    position = "K",
    height = "5-11",
    weight = "187",
    dob = "1996-04-09",
    college = "Illinois"
  )

  player_2349 = Player(
    player_id = 2349,
    full_name = "Brandon McManus",
    last_name = "McManus",
    first_name = "Brandon",
    nfl_team = "DEN",
    position = "K",
    height = "6-3",
    weight = "201",
    dob = "1991-07-25",
    college = "Temple"
  )

  player_3018 = Player(
    player_id = 3018,
    full_name = "Jason Myers",
    last_name = "Myers",
    first_name = "Jason",
    nfl_team = "SEA",
    position = "K",
    height = "5-10",
    weight = "190",
    dob = "1991-05-12",
    college = "Marist"
  )

  player_2626 = Player(
    player_id = 2626,
    full_name = "Cody Parkey",
    last_name = "Parkey",
    first_name = "Cody",
    nfl_team = "CLE",
    position = "K",
    height = "6-0",
    weight = "190",
    dob = "1992-02-19",
    college = "Auburn"
  )

  player_3723 = Player(
    player_id = 3723,
    full_name = "Eddy Pineiro",
    last_name = "Pineiro",
    first_name = "Eddy",
    nfl_team = "CHI",
    position = "K",
    height = "5-11",
    weight = "177",
    dob = "1995-09-13",
    college = "Florida"
  )

  player_769 = Player(
    player_id = 769,
    full_name = "Matt Prater",
    last_name = "Prater",
    first_name = "Matt",
    nfl_team = "DET",
    position = "K",
    height = "5-10",
    weight = "201",
    dob = "1984-08-10",
    college = "Central Florida"
  )

  player_4195 = Player(
    player_id = 4195,
    full_name = "Justin Rohrwasser",
    last_name = "Rohrwasser",
    first_name = "Justin",
    nfl_team = "NE",
    position = "K",
    height = "6-3",
    weight = "230",
    dob = "1996-12-07",
    college = "Marshall"
  )

  player_3241 = Player(
    player_id = 3241,
    full_name = "Aldrick Rosas",
    last_name = "Rosas",
    first_name = "Aldrick",
    nfl_team = "JAC",
    position = "K",
    height = "6-3",
    weight = "221",
    dob = "1994-12-30",
    college = "Southern Oregon"
  )

  player_3622 = Player(
    player_id = 3622,
    full_name = "Jason Sanders",
    last_name = "Sanders",
    first_name = "Jason",
    nfl_team = "MIA",
    position = "K",
    height = "5-11",
    weight = "186",
    dob = "1995-11-16",
    college = "New Mexico"
  )

  player_2502 = Player(
    player_id = 2502,
    full_name = "Cairo Santos",
    last_name = "Santos",
    first_name = "Cairo",
    nfl_team = "CHI",
    position = "K",
    height = "5-8",
    weight = "160",
    dob = "1991-11-12",
    college = "Tulane"
  )

  player_3916 = Player(
    player_id = 3916,
    full_name = "Austin Seibert",
    last_name = "Seibert",
    first_name = "Austin",
    nfl_team = "CLE",
    position = "K",
    height = "5-9",
    weight = "214",
    dob = "1996-11-15",
    college = "Oklahoma"
  )

  player_4285 = Player(
    player_id = 4285,
    full_name = "Sam Sloman",
    last_name = "Sloman",
    first_name = "Sam",
    nfl_team = "LAR",
    position = "K",
    height = "5-8",
    weight = "205",
    dob = "1997-09-19",
    college = "Miami, O."
  )

  player_4120 = Player(
    player_id = 4120,
    full_name = "Joey Slye",
    last_name = "Slye",
    first_name = "Joey",
    nfl_team = "CAR",
    position = "K",
    height = "5-11",
    weight = "213",
    dob = "1996-04-10",
    college = "Virginia Tech"
  )

  player_893 = Player(
    player_id = 893,
    full_name = "Ryan Succop",
    last_name = "Succop",
    first_name = "Ryan",
    nfl_team = "TB",
    position = "K",
    height = "6-2",
    weight = "218",
    dob = "1986-09-19",
    college = "South Carolina"
  )

  player_2079 = Player(
    player_id = 2079,
    full_name = "Justin Tucker",
    last_name = "Tucker",
    first_name = "Justin",
    nfl_team = "BAL",
    position = "K",
    height = "6-1",
    weight = "183",
    dob = "1989-11-21",
    college = "Texas"
  )

  player_4122 = Player(
    player_id = 4122,
    full_name = "Kaare Vedvik",
    last_name = "Vedvik",
    first_name = "Kaare",
    nfl_team = "BUF",
    position = "K",
    height = "6-3",
    weight = "210",
    dob = "1994-03-16",
    college = "Marshall"
  )

  player_4125 = Player(
    player_id = 4125,
    full_name = "Tristan Vizcaino",
    last_name = "Vizcaino",
    first_name = "Tristan",
    nfl_team = "CIN",
    position = "K",
    height = "6-2",
    weight = "205",
    dob = "1996-07-31",
    college = "Washington"
  )

  player_4294 = Player(
    player_id = 4294,
    full_name = "Nick Vogel",
    last_name = "Vogel",
    first_name = "Nick",
    nfl_team = "BAL",
    position = "K",
    height = "5-9",
    weight = "188",
    dob = "1995-12-23",
    college = "UAB"
  )

  player_4376 = Player(
    player_id = 4376,
    full_name = "Brandon Wright",
    last_name = "Wright",
    first_name = "Brandon",
    nfl_team = "JAC",
    position = "K",
    height = "5-10",
    weight = "182",
    dob = "1997-02-18",
    college = "Georgia State"
  )

  player_1865 = Player(
    player_id = 1865,
    full_name = "Greg Zuerlein",
    last_name = "Zuerlein",
    first_name = "Greg",
    nfl_team = "DAL",
    position = "K",
    height = "6-0",
    weight = "191",
    dob = "1987-12-27",
    college = "Missouri Western"
  )

  player_1057 = Player(
    player_id = 1057,
    full_name = "Tampa Bay Buccaneers",
    last_name = "Bay Buccaneers",
    first_name = "Tampa",
    nfl_team = "TB",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1050 = Player(
    player_id = 1050,
    full_name = "Green Bay Packers",
    last_name = "Bay Packers",
    first_name = "Green",
    nfl_team = "GB",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1049 = Player(
    player_id = 1049,
    full_name = "Chicago Bears",
    last_name = "Bears",
    first_name = "Chicago",
    nfl_team = "CHI",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1059 = Player(
    player_id = 1059,
    full_name = "Cincinnati Bengals",
    last_name = "Bengals",
    first_name = "Cincinnati",
    nfl_team = "CIN",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1047 = Player(
    player_id = 1047,
    full_name = "Buffalo Bills",
    last_name = "Bills",
    first_name = "Buffalo",
    nfl_team = "BUF",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1061 = Player(
    player_id = 1061,
    full_name = "Denver Broncos",
    last_name = "Broncos",
    first_name = "Denver",
    nfl_team = "DEN",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1060 = Player(
    player_id = 1060,
    full_name = "Cleveland Browns",
    last_name = "Browns",
    first_name = "Cleveland",
    nfl_team = "CLE",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1045 = Player(
    player_id = 1045,
    full_name = "Arizona Cardinals",
    last_name = "Cardinals",
    first_name = "Arizona",
    nfl_team = "ARI",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1054 = Player(
    player_id = 1054,
    full_name = "Los Angeles Chargers",
    last_name = "Chargers",
    first_name = "Los Angeles",
    nfl_team = "LAC",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1064 = Player(
    player_id = 1064,
    full_name = "Kansas City Chiefs",
    last_name = "City Chiefs",
    first_name = "Kansas",
    nfl_team = "KC",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1051 = Player(
    player_id = 1051,
    full_name = "Indianapolis Colts",
    last_name = "Colts",
    first_name = "Indianapolis",
    nfl_team = "IND",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1039 = Player(
    player_id = 1039,
    full_name = "Dallas Cowboys",
    last_name = "Cowboys",
    first_name = "Dallas",
    nfl_team = "DAL",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1053 = Player(
    player_id = 1053,
    full_name = "Miami Dolphins",
    last_name = "Dolphins",
    first_name = "Miami",
    nfl_team = "MIA",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1043 = Player(
    player_id = 1043,
    full_name = "Philadelphia Eagles",
    last_name = "Eagles",
    first_name = "Philadelphia",
    nfl_team = "PHI",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1041 = Player(
    player_id = 1041,
    full_name = "New England Patriots",
    last_name = "England Patriots",
    first_name = "New",
    nfl_team = "NE",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1046 = Player(
    player_id = 1046,
    full_name = "Atlanta Falcons",
    last_name = "Falcons",
    first_name = "Atlanta",
    nfl_team = "ATL",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1058 = Player(
    player_id = 1058,
    full_name = "Washington Football Team",
    last_name = "Football Team",
    first_name = "Washington",
    nfl_team = "WAS",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1055 = Player(
    player_id = 1055,
    full_name = "San Francisco 49ers",
    last_name = "Francisco 49ers",
    first_name = "San",
    nfl_team = "SF",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1052 = Player(
    player_id = 1052,
    full_name = "Jacksonville Jaguars",
    last_name = "Jaguars",
    first_name = "Jacksonville",
    nfl_team = "JAC",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1062 = Player(
    player_id = 1062,
    full_name = "Detroit Lions",
    last_name = "Lions",
    first_name = "Detroit",
    nfl_team = "DET",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1065 = Player(
    player_id = 1065,
    full_name = "New Orleans Saints",
    last_name = "Orleans Saints",
    first_name = "New",
    nfl_team = "NO",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1048 = Player(
    player_id = 1048,
    full_name = "Carolina Panthers",
    last_name = "Panthers",
    first_name = "Carolina",
    nfl_team = "CAR",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1066 = Player(
    player_id = 1066,
    full_name = "Las Vegas Raiders",
    last_name = "Raiders",
    first_name = "Las Vegas",
    nfl_team = "LV",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1067 = Player(
    player_id = 1067,
    full_name = "Los Angeles Rams",
    last_name = "Rams",
    first_name = "Los Angeles",
    nfl_team = "LAR",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1038 = Player(
    player_id = 1038,
    full_name = "Baltimore Ravens",
    last_name = "Ravens",
    first_name = "Baltimore",
    nfl_team = "BAL",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1056 = Player(
    player_id = 1056,
    full_name = "Seattle Seahawks",
    last_name = "Seahawks",
    first_name = "Seattle",
    nfl_team = "SEA",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1037 = Player(
    player_id = 1037,
    full_name = "Pittsburgh Steelers",
    last_name = "Steelers",
    first_name = "Pittsburgh",
    nfl_team = "PIT",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1063 = Player(
    player_id = 1063,
    full_name = "Houston Texans",
    last_name = "Texans",
    first_name = "Houston",
    nfl_team = "HOU",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1044 = Player(
    player_id = 1044,
    full_name = "Tennessee Titans",
    last_name = "Titans",
    first_name = "Tennessee",
    nfl_team = "TEN",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1040 = Player(
    player_id = 1040,
    full_name = "Minnesota Vikings",
    last_name = "Vikings",
    first_name = "Minnesota",
    nfl_team = "MIN",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1036 = Player(
    player_id = 1036,
    full_name = "New York Giants",
    last_name = "York Giants",
    first_name = "New",
    nfl_team = "NYG",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

  player_1042 = Player(
    player_id = 1042,
    full_name = "New York Jets",
    last_name = "York Jets",
    first_name = "New",
    nfl_team = "NYJ",
    position = "DEF",
    height = "",
    weight = "",
    dob = "0000-00-00",
    college = ""
  )

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

  db.session.add(player_3274)
  db.session.add(player_3826)
  db.session.add(player_3577)
  db.session.add(player_3994)
  db.session.add(player_2168)
  db.session.add(player_3829)
  db.session.add(player_3321)
  db.session.add(player_3814)
  db.session.add(player_4028)
  db.session.add(player_3784)
  db.session.add(player_13)
  db.session.add(player_2191)
  db.session.add(player_14)
  db.session.add(player_2601)
  db.session.add(player_3030)
  db.session.add(player_4049)
  db.session.add(player_4139)
  db.session.add(player_2503)
  db.session.add(player_4206)
  db.session.add(player_1805)
  db.session.add(player_1391)
  db.session.add(player_786)
  db.session.add(player_3580)
  db.session.add(player_4298)
  db.session.add(player_4198)
  db.session.add(player_3338)
  db.session.add(player_4022)
  db.session.add(player_3064)
  db.session.add(player_4174)
  db.session.add(player_3623)
  db.session.add(player_2578)
  db.session.add(player_3911)
  db.session.add(player_34)
  db.session.add(player_35)
  db.session.add(player_1801)
  db.session.add(player_4181)
  db.session.add(player_1393)
  db.session.add(player_2441)
  db.session.add(player_2540)
  db.session.add(player_2392)
  db.session.add(player_3072)
  db.session.add(player_4266)
  db.session.add(player_3942)
  db.session.add(player_1806)
  db.session.add(player_2385)
  db.session.add(player_3873)
  db.session.add(player_52)
  db.session.add(player_4135)
  db.session.add(player_3441)
  db.session.add(player_4034)
  db.session.add(player_901)
  db.session.add(player_2790)
  db.session.add(player_4286)
  db.session.add(player_4154)
  db.session.add(player_3596)
  db.session.add(player_3868)
  db.session.add(player_1926)
  db.session.add(player_3304)
  db.session.add(player_3334)
  db.session.add(player_3632)
  db.session.add(player_4189)
  db.session.add(player_3879)
  db.session.add(player_4142)
  db.session.add(player_4275)
  db.session.add(player_4333)
  db.session.add(player_3051)
  db.session.add(player_3311)
  db.session.add(player_2770)
  db.session.add(player_2801)
  db.session.add(player_3599)
  db.session.add(player_2554)
  db.session.add(player_1116)
  db.session.add(player_4343)
  db.session.add(player_3647)
  db.session.add(player_3907)
  db.session.add(player_3936)
  db.session.add(player_4220)
  db.session.add(player_72)
  db.session.add(player_4151)
  db.session.add(player_4314)
  db.session.add(player_3415)
  db.session.add(player_3893)
  db.session.add(player_4225)
  db.session.add(player_1398)
  db.session.add(player_4374)
  db.session.add(player_4276)
  db.session.add(player_3280)
  db.session.add(player_3036)
  db.session.add(player_86)
  db.session.add(player_87)
  db.session.add(player_88)
  db.session.add(player_3591)
  db.session.add(player_3093)
  db.session.add(player_3601)
  db.session.add(player_3478)
  db.session.add(player_4258)
  db.session.add(player_93)
  db.session.add(player_3951)
  db.session.add(player_94)
  db.session.add(player_3978)
  db.session.add(player_2750)
  db.session.add(player_4365)
  db.session.add(player_4190)
  db.session.add(player_97)
  db.session.add(player_2146)
  db.session.add(player_793)
  db.session.add(player_4318)
  db.session.add(player_3892)
  db.session.add(player_3861)
  db.session.add(player_4126)
  db.session.add(player_3047)
  db.session.add(player_4116)
  db.session.add(player_4129)
  db.session.add(player_1758)
  db.session.add(player_2084)
  db.session.add(player_1401)
  db.session.add(player_3870)
  db.session.add(player_4324)
  db.session.add(player_3342)
  db.session.add(player_3453)
  db.session.add(player_3360)
  db.session.add(player_3292)
  db.session.add(player_3044)
  db.session.add(player_3628)
  db.session.add(player_4046)
  db.session.add(player_1847)
  db.session.add(player_2812)
  db.session.add(player_3905)
  db.session.add(player_3652)
  db.session.add(player_2788)
  db.session.add(player_3697)
  db.session.add(player_4259)
  db.session.add(player_4162)
  db.session.add(player_3912)
  db.session.add(player_4199)
  db.session.add(player_4085)
  db.session.add(player_3571)
  db.session.add(player_3937)
  db.session.add(player_3952)
  db.session.add(player_3620)
  db.session.add(player_3258)
  db.session.add(player_4322)
  db.session.add(player_2378)
  db.session.add(player_3659)
  db.session.add(player_2289)
  db.session.add(player_4226)
  db.session.add(player_3779)
  db.session.add(player_4247)
  db.session.add(player_2273)
  db.session.add(player_4050)
  db.session.add(player_1769)
  db.session.add(player_3827)
  db.session.add(player_3052)
  db.session.add(player_3790)
  db.session.add(player_4239)
  db.session.add(player_3416)
  db.session.add(player_4074)
  db.session.add(player_2937)
  db.session.add(player_2274)
  db.session.add(player_2789)
  db.session.add(player_4366)
  db.session.add(player_3626)
  db.session.add(player_4267)
  db.session.add(player_3192)
  db.session.add(player_3326)
  db.session.add(player_4005)
  db.session.add(player_3600)
  db.session.add(player_3691)
  db.session.add(player_3486)
  db.session.add(player_3343)
  db.session.add(player_2806)
  db.session.add(player_3339)
  db.session.add(player_3354)
  db.session.add(player_4334)
  db.session.add(player_3860)
  db.session.add(player_3988)
  db.session.add(player_4101)
  db.session.add(player_4268)
  db.session.add(player_4350)
  db.session.add(player_2763)
  db.session.add(player_3807)
  db.session.add(player_1381)
  db.session.add(player_4172)
  db.session.add(player_1720)
  db.session.add(player_3077)
  db.session.add(player_4164)
  db.session.add(player_4200)
  db.session.add(player_3026)
  db.session.add(player_3642)
  db.session.add(player_3548)
  db.session.add(player_3751)
  db.session.add(player_4133)
  db.session.add(player_3392)
  db.session.add(player_3037)
  db.session.add(player_3102)
  db.session.add(player_4178)
  db.session.add(player_4335)
  db.session.add(player_3256)
  db.session.add(player_3129)
  db.session.add(player_3364)
  db.session.add(player_3588)
  db.session.add(player_2651)
  db.session.add(player_3293)
  db.session.add(player_3859)
  db.session.add(player_4155)
  db.session.add(player_4277)
  db.session.add(player_3933)
  db.session.add(player_2759)
  db.session.add(player_4107)
  db.session.add(player_180)
  db.session.add(player_2771)
  db.session.add(player_4024)
  db.session.add(player_3226)
  db.session.add(player_3862)
  db.session.add(player_4260)
  db.session.add(player_3906)
  db.session.add(player_3112)
  db.session.add(player_4299)
  db.session.add(player_4054)
  db.session.add(player_3376)
  db.session.add(player_3908)
  db.session.add(player_2555)
  db.session.add(player_3766)
  db.session.add(player_3971)
  db.session.add(player_3995)
  db.session.add(player_3667)
  db.session.add(player_4248)
  db.session.add(player_4261)
  db.session.add(player_4240)
  db.session.add(player_4079)
  db.session.add(player_3901)
  db.session.add(player_3091)
  db.session.add(player_3684)
  db.session.add(player_3312)
  db.session.add(player_4310)
  db.session.add(player_2530)
  db.session.add(player_3985)
  db.session.add(player_1415)
  db.session.add(player_3640)
  db.session.add(player_3038)
  db.session.add(player_3889)
  db.session.add(player_3053)
  db.session.add(player_3604)
  db.session.add(player_3863)
  db.session.add(player_3923)
  db.session.add(player_4030)
  db.session.add(player_2760)
  db.session.add(player_2781)
  db.session.add(player_3349)
  db.session.add(player_3614)
  db.session.add(player_1416)
  db.session.add(player_4269)
  db.session.add(player_4278)
  db.session.add(player_4317)
  db.session.add(player_4362)
  db.session.add(player_2265)
  db.session.add(player_3384)
  db.session.add(player_4160)
  db.session.add(player_3649)
  db.session.add(player_4213)
  db.session.add(player_3961)
  db.session.add(player_4207)
  db.session.add(player_4300)
  db.session.add(player_1418)
  db.session.add(player_3707)
  db.session.add(player_2326)
  db.session.add(player_3317)
  db.session.add(player_3874)
  db.session.add(player_3362)
  db.session.add(player_3979)
  db.session.add(player_3929)
  db.session.add(player_4306)
  db.session.add(player_3379)
  db.session.add(player_810)
  db.session.add(player_4168)
  db.session.add(player_4063)
  db.session.add(player_3283)
  db.session.add(player_2602)
  db.session.add(player_3245)
  db.session.add(player_3387)
  db.session.add(player_3579)
  db.session.add(player_1761)
  db.session.add(player_3329)
  db.session.add(player_3920)
  db.session.add(player_2792)
  db.session.add(player_4124)
  db.session.add(player_4147)
  db.session.add(player_2898)
  db.session.add(player_3371)
  db.session.add(player_2811)
  db.session.add(player_2201)
  db.session.add(player_4245)
  db.session.add(player_3776)
  db.session.add(player_4305)
  db.session.add(player_2730)
  db.session.add(player_3524)
  db.session.add(player_1990)
  db.session.add(player_3941)
  db.session.add(player_4201)
  db.session.add(player_3426)
  db.session.add(player_4081)
  db.session.add(player_4140)
  db.session.add(player_3595)
  db.session.add(player_3173)
  db.session.add(player_4152)
  db.session.add(player_3300)
  db.session.add(player_3040)
  db.session.add(player_2581)
  db.session.add(player_4186)
  db.session.add(player_259)
  db.session.add(player_4325)
  db.session.add(player_4307)
  db.session.add(player_4373)
  db.session.add(player_3866)
  db.session.add(player_3265)
  db.session.add(player_3069)
  db.session.add(player_4287)
  db.session.add(player_3976)
  db.session.add(player_3846)
  db.session.add(player_3156)
  db.session.add(player_2305)
  db.session.add(player_4336)
  db.session.add(player_3657)
  db.session.add(player_3871)
  db.session.add(player_3629)
  db.session.add(player_3943)
  db.session.add(player_4344)
  db.session.add(player_3676)
  db.session.add(player_4311)
  db.session.add(player_1427)
  db.session.add(player_3855)
  db.session.add(player_4337)
  db.session.add(player_3045)
  db.session.add(player_4356)
  db.session.add(player_3673)
  db.session.add(player_2934)
  db.session.add(player_3263)
  db.session.add(player_3917)
  db.session.add(player_3443)
  db.session.add(player_3792)
  db.session.add(player_4171)
  db.session.add(player_4369)
  db.session.add(player_4175)
  db.session.add(player_4315)
  db.session.add(player_3886)
  db.session.add(player_2176)
  db.session.add(player_3752)
  db.session.add(player_3753)
  db.session.add(player_4180)
  db.session.add(player_3120)
  db.session.add(player_3849)
  db.session.add(player_4249)
  db.session.add(player_4108)
  db.session.add(player_4214)
  db.session.add(player_3094)
  db.session.add(player_3060)
  db.session.add(player_3062)
  db.session.add(player_3686)
  db.session.add(player_3867)
  db.session.add(player_3706)
  db.session.add(player_4295)
  db.session.add(player_2444)
  db.session.add(player_3921)
  db.session.add(player_3668)
  db.session.add(player_1542)
  db.session.add(player_3351)
  db.session.add(player_3913)
  db.session.add(player_3927)
  db.session.add(player_4183)
  db.session.add(player_3712)
  db.session.add(player_2435)
  db.session.add(player_4288)
  db.session.add(player_3740)
  db.session.add(player_3835)
  db.session.add(player_2878)
  db.session.add(player_3355)
  db.session.add(player_2596)
  db.session.add(player_3344)
  db.session.add(player_3427)
  db.session.add(player_2744)
  db.session.add(player_4381)
  db.session.add(player_4136)
  db.session.add(player_2215)
  db.session.add(player_3223)
  db.session.add(player_323)
  db.session.add(player_3259)
  db.session.add(player_3872)
  db.session.add(player_3639)
  db.session.add(player_2257)
  db.session.add(player_4230)
  db.session.add(player_4009)
  db.session.add(player_4215)
  db.session.add(player_3809)
  db.session.add(player_4357)
  db.session.add(player_1787)
  db.session.add(player_2465)
  db.session.add(player_3794)
  db.session.add(player_4128)
  db.session.add(player_2006)
  db.session.add(player_1883)
  db.session.add(player_3881)
  db.session.add(player_3624)
  db.session.add(player_3720)
  db.session.add(player_3819)
  db.session.add(player_3428)
  db.session.add(player_3417)
  db.session.add(player_3418)
  db.session.add(player_4158)
  db.session.add(player_3081)
  db.session.add(player_3909)
  db.session.add(player_4301)
  db.session.add(player_4250)
  db.session.add(player_3910)
  db.session.add(player_3939)
  db.session.add(player_3747)
  db.session.add(player_2223)
  db.session.add(player_4302)
  db.session.add(player_3290)
  db.session.add(player_2523)
  db.session.add(player_4025)
  db.session.add(player_3810)
  db.session.add(player_3894)
  db.session.add(player_3954)
  db.session.add(player_3016)
  db.session.add(player_4251)
  db.session.add(player_4196)
  db.session.add(player_3669)
  db.session.add(player_4363)
  db.session.add(player_3935)
  db.session.add(player_4197)
  db.session.add(player_3402)
  db.session.add(player_2840)
  db.session.add(player_4312)
  db.session.add(player_3609)
  db.session.add(player_3314)
  db.session.add(player_4319)
  db.session.add(player_4169)
  db.session.add(player_4227)
  db.session.add(player_1437)
  db.session.add(player_4187)
  db.session.add(player_3534)
  db.session.add(player_3084)
  db.session.add(player_2754)
  db.session.add(player_2669)
  db.session.add(player_3073)
  db.session.add(player_2756)
  db.session.add(player_3082)
  db.session.add(player_4241)
  db.session.add(player_4326)
  db.session.add(player_3665)
  db.session.add(player_3589)
  db.session.add(player_2748)
  db.session.add(player_3981)
  db.session.add(player_3327)
  db.session.add(player_3096)
  db.session.add(player_3372)
  db.session.add(player_4148)
  db.session.add(player_2743)
  db.session.add(player_4051)
  db.session.add(player_3542)
  db.session.add(player_4320)
  db.session.add(player_3301)
  db.session.add(player_3583)
  db.session.add(player_3982)
  db.session.add(player_4270)
  db.session.add(player_4289)
  db.session.add(player_3492)
  db.session.add(player_2794)
  db.session.add(player_4208)
  db.session.add(player_4056)
  db.session.add(player_3050)
  db.session.add(player_2800)
  db.session.add(player_3966)
  db.session.add(player_3987)
  db.session.add(player_4044)
  db.session.add(player_4059)
  db.session.add(player_4165)
  db.session.add(player_3956)
  db.session.add(player_832)
  db.session.add(player_4159)
  db.session.add(player_4279)
  db.session.add(player_2451)
  db.session.add(player_3195)
  db.session.add(player_2677)
  db.session.add(player_4231)
  db.session.add(player_4262)
  db.session.add(player_394)
  db.session.add(player_3282)
  db.session.add(player_3984)
  db.session.add(player_3681)
  db.session.add(player_3670)
  db.session.add(player_2490)
  db.session.add(player_4146)
  db.session.add(player_3924)
  db.session.add(player_3103)
  db.session.add(player_4271)
  db.session.add(player_2809)
  db.session.add(player_4096)
  db.session.add(player_3674)
  db.session.add(player_3581)
  db.session.add(player_4221)
  db.session.add(player_3298)
  db.session.add(player_406)
  db.session.add(player_3389)
  db.session.add(player_3944)
  db.session.add(player_3347)
  db.session.add(player_2118)
  db.session.add(player_2092)
  db.session.add(player_3028)
  db.session.add(player_3821)
  db.session.add(player_3422)
  db.session.add(player_3940)
  db.session.add(player_1441)
  db.session.add(player_4351)
  db.session.add(player_4372)
  db.session.add(player_3968)
  db.session.add(player_3158)
  db.session.add(player_4038)
  db.session.add(player_3637)
  db.session.add(player_4156)
  db.session.add(player_4338)
  db.session.add(player_3284)
  db.session.add(player_3888)
  db.session.add(player_3875)
  db.session.add(player_3152)
  db.session.add(player_4329)
  db.session.add(player_4082)
  db.session.add(player_3864)
  db.session.add(player_4060)
  db.session.add(player_4191)
  db.session.add(player_3411)
  db.session.add(player_3772)
  db.session.add(player_4002)
  db.session.add(player_4232)
  db.session.add(player_3086)
  db.session.add(player_4166)
  db.session.add(player_4216)
  db.session.add(player_4358)
  db.session.add(player_4242)
  db.session.add(player_3056)
  db.session.add(player_1937)
  db.session.add(player_4228)
  db.session.add(player_3748)
  db.session.add(player_4184)
  db.session.add(player_1590)
  db.session.add(player_3503)
  db.session.add(player_4052)
  db.session.add(player_3299)
  db.session.add(player_3403)
  db.session.add(player_3160)
  db.session.add(player_2338)
  db.session.add(player_4083)
  db.session.add(player_2979)
  db.session.add(player_3898)
  db.session.add(player_2633)
  db.session.add(player_4378)
  db.session.add(player_3915)
  db.session.add(player_1594)
  db.session.add(player_3962)
  db.session.add(player_3895)
  db.session.add(player_3802)
  db.session.add(player_4039)
  db.session.add(player_4280)
  db.session.add(player_441)
  db.session.add(player_3645)
  db.session.add(player_4080)
  db.session.add(player_4144)
  db.session.add(player_4163)
  db.session.add(player_1895)
  db.session.add(player_2945)
  db.session.add(player_4263)
  db.session.add(player_3902)
  db.session.add(player_4132)
  db.session.add(player_4364)
  db.session.add(player_4367)
  db.session.add(player_3896)
  db.session.add(player_3143)
  db.session.add(player_3918)
  db.session.add(player_3930)
  db.session.add(player_4222)
  db.session.add(player_3969)
  db.session.add(player_4057)
  db.session.add(player_4339)
  db.session.add(player_4086)
  db.session.add(player_3135)
  db.session.add(player_1872)
  db.session.add(player_3232)
  db.session.add(player_1446)
  db.session.add(player_3281)
  db.session.add(player_4379)
  db.session.add(player_3493)
  db.session.add(player_4045)
  db.session.add(player_3702)
  db.session.add(player_4345)
  db.session.add(player_3593)
  db.session.add(player_3830)
  db.session.add(player_4281)
  db.session.add(player_2845)
  db.session.add(player_3559)
  db.session.add(player_3781)
  db.session.add(player_4130)
  db.session.add(player_2437)
  db.session.add(player_2492)
  db.session.add(player_3805)
  db.session.add(player_4252)
  db.session.add(player_2634)
  db.session.add(player_3480)
  db.session.add(player_3270)
  db.session.add(player_4233)
  db.session.add(player_2769)
  db.session.add(player_4087)
  db.session.add(player_3087)
  db.session.add(player_4210)
  db.session.add(player_3330)
  db.session.add(player_4229)
  db.session.add(player_4236)
  db.session.add(player_4352)
  db.session.add(player_3618)
  db.session.add(player_3307)
  db.session.add(player_3953)
  db.session.add(player_3876)
  db.session.add(player_4253)
  db.session.add(player_4188)
  db.session.add(player_3903)
  db.session.add(player_3949)
  db.session.add(player_3228)
  db.session.add(player_3162)
  db.session.add(player_3603)
  db.session.add(player_3946)
  db.session.add(player_4153)
  db.session.add(player_3844)
  db.session.add(player_3931)
  db.session.add(player_3749)
  db.session.add(player_4017)
  db.session.add(player_2622)
  db.session.add(player_4032)
  db.session.add(player_4308)
  db.session.add(player_3328)
  db.session.add(player_3080)
  db.session.add(player_3612)
  db.session.add(player_3660)
  db.session.add(player_3989)
  db.session.add(player_4290)
  db.session.add(player_4026)
  db.session.add(player_3459)
  db.session.add(player_2761)
  db.session.add(player_3965)
  db.session.add(player_4321)
  db.session.add(player_4202)
  db.session.add(player_2737)
  db.session.add(player_3409)
  db.session.add(player_4330)
  db.session.add(player_3429)
  db.session.add(player_2328)
  db.session.add(player_3498)
  db.session.add(player_3035)
  db.session.add(player_4380)
  db.session.add(player_4303)
  db.session.add(player_2774)
  db.session.add(player_3594)
  db.session.add(player_4254)
  db.session.add(player_3682)
  db.session.add(player_3853)
  db.session.add(player_4176)
  db.session.add(player_4003)
  db.session.add(player_4282)
  db.session.add(player_3782)
  db.session.add(player_3714)
  db.session.add(player_4291)
  db.session.add(player_3635)
  db.session.add(player_3656)
  db.session.add(player_4072)
  db.session.add(player_3308)
  db.session.add(player_4131)
  db.session.add(player_4243)
  db.session.add(player_3890)
  db.session.add(player_3560)
  db.session.add(player_3998)
  db.session.add(player_2537)
  db.session.add(player_3611)
  db.session.add(player_3922)
  db.session.add(player_4192)
  db.session.add(player_1166)
  db.session.add(player_2508)
  db.session.add(player_2635)
  db.session.add(player_3057)
  db.session.add(player_3108)
  db.session.add(player_4203)
  db.session.add(player_3331)
  db.session.add(player_3811)
  db.session.add(player_4340)
  db.session.add(player_4353)
  db.session.add(player_4134)
  db.session.add(player_3381)
  db.session.add(player_3899)
  db.session.add(player_1168)
  db.session.add(player_1875)
  db.session.add(player_4088)
  db.session.add(player_4244)
  db.session.add(player_3651)
  db.session.add(player_3499)
  db.session.add(player_3769)
  db.session.add(player_3113)
  db.session.add(player_4234)
  db.session.add(player_4177)
  db.session.add(player_3042)
  db.session.add(player_4048)
  db.session.add(player_3734)
  db.session.add(player_3957)
  db.session.add(player_4327)
  db.session.add(player_3703)
  db.session.add(player_3878)
  db.session.add(player_537)
  db.session.add(player_3869)
  db.session.add(player_3617)
  db.session.add(player_3967)
  db.session.add(player_2740)
  db.session.add(player_3800)
  db.session.add(player_3340)
  db.session.add(player_2571)
  db.session.add(player_2697)
  db.session.add(player_3661)
  db.session.add(player_4316)
  db.session.add(player_2388)
  db.session.add(player_4272)
  db.session.add(player_4273)
  db.session.add(player_3291)
  db.session.add(player_3654)
  db.session.add(player_4217)
  db.session.add(player_1170)
  db.session.add(player_4102)
  db.session.add(player_3374)
  db.session.add(player_3323)
  db.session.add(player_2330)
  db.session.add(player_3119)
  db.session.add(player_860)
  db.session.add(player_4193)
  db.session.add(player_2496)
  db.session.add(player_3975)
  db.session.add(player_3983)
  db.session.add(player_3990)
  db.session.add(player_3529)
  db.session.add(player_3100)
  db.session.add(player_3744)
  db.session.add(player_3904)
  db.session.add(player_3662)
  db.session.add(player_3812)
  db.session.add(player_4211)
  db.session.add(player_4309)
  db.session.add(player_4067)
  db.session.add(player_3487)
  db.session.add(player_4255)
  db.session.add(player_3602)
  db.session.add(player_4296)
  db.session.add(player_4218)
  db.session.add(player_2432)
  db.session.add(player_3678)
  db.session.add(player_3801)
  db.session.add(player_4012)
  db.session.add(player_3972)
  db.session.add(player_4019)
  db.session.add(player_4377)
  db.session.add(player_3369)
  db.session.add(player_2837)
  db.session.add(player_3430)
  db.session.add(player_4235)
  db.session.add(player_2787)
  db.session.add(player_3973)
  db.session.add(player_3412)
  db.session.add(player_4346)
  db.session.add(player_3842)
  db.session.add(player_2920)
  db.session.add(player_3963)
  db.session.add(player_3316)
  db.session.add(player_3320)
  db.session.add(player_4347)
  db.session.add(player_4027)
  db.session.add(player_3630)
  db.session.add(player_2501)
  db.session.add(player_3658)
  db.session.add(player_3883)
  db.session.add(player_4283)
  db.session.add(player_2122)
  db.session.add(player_4223)
  db.session.add(player_4007)
  db.session.add(player_4078)
  db.session.add(player_4370)
  db.session.add(player_3605)
  db.session.add(player_3043)
  db.session.add(player_3616)
  db.session.add(player_3363)
  db.session.add(player_3235)
  db.session.add(player_3615)
  db.session.add(player_3566)
  db.session.add(player_4149)
  db.session.add(player_3553)
  db.session.add(player_3721)
  db.session.add(player_3530)
  db.session.add(player_3950)
  db.session.add(player_4256)
  db.session.add(player_4091)
  db.session.add(player_2767)
  db.session.add(player_4371)
  db.session.add(player_4013)
  db.session.add(player_3099)
  db.session.add(player_4237)
  db.session.add(player_2776)
  db.session.add(player_2681)
  db.session.add(player_3210)
  db.session.add(player_4292)
  db.session.add(player_2113)
  db.session.add(player_3414)
  db.session.add(player_3000)
  db.session.add(player_3555)
  db.session.add(player_4167)
  db.session.add(player_4313)
  db.session.add(player_4040)
  db.session.add(player_4194)
  db.session.add(player_2474)
  db.session.add(player_3722)
  db.session.add(player_3309)
  db.session.add(player_3641)
  db.session.add(player_4033)
  db.session.add(player_1825)
  db.session.add(player_3436)
  db.session.add(player_4127)
  db.session.add(player_3663)
  db.session.add(player_3974)
  db.session.add(player_872)
  db.session.add(player_3472)
  db.session.add(player_3460)
  db.session.add(player_4341)
  db.session.add(player_4173)
  db.session.add(player_3085)
  db.session.add(player_3696)
  db.session.add(player_4053)
  db.session.add(player_3648)
  db.session.add(player_2364)
  db.session.add(player_3646)
  db.session.add(player_2587)
  db.session.add(player_2279)
  db.session.add(player_4342)
  db.session.add(player_3240)
  db.session.add(player_3296)
  db.session.add(player_2173)
  db.session.add(player_3562)
  db.session.add(player_3884)
  db.session.add(player_2249)
  db.session.add(player_3405)
  db.session.add(player_3885)
  db.session.add(player_3764)
  db.session.add(player_3638)
  db.session.add(player_3919)
  db.session.add(player_3578)
  db.session.add(player_4182)
  db.session.add(player_3584)
  db.session.add(player_1187)
  db.session.add(player_3823)
  db.session.add(player_1463)
  db.session.add(player_4331)
  db.session.add(player_2342)
  db.session.add(player_3254)
  db.session.add(player_4323)
  db.session.add(player_2466)
  db.session.add(player_1189)
  db.session.add(player_4264)
  db.session.add(player_649)
  db.session.add(player_2197)
  db.session.add(player_3992)
  db.session.add(player_3075)
  db.session.add(player_3063)
  db.session.add(player_4061)
  db.session.add(player_4020)
  db.session.add(player_3627)
  db.session.add(player_4073)
  db.session.add(player_2752)
  db.session.add(player_3076)
  db.session.add(player_3420)
  db.session.add(player_2389)
  db.session.add(player_3925)
  db.session.add(player_3404)
  db.session.add(player_3201)
  db.session.add(player_3115)
  db.session.add(player_4284)
  db.session.add(player_4041)
  db.session.add(player_4257)
  db.session.add(player_3390)
  db.session.add(player_3457)
  db.session.add(player_4348)
  db.session.add(player_3839)
  db.session.add(player_3597)
  db.session.add(player_3625)
  db.session.add(player_2785)
  db.session.add(player_3481)
  db.session.add(player_4209)
  db.session.add(player_4098)
  db.session.add(player_4069)
  db.session.add(player_4150)
  db.session.add(player_3758)
  db.session.add(player_2198)
  db.session.add(player_3324)
  db.session.add(player_4170)
  db.session.add(player_3857)
  db.session.add(player_2779)
  db.session.add(player_2897)
  db.session.add(player_2867)
  db.session.add(player_3287)
  db.session.add(player_2846)
  db.session.add(player_668)
  db.session.add(player_4143)
  db.session.add(player_4274)
  db.session.add(player_3945)
  db.session.add(player_2724)
  db.session.add(player_4212)
  db.session.add(player_2242)
  db.session.add(player_3750)
  db.session.add(player_4204)
  db.session.add(player_4118)
  db.session.add(player_3891)
  db.session.add(player_4224)
  db.session.add(player_3563)
  db.session.add(player_3964)
  db.session.add(player_3926)
  db.session.add(player_2240)
  db.session.add(player_3336)
  db.session.add(player_2734)
  db.session.add(player_2755)
  db.session.add(player_4157)
  db.session.add(player_3938)
  db.session.add(player_684)
  db.session.add(player_4093)
  db.session.add(player_4161)
  db.session.add(player_3246)
  db.session.add(player_4354)
  db.session.add(player_2795)
  db.session.add(player_3787)
  db.session.add(player_4042)
  db.session.add(player_2181)
  db.session.add(player_4355)
  db.session.add(player_4359)
  db.session.add(player_4246)
  db.session.add(player_3348)
  db.session.add(player_2600)
  db.session.add(player_1467)
  db.session.add(player_3914)
  db.session.add(player_3378)
  db.session.add(player_4021)
  db.session.add(player_3332)
  db.session.add(player_3631)
  db.session.add(player_3775)
  db.session.add(player_3504)
  db.session.add(player_3345)
  db.session.add(player_3375)
  db.session.add(player_3900)
  db.session.add(player_1468)
  db.session.add(player_3932)
  db.session.add(player_3621)
  db.session.add(player_3993)
  db.session.add(player_3303)
  db.session.add(player_4328)
  db.session.add(player_3928)
  db.session.add(player_4361)
  db.session.add(player_1469)
  db.session.add(player_4360)
  db.session.add(player_2741)
  db.session.add(player_3858)
  db.session.add(player_4205)
  db.session.add(player_3666)
  db.session.add(player_3675)
  db.session.add(player_2520)
  db.session.add(player_3554)
  db.session.add(player_4219)
  db.session.add(player_2375)
  db.session.add(player_2903)
  db.session.add(player_3522)
  db.session.add(player_4179)
  db.session.add(player_3058)
  db.session.add(player_2780)
  db.session.add(player_3288)
  db.session.add(player_3071)
  db.session.add(player_3738)
  db.session.add(player_2775)
  db.session.add(player_3934)
  db.session.add(player_3865)
  db.session.add(player_3216)
  db.session.add(player_4304)
  db.session.add(player_4297)
  db.session.add(player_2777)
  db.session.add(player_2251)
  db.session.add(player_3897)
  db.session.add(player_733)
  db.session.add(player_4265)
  db.session.add(player_4293)
  db.session.add(player_3813)
  db.session.add(player_4375)
  db.session.add(player_3833)
  db.session.add(player_4141)
  db.session.add(player_3803)
  db.session.add(player_1685)
  db.session.add(player_4185)
  db.session.add(player_4332)
  db.session.add(player_2617)
  db.session.add(player_3198)
  db.session.add(player_1930)
  db.session.add(player_3383)
  db.session.add(player_3664)
  db.session.add(player_2528)
  db.session.add(player_747)
  db.session.add(player_4238)
  db.session.add(player_3333)
  db.session.add(player_3269)
  db.session.add(player_3575)
  db.session.add(player_751)
  db.session.add(player_1687)
  db.session.add(player_4100)
  db.session.add(player_1031)
  db.session.add(player_3337)
  db.session.add(player_752)
  db.session.add(player_753)
  db.session.add(player_4137)
  db.session.add(player_758)
  db.session.add(player_2124)
  db.session.add(player_3685)
  db.session.add(player_3395)
  db.session.add(player_2924)
  db.session.add(player_3190)
  db.session.add(player_4138)
  db.session.add(player_2154)
  db.session.add(player_2309)
  db.session.add(player_4349)
  db.session.add(player_3960)
  db.session.add(player_2349)
  db.session.add(player_3018)
  db.session.add(player_2626)
  db.session.add(player_3723)
  db.session.add(player_769)
  db.session.add(player_4195)
  db.session.add(player_3241)
  db.session.add(player_3622)
  db.session.add(player_2502)
  db.session.add(player_3916)
  db.session.add(player_4285)
  db.session.add(player_4120)
  db.session.add(player_893)
  db.session.add(player_2079)
  db.session.add(player_4122)
  db.session.add(player_4125)
  db.session.add(player_4294)
  db.session.add(player_4376)
  db.session.add(player_1865)
  db.session.add(player_1057)
  db.session.add(player_1050)
  db.session.add(player_1049)
  db.session.add(player_1059)
  db.session.add(player_1047)
  db.session.add(player_1061)
  db.session.add(player_1060)
  db.session.add(player_1045)
  db.session.add(player_1054)
  db.session.add(player_1064)
  db.session.add(player_1051)
  db.session.add(player_1039)
  db.session.add(player_1053)
  db.session.add(player_1043)
  db.session.add(player_1041)
  db.session.add(player_1046)
  db.session.add(player_1058)
  db.session.add(player_1055)
  db.session.add(player_1052)
  db.session.add(player_1062)
  db.session.add(player_1065)
  db.session.add(player_1048)
  db.session.add(player_1066)
  db.session.add(player_1067)
  db.session.add(player_1038)
  db.session.add(player_1056)
  db.session.add(player_1037)
  db.session.add(player_1063)
  db.session.add(player_1044)
  db.session.add(player_1040)
  db.session.add(player_1036)
  db.session.add(player_1042)
  db.session.commit()

  ffsplayer_1 = FFSplayer(player_id = 13, team_id = 1, league_id = 1)
  ffsplayer_2 = FFSplayer(player_id = 3379, team_id = 1, league_id = 1)
  ffsplayer_3 = FFSplayer(player_id = 14, team_id = 2, league_id = 1)
  ffsplayer_4 = FFSplayer(player_id = 3354, team_id = 1, league_id = 1)
  ffsplayer_5 = FFSplayer(player_id = 2338, team_id = 2, league_id = 1)
  ffsplayer_6 = FFSplayer(player_id = 1446, team_id = 2, league_id = 1)
  ffsplayer_7 = FFSplayer(player_id = 2596, team_id = 1, league_id = 1)
  ffsplayer_8 = FFSplayer(player_id = 2198, team_id = 1, league_id = 1)
  ffsplayer_9 = FFSplayer(player_id = 1189, team_id = 2, league_id = 1)
  ffsplayer_10 = FFSplayer(player_id = 2079, team_id = 1, league_id = 1)
  ffsplayer_11 = FFSplayer(player_id = 769, team_id = 2, league_id = 1)
  ffsplayer_12 = FFSplayer(player_id = 1037, team_id = 1, league_id = 1)
  ffsplayer_13 = FFSplayer(player_id = 1038, team_id = 2, league_id = 1)

  db.session.add(ffsplayer_1)
  db.session.add(ffsplayer_2)
  db.session.add(ffsplayer_3)
  db.session.add(ffsplayer_4)
  db.session.add(ffsplayer_5)
  db.session.add(ffsplayer_6)
  db.session.add(ffsplayer_7)
  db.session.add(ffsplayer_8)
  db.session.add(ffsplayer_9)
  db.session.add(ffsplayer_10)
  db.session.add(ffsplayer_11)
  db.session.add(ffsplayer_12)
  db.session.add(ffsplayer_13)
  db.session.commit()

  # Spot for players' seeders

  # Spot for ffsplayers' seeders

  db.session.add(ian)
  db.session.add(javier)
  db.session.add(dean)
  db.session.add(angela)
  db.session.add(soonmi)
  db.session.add(alissa)


  db.session.add(ian_league)
  db.session.add(javier_league)
  db.session.commit()

  db.session.add(ian_team)
  db.session.add(javier_team)
  db.session.add(angela_team)
  db.session.commit()


  db.session.commit()
  ffsplayer_1 = FFSplayer(player_id = 13, team_id = 1, league_id = 1)
  ffsplayer_2 = FFSplayer(player_id = 3379, team_id = 1, league_id = 1)
  ffsplayer_3 = FFSplayer(player_id = 14, team_id = 2, league_id = 1)
  ffsplayer_4 = FFSplayer(player_id = 3354, team_id = 1, league_id = 1)
  ffsplayer_5 = FFSplayer(player_id = 2338, team_id = 2, league_id = 1)
  ffsplayer_6 = FFSplayer(player_id = 1446, team_id = 2, league_id = 1)
  ffsplayer_7 = FFSplayer(player_id = 2596, team_id = 1, league_id = 1)
  ffsplayer_8 = FFSplayer(player_id = 2198, team_id = 1, league_id = 1)
  ffsplayer_9 = FFSplayer(player_id = 1189, team_id = 2, league_id = 1)
  ffsplayer_10 = FFSplayer(player_id = 2079, team_id = 1, league_id = 1)
  ffsplayer_11 = FFSplayer(player_id = 769, team_id = 2, league_id = 1)
  ffsplayer_12 = FFSplayer(player_id = 1037, team_id = 1, league_id = 1)
  ffsplayer_13 = FFSplayer(player_id = 1038, team_id = 2, league_id = 1)

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
