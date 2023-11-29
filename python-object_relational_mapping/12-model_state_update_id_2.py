#!/usr/bin/python3
"""script that changes the name of a State object
    from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, database):
    """Function changes the name of a State object
        from the database hbtn_0e_6_usa """

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id.like(2)).first()
    states.name = 'New Mexico'
    session.commit()


if __name__ == "__main__":
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
