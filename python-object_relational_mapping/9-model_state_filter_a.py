#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a' from hbtn_0e_6_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by states.id.
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

    # Query State objects containing 'a', sorted by id
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
