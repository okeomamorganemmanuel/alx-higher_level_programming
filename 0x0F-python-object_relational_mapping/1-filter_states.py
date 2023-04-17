#!/usr/bin/python3
"""script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa:
    Usage: ./0-select_states.py <mysql username>\
 <mysql password> <database name>\
"""
import MySQLdb, sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
results = c.fetchall()
[print(row) for row in results]
db.close()
