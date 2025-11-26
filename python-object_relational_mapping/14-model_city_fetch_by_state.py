#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by cities.id.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query all City objects with their State, sorted by cities.id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
