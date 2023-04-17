#!/usr/bin/python3
"""
    A script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
    Usage: ./0-select_states.py <mysql username>\
            <mysql password> <database name>\
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    search = sys.argv[4]
    query = "SELECT cities.id, cities.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name=%s\
            ORDER BY id ASC"
    cursor.execute(query, (search,))
    states = cursor.fetchall()
    cities = []

    for city in states:
        cities.append(city[1])
    print(", ".join(cities))

    cursor.close()
    db.close()
