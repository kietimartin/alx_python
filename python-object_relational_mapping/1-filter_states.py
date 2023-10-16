'''This is a script listing all names starting with an N
from the database hbtn_0e_0_usa

Arguements:
            username,
            password
            database name
'''
import MySQLdb
from sys import argv
# Creating the connection
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
query = "SELECT * FROM states ORDER BY id ASC;"
cur.execute(query)
""" Fetch a rows """
results = cur.fetchall()
for row in results:
    if row[1].startswith("N"):
        print(row)
"""close both database and cursor"""
cur.close()
conn.close()
