from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm import Base, EventExplain, Player

engine = create_engine('sqlite:///dev.db.sqlite')
# Bind the engine to the metadata of the Base class so that

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
# Insert a Player in the person table
mata = Player(id=222, first_name="Juan")
session.add(mata)
session.commit()

 
# Insert an Address in the address table
new_event_explain = EventExplain(id=1, minutes_played=90, col2=0, col3=0,	player=mata)
session.add(new_event_explain)
session.commit()