#!/usr/bin/python3
"""Filter states by name (case sensitive)"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database_name, state_name):
    """Displays states matching the given name (case-sensitive)"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        cursor = db.cursor()

        query = (
            "SELECT * FROM states "
            "WHERE name = BINARY '{}' "
            "ORDER BY id ASC"
        ).format(state_name)

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    filter_states_by_name(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )
