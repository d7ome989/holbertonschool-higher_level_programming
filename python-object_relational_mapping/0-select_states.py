#!/usr/bin/python3
"""List all states from a MySQL database."""
import sys

import MySQLdb


def main():
    """Connect to MySQL and print all states ordered by id."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=password,
                           db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
