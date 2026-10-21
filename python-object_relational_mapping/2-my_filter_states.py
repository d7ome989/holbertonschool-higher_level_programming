#!/usr/bin/python3
"""Display the states whose name matches the given argument."""
import sys

import MySQLdb


def main():
    """Connect to MySQL and print states matching the searched name."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=password,
                           db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = '{}' "
                "ORDER BY id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
