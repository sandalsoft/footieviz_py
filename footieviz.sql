-- SQLITE
-- postgres input: /path/to/psql -d database -U username -W < /the/path/to/sqlite-dumpfile.sql

CREATE TABLE teams (
  id INTEGER PRIMARY KEY,
  api_name TEXT,
  name TEXT,
  short_name TEXT
);
CREATE TABLE statuses (
  id INTEGER PRIMARY KEY,
  status TEXT
);

CREATE TABLE positions (
  id INTEGER PRIMARY KEY,
  name TEXT
);


CREATE TABLE players (
  id INTEGER PRIMARY KEY,
  transfers_out INTEGER,
  code INTEGER,
  event_total INTEGER,
  last_season_points INTEGER,
  squad_number INTEGER,
  event_cost INTEGER,
  web_name TEXT,
  in_dreamteam INTEGER,
  team_code INTEGER,
  shirt_image_url TEXT,
  first_name TEXT,
  transfers_out_event INTEGER,
  element_type_id INTEGER,
  max_cost INTEGER,
  selected_total INTEGER,
  min_cost INTEGER,
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
  original_cost INTEGER,
  event_points INTEGER,
  next_fixture INTEGER,
  transfers_in_event INTEGER,
  selected_by NUMERIC,
  last_name TEXT,
  photo_mobile_url TEXT,
  created_at TEXT,
  FOREIGN KEY(status_id) REFERENCES statuses(id),
  FOREIGN KEY(team_id) REFERENCES teams(id),
  FOREIGN KEY(position_id) REFERENCES positions(id)
);

CREATE TABLE news (
  id INTEGER PRIMARY KEY,
  news_updated TEXT,
  news_added TEXT,
  news TEXT,
  news_return TEXT,
  player_id INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id)
);

CREATE TABLE eventsexplain (
  id INTEGER PRIMARY KEY,
  minutes_played TEXT,
  col2 INTEGER,
  col3 INTEGER,
  player_id INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id)
);

CREATE TABLE fixtures (
  id INTEGER PRIMARY KEY,
  date_time TEXT,
  gameweek INTEGER,
  opponent_team_id INTEGER,
  is_homegame INTEGER,
  player_id INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id),
  FOREIGN KEY(opponent_team_id) REFERENCES teams(id)
);



CREATE TABLE seasonshistory (
  id INTEGER PRIMARY KEY,
  season TEXT,
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
  net_transfers INTEGER,
  value INTEGER,
  points INTEGER,
  player_id INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id)
);





CREATE TABLE fixtureshistory (
  id INTEGER PRIMARY KEY,
  player_id INTEGER,
  fixture_date TEXT,
  game_week INTEGER,
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
  bonuses_points_system INTEGER,
  net_transfers INTEGER,
  value INTEGER,
  points INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id)
);


-- DELETE FROM fixtures;
-- DELETE FROM fixtureshistory;
-- DELETE FROM eventsexplain;
-- DELETE FROM players;
-- DELETE FROM seasonshistory;