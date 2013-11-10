from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from orm import Base, Player, Fixture, FixtureHistory

engine = create_engine('sqlite:///dev.db.sqlite')
# Bind the engine to the metadata of the Base class so that

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
player_id = 222
# Insert a Player in the person table
mata = Player(id=player_id, first_name="Juan")
session.add(mata)

fh = ["19 Aug 20:00", 1, "NEW(H) 4-0", 90, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 22, 11, 0, 60, 10], ["25 Aug 16:00", 2, "CAR(A) 2-3", 90, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 4, 120945, 61, 1]
fix_history = FixtureHistory(id=1, player_id=player_id, date_text="19 Aug 20:00", gameweek=1,result="NEW(H) 4-0", minutes_played=90,goals_scored= 0,assists= 1,clean_sheets= 1,goals_conceded= 0,own_goals= 0,penalties_saved= 0,penalties_missed= 0,yellow_cards= 0,red_cards=0,saves= 0,bonus= 1,ea_sports_ppi=22,bonuses_points_system= 11,net_transfers= 0,value= 60,points= 10)

session.add(fix_history)

dt = datetime.datetime.strptime("10 Nov 14:05 2013", '%d %b %H:%M %Y')
dt2 = datetime.datetime.strptime("24 Nov 13:30 2013", '%d %b %H:%M %Y')
fixture = Fixture(id=1, date_time=dt, gameweek=11, is_homegame=False, opponent_team_id=16, player_id=player_id)
fixture2 = Fixture(id=2, date_time=dt, gameweek=11, is_homegame=True, opponent_team_id=18, player_id=player_id)
session.add(fixture)
session.add(fixture2)
session.commit()