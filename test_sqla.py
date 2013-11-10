from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from orm import Base, Player, Fixture

engine = create_engine('sqlite:///dev.db.sqlite')
# Bind the engine to the metadata of the Base class so that

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
# Insert a Player in the person table
mata = Player(id=222, first_name="Juan")
session.add(mata)
# session.commit()

 
# Insert an Address in the address table
# id = Column(Integer, primary_key=True)
# 	date_time = Column(DateTime, nullable=False)
# 	gameweek = Column(Integer, nullable=False)
# 	opponent_team_id = = Column(Integer, ForeignKey('Teams.id'))
	# player_id = Column(Integer, ForeignKey('Players.id')) 
dt = datetime.datetime.strptime("10 Nov 14:05 2013", '%d %b %H:%M %Y')
dt2 = datetime.datetime.strptime("24 Nov 13:30 2013", '%d %b %H:%M %Y')
fixture = Fixture(id=1, date_time=dt, gameweek=11, is_homegame=False, opponent_team_id=16, player_id=222)
fixture2 = Fixture(id=2, date_time=dt, gameweek=11, is_homegame=True, opponent_team_id=18, player_id=222)
session.add(fixture)
session.add(fixture2)
session.commit()