#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""

import sys
import MySQLdb


def list_states(username, password, database):
    """Function to lists that lists all cities
        from the database hbtn_0e_4_usa."""

    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         host='localhost', port=3306)
    cursor = db.cursor()

    cursor.execute(
                    "SELECT cities.id, cities.name, states.name "
                    "FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id ASC"
                    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
