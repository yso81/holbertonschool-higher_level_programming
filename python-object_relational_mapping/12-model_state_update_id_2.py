#!/usr/bin/python3
"""
A script that changes the name of a State object from the database
hbtn_0e_6_usa
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

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object where id is 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
