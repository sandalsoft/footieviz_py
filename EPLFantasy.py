#!/usr/bin/env python
import urllib2
import json
import sys
from pprint import pprint
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
from orm import Base, Player, Fixture, FixtureHistory, SeasonHistory, News
from random import randrange

FANTASY_STATS_BASE_URL = 'http://fantasy.premierleague.com/web/api/elements/'
# MAX_PLAYERS = 675
# This seems to have changed to ~600 now?
MAX_PLAYERS = 600
NOW = datetime.datetime.now()

# Local SQLIte
# engine = create_engine('sqlite:///dev.db.sqlite')

# Local Postgres
# engine = create_engine('postgresql://Eric:@localhost/footieviz-dev')

# AWS dev
engine = create_engine('postgresql://footiedb:FOOTIEd33b33@footievizdev.c3hd4gvq8fyh.us-east-1.rds.amazonaws.com/footievizdev')

def main():

# LOAD FROM INTARWEBZ
	# starting_player_id = randrange(1,MAX_PLAYERS)
	if (len(sys.argv) > 1):
		starting_player_id = int(sys.argv[1])
	else:
		starting_player_id = 1

	print "STARTING ID: " + str(starting_player_id)

	for x in range(starting_player_id, MAX_PLAYERS):
		json_data = getPlayerData(x)
		player = mapJsonToPlayerDict(json_data)
		savePlayer(player)


	# 	# time.sleep(.2)

# # LOAD FROM FILE
	# json_data_all_players = loadPlayerData('raw_data.json')
	# for json_data in json_data_all_players:
	# 	player = mapJsonToPlayerDict(json_data)
	# 	savePlayer(player)
	# 	# print json_data



def loadPlayerData(filename):
	json_data=open(filename)
	data = json.load(json_data)
	return data
	# pprint(data)

def getPlayerData(x):
	headers = { 
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
			# 'Host' : 'fantasy.premierleague.com',
			# 'DNT' : '1',
			# 'Connection' : 'keep-alive',
			# 'Cache-Control' : 'max-age=0',
			# 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			# 'Accept-Encoding' : 'gzip,deflate,sdch',
			# 'Accept-Language' : 'en-US,en;q=0.8'
	}

	
	stats_url = FANTASY_STATS_BASE_URL + str(x)
	try:
		req = urllib2.Request(stats_url, None, headers)
		response = urllib2.urlopen(req)
		data = response.read()
		json_data = json.loads(data)

	except urllib2.URLError, e:
		print e

	except ValueError:
		# Decoding failed
		print "ERROR: JSON value decoding error on id " + str(x)
		print response.info()
		print data

	else:
		return json_data
		# pprint(player)
		# return player
		# time.sleep(.2)
		# continue


#
# SQLA ORM Insertion
#
def savePlayer(player):

# Bind the engine to the metadata of the Base class so that
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	 
	player_id = int(player['id'])
	print "Starting ID: " + str(player_id)

# Create and add Player Object ORM to session
	playerORM = createPlayerORM(player)
	session.add(playerORM)
	session.commit()

# Create and add News Object ORM to session
	newsORM = createNewsORM(player)
	if (newsORM):
		session.add(newsORM)


# Create and add Fixtures ORM to session
	for fixture in player['fixtures']:
		fixturesORM = createFixturesORM(player['id'], fixture)
		session.add(fixturesORM)

# Create Fixtures History for the current year
	## REFACTOR THIS INTO A METHOD OR CLASS
	try:
	# # Add array of season historys
		if (len(player['season_history']) is not 0):
			for season in player['season_history']:
				seasonHistoryORM = createSeasonHistoryORM(player_id, season)
				session.add(seasonHistoryORM)
	
	# Add array of fixture histories
		for fixture_history in player['fixture_history']:
			fixtureHistoryORM = createFixtureHistoryORM(player_id, fixture_history)
			session.add(fixtureHistoryORM)	

	# Commit session
		session.commit()
		print "Inserted: " + str(player_id)								
	except IntegrityError, e:
		print "INTEGRITY ERROR YO: " + str(e)
	else:
		pass
			
	# pprint(player, indent=2)



