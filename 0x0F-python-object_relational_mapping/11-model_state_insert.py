#!/usr/bin/python3

""" a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """A function that add State"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()

    print('{}'.format(new_state.id))

    session.close()


if __name__ == "__main__":
    main()
