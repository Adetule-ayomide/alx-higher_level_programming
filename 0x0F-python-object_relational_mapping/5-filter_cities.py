#!/usr/bin/python3

"""a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def main():
    """A function that list cities based on their states """
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cursor = db.cursor()

    cursor.execute("""
                    SELECT cities.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC
                    """, (state_name,))

    cities = cursor.fetchall()

    city_names = ", ".join(city[0] for city in cities)
    print(city_names)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
