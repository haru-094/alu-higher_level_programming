#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument.
SQL injection free using SQLAlchemy ORM.

Takes 4 arguments: mysql username, mysql password, database name, and state name.
Displays the states.id or "Not found" if no match.
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
    state_name = sys.argv[4]

    # Create engine and connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given name (SQL injection free)
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close session
    session.close()
