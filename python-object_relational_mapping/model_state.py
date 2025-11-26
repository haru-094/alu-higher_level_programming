#!/usr/bin/python3
"""
Module that contains the class definition of a State and Base instance.

State class links to the MySQL table 'states' using SQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the states table in MySQL.

    Attributes:
        id (int): Auto-generated unique integer, primary key, cannot be null
        name (str): String with maximum 128 characters, cannot be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
