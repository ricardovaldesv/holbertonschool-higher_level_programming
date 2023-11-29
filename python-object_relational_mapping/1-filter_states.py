#!/usr/bin/python3
"""A script to list all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa."""

import sys
import MySQLdb


def list_states(username, password, database):
    """Function to lists all states with a name starting with N
        (upper N) from the database hbtn_0e_0_usa."""

    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         host='localhost', port=3306)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
