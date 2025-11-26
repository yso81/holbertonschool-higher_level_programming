#!/usr/bin/python3
"""
Lists all cities from table of hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    cities_list = []
    for row in rows:
        cities_list.append(row[0])
    print(", ".join(cities_list))

    cur.close()
    db.close()
