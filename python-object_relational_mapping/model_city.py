#!/usr/bin/python3
"""
Module that contains the class definition of a City.

City class links to the MySQL table 'cities' using SQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents the cities table in MySQL.

    Attributes:
        id (int): Auto-generated unique integer, primary key, cannot be null
        name (str): String with maximum 128 characters, cannot be null
        state_id (int): Integer, foreign key to states.id, cannot be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
