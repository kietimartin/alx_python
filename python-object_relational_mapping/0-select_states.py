'''This is a creipt that list all states fro  the database 'hbtn_0e_0_usa'

Arguements taken:
                mysql username, 
                mysql password and 
                database name

Returns; results sorted in ascending order by states.id
'''
import MySQLdb
from sys import argv
'''Connecting to the database
'''

db_conn = MySQLdb.connect(
    host='localhost', port='3306', user=argv[1], passwd=argv[2], db=argv[3])
# Mapping the object to the cursor method
db_curs = db_conn.cursor()
# Executing the query
query = "SELECT * FROM states ORDER BY id ASC;"
db_curs.execute(query)
# Fetching the results
result = db_curs.fetchall()
for row in result:
    print(row)
# closing both the database and cursor
db_curs.close()
db_conn.close()
