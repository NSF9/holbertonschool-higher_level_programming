#!/usr/bin/python3
""" List all cities with their corresponding state names """

import MySQLdb
import sys


def list_cities(username, password, dbname):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )

        cur = db.cursor()
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
        cur.execute(query)

        for row in cur.fetchall():
            print(row)

        cur.close()
        db.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
