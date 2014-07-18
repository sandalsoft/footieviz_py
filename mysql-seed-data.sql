
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone="+00:00";

set foreign_key_checks=0;

drop database footievizdev;

CREATE DATABASE `footievizdev` DEFAULT CHARACTER SET `utf8`;
USE footievizdev;


CREATE TABLE `fixtures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` text,
  `gameweek` int(11) DEFAULT NULL,
  `opponent_team_id` int(11) DEFAULT NULL,
  `is_homegame` tinyint(1) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1128 DEFAULT CHARSET=latin1;

CREATE TABLE `fixtureshistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `fixture_date` text,
  `game_week` int(11) DEFAULT NULL,
  `result` text,
  `minutes_played` int(11) DEFAULT NULL,
  `goals_scored` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `clean_sheets` int(11) DEFAULT NULL,
  `goals_conceded` int(11) DEFAULT NULL,
  `own_goals` int(11) DEFAULT NULL,
  `penalties_saved` int(11) DEFAULT NULL,
  `penalties_missed` int(11) DEFAULT NULL,
  `yellow_cards` int(11) DEFAULT NULL,
  `red_cards` int(11) DEFAULT NULL,
  `saves` int(11) DEFAULT NULL,
  `bonus` int(11) DEFAULT NULL,
  `ea_sports_ppi` int(11) DEFAULT NULL,
  `bonuses_points_system` int(11) DEFAULT NULL,
  `net_transfers` int(11) DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=736 DEFAULT CHARSET=latin1;

CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `news_updated` text,
  `news_added` text,
  `news` text,
  `news_return` text,
  `player_id` int(11) DEFAULT NULL,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

CREATE TABLE `players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` text,
  -- `event_explain_id` int(11) not NULL,
  -- `fixture_history_id` int(11) not NULL,
  -- `season_history_id` int(11) not NULL,
  -- `fixtures_id` int(11) not NULL,
  -- `news_id` int(11) not NULL,

  `event_total` int(11) DEFAULT NULL,
  `type_name` text,
  `team_name` text,
  `selected_by` decimal(10,2) DEFAULT NULL,
  `total_points` int(11) DEFAULT NULL,
  `current_fixture` text,
  `next_fixture` text,
  `team_code` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `status` text,
  `code` int(11) DEFAULT NULL,
  `first_name` text,
  `second_name` text,
  `web_name` text,
  `now_cost` int(11) DEFAULT NULL,
  `chance_of_playing_this_round` text,
  `chance_of_playing_next_round` text,
  `value_form` decimal(10,2) DEFAULT NULL,
  `value_season` decimal(10,2) DEFAULT NULL,
  `cost_change_start` int(11) DEFAULT NULL,
  `cost_change_event` int(11) DEFAULT NULL,
  `cost_change_start_fall` int(11) DEFAULT NULL,
  `cost_change_event_fall` int(11) DEFAULT NULL,
  `in_dreamteam` tinyint(1) DEFAULT NULL,
  `dreamteam_count` int(11) DEFAULT NULL,
  `selected_by_percent` decimal(10,2) DEFAULT NULL,
  `form` decimal(10,2) DEFAULT NULL,
  `transfers_out` int(11) DEFAULT NULL,
  `transfers_in` int(11) DEFAULT NULL,
  `transfers_out_event` int(11) DEFAULT NULL,
  `transfers_in_event` int(11) DEFAULT NULL,
  `event_points` int(11) DEFAULT NULL,
  `points_per_game` decimal(10,2) DEFAULT NULL,
  `ep_this` decimal(10,2) DEFAULT NULL,
  `ep_next` decimal(10,2) DEFAULT NULL,
  `special` tinyint(1) DEFAULT NULL,
  `minutes` int(11) DEFAULT NULL,
  `goals_scored` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `clean_sheets` int(11) DEFAULT NULL,
  `goals_conceded` int(11) DEFAULT NULL,
  `own_goals` int(11) DEFAULT NULL,
  `penalties_saved` int(11) DEFAULT NULL,
  `penalties_missed` int(11) DEFAULT NULL,
  `yellow_cards` int(11) DEFAULT NULL,
  `red_cards` int(11) DEFAULT NULL,
  `saves` int(11) DEFAULT NULL,
  `bonus` int(11) DEFAULT NULL,
  `ea_index` int(11) DEFAULT NULL,
  `bps` int(11) DEFAULT NULL,
  `element_type` int(11) DEFAULT NULL,
  `team` int(11) DEFAULT NULL,
  `current_fixture_team_id` int not NULL,
  `current_fixture_is_home` tinyint(1) DEFAULT NULL,
  `created_at` text,
  
  -- FOREIGN KEY (event_explain_id) REFERENCES eventsexplain(id),
  -- FOREIGN KEY (fixture_history_id) REFERENCES fixtureshistory(id),
  -- FOREIGN KEY (season_history_id) REFERENCES seasonshistory(id),
  -- FOREIGN KEY (fixtures_id) REFERENCES fixtures(id),
  -- FOREIGN KEY (current_fixture_team_id) REFERENCES teams(id),
  -- FOREIGN KEY (news_id) REFERENCES news(id),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE `positions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `seasonshistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `season` text,
  `minutes_played` int(11) DEFAULT NULL,
  `goals_scored` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `clean_sheets` int(11) DEFAULT NULL,
  `goals_conceded` int(11) DEFAULT NULL,
  `own_goals` int(11) DEFAULT NULL,
  `penalties_saved` int(11) DEFAULT NULL,
  `penalties_missed` int(11) DEFAULT NULL,
  `yellow_cards` int(11) DEFAULT NULL,
  `red_cards` int(11) DEFAULT NULL,
  `saves` int(11) DEFAULT NULL,
  `bonus` int(11) DEFAULT NULL,
  `ea_sports_ppi` int(11) DEFAULT NULL,
  `net_transfers` int(11) DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=latin1;

CREATE TABLE `statuses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `teams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `api_name` text,
  `name` text,
  `short_name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO statuses(status) VALUES ('i'),('a'),('d'),('n'),('s'),('u');
INSERT INTO teams(api_name, `name`, short_name) VALUES ('Arsenal', 'Arsenal', 'ARS'),('Aston Villa', 'Aston Villa', 'AV'),('Chelsea', 'Chelsea', 'CHE'),('Crystal Palace', 'Crystal Palace', 'CRY'),('Everton', 'Everton', 'EVE'),('Hull', 'Hull City', 'HUL'),('Liverpool', 'Liverpool', 'LIV'),('Man City', 'Manchester City', 'MC'),('Man Utd', 'Manchester United', 'MUN'),('Newcastle', 'Newcastle', 'NEW'),('Southampton', 'Southampton', 'SOU'),('Stoke', 'Stoke City', 'STK'),('Sunderland', 'Sunderland', 'SUN'),('Swansea City', 'Swansea City', 'SWA'),('Spurs', 'Tottenham Hotspur', 'TOT'),('West Brom', 'West Bromwich Albion', 'WBA'),('West Ham', 'West Ham United', 'WHU'),('QPR', 'QPR', 'QPR'), ('Burnley', 'Burnley', 'BUR'), ('Leicester', 'Leicester City', 'LEI');
INSERT INTO positions(`name`) VALUES ('Goalkeeper'),('Defender'),('Midfielder'),('Forward');

