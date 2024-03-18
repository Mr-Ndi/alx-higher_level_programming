#!/usr/bin/python3
"""
importing python
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":

    my_engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    sessione_meker = sessionmaker(bind=my_engine)
    session = sessione_meker()

    for state in session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
    session.close()
