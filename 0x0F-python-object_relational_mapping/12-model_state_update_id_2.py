#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # declaring the vars
    my_host = 'localhost'
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]
    port = 3306
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        users, my_password, my_db),  pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = sessionmaker()
    new_state = "New Mexico"
    state = session.query(State).filter_by(id = 2).first()
    if state:
        state.name = new_state
        session.commit()

    session.close()
