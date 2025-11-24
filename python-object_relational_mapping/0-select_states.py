#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
)

c = db.cursor()

c.execute("SELECT * FROM states ORDER BY states.id ASC")

states_id = c.fetchall()

for row in states_id:
    print(row)


c.close()
db.close()
