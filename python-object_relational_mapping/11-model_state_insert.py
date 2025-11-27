#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create the new State object
    new_state = State(name="Louisiana")

    # Add the new object to the session
    session.add(new_state)

    # Commit the session to save the changes to the database
    session.commit()

    # Print the new states.id
    print(new_state.id)

    session.close()
