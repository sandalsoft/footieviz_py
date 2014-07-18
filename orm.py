from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class News(Base):
  __tablename__ = "news"
  id = Column(Integer, primary_key=True, autoincrement=True)
  news_added = Column(DateTime, nullable=True)
  news_updated = Column(DateTime, nullable=True)
  news_return = Column(DateTime, nullable=True)
  news = Column(String(50), nullable=True)
  created_at = Column(DateTime, nullable=False)
  player_id = Column(Integer, ForeignKey('players.id'))


class EventExplain(Base):
  __tablename__ = "eventsexplain"
  id = Column(Integer, primary_key=True, autoincrement=True)
  minutes_played = Column(Integer, nullable=True)
  col2 = Column(Integer, nullable=True)
  col3 = Column(Integer, nullable=True)
  created_at = Column(DateTime, nullable=False)
  player_id = Column(Integer, ForeignKey('players.id'))


class Fixture(Base):
  __tablename__ = "fixtures"
  id = Column(Integer, primary_key=True, autoincrement=True)
  date_time = Column(DateTime, nullable=False)
  gameweek = Column(Integer, nullable=False)
  is_homegame = Column(Boolean, nullable=False)
  created_at = Column(DateTime, nullable=False)
  opponent_team_id = Column(Integer, ForeignKey('teams.id'))
  player_id = Column(Integer, ForeignKey('players.id'))


class FixtureHistory(Base):
  __tablename__ = "fixtureshistory"
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
  created_at = Column(DateTime, nullable=False)
  opponent_team_id = Column(Integer, ForeignKey('teams.id'))
  match_points = Column(Integer, nullable=False)
  player_id = Column(Integer, ForeignKey('players.id'))


class Player(Base):
  __tablename__ = "players"
  id = Column(Integer, primary_key=True)
  photo = Column(String(100), nullable=False)
  event_explain = Column(Integer, ForeignKey('eventsexplain.id'))
  fixture_history = Column(Integer, ForeignKey('fixtureshistory.id'))
  season_history = Column(Integer, ForeignKey('seasonshistory.id'))
  fixtures = Column(Integer, ForeignKey('fixtures.id'))
  event_total = Column(Integer, nullable=False)
  type_name = Column(String(100), nullable=False)
  team_name = Column(String(100), nullable=True)
  selected_by = Column(Float, nullable=True)
  total_points = Column(Integer, nullable=False)
  current_fixture = Column(String(30), nullable=True)
  next_fixture = Column(String(100), nullable=True)
  team_code = Column(Integer, nullable=False)
  news = Column(Integer, ForeignKey('news.id'))
  team_id = Column(Integer, nullable=False)
  status = Column(String(100), nullable=False)
  code = Column(Integer, nullable=False)
  first_name = Column(String(100), nullable=False)
  second_name = Column(String(100), nullable=True)
  web_name = Column(String(100), nullable=True)
  now_cost = Column(Integer, nullable=False)
  chance_of_playing_this_round = Column(String(100), nullable=False)
  chance_of_playing_next_round = Column(String(100), nullable=False)
  value_form = Column(Float, nullable=True)
  value_season = Column(Float, nullable=True)
  cost_change_start = Column(Integer, nullable=False)
  cost_change_event = Column(Integer, nullable=False)
  cost_change_start_fall = Column(Integer, nullable=False)
  cost_change_event_fall = Column(Integer, nullable=False)
  in_dreamteam = Column(Boolean, nullable=False)
  dreamteam_count = Column(Integer, nullable=False)
  selected_by_percent = Column(Float, nullable=False)
  form = Column(Float, nullable=False)
  transfers_out = Column(Integer, nullable=False)
  transfers_in = Column(Integer, nullable=False)
  transfers_out_event = Column(Integer, nullable=False)
  transfers_in_event = Column(Integer, nullable=False)
  event_points = Column(Integer, nullable=False)
  points_per_game = Column(Float, nullable=True)
  ep_this = Column(Float, nullable=True)
  ep_next = Column(Float, nullable=True)
  special = Column(Boolean, nullable=False)
  minutes = Column(Integer, nullable=False)
  goals_scored = Column(Integer, nullable=False)
  assists = Column(Integer, nullable=False)
  clean_sheets = Column(Integer, nullable=False)
  goals_conceded = Column(Integer, nullable=False)
  own_goals = Column(Integer, nullable=False)
  penalties_saved = Column(Integer, nullable=False)
  penalties_missed = Column(Integer, nullable=False)
  yellow_cards = Column(Integer, nullable=False)
  red_cards = Column(Integer, nullable=False)
  saves = Column(Integer, nullable=False)
  bonus = Column(Integer, nullable=False)
  ea_index = Column(Integer, nullable=False)
  bps = Column(Integer, nullable=False)
  element_type = Column(Integer, nullable=False)
  team = Column(Integer, nullable=False)
  current_fixture_is_home = Column(Boolean, nullable=False)
  current_fixture_team_id = Column(Integer, ForeignKey('teams.id'))
  created_at = Column(DateTime, nullable=False)
  

class SeasonHistory(Base):
  __tablename__ = "seasonshistory"
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
  created_at = Column(DateTime, nullable=False)
  player_id = Column(Integer, ForeignKey('players.id'))


class Position(Base):
  __tablename__ = "positions"
  id = Column(Integer, primary_key=True)
  name = Column(String(50), nullable=False)
  short_name = Column(String(4), nullable=False)


class Teams(Base):
  __tablename__ = "teams"
  id = Column(Integer, primary_key=True)
  api_name = Column(String(50), nullable=False)
  name = Column(String(50), nullable=False)
  short_name = Column(String(4), nullable=False)


class Status(Base):
  __tablename__ = "statuses"
  id = Column(Integer, primary_key=True)
  status = Column(String(), nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# Base.metadata.create_all(engine)
