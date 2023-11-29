#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""

import sys
import MySQLdb


def list_states(username, password, database, state_name):
    """Function to lists that lists all cities
        from the database hbtn_0e_4_usa."""

    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         host='localhost', port=3306)
    cursor = db.cursor()

    cursor.execute(
                    "SELECT cities.name "
                    "FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "WHERE states.name = %s "
                    "ORDER BY cities.id ASC",
                    (state_name,)
                    )

    results = cursor.fetchall()
    city_names = ', '.join(city[0] for city in results)
    print(city_names)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    database, state_name = sys.argv[3], sys.argv[4]
    list_states(username, password, database, state_name)
