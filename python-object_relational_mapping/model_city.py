#!/usr/bin/python3
"""Define the City class linked to the cities table."""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """Represent a row of the cities table.

    Attributes:
        id: Auto-generated unique integer, primary key, not null.
        name: String of at most 128 characters, not null.
        state_id: Integer foreign key to states.id, not null.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
