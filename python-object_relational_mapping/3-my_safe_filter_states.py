#!/usr/bin/python3
"""Safe from SQL injection: filter states by user input"""

import MySQLdb
import sys


def safe_filter_states(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    safe_filter_states(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )
