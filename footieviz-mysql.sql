
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone="+00:00";

CREATE TABLE eventsexplain (
  `id` int(11) auto_increment NOT NULL,
  minutes_played text,
  col2 int4,
  col3 int4,
  player_id int4,
  created_at text,
  PRIMARY KEY(`id`)
);

CREATE TABLE fixtures (
  `id` int(11) auto_increment NOT NULL,
  date_time text,
  gameweek int4,
  opponent_team_id int4,
  is_homegame bool,
  player_id int4,
  created_at text,
  PRIMARY KEY (`id`)
);

CREATE TABLE fixtureshistory (
  `id` int(11) auto_increment NOT NULL,
  player_id int4,
  fixture_date text,
  game_week int4,
  `result` text,
  minutes_played int4,
  goals_scored int4,
  assists int4,
  clean_sheets int4,
  goals_conceded int4,
  own_goals int4,
  penalties_saved int4,
  penalties_missed int4,
  yellow_cards int4,
  red_cards int4,
  saves int4,
  bonus int4,
  ea_sports_ppi int4,
  bonuses_points_system int4,
  net_transfers int4,
  `value` int4,
  points int4,
  created_at text,
  PRIMARY KEY (`id`)
);

CREATE TABLE news (
  `id` int(11) auto_increment NOT NULL,
  news_updated text,
  news_added text,
  news text,
  news_return text,
  player_id int4,
  created_at text,
  PRIMARY KEY (`id`)
);

CREATE TABLE players (
  `id` int(11) auto_increment NOT NULL,
  transfers_out int4,
  code int4,
  event_total int4,
  last_season_points int4,
  squad_number int4,
  event_cost int4,
  web_name text,
  in_dreamteam bool,
  team_code int4,
  shirt_image_url text,
  first_name text,
  transfers_out_event int4,
  element_type_id int4,
  max_cost int4,
  selected_total int4,
  min_cost int4,
  total_points int4,
  position_id int4,
  team_id int4,
  status_id int4,
  added text,
  form numeric,
  shirt_mobile_image_url text,
  current_fixture text,
  now_cost int4,
  points_per_game numeric,
  transfers_in int4,
  original_cost int4,
  event_points int4,
  next_fixture text,
  transfers_in_event int4,
  selected_by numeric,
  last_name text,
  photo_mobile_url text,
  created_at text,
  PRIMARY KEY (`id`)
);

CREATE TABLE positions (
  `id` int(11) auto_increment NOT NULL,
  `name` text,
  PRIMARY KEY (`id`)
);

CREATE TABLE seasonshistory (
  `id` int(11) auto_increment NOT NULL,
  season text,
  minutes_played int4,
  goals_scored int4,
  assists int4,
  clean_sheets int4,
  goals_conceded int4,
  own_goals int4,
  penalties_saved int4,
  penalties_missed int4,
  yellow_cards int4,
  red_cards int4,
  saves int4,
  bonus int4,
  ea_sports_ppi int4,
  net_transfers int4,
  `value` int4,
  points int4,
  player_id int4,
  created_at text,
  PRIMARY KEY (`id`)
);

CREATE TABLE statuses (
  `id` int(11) auto_increment NOT NULL,
  `status` text,
  PRIMARY KEY (`id`)
);

CREATE TABLE teams (
  `id` int(11) auto_increment NOT NULL,
  api_name text,
  `name` text,
  short_name text,
  PRIMARY KEY (`id`)
);
