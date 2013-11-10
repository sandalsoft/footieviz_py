-- generated by dbdsgnr.appspot.com

CREATE TABLE EventsExplain (
  id INTEGER PRIMARY KEY,
  mins_played TEXT,
  col2 INTEGER,
  col3 INTEGER
);

CREATE TABLE Fixtures (
  id INTEGER PRIMARY KEY,
  date_time TEXT,
  gameweek INTEGER
);

CREATE TABLE Teams (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE SeasonsHistory (
  id INTEGER PRIMARY KEY,
  season_name TEXT
);

CREATE TABLE Statuses (
  id INTEGER PRIMARY KEY,
  status TEXT
);

CREATE TABLE Positions (
  id INTEGER PRIMARY KEY,
  position TEXT
);

CREATE TABLE Players (
  id INTEGER PRIMARY KEY,
  transfers_out INTEGER,
  code INTEGER,
  event_total INTEGER,
  last_season_points INTEGER,
  squad_number INTEGER,
  news_updated INTEGER,
  event_cost INTEGER,
  news_added INTEGER,
  web_name TEXT,
  in_dreamteam INTEGER,
  team_code INTEGER,
  shirt_image_url TEXT,
  first_name TEXT,
  transfers_out_event INTEGER,
  element_type_id INTEGER,
  max_cost INTEGER,
  event_explain_id INTEGER,
  selected_total INTEGER,
  min_cost INTEGER,
  fixture_id INTEGER,
  pts INTEGER,
  season_history_id INTEGER,
  total_points INTEGER,
  position_id INTEGER,
  team_id INTEGER,
  status_id INTEGER,
  added TEXT,
  form NUMERIC,
  shirt_mobile_image_url TEXT,
  current_fixture INTEGER,
  now_cost INTEGER,
  points_per_game NUMERIC,
  transfers_in INTEGER,
  news TEXT,
  original_cost INTEGER,
  event_points INTEGER,
  news_returns TEXT,
  fixture_history_id INTEGER,
  next_fixture INTEGER,
  transfers_in_event INTEGER,
  selected_by NUMERIC,
  last_name TEXT,
  phone_mobile_url TEXT,
  FOREIGN KEY(event_explain_id) REFERENCES EventsExplain(id), 
  FOREIGN KEY(fixture_history_id) REFERENCES FixturesHistory(id),
  FOREIGN KEY(status_id) REFERENCES Statuses(id),
  FOREIGN KEY(team_id) REFERENCES Teams(id),
  FOREIGN KEY(position_id) REFERENCES Positions(id),
  FOREIGN KEY(season_history_id) REFERENCES SeasonsHistory(id)
);


CREATE TABLE FixturesHistory (
  id INTEGER PRIMARY KEY,
  player_id INTEGER,
  date_text TEXT,
  gameweek INTEGER,
  result TEXT,
  minutes_played INTEGER,
  goals_scored INTEGER,
  assists INTEGER,
  clean_sheets INTEGER,
  goals_conceded INTEGER,
  own_goals INTEGER,
  penalties_saved INTEGER,
  penalties_missed INTEGER,
  yellow_cards INTEGER,
  red_cards INTEGER,
  saves INTEGER,
  bonus INTEGER,
  ea_sports_ppi INTEGER,
  bonues_points_system INTEGER,
  net_transfers INTEGER,
  value INTEGER,
  points INTEGER,
  FOREIGN KEY(player_id) REFERENCES Players(id)
);
