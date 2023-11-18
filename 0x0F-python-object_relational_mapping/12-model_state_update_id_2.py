#!/usr/bin/python3

"""a script that changes the name of a State object
    from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """A function that change the name of State"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, passwd, host, port, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    updated_state = session.query(State).filter_by(id=2).first()

    if updated_state:
        updated_state.name = "New Mexico"

        session.commit()

    session.close()


if __name__ == "__main__":
    main()
