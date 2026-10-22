# Python - Object Relational Mapping

This project introduces how Python talks to a MySQL database. The first
part uses the low-level driver **MySQLdb** (`mysqlclient`) to run raw SQL
queries. The second part uses the **SQLAlchemy** ORM to work with
database rows as Python objects.

## Learning Objectives

- Connect to a MySQL server from a Python script
- Run SQL queries with a cursor and read the results
- Filter and sort results with `WHERE`, `LIKE`, and `ORDER BY`
- Join two tables in a single query
- Understand how SQL injection works and how to prevent it
- Understand what an ORM is and why it is useful
- Map a Python class to a table with SQLAlchemy
- Create, read, and update rows using Python objects and a session

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

Each group of tasks ships with an SQL file that creates its database
and data.

```bash
# Tasks 0 to 3 (database hbtn_0e_0_usa)
cat 0-select_states.sql | sudo mysql

# Tasks 4 and 5 (database hbtn_0e_4_usa)
cat 4-cities_by_state.sql | sudo mysql

# Tasks 6 to 12 (database hbtn_0e_6_usa): create the database, then the
# table from the model, then insert the sample data
sudo mysql -e "CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;"
./6-model_state.py <user> <password> hbtn_0e_6_usa
cat 7-model_state_fetch_all.sql | sudo mysql hbtn_0e_6_usa
```

## Usage

All scripts take three arguments: MySQL username, MySQL password, and
database name. Some tasks take a fourth argument. Usernames and
passwords are case sensitive.

```bash
./<script>.py <mysql username> <mysql password> <database name>
```

### Part 1 - MySQLdb

**Task 0 - Get all states**

```bash
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

**Task 1 - Filter states** (names starting with `N`)

```bash
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

**Task 2 - Filter states by user input** (built with `format`,
vulnerable to SQL injection, for learning only)

```bash
$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

**Task 3 - SQL injection safe version**

```bash
$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

**Task 4 - Cities by state** (uses a `JOIN`, a single `execute()`)

```bash
$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
...
(15, 'Carson City', 'Nevada')
```

**Task 5 - All cities by state** (safe from SQL injection)

```bash
$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
```

### Part 2 - SQLAlchemy

**Task 6 - First state model**

`model_state.py` defines `Base` and the `State` class linked to the
`states` table. `6-model_state.py` creates the table from the model.

```bash
$ ./6-model_state.py root root hbtn_0e_6_usa
```

**Task 7 - All states via SQLAlchemy**

```bash
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

**Task 8 - First state** (prints `Nothing` if the table is empty)

```bash
$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
```

**Task 9 - Contains `a`**

```bash
$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
```

**Task 10 - Get a state** (prints the id, or `Not found`)

```bash
$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
```

**Task 11 - Add a new state**

```bash
$ ./11-model_state_insert.py root root hbtn_0e_6_usa
6
```

**Task 12 - Update a state** (changes `id = 2` to `New Mexico`)

```bash
$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
```

## Files

| File | Description |
|------|-------------|
| `0-select_states.sql` | Creates `hbtn_0e_0_usa` and the `states` table with sample data |
| `0-select_states.py` | Lists all states, sorted by `states.id`, using `MySQLdb` |
| `1-filter_states.py` | Lists states whose name starts with `N` (uppercase) |
| `2-my_filter_states.py` | Displays states matching the name given as argument, building the query with `format` |
| `3-my_safe_filter_states.py` | Same as task 2, safe from SQL injection with a `%s` placeholder |
| `4-cities_by_state.sql` | Creates `hbtn_0e_4_usa` with the `states` and `cities` tables and sample data |
| `4-cities_by_state.py` | Lists all cities with their state names using a `JOIN` |
| `5-filter_cities.py` | Lists the cities of a state given as argument, safe from SQL injection |
| `model_state.py` | Defines the `State` class mapped to the `states` table |
| `6-model_state.py` | Creates the `states` table from the `State` model |
| `7-model_state_fetch_all.sql` | Inserts the sample states into `hbtn_0e_6_usa` |
| `7-model_state_fetch_all.py` | Lists all `State` objects, sorted by `states.id` |
| `8-model_state_fetch_first.py` | Prints the first `State` object, or `Nothing` if empty |
| `9-model_state_filter_a.py` | Lists all `State` objects whose name contains the letter `a` |
| `10-model_state_my_get.py` | Prints the id of the state whose name is given, or `Not found` |
| `11-model_state_insert.py` | Adds the state `Louisiana` and prints its new id |
| `12-model_state_update_id_2.py` | Changes the name of the `State` with `id = 2` to `New Mexico` |

## Notes

- Scripts connect to a MySQL server on `localhost`, port `3306`.
- `LIKE BINARY` is used in task 1 so the match is case sensitive.
- Task 2 builds the query with `format`, so an input such as
  `x' OR '1'='1` returns every row. Never do this in real code.
- Task 3 passes the value separately: `cur.execute(query, (value,))`.
  The same input is treated as plain text and returns nothing.
- With SQLAlchemy, `filter(State.name == value)` also sends the value as
  a separate parameter, so it is safe from SQL injection.
- A SQLAlchemy query is built step by step and only runs when you call
  `all()`, `first()`, or iterate over it.
- Changes made through a session are saved only after `session.commit()`.
- Check style with:

```bash
pycodestyle *.py
```

## Author

Abdulrhman Saleh Alduqil - [d7ome989](https://github.com/d7ome989)