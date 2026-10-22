#!/usr/bin/python3
"""Define the State class linked to the states table."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a row of the states table.

    Attributes:
        id: Auto-generated unique integer, primary key, not null.
        name: String of at most 128 characters, not null.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
