#!/usr/bin/python3
""" List all cities of a state from the database hbtn_0e_4_usa (safe from SQL injection) """

import MySQLdb
import sys


def list_cities_by_state(username, password, dbname, state_name):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )

        cur = db.cursor()
        query = (
            "SELECT cities.id, cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC;"
        )
        cur.execute(query, (state_name,))
        rows = cur.fetchall()

        print(", ".join([row[1] for row in rows]))

        cur.close()
        db.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )
