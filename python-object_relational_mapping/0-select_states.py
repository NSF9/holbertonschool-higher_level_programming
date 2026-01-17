#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <password> <database_name>
"""

import MySQLdb
import sys


def list_all_states(username, password, database_name):
    """Connects to MySQL and lists all states sorted by id ASC"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
