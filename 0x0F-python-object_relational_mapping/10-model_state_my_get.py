#!/usr/bin/python3

"""a script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """A function that prints State passed as argument"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    my_state = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == my_state).first()

    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
