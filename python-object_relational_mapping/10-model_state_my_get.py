#!/usr/bin/python3
"""script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, database, state_name):
    """Function to lists State object with the name passed
        as argument"""

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(state_name)).first()

    if states:
        print(states.id)
    else:
        print('Not found')


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    database, state_name = sys.argv[3], sys.argv[4]
    list_states(username, password, database, state_name)
