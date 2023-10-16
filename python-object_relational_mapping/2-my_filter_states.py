'''
a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
'''
#!/usr/bin/env python
"""importing modules"""
import MySQLdb
from sys import argv
"""open database communication"""
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
query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
query = query.format(argv[4])
cur.execute(query)
"""# Fetch a rows """
results = cur.fetchall()
for row in results:
        print(row)
"""close both database and cursor"""
cur.close()
conn.close()