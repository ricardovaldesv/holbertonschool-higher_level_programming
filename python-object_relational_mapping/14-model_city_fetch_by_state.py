#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def list_states(username, password, database):
    """Function to lists all City objects from the database hbtn_0e_14_usa"""

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_with_states = session.query(City, State).join(State).all()

    for city, state in cities_with_states:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
