#!/usr/bin/env python
import urllib2
import json
import sys
# from pprint import pprint
# import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
from orm import Base, Player, Fixture, FixtureHistory, SeasonHistory, News
from random import randrange

TESTING = False
FANTASY_STATS_BASE_URL = 'http://fantasy.premierleague.com/web/api/elements/'
FANTASY_STATS_JSON_PARAM = '/?format=json'
# MAX_PLAYERS = 675
# This seems to have changed to ~600 now?
MAX_PLAYERS = 529
NOW = datetime.datetime.now()
ERROR_PLAYERS = []

# Local SQLIte
# engine = create_engine('sqlite:///dev.db.sqlite')

# Local Postgres
# engine = create_engine('postgresql://Eric:@localhost/footieviz-dev')

# AWS postgres dev
# engine =
# create_engine('postgresql://footiedb:FOOTIEd33b33@footievizdev.c3hd4gvq8fyh.us-east-1.rds.amazonaws.com/footievizdev')

# AWS mysql dev
engine = create_engine(
    'mysql://footiedb:FOOTIEd33b33@footivizdev.c3hd4gvq8fyh.us-east-1.rds.amazonaws.com/footievizdev')


def main():

    if not (TESTING):
        # LOAD FROM INTARWEBZ
        starting_player_id = randrange(1, MAX_PLAYERS)
        if (len(sys.argv) > 1):
            starting_player_id = int(sys.argv[1])
        else:
            starting_player_id = 1

        print "STARTING ID: " + str(starting_player_id)

        for x in range(starting_player_id, MAX_PLAYERS):
            json_data = getPlayerData(x)
            if (json_data is None):
                print "ERROR_PLAYERS #: " + str(len(ERROR_PLAYERS))
                continue

            player = mapJsonToPlayerDict(json_data)
            savePlayer(player)

        processErrorPlayerIds()
    # time.sleep(.2)

# LOAD FROM FILE
    else:
        json_data_all_players = loadPlayerData('raw_data.json')
        for json_data in json_data_all_players:
            player = mapJsonToPlayerDict(json_data)
            savePlayer(player)
            # print json_data


def processErrorPlayerIds():
    print "STARTING ERROR_PLAYERS #: " + str(len(ERROR_PLAYERS))
    print ERROR_PLAYERS
    for player_id in ERROR_PLAYERS:
        json_data = getPlayerData(player_id)
        if (json_data is None):
            print "PERSISTENT ERROR WITH " + str(player_id)
            with open("ERROR_PLAYERS.txt", "a") as myfile:
                myfile.write(player_id)
            continue
        player = mapJsonToPlayerDict(json_data)
        savePlayer(player)


def loadPlayerData(filename):
    json_data = open(filename)
    data = json.load(json_data)
    return data
    # pprint(data)


def getPlayerData(x):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    stats_url = FANTASY_STATS_BASE_URL + str(x) + FANTASY_STATS_JSON_PARAM
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
        # print response.info()
        # print data
        ERROR_PLAYERS.append(x)
        return None

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

   # Update instead of insert?
# http://stackoverflow.com/questions/2631935/sqlalchemy-a-better-way-for-update-with-declarative
# session.query(User).filter_by(id=123).update({"name": u"Bob Marley"})
# Create and add Player Object ORM to session

    playerORM = createPlayerORM(player)
    # p = session.query(FixtureHistory).filter_by(player_id=int(player['id']))
    # print p
    session.merge(playerORM)
    session.commit()

# Create and add News Object ORM to session
    # newsORM = createNewsORM(player)
    # if (newsORM):
    #     session.merge(newsORM)

# Create and add Fixtures ORM to session
    for fixture in player['fixtures']:
        fixturesORM = createFixturesORM(player['id'], fixture)
        session.merge(fixturesORM)

