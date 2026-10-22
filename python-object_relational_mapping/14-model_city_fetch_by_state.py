#!/usr/bin/python3
"""Print all City objects with their state from hbtn_0e_14_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State


def main():
    """Print each city as <state name>: (<city id>) <city name>."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = (session.query(State, City)
            .filter(State.id == City.state_id)
            .order_by(City.id)
            .all())
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    main()
