#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
taking 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL server
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

    # Execute the SQL query using "states.id" explicitly
    c.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    states_id = c.fetchall()

    for row in states_id:
        print(row)


    c.close()
    db.close()