# Create Fixtures History for the current year
    # REFACTOR THIS INTO A METHOD OR CLASS
    try:
    # Add array of season historys
        if (len(player['season_history']) is not 0):
            for season in player['season_history']:
                seasonHistoryORM = createSeasonHistoryORM(
                    player_id, season)
                session.merge(seasonHistoryORM)

    # Add array of fixture histories
        for fixture_history in player['fixture_history']:
            fixtureHistoryORM = createFixtureHistoryORM(
                player_id, fixture_history)
            session.merge(fixtureHistoryORM)

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
    player['photo'] = json_data['photo']
    player['event_explain'] = json_data['event_explain']
    player['event_total'] = json_data['event_total']
    player['type_name'] = json_data['type_name']
    player['team_name'] = json_data['team_name']
    player['selected_by'] = json_data['selected_by']
    player['total_points'] = json_data['total_points']
    player['current_fixture'] = json_data['current_fixture']
    player['next_fixture'] = json_data['next_fixture']
    player['team_code'] = json_data['team_code']
    player['news'] = json_data['news']
    player['team_id'] = json_data['team_id']
    player['status'] = json_data['status']
    player['code'] = json_data['code']
    player['first_name'] = json_data['first_name']
    player['second_name'] = json_data['second_name']
    player['web_name'] = json_data['web_name']
    player['now_cost'] = json_data['now_cost']
    player['chance_of_playing_this_round'] = json_data['chance_of_playing_this_round']
    player['chance_of_playing_next_round'] = json_data['chance_of_playing_next_round']
    player['value_form'] = json_data['value_form']
    player['value_season'] = json_data['value_season']
    player['cost_change_start'] = json_data['cost_change_start']
    player['cost_change_event'] = json_data['cost_change_event']
    player['cost_change_start_fall'] = json_data['cost_change_start_fall']
    player['cost_change_event_fall'] = json_data['cost_change_event_fall']
    player['in_dreamteam'] = json_data['in_dreamteam']
    player['dreamteam_count'] = json_data['dreamteam_count']
    player['selected_by_percent'] = json_data['selected_by_percent']
    player['form'] = json_data['form']
    player['transfers_out'] = json_data['transfers_out']
    player['transfers_in'] = json_data['transfers_in']
    player['transfers_out_event'] = json_data['transfers_out_event']
    player['transfers_in_event'] = json_data['transfers_in_event']
    player['event_points'] = json_data['event_points']
    player['points_per_game'] = json_data['points_per_game']
    player['ep_this'] = json_data['ep_this']
    player['ep_next'] = json_data['ep_next']
    player['special'] = json_data['special']
    player['minutes'] = json_data['minutes']
    player['goals_scored'] = json_data['goals_scored']
    player['assists'] = json_data['assists']
    player['clean_sheets'] = json_data['clean_sheets']
    player['goals_conceded'] = json_data['goals_conceded']
    player['own_goals'] = json_data['own_goals']
    player['penalties_saved'] = json_data['penalties_saved']
    player['penalties_missed'] = json_data['penalties_missed']
    player['yellow_cards'] = json_data['yellow_cards']
    player['red_cards'] = json_data['red_cards']
    player['saves'] = json_data['saves']
    player['bonus'] = json_data['bonus']
    player['ea_index'] = json_data['ea_index']
    player['bps'] = json_data['bps']
    player['element_type'] = json_data['element_type']
    player['team'] = json_data['team']

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
# 0 "12 Feb 19:45",
# 1 "Gameweek 26",
# 2 "Newcastle (A)" tits
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

    # player['total_points'] = json_data['total_points']
    # player['status'] = json_data['status']
    # player['added'] = json_data['added']
    # player['form'] = json_data['form']
    # player['shirt_mobile_image_url'] = json_data['shirt_mobile_image_url']
    # player['current_fixture'] = json_data['current_fixture']
    # player['now_cost'] = json_data['now_cost']
    # player['points_per_game'] = json_data['points_per_game']
    # player['transfers_in'] = json_data['transfers_in']
    # player['news'] = json_data['news']
    # player['original_cost'] = json_data['original_cost']
    # player['event_points'] = json_data['event_points']
    # player['news_return'] = json_data['news_return']

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

    # player['next_fixture'] = json_data['next_fixture']
    # player['transfers_in_event'] = json_data['transfers_in_event']
    # player['selected_by'] = json_data['selected_by']
    # player['team_id'] = json_data['team_id']
    # player['last_name'] = json_data['second_name']
    # player['photo_mobile_url'] = json_data['photo_mobile_url']
    return player


def isHomeMatch(fixture_str):
    home_away_char = fixture_str.split(')')[0][-1]
    if (home_away_char == 'H'):
        return True
    else:
        return False


def getMatchPoints(fixture_str):
    # print "Fixture str: " + fixture_str
    scores = fixture_str.split('-')
    if (len(scores) < 2):
        return None
    # print "scores: " + str(scores)
    my_score = scores[0][-1]
    # print "my score: "  + my_score
    opponent_score = scores[1]
    # print "opponent score: " + opponent_score

    if (int(my_score) > int(opponent_score)):
        return 3
    if (int(opponent_score) > int(my_score)):
        return 0
    if (int(my_score) == int(opponent_score)):
        return 1


