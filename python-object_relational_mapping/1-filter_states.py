#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_all_states(username, password, database_name):
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
