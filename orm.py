from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class EventExplain(Base):
  __tablename__ = "EventsExplain"
  id = Column(Integer, primary_key=True)
  minutes_played = Column(Integer, nullable=True)
  col2 = Column(Integer, nullable=True)
  col3 = Column(Integer, nullable=True)
  player_id = Column(Integer, ForeignKey('Players.id'))

class Fixture(Base):
  __tablename__ = "Fixtures"
  id = Column(Integer, primary_key=True)
  date_time = Column(DateTime, nullable=False)
  gameweek = Column(Integer, nullable=False)
  is_homegame = Column(Boolean, nullable=False)
  opponent_team_id = Column(Integer, ForeignKey('Teams.id'))
  player_id = Column(Integer, ForeignKey('Players.id')) 


class FixtureHistory(Base):
  __tablename__ = "FixturesHistory"
  id = Column(Integer, primary_key=True)
  player_id = Column(Integer, nullable=True)
  date_text = Column(String(50), nullable=False)
  gameweek = Column(Integer, nullable=True)
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
  transfers_out = Column(Integer, nullable=False)
  code = Column(Integer, nullable=False)
  event_total = Column(Integer, nullable=False)
  last_season_points= Column(Integer, nullable=False)
  squad_number= Column(Integer, nullable=False)
  news_updated= Column(Integer, nullable=False)
  event_cost= Column(Integer, nullable=False)
  news_added= Column(Integer, nullable=False)
  web_name= Column(String(50), nullable=False)
  in_dreamteam= Column(Integer, nullable=False)
  team_code= Column(Integer, nullable=False)
  shirt_image_url= Column(String(250), nullable=False)
  first_name= Column(String(50), nullable=False)
  transfers_out_event= Column(Integer, nullable=False)
  element_type_id= Column(Integer, nullable=False)
  max_cost= Column(Integer, nullable=False)
  event_explain_id= Column(Integer, nullable=False)
  selected_total= Column(Integer, nullable=False)
  min_cost= Column(Integer, nullable=False)
  fixture_id= Column(Integer, nullable=False)
  season_history_id= Column(Integer, nullable=False)
  total_points= Column(Integer, nullable=False)
  position_id= Column(Integer, nullable=False)
  team_id= Column(Integer, nullable=False)
  status_id= Column(Integer, nullable=False)
  added= Column(String(100), nullable=False)
  form = Column(Float, nullable=False)
  shirt_mobile_image_url= Column(String(250), nullable=False)
  current_fixture= Column(Integer, nullable=False)
  now_cost= Column(Integer, nullable=False)
  points_per_game  = Column(Float, nullable=False)
  transfers_in= Column(Integer, nullable=False)
  news= Column(String(500), nullable=False)
  original_cost= Column(Integer, nullable=False)
  event_points= Column(Integer, nullable=False)
  news_return= Column(String(500), nullable=False)
  fixture_history_id= Column(Integer, nullable=False)
  next_fixture= Column(Integer, nullable=False)
  transfers_in_event= Column(Integer, nullable=False)
  selected_by  = Column(Float, nullable=False)
  last_name= Column(String(50), nullable=False)
  phone_mobile_url= Column(String(250), nullable=False)

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
  id = Column(Integer, primary_key=True)
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
  bonuses_points_system = Column(Integer, nullable=True)
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