def getOpponentTeamId(fixture_str):
    opponent = fixture_str.split('(')[0]
    return getTeamId(getLongTeamName(opponent))


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
        'Defender': 2,
        'Midfielder': 3,
        "Forward": 4
    }[position]


def getLongTeamName(shortName):
    if (shortName == 'ARS'):
        return 'Arsenal'
    if (shortName == 'AVL'):
        return 'Aston Villa'
    if (shortName == 'CAR'):
        return 'Cardiff City'
    if (shortName == 'CHE'):
        return 'Chelsea'
    if (shortName == 'CRY'):
        return 'Crystal Palace'
    if (shortName == 'EVE'):
        return 'Everton'
    if (shortName == 'FUL'):
        return 'Fulham'
    if (shortName == 'HUL'):
        return 'Hull City'
    if (shortName == 'LIV'):
        return 'Liverpool'
    if (shortName == 'MCI'):
        return 'Man City'
    if (shortName == 'MUN'):
        return 'Man Utd'
    if (shortName == 'NEW'):
        return 'Newcastle'
    if (shortName == 'NOR'):
        return 'Norwich'
    if (shortName == 'SOU'):
        return 'Southampton'
    if (shortName == 'STK'):
        return 'Stoke City'
    if (shortName == 'SUN'):
        return 'Sunderland'
    if (shortName == 'SWA'):
        return 'Swansea'
    if (shortName == 'TOT'):
        return 'Tottenham'
    if (shortName == 'WBA'):
        return 'West Brom'
    if (shortName == 'WHU'):
        return 'West Ham'


def getTeamId(team):
    return {
        'Arsenal': 1,
        'Aston Villa': 2,
        'Chelsea': 3,
        'Crystal Palace': 4,
        'Everton': 5,
        'Hull': 6,
        'Liverpool': 7,
        'Man City': 8,
        'Man Utd': 9,
        'Newcastle': 10,
        'Southampton': 11,
        'Stoke': 12,
        'Sunderland': 13,
        'Swansea': 14,
        'Spurs': 15,
        'West Brom': 16,
        'West Ham': 17,
        'QPR': 18,
        'Burnley': 19,
        'Leicester': 20
    }[team]


#
# MAP
#
def createFixturesORM(player_id, fixture):
    # pprint(player['fixtures'])
    fixture_orm = Fixture(id=None,
                          date_time=fixture['date_time'],
                          gameweek=fixture['gameweek'],
                          is_homegame=fixture['is_homegame'],
                          opponent_team_id=fixture['opponent_team_id'],
                          player_id=player_id,
                          created_at=NOW
                          )
    return fixture_orm


def createPlayerORM(player):
    # print "496-DEBUG: " + str(player)
    current_fixture_str = player['current_fixture']

    # if current_fixture is "" (this happens at before the season and maybe during bye week)
    if len(current_fixture_str) is 0:
         current_fixture_is_home = False
         opponent = None
         current_fixture_team_id = None
    else:
        if 'A' not in current_fixture_str.split(' (')[1]:
            current_fixture_is_home = True
        else:
            current_fixture_is_home = False

        opponent = current_fixture_str.split(' (')[0]
        # print "508-DEBUG: " + str(opponent)
        current_fixture_team_id = getTeamId(opponent)
    # print "513-DEBUG: " + str(current_fixture_is_home)
    player_orm = Player(id=player['id'],
                        photo=player['photo'],
                        # event_explain=player['event_explain'],
                        # fixture_history=player['fixture_history'],
                        # fixtures=player['fixtures'],
                        event_total=player['event_total'],
                        type_name=player['type_name'],
                        team_name=player['team_name'],
                        selected_by=player['selected_by'],
                        total_points=player['total_points'],
                        current_fixture=player['current_fixture'],
                        next_fixture=player['next_fixture'],
                        team_code=player['team_code'],
                        # news=player['news'],
                        team_id=player['team_id'],
                        status=player['status'],
                        code=player['code'],
                        first_name=player['first_name'],
                        second_name=player['second_name'],
                        web_name=player['web_name'],
                        now_cost=player['now_cost'],
                        chance_of_playing_this_round=player['chance_of_playing_this_round'],
                        chance_of_playing_next_round=player['chance_of_playing_next_round'],
                        value_form=player['value_form'],
                        value_season=player['value_season'],
                        cost_change_start=player['cost_change_start'],
                        cost_change_event=player['cost_change_event'],
                        cost_change_start_fall=player['cost_change_start_fall'],
                        cost_change_event_fall=player['cost_change_event_fall'],
                        in_dreamteam=player['in_dreamteam'],
                        dreamteam_count=player['dreamteam_count'],
                        selected_by_percent=player['selected_by_percent'],
                        form=player['form'],
                        transfers_out=player['transfers_out'],
                        transfers_in=player['transfers_in'],
                        transfers_out_event=player['transfers_out_event'],
                        transfers_in_event=player['transfers_in_event'],
                        event_points=player['event_points'],
                        points_per_game=player['points_per_game'],
                        ep_this=player['ep_this'],
                        ep_next=player['ep_next'],
                        special=player['special'],
                        minutes=player['minutes'],
                        goals_scored=player['goals_scored'],
                        assists=player['assists'],
                        clean_sheets=player['clean_sheets'],
                        goals_conceded=player['goals_conceded'],
                        own_goals=player['own_goals'],
                        penalties_saved=player['penalties_saved'],
                        penalties_missed=player['penalties_missed'],
                        yellow_cards=player['yellow_cards'],
                        red_cards=player['red_cards'],
                        saves=player['saves'],
                        bonus=player['bonus'],
                        ea_index=player['ea_index'],
                        bps=player['bps'],
                        element_type=player['element_type'],
                        team=player['team'],
                        current_fixture_is_home=current_fixture_is_home,
                        current_fixture_team_id=current_fixture_team_id,
                        created_at=NOW
                        )
    return player_orm


