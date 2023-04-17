#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city_state = State(name="California")
    city = City(name="San Francisco", state=city_state)

    session.add(city)
    session.commit()

    session.close()
