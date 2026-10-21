# Python - Object Relational Mapping

This project introduces how Python talks to a MySQL database. The first
part uses the low-level driver **MySQLdb** (`mysqlclient`) to run raw SQL
queries. The second part uses the **SQLAlchemy** ORM to work with
database rows as Python objects.

## Learning Objectives

- Connect to a MySQL server from a Python script
- Run SQL queries with a cursor and read the results
- Filter and sort results with `WHERE`, `LIKE`, and `ORDER BY`
- Understand how SQL injection works and how to prevent it
- Understand what an ORM is and why it is useful
- Map a Python class to a table with SQLAlchemy

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0
- `MySQLdb` (`mysqlclient`) and `SQLAlchemy`
- Code style checked with `pycodestyle` (PEP 8)
- Every module, class, and function has a docstring (PEP 257)
- All files are executable and start with `#!/usr/bin/python3`
- All files end with a new line
- Code must not run when imported

## Installation

```bash
sudo apt install -y python3-dev default-libmysqlclient-dev \
    build-essential pkg-config
python3 -m venv venv
source venv/bin/activate
pip install mysqlclient SQLAlchemy pycodestyle
```

## Database Setup

Each task ships with an SQL file that creates its database and data.
For tasks 0 to 3:

```bash
cat 0-select_states.sql | sudo mysql
```

## Usage

All scripts take three arguments: MySQL username, MySQL password, and
database name. Tasks 2 and 3 take a fourth argument: the state name to
search. Usernames and passwords are case sensitive.

```bash
./<script>.py <mysql username> <mysql password> <database name>
```

### Task 0 - Get all states

```bash
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

### Task 1 - Filter states

```bash
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

### Task 2 - Filter states by user input

```bash
$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

### Task 3 - SQL injection safe version

```bash
$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

## Files

| File | Description |
|------|-------------|
| `0-select_states.sql` | Creates the `hbtn_0e_0_usa` database and the `states` table with sample data |
| `0-select_states.py` | Lists all states from `hbtn_0e_0_usa`, sorted by `states.id`, using `MySQLdb` |
| `1-filter_states.py` | Lists states whose name starts with `N` (uppercase), sorted by `states.id` |
| `2-my_filter_states.py` | Displays states matching the name given as argument, building the query with `format` (vulnerable to SQL injection, for learning only) |
| `3-my_safe_filter_states.py` | Same as task 2, but safe from SQL injection using a `%s` placeholder and a parameter tuple |

## Notes

- Scripts connect to a MySQL server on `localhost`, port `3306`.
- `LIKE BINARY` is used so the match is case sensitive.
- Task 2 builds the query with `format`, so an input such as
  `x' OR '1'='1` returns every row. Never do this in real code.
- Task 3 passes the value separately: `cur.execute(query, (value,))`.
  The same input is treated as plain text and returns nothing.
- Check style with:

```bash
pycodestyle 0-select_states.py 1-filter_states.py \
    2-my_filter_states.py 3-my_safe_filter_states.py
```

## Author

Abdulrhman Saleh Alduqil - [d7ome989](https://github.com/d7ome989)