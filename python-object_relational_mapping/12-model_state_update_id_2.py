#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Changes the name of the State where id = 2 to "New Mexico".
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

    # Query the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name if state exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
