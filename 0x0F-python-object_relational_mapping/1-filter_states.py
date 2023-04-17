#!/usr/bin/python3
"""script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa:
    Usage: ./0-select_states.py <mysql username>\
 <mysql password> <database name>\
"""
import MySQLdb, sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC ")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == "N":
            print(state)