def mapJsonToPlayerDict(json_data):
	player = {}
	player['id'] = json_data['id']
	player['team'] = json_data['team_name']
	player['first_name'] = json_data['first_name']
	player['web_name'] = json_data['web_name']
	player['position'] = json_data['type_name']
	player['transfers_out'] = json_data['transfers_out']
	player['code'] = json_data['code']
	player['event_total'] = json_data['event_total']
	player['last_season_points'] = json_data['last_season_points']
	player['squad_number'] = json_data['squad_number']
	player['news_updated'] = json_data['news_updated']
	player['event_cost'] = json_data['event_cost']
	player['news_added'] = json_data['news_added']
	player['in_dreamteam'] = json_data['in_dreamteam']
	player['team_code'] = json_data['team_code']
	player['shirt_image_url'] = json_data['shirt_image_url']
	player['transfers_out_event'] = json_data['transfers_out_event']
	player['element_type_id'] = json_data['element_type_id']
	player['max_cost'] = json_data['max_cost']
	player['event_explain'] = json_data['event_explain']
	player['selected_total'] = json_data['selected']
	player['min_cost'] = json_data['min_cost']


# FIXTURES
	fixtures = []
	for fixture in json_data['fixtures']['all']:
		myfixture = {}
# Create datetime of fixture week string
		dt = datetime.datetime.strptime(fixture[0] + " 2013", '%d %b %H:%M %Y')
		myfixture['date_time'] = dt

# Create gameweek int 
		myfixture['gameweek'] = int(fixture[1].split(' ')[1])

# Create is_homegame boolean
		if 'A' not in fixture[2].split(' (')[1]:
			myfixture['is_homegame'] = True
		else:
			myfixture['is_homegame'] = False

# Create opponent TeamId
#0 "12 Feb 19:45",
#1 "Gameweek 26",
#2 "Newcastle (A)"
		opponent = fixture[2].split(' (')[0]

		myfixture['opponent_team_id'] = getTeamId(opponent)

# Set player_id
		myfixture['player_id'] = player['id']
		fixtures.append(myfixture)
	player['fixtures'] = fixtures

