#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, database):
    """Function to adds the State object “Louisiana”
        to the database hbtn_0e_6_usa"""

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()

    states = session.query(State).filter(State.name.like('Louisiana')).first()

    if states:
        print(states.id)
    else:
        print('Not found')


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
