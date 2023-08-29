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
conn = MySQLdb.connect(
    host='localhost', port='3306', user=argv[1], passwd=argv[2], db=argv[3], charset="utf8"
)
# Initializing the cursor method
curs = conn.cursor()
# Exceuting the query
query = "SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ORDER BY id ASC;"
curs.execute(query)
#  Fetching data
result = curs.fetchall()
for row in result:
    print(row)
# Closing the cursor and connection
curs.close()
conn.close()
