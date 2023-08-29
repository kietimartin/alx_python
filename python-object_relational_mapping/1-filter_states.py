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
if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)