#!/usr/bin/env python
import urllib2
import datetime
import json
from pprint import pprint
import time
import sqlite3 as lite

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

	for x in range(1, 2):
		stats_url = FANTASY_STATS_BASE_URL + str(x)
		try:
			req = urllib2.Request(stats_url, None, headers)
			response = urllib2.urlopen(req)
			data = response.read()
			json_data = json.loads(data)
			# json_data = json.loads(urllib2.urlopen(stats_url).read())
			# print json_data
			# pprint(player)
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
def savePlayer(player):
	con = lite.connect('db.sqlite')
	with con:
		cur = con.cursor()  
		cur.execute("INSERT INTO Players VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [player['id'],player['transfers_out'],player['code'], player['event_total'],player['last_season_points'],player['squad_number'],player['news_updated'],None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None])
												
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
	player['selected'] = json_data['selected']
	player['min_cost'] = json_data['min_cost']
	player['fixtures'] = json_data['fixtures']
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