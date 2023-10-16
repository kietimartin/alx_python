#!/usr/bin/env python
"""open database communication"""
from sys import argv
import MySQLdb
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    charset="utf8"
    )
cur = conn.cursor()
# execute SQL query using execute() method
query = (
    "SELECT cities.name "
    "FROM cities "
    "INNER JOIN states ON cities.state_id = states.id "
    "WHERE states.name = %s "
    "ORDER BY cities.id ASC"
    )
cur.execute(query, (argv[4], ))
"""# Fetch a rows """
results = cur.fetchall()
city_names = [row[0] for row in results]
cities_str = ', '.join(city_names)
print(cities_str)
"""close both database and cursor"""
cur.close()
conn.close()