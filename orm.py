from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class EventExplain(Base):
  __tablename__ = "EventsExplain"
  id = Column(Integer, primary_key=True, autoincrement=True)
  minutes_played = Column(Integer, nullable=True)
  col2 = Column(Integer, nullable=True)
  col3 = Column(Integer, nullable=True)
  player_id = Column(Integer, ForeignKey('Players.id'))

class Fixture(Base):
  __tablename__ = "Fixtures"
  id = Column(Integer, primary_key=True, autoincrement=True)
  date_time = Column(DateTime, nullable=False)
  gameweek = Column(Integer, nullable=False)
  is_homegame = Column(Boolean, nullable=False)
  opponent_team_id = Column(Integer, ForeignKey('Teams.id'))
  player_id = Column(Integer, ForeignKey('Players.id')) 


class FixtureHistory(Base):
  __tablename__ = "FixturesHistory"
  id = Column(Integer, primary_key=True, autoincrement=True)
  player_id = Column(Integer, nullable=True)
  fixture_date = Column(String(50), nullable=False)
  game_week = Column(Integer, nullable=True)
  result = Column(String(50), nullable=False)
  minutes_played = Column(Integer, nullable=True)
  goals_scored = Column(Integer, nullable=True)
  assists = Column(Integer, nullable=True)
  clean_sheets = Column(Integer, nullable=True)
  goals_conceded = Column(Integer, nullable=True)
  own_goals = Column(Integer, nullable=True)
  penalties_saved = Column(Integer, nullable=True)
  penalties_missed = Column(Integer, nullable=True)
  yellow_cards = Column(Integer, nullable=True)
  red_cards = Column(Integer, nullable=True)
  saves = Column(Integer, nullable=True)
  bonus = Column(Integer, nullable=True)
  ea_sports_ppi = Column(Integer, nullable=True)
  bonuses_points_system = Column(Integer, nullable=True)
  net_transfers = Column(Integer, nullable=True)
  value = Column(Integer, nullable=True)
  points = Column(Integer, nullable=True)
  player_id = Column(Integer, ForeignKey('Players.id')) 

class Player(Base):
  __tablename__ = "Players"
  id = Column(Integer, primary_key=True)
  transfers_out = Column(Integer, nullable=True)
  code = Column(Integer, nullable=True)
  event_total = Column(Integer, nullable=True)
  last_season_points= Column(Integer, nullable=True)
  squad_number= Column(Integer, nullable=True)
  news_updated= Column(Integer, nullable=True)
  event_cost= Column(Integer, nullable=True)
  news_added= Column(Integer, nullable=True)
  web_name= Column(String(50), nullable=True)
  in_dreamteam= Column(Integer, nullable=True)
  team_code= Column(Integer, nullable=True)
  shirt_image_url= Column(String(250), nullable=True)
  first_name= Column(String(50), nullable=True)
  transfers_out_event= Column(Integer, nullable=True)
  element_type_id= Column(Integer, nullable=True)
  max_cost= Column(Integer, nullable=True)
  # event_explain_id= Column(Integer, nullable=True)
  selected_total= Column(Integer, nullable=True)
  min_cost= Column(Integer, nullable=True)
  # fixture_id= Column(Integer, nullable=True)
  # season_history_id= Column(Integer, nullable=True)
  total_points= Column(Integer, nullable=True)
  position_id= Column(Integer, nullable=True)
  team_id= Column(Integer, nullable=True)
  status_id= Column(Integer, nullable=True)
  added= Column(String(100), nullable=True)
  form = Column(Float, nullable=True)
  shirt_mobile_image_url= Column(String(250), nullable=True)
  current_fixture= Column(Integer, nullable=True)
  now_cost= Column(Integer, nullable=True)
  points_per_game  = Column(Float, nullable=True)
  transfers_in= Column(Integer, nullable=True)
  news= Column(String(500), nullable=True)
  original_cost= Column(Integer, nullable=True)
  event_points= Column(Integer, nullable=True)
  news_return= Column(String(500), nullable=True)
  # fixture_history_id= Column(Integer, nullable=True)
  next_fixture= Column(Integer, nullable=True)
  transfers_in_event= Column(Integer, nullable=True)
  selected_by  = Column(Float, nullable=True)
  last_name= Column(String(50), nullable=True)
  photo_mobile_url= Column(String(250), nullable=True)

# Don't think I need these inverse relationships
  # event_explain_id = Column(Integer, ForeignKey('EventsExplain.id'))
  # event_explains = relationship("EventsExplain", order_by="EventsExplain.id", backref=backref('Players', order_by=id))
  # fixture_id = Column(Integer, ForeignKey('Fixtures.id'))
  # fixture = relationship("Fixture", backref="player")

class Position(Base):
  __tablename__ = "Positions"
  id = Column(Integer, primary_key=True)
  name = Column(String(50), nullable=False)
  short_name = Column(String(4), nullable=False)

class SeasonHistory(Base):
  __tablename__ = "SeasonsHistory"
  id = Column(Integer, primary_key=True, autoincrement=True)
  season = Column(String(10), nullable=False)
  minutes_played = Column(Integer, nullable=True)
  goals_scored = Column(Integer, nullable=True)
  assists = Column(Integer, nullable=True)
  clean_sheets = Column(Integer, nullable=True)
  goals_conceded = Column(Integer, nullable=True)
  own_goals = Column(Integer, nullable=True)
  penalties_saved = Column(Integer, nullable=True)
  penalties_missed = Column(Integer, nullable=True)
  yellow_cards = Column(Integer, nullable=True)
  red_cards = Column(Integer, nullable=True)
  saves = Column(Integer, nullable=True)
  bonus = Column(Integer, nullable=True)
  ea_sports_ppi = Column(Integer, nullable=True)
  # bonuses_points_system = Column(Integer, nullable=True)
  net_transfers = Column(Integer, nullable=True)
  value = Column(Integer, nullable=True)
  points = Column(Integer, nullable=True)
  player_id = Column(Integer, nullable=True)
  player_id = Column(Integer, ForeignKey('Players.id')) 

class Teams(Base):
	__tablename__ = "Teams"
	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	short_name = Column(String(4), nullable=False)



# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)