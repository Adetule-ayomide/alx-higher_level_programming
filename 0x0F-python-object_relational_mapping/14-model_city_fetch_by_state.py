#!/usr/bin/python3

"""a Python file similar to model_state.py named model_city.py
    that contains the class definition of a City"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def main():
    """A function that list all cities"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