def createNewsORM(player):
    if (player['news']):
        news = player['news']

    if (news_added or news_updated or news_return or news):
        news_orm = News(id=None,
                        player_id=player['id'],
                        news_added=news_added,
                        news_updated=news_updated,
                        news_return=news_return,
                        news=news,
                        created_at=NOW
                        )
        return news_orm
    else:
        return None


def createFixtureHistoryORM(player_id, fixture_stats):
    # tits
    # home_team_id = DONE
    # away_team_id = DONE
    # winning_team_id = DONE
    # did_win_match =   #bool DONE with match points_per_game
    # winning_team_goals =
    # losing_team_goals =

    fixture_history_ORM = FixtureHistory(id=None,
                                         player_id=player_id,
                                         fixture_date=fixture_stats[
                                             'date_text'],
                                         game_week=fixture_stats['game_week'],
                                         result=fixture_stats['result'],
                                         opponent_team_id=getOpponentTeamId(
                                             fixture_stats['result']),
                                         match_points=getMatchPoints(
                                             fixture_stats['result']),
                                         minutes_played=fixture_stats[
                                             'minutes_played'],
                                         goals_scored=fixture_stats[
                                             'goals_scored'],
                                         assists=fixture_stats['assists'],
                                         clean_sheets=fixture_stats[
                                             'clean_sheets'],
                                         goals_conceded=fixture_stats[
                                             'goals_conceded'],
                                         own_goals=fixture_stats['own_goals'],
                                         penalties_saved=fixture_stats[
                                             'penalties_saved'],
                                         penalties_missed=fixture_stats[
                                             'penalties_missed'],
                                         yellow_cards=fixture_stats[
                                             'yellow_cards'],
                                         red_cards=fixture_stats['red_cards'],
                                         saves=fixture_stats['saves'],
                                         bonus=fixture_stats['bonus'],
                                         ea_sports_ppi=fixture_stats[
                                             'ea_sports_ppi'],
                                         bonuses_points_system=fixture_stats[
                                             'bonuses_points_system'],
                                         net_transfers=fixture_stats[
                                             'net_transfers'],
                                         value=fixture_stats['value'],
                                         points=fixture_stats['points'],
                                         created_at=NOW,
                                         )
    return fixture_history_ORM


def createSeasonHistoryORM(player_id, season):
    season_history_ORM = SeasonHistory(id=None,
                                       player_id=player_id,
                                       season=season['season'],
                                       minutes_played=season['minutes_played'],
                                       goals_scored=season['goals_scored'],
                                       assists=season['assists'],
                                       clean_sheets=season['clean_sheets'],
                                       goals_conceded=season['goals_conceded'],
                                       own_goals=season['own_goals'],
                                       penalties_saved=season[
                                           'penalties_saved'],
                                       penalties_missed=season[
                                           'penalties_missed'],
                                       yellow_cards=season['yellow_cards'],
                                       red_cards=season['red_cards'],
                                       saves=season['saves'],
                                       bonus=season['bonus'],
                                       ea_sports_ppi=season['ea_sports_ppi'],
                                       # bonuses_points_system = season['bonuses_poin   ts_system'],
                                       net_transfers=season['net_transfers'],
                                       value=season['value'],
                                       points=season['points'],
                                       created_at=NOW,
                                       )
    return season_history_ORM


if __name__ == "__main__":
    main()