# SEASON HISTORY
	history = []
	for season in json_data['season_history']:
		try:
			season_stats = {}
			season_stats['season'] = season[0]
			season_stats['minutes_played'] = season[1]
			season_stats['goals_scored'] = season[2]
			season_stats['assists'] = season[3]
			season_stats['clean_sheets'] = season[4]
			season_stats['goals_conceded'] = season[5]
			season_stats['own_goals'] = season[6]
			season_stats['penalties_saved'] = season[7]
			season_stats['penalties_missed'] = season[8]
			season_stats['yellow_cards'] = season[9]
			season_stats['red_cards'] = season[10]
			season_stats['saves'] = season[11]
			season_stats['bonus'] = season[12]
			season_stats['ea_sports_ppi'] = season[13]
			#  This isn't in seasons history stats
			# season_stats['bous_points_system'] = season[14]
			season_stats['net_transfers'] = season[14]
			season_stats['value'] = season[15]
			season_stats['points'] = season[16]
			history.append(season_stats)
		except IndexError:
			print json_data['season_history']
			print "INDEX ERROR MAPPNIG SEASON HISTORY"

	player['season_history'] = history
	# pprint(player['season_history'])
	# print "told ya"


	player['total_points'] = json_data['total_points']
	player['status'] = json_data['status']
	player['added'] = json_data['added']
	player['form'] = json_data['form']
	player['shirt_mobile_image_url'] = json_data['shirt_mobile_image_url']
	player['current_fixture'] = json_data['current_fixture']
	player['now_cost'] = json_data['now_cost']
	player['points_per_game'] = json_data['points_per_game']
	player['transfers_in'] = json_data['transfers_in']
	player['news'] = json_data['news']
	player['original_cost'] = json_data['original_cost']
	player['event_points'] = json_data['event_points']
	player['news_return'] = json_data['news_return']

	events = []
	for event in json_data['fixture_history']['all']:
		fixture_event = {}
		fixture_event['date_text'] = event[0]
		fixture_event['game_week'] = event[1]	
		fixture_event['result'] = event[2]
		fixture_event['minutes_played'] = event[3]
		fixture_event['goals_scored'] = event[4]
		fixture_event['assists'] = event[5]
		fixture_event['clean_sheets'] = event[6]
		fixture_event['goals_conceded'] = event[7]
		fixture_event['own_goals'] = event[8]
		fixture_event['penalties_saved'] = event[9]
		fixture_event['penalties_missed'] = event[10]
		fixture_event['yellow_cards'] = event[11]
		fixture_event['red_cards'] = event[12]
		fixture_event['saves'] = event[13]
		fixture_event['bonus'] = event[14]
		fixture_event['ea_sports_ppi'] = event[15]
		fixture_event['bonuses_points_system'] = event[16]
		fixture_event['net_transfers'] = event[17]
		fixture_event['value'] = event[18]
		fixture_event['points'] = event[19]
		events.append(fixture_event)
	player['fixture_history'] = events
	
	player['next_fixture'] = json_data['next_fixture']
	player['transfers_in_event'] = json_data['transfers_in_event']
	player['selected_by'] = json_data['selected_by']
	player['team_id'] = json_data['team_id']
	player['last_name'] = json_data['second_name']
	player['photo_mobile_url'] = json_data['photo_mobile_url']
	return player

def getStatusId(status):
	return {
		'i': 1,
		'a': 2,
		'd': 3,
		'n': 4,
		's': 5,
		'u': 6
	}[status]

def getTeamThree(team):
	return 3

def getPositionId(position):
	return {
		'Goalkeeper': 1,
		'Defender' : 2,
		'Midfielder' : 3,
		"Forward" : 4
	}[position]
def getTeamId(team):
	return {
		'Arsenal': 1,
		'Aston Villa': 2,
		'Cardiff City': 3,
		'Chelsea': 4,
		'Crystal Palace': 5,
		'Everton': 6,
		'Fulham': 7,
		'Hull City': 8,
		'Liverpool': 9,
		'Man City': 10,
		'Man Utd': 11,
		'Newcastle': 12,
		'Norwich': 13,
		'Southampton': 14,
		'Stoke City': 15,
		'Sunderland': 16,
		'Swansea': 17,
		'Tottenham': 18,
		'West Brom': 19,
		'West Ham': 20
	}[team]








######################################################################




####                                    MAP



######################################################################









def createFixturesORM(player_id, fixture):
	# pprint(player['fixtures'])
	fixture_orm = Fixture(id=None,
		date_time = fixture['date_time'],
		gameweek = fixture['gameweek'],
		is_homegame = fixture['is_homegame'],
		opponent_team_id = fixture['opponent_team_id'],
		player_id = player_id,
		created_at = NOW
		)
	return fixture_orm

def createPlayerORM(player):	
	player_orm = Player(id=player['id'],
		transfers_out =player['transfers_out'],
		code =player['code'],
		event_total =player['event_total'],
		last_season_points =player['last_season_points'],
		squad_number =player['squad_number'],
		event_cost =player['event_cost'],
		web_name =player['web_name'],
		in_dreamteam =player['in_dreamteam'],
		team_code =player['team_code'],
		shirt_image_url =player['shirt_image_url'],
		first_name =player['first_name'],
		transfers_out_event =player['transfers_out_event'],
		element_type_id =player['element_type_id'],
		max_cost =player['max_cost'],
		selected_total =player['selected_total'],
		min_cost =player['min_cost'],
		total_points =player['total_points'],
		position_id = getPositionId(player['position']),
		team_id =player['team_id'],
		status_id= getStatusId(player['status']),
		added =player['added'],
		form =player['form'],
		shirt_mobile_image_url =player['shirt_mobile_image_url'],
		current_fixture =player['current_fixture'],
		now_cost =player['now_cost'],
		points_per_game= player['points_per_game'],
		transfers_in =player['transfers_in'],
		original_cost =player['original_cost'],
		event_points =player['event_points'],
		next_fixture =player['next_fixture'],
		transfers_in_event =player['transfers_in_event'],
		selected_by = player['selected_by'],
		last_name =player['last_name'],
		photo_mobile_url =player['photo_mobile_url'],
		created_at = NOW
		)
	return player_orm

