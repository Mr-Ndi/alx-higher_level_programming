#!/usr/bin/python3

"""
importing the pyython3
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    my_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    my_session_maker = sessionmaker(bind=my_engine)
    my_session = my_session_maker()

    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    my_session.close()
