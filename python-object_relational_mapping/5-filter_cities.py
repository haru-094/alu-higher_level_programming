#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
Safe from SQL injection using parameterized queries.

Takes 4 arguments: mysql username, mysql password, database name, and state name.
Results are sorted in ascending order by cities.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query using parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and display results
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))

    # Close cursor and connection
    cursor.close()
    db.close()
