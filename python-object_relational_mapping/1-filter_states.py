#!/usr/bin/python3
"""List all states starting with N from a MySQL database."""
import sys

import MySQLdb


def main():
    """Connect to MySQL and print states whose name starts with N."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=password,
                           db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
