

DROP TABLE IF EXISTS "statuses";
CREATE TABLE statuses (
  id INTEGER PRIMARY KEY,
  status TEXT
);
INSERT INTO "statuses" VALUES(1,'i');
INSERT INTO "statuses" VALUES(2,'a');
INSERT INTO "statuses" VALUES(3,'d');
INSERT INTO "statuses" VALUES(4,'n');
INSERT INTO "statuses" VALUES(5,'s');
INSERT INTO "statuses" VALUES(6,'u');




DROP TABLE IF EXISTS "positions";
CREATE TABLE positions (
  id INTEGER PRIMARY KEY,
  name TEXT
);
INSERT INTO "positions" VALUES(1,'Goalkeeper');
INSERT INTO "positions" VALUES(2,'Defender');
INSERT INTO "positions" VALUES(3,'Midfielder');
INSERT INTO "positions" VALUES(4,'Forward');




DROP TABLE IF EXISTS "teams";
CREATE TABLE teams (
  id INTEGER PRIMARY KEY,
  api_name TEXT,
  name TEXT,
  short_name TEXT);
INSERT INTO "teams" VALUES(1,'Arsenal','Arsenal','ARS');
INSERT INTO "teams" VALUES(3,'Cardiff City','Cardiff City','CAR');
INSERT INTO "teams" VALUES(4,'Chelsea','Chelsea','CHE');
INSERT INTO "teams" VALUES(5,'Crystal Palace','Crystal Palace','CRY');
INSERT INTO "teams" VALUES(6,'Everton','Everton','EVE');
INSERT INTO "teams" VALUES(7,'Fulham','Fulham','FUL');
INSERT INTO "teams" VALUES(8,'Hull City','Hull City','HUL');
INSERT INTO "teams" VALUES(9,'Liverpool','Liverpool','LIV');
INSERT INTO "teams" VALUES(10,'Man City','Manchester City','MC');
INSERT INTO "teams" VALUES(11,'Man Utd','Manchester United','MUN');
INSERT INTO "teams" VALUES(12,'Newcastle','Newcastle','NEW');
INSERT INTO "teams" VALUES(13,'Norwich','Norwich City','NOR');
INSERT INTO "teams" VALUES(14,'Southampton','Southampton','SOU');
INSERT INTO "teams" VALUES(15,'Stoke City','Stoke City','STK');
INSERT INTO "teams" VALUES(16,'Sunderland','Sunderland','SUN');
INSERT INTO "teams" VALUES(17,'Swansea City','Swansea City','SWA');
INSERT INTO "teams" VALUES(18,'Tottenham','Tottenham Hotspur','TOT');
INSERT INTO "teams" VALUES(19,'West Brom','West Bromwich Albion','WBA');
INSERT INTO "teams" VALUES(20,'West Ham','West Ham United','WHU');


DROP TABLE IF EXISTS "players";
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



DROP TABLE IF EXISTS "eventsexplain";
CREATE TABLE eventsexplain (
  id INTEGER PRIMARY KEY,
  minutes_played TEXT,
  col2 INTEGER,
  col3 INTEGER,
  player_id INTEGER,
  created_at TEXT,
  FOREIGN KEY(player_id) REFERENCES players(id)
);


DROP TABLE IF EXISTS "fixtures";
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


DROP TABLE IF EXISTS "fixtureshistory";
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


DROP TABLE IF EXISTS "news";
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



DROP TABLE IF EXISTS "seasonshistory";
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
