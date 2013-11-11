#!/usr/bin/env python
import urllib2
import json
from pprint import pprint
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
from orm import Base, Player, Fixture, FixtureHistory, SeasonHistory
from random import randrange

FANTASY_STATS_BASE_URL = 'http://fantasy.premierleague.com/web/api/elements/'
MAX_PLAYERS = 675


def main():
	json_data = getPlayerData()
	# print json_data

def getPlayerData():
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

	for x in range(1, 130):
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
			player = mapJsonToPlayerDict(json_data)
			savePlayer(player)
			time.sleep(.2)
			continue
def getStatusId(status):
	return {
		'i': 1,
		'a': 2,
		'd': 3,
	}[status]

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
		'Manchester City': 10,
		'Manchester United': 11,
		'Newcastle': 12,
		'Norwich City': 13,
		'Southampton': 14,
		'Stoke City': 15,
		'Sunderland': 16,
		'Swansea City': 17,
		'Tottenham Hotspur': 18,
		'West Bromwich Albion': 19,
		'West Ham United': 20
	}[team]

#
# SQLA ORM Insertion
#
def savePlayer(player):
	engine = create_engine('sqlite:///dev.db.sqlite')
# Bind the engine to the metadata of the Base class so that
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	 
	player_id = player['id']
	player = Player(id=player_id,
		transfers_out =player['transfers_out'],
		code =player['code'],
		event_total =player['event_total'],
		last_season_points =player['last_season_points'],
		squad_number =player['squad_number'],
		news_updated =player['news_updated'],
		event_cost =player['event_cost'],
		news_added =player['news_added'],
		web_name =player['web_name'],
		in_dreamteam =player['in_dreamteam'],
		team_code =player['team_code'],
		shirt_image_url =player['shirt_image_url'],
		first_name =player['first_name'],
		transfers_out_event =player['transfers_out_event'],
		element_type_id =player['element_type_id'],
		max_cost =player['max_cost'],
		# event_explain_id =player['event_explain_id'],
		selected_total =player['selected_total'],
		min_cost =player['min_cost'],
		# fixture_id =player['fixture_id'],
		# season_history_id =player['season_history_id'],
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
		news =player['news'],
		original_cost =player['original_cost'],
		event_points =player['event_points'],
		news_return =player['news_return'],
		# fixture_history_id =player['fixture_history_id'],
		next_fixture =player['next_fixture'],
		transfers_in_event =player['transfers_in_event'],
		selected_by = player['selected_by'],
		last_name =player['last_name'],
		photo_mobile_url =player['photo_mobile_url']
		)
		#player_id=player_id, date_text="19 Aug 20:00", gameweek=1,result="NEW(H) 4-0", minutes_played=90,goals_scored= 0,assists= 1,clean_sheets= 1,goals_conceded= 0,own_goals= 0,penalties_saved= 0,penalties_missed= 0,yellow_cards= 0,red_cards=0,saves= 0,bonus= 1,ea_sports_ppi=22,bonuses_points_system= 11,net_transfers= 0,value= 60,points= 10)

	try:
		session.add(player)
		session.commit()
		print "Inserted: " # + str(player_id)								
	except IntegrityError, e:
		print "Record already exists: " + e
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
	player['fixtures'] = json_data['fixtures']
	history = []
	for season in json_data['season_history']:
		try:
			season_stats = {}
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
			season_stats['EA_Sports_PPI'] = season[13]
			#  This isn't in seasons history stats
			# season_stats['bous_points_system'] = season[14]
			season_stats['net_transfers'] = season[14]
			season_stats['value'] = season[15]
			season_stats['points'] = season[16]
			history.append(season_stats)
		except IndexError:
			print json_data['season_history']
			print "INDEX ERROR MAPPNIG SEASON HISTORY"

	player['season_history'] = json_data['season_history']
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
		fixture_event['date'] = event[0]
		fixture_event['week'] = event[1]
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
		fixture_event['EA_Sports_PPI'] = event[15]
		fixture_event['bous_points_system'] = event[16]
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

if __name__ == "__main__":
    main()