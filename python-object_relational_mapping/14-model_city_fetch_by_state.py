#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query all City objects and their associated State objects
    results = session.query(City, State).filter(City.state_id == State.id) \
                                        .order_by(City.id).all()

    # Display results
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
