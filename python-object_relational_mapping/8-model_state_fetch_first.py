#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Displays the first state by states.id, or "Nothing" if table is empty.
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

    # Query the first State object ordered by id
    state = session.query(State).order_by(State.id).first()

    # Display result
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
