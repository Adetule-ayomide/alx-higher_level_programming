#!/usr/bin/python3

"""a script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys


def main():
    """A function that display all values that match an argument passed"""

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cursor = db.cursor()
    cursor.execute("""
                    SELECT * FROM states
                    WHERE name LIKE %s
                    ORDER BY id ASC""", (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":

    main()
