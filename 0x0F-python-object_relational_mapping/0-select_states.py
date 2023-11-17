#!/usr/bin/python3

"""a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():
    """A function that list all states"""

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":

    main()
