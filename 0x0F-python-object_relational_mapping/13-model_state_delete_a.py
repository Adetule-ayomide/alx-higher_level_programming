#!/usr/bin/python3

"""a script that deletes State objects with names containing the letter "a"
    from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """A function that deletes State objects"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_delete = session.query(State).filter(State.name.like('%a%')).all()

    if states_delete:
        for state in states_delete:
            session.delete(state)

        session.commit()

    session.close()


if __name__ == "__main__":
    main()
