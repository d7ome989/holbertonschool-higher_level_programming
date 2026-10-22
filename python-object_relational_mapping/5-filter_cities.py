#!/usr/bin/python3
"""List all cities of a given state, safe from SQL injection."""
import sys

import MySQLdb


def main():
    """Connect to MySQL and print the cities of the searched state."""
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
    cur.execute("SELECT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC",
                (state_name,))
    rows = cur.fetchall()
    names = [row[0] for row in rows]
    print(", ".join(names))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
