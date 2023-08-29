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

connect  = MySQLdb.connect(host='localhost', port='3306', user=argv[1], passwd=argv[2], db=argv[3] )
# Mapiing the object to the cursor method
db_cursor = connect.cursor()
# Executing the query
query = "SELECT * FROM states ORDER BY id ASC;"
db_cursor.execute(query)
# Fetching the results
result = db_cursor.fetchall()
for row in result:
    print(row)

#closing both the database and cursor
db_cursor.close()
connect.close()