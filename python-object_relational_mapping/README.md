# Python - Object Relational Mapping

This project introduces how Python talks to a MySQL database. The first
part uses the low-level driver **MySQLdb** (`mysqlclient`) to run raw SQL
queries. The second part uses the **SQLAlchemy** ORM to work with
database rows as Python objects.

## Learning Objectives

- Connect to a MySQL server from a Python script
- Run SQL queries with a cursor and read the results
- Filter and sort results with `WHERE`, `LIKE`, and `ORDER BY`
- Protect queries against SQL injection
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
For tasks 0 and 1:

```bash
cat 0-select_states.sql | sudo mysql
```

## Usage

All scripts take three arguments: MySQL username, MySQL password, and
database name. Usernames and passwords are case sensitive.

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

## Files

| File | Description |
|------|-------------|
| `0-select_states.sql` | Creates the `hbtn_0e_0_usa` database and the `states` table with sample data |
| `0-select_states.py` | Lists all states from `hbtn_0e_0_usa`, sorted by `states.id`, using `MySQLdb` |
| `1-filter_states.py` | Lists states whose name starts with `N` (uppercase), sorted by `states.id`, using `MySQLdb` |

## Notes

- Scripts connect to a MySQL server on `localhost`, port `3306`.
- `LIKE BINARY` is used in task 1 so the match is case sensitive.
- Queries that include user input must use `%s` placeholders instead of
  string concatenation.
- Check style with:

```bash
pycodestyle 0-select_states.py 1-filter_states.py
```

## Author

Abdulrhman Saleh Alduqil - [d7ome989](https://github.com/d7ome989)