def createNewsORM(player):
	news_added = news_updated = news_return = news = None
	#"2013-10-04T16:01:14 UTC+0000",
	if (player['news_added']):
		news_added = datetime.datetime.strptime(player['news_added'], '%Y-%m-%dT%H:%M:%S UTC+0000')
	if (player['news_updated']):
		news_updated = datetime.datetime.strptime(player['news_updated'], '%Y-%m-%dT%H:%M:%S UTC+0000')
	if (player['news_return']):
		news_return = datetime.datetime.strptime(player['news_return'], '%Y-%m-%dT%H:%M:%S UTC+0000')
	if (player['news']):
		news = player['news']

	if (news_added or news_updated or news_return or news):
		news_orm = News(id=None,
			player_id = player['id'],
			news_added = news_added,
			news_updated = news_updated,
			news_return = news_return,
			news = news,
			created_at = NOW
			)
		return news_orm
	else:
		return None


def createFixtureHistoryORM(player_id, fixture_stats):
	fixture_history_ORM = FixtureHistory(id=None,
		player_id = player_id,
		fixture_date = fixture_stats['date_text'],
		game_week = fixture_stats['game_week'],
		result = fixture_stats['result'],
		minutes_played = fixture_stats['minutes_played'],
		goals_scored = fixture_stats['goals_scored'],
		assists = fixture_stats['assists'],
		clean_sheets = fixture_stats['clean_sheets'],
		goals_conceded = fixture_stats['goals_conceded'],
		own_goals = fixture_stats['own_goals'],
		penalties_saved = fixture_stats['penalties_saved'],
		penalties_missed = fixture_stats['penalties_missed'],
		yellow_cards = fixture_stats['yellow_cards'],
		red_cards = fixture_stats['red_cards'],
		saves = fixture_stats['saves'],
		bonus = fixture_stats['bonus'],
		ea_sports_ppi = fixture_stats['ea_sports_ppi'],
		bonuses_points_system = fixture_stats['bonuses_points_system'],
		net_transfers = fixture_stats['net_transfers'],
		value = fixture_stats['value'],
		points = fixture_stats['points'],
		created_at = NOW,
		)
	return fixture_history_ORM

def createSeasonHistoryORM(player_id, season):
	season_history_ORM = SeasonHistory(id=None,
		player_id = player_id,
		season=season['season'],
		minutes_played = season['minutes_played'],
	  goals_scored = season['goals_scored'],
	  assists = season['assists'],
	  clean_sheets = season['clean_sheets'],
	  goals_conceded = season['goals_conceded'],
	  own_goals = season['own_goals'],
	  penalties_saved = season['penalties_saved'],
	  penalties_missed = season['penalties_missed'],
	  yellow_cards = season['yellow_cards'],
	  red_cards = season['red_cards'],
	  saves = season['saves'],
	  bonus = season['bonus'],
	  ea_sports_ppi = season['ea_sports_ppi'],
	  # bonuses_points_system = season['bonuses_poin	ts_system'],
	  net_transfers = season['net_transfers'],
	  value = season['value'],
	  points = season['points'],
	  created_at = NOW,
		)
	return season_history_ORM


if __name__ == "__main__":
    main()