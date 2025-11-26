#!/usr/bin/python3
"""
Script that deletes all State objects with name containing 'a' from hbtn_0e_6_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Deletes all states with 'a' in their name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state
    for state in states:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close session
    session.close()
