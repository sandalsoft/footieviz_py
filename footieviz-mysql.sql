
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone="+00:00";

CREATE TABLE `eventsexplain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minutes_played` text,
  `col2` int(11) DEFAULT NULL,
  `col3` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `opponent_team_id` int(11) DEFAULT NULL,
  `match_points` int(11) DEFAULT NULL,
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
  `transfers_out` int(11) DEFAULT NULL,
  `code` int(11) DEFAULT NULL,
  `event_total` int(11) DEFAULT NULL,
  `last_season_points` int(11) DEFAULT NULL,
  `squad_number` int(11) DEFAULT NULL,
  `event_cost` int(11) DEFAULT NULL,
  `web_name` text,
  `in_dreamteam` tinyint(1) DEFAULT NULL,
  `team_code` int(11) DEFAULT NULL,
  `shirt_image_url` text,
  `first_name` text,
  `transfers_out_event` int(11) DEFAULT NULL,
  `element_type_id` int(11) DEFAULT NULL,
  `max_cost` bigint(11) DEFAULT NULL,
  `selected_total` int(11) DEFAULT NULL,
  `min_cost` int(11) DEFAULT NULL,
  `total_points` int(11) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `added` text,
  `form` decimal(10,2) DEFAULT NULL,
  `shirt_mobile_image_url` text,
  `current_fixture` text,
  `now_cost` int(11) DEFAULT NULL,
  `points_per_game` decimal(10,2) DEFAULT NULL,
  `transfers_in` int(11) DEFAULT NULL,
  `original_cost` int(11) DEFAULT NULL,
  `event_points` int(11) DEFAULT NULL,
  `next_fixture` text,
  `transfers_in_event` int(11) DEFAULT NULL,
  `selected_by` decimal(10,2) DEFAULT NULL,
  `last_name` text,
  `photo_mobile_url` text,
  `created_at` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

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
