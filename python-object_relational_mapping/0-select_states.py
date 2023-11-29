#!/usr/bin/python3
"""Represent a clas Rectangle."""

import sys
import MySQLdb

def list_states(username, password, database):
    """Represent a Rectangle."""

    db = MySQLdb.connect(user=username, passwd=password, db=database, host='localhost', port=3306)
    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id"
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database)
