#!/usr/bin/python3

"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def main():
    """A function that list """
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cursor = db.cursor()

    cursor.execute("""
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC
                    """)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
