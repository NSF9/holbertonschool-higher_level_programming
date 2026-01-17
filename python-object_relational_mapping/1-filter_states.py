#!/usr/bin/python3
"""List all states starting with 'N' from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states_starting_with_n(username, password, database_name):
    """Lists states starting with uppercase N"""
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
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
        )

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    list_states_starting_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
