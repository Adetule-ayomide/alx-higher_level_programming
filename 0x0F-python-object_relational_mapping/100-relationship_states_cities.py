#!/usr/bin/python3

"""a script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base


def main():
    """A function that create state and city"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, passwd, host, port, db))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name='San Francisco', state=State(name='California'))

    session.add(new_city)

    session.commit()

    session.close()


if __name__ == "__main__":
    main()
