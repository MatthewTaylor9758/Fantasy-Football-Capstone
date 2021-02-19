# FFStockpile
*By Matt Taylor*
## Table of Contents 
- [FFStockpile Overview](#ffstockpile-overview)
- [Application Architecture and Technologies Involved](#application-architecture)
- [Front End Overview](#front-end-overview)
- [Back End Overview](#back-end-overview)
- [Moving Forward](#moving-forward)
## FFStockpile Overview
FFStockpile is a site that is meant for passionate fantasy football fans. It is made to be a one stop shop for all the data you can need to make informed decisions when selecting players to draft, pick up on waivers, and just do general research on.
</br>
</br>
The front end was built using HTML, CSS, Material-UI, React, and Redux, while the back end was developed using Flask, SQLAlchemy, Alembic and PostgreSQL.
</br>
</br>
Users can see their own team, the league they are in, the available players to pick up in their league and some stats as well.
</br>
</br>
![](https://media.giphy.com/media/Q2AqJPRb2qUgLIBoJ6/giphy.gif)
</br>
</br>
## Application Architecture
![FFStockpile Architecture](https://raw.githubusercontent.com/MatthewTaylor9758/Fantasy-Football-Capstone/main/flask_react_starter/client/src/images/FFStockpile%20Architecture.png)
</br>
</br>
## Front End Overview
### React
React components are used throughout the site to provide a seamless UX, whether that be navigating from your team page to the available players page, selecting the position of the players you want to look at, dropping and adding players etc.</br>
</br>
### Redux
Redux, react-redux, and redux-thunk are the foundation that manage the application's state, and provide requests and responses between the React front end and the Flask based back end.
</br>
</br>
In most instances, the front end will react to a change the user makes and send that change to Redux. From there Redux will update its store and then send that information to the Flask based server. Since the Redux store has the information on the change that was made, the Redux store will persist the data between refreshes just as designed.
</br>
</br>
### Material-UI
Material-UI was chosen because mainly because of its built in functions and models. It has many models that can be used, but not only that, you can build on those models to create a custom look with the base that Material-UI gave you. It is very handy, and made my design much more efficient and elegant.
</br>
</br>
## Back End Overview
### Flask
I decided to use the Flask framework for its intuitive approach to creating a server. Flask interacts with SQLAlchemy, PostgreSQL and Alembic seamlessly and helped streamline my interactions with the database in all facets.
</br>
</br>
### PostgreSQL
I leveraged PostgreSQL's ability to use different transactions, foreign keys, subqueries, triggers, and different user-defined types and functions to create my site. Flask, SQLAlchemy and PostgreSQL work together to make my database construction, alterations, and interactions smoother.
</br>
</br>
### SQLAlchemy
I chose the SQLAlchemy ORM for its ease of mapping, its far superior readability when compared to other ORMs, and the intuitive nature with which you can create models. When combined with my other back end technologies, it makes for a fantastic experience. Oh, and SQLAlchemy has amazing documentation so that always helps!
</br>
</br>
### Alembic
I landed on Alembic naturally, being so close to SQLAlchemy, and I thrived using its almost instinctual method of creating migrations and interacting with SQLAlchemy to make the necessary changes to my database.
</br>
```
class Team(db.Model):
  __tablename__ = 'teams'
  __table_args__ = (
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


class Player(db.Model):
  __tablename__ = 'players'

  player_id = db.Column(db.Integer, nullable= False, primary_key = True, autoincrement = False)
  full_name = db.Column(db.String(100), nullable = False)
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
      'player_id': self.player_id,
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
    UniqueConstraint('player_id', 'league_id', name='player_in_league_only_once_uidx'),
  )
  id = db.Column(db.Integer, nullable = False,  primary_key = True)
  player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable = False)
  team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = False)
  league_id = db.Column(db.Integer, nullable = False)

  def to_dict(self):
    return {
      'id': self.id,
      'player_id': self.player_id,
      'team_id': self.team_id,
      'league_id': self.league_id
    }
```
The code above contains some of the models I used in creating FFStockpile. This specific code takes advantage of the abilities of Flask and SQLAlchemy to easily interact with the PostgreSQL based database. In the Players model there is just the normal set up of a model that will be used for all of the players in the NFL, in the other two however, there are not just column constraints, but table constraints. One is essentially used to make sure that no player can be in a single league more than once, but can appear in different leagues. The other is used to make sure that the a team cannot appear in a league more than once, but can appear in different leagues. 

## Moving Forward
The first and biggest thing I would like to do next is to give more stats to each player, however those APIs cost hundreds and sometimes even thousands of dollars to gain access to. If I find a work around in the future though, that will be the first thing I do. Next would be to add some more stylistic flare to the site, and finally I would love the ability to host real simulated matchups and maybe real-time access to NFL box scores.

### Thank You

I sincerely apprectiate the time you have taken out of your day to read this far and parse through the site I had a ton of fun making! Creating this site from the ground up was a very rewarding experience and I cannot wait to work on it in the future!

### Credits:

<ul>
  <li>Gifs: Giphy.com</li>
  <li>Architecture Diagram is courtesy of https://app.diagrams.net/</li> 
</ul>
