#!/usr/bin/python3

"""a script that print the firdt  State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """A function that print the first State objects"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                            .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))

    session.close()

if __name__ == "__main__":
    main()